from fastapi import APIRouter, Depends, HTTPException, status
import httpx
from sqlalchemy.orm import Session

from .crud import (
    get_history_by_cadastre_number, get_all_request_history, save_request
)
from .database import get_db
from .models import QueryData


router = APIRouter()


@router.get('/query')
def create_query(query_data: QueryData, db: Session = Depends(get_db)):
    """Создание запроса к внешнему сервису"""

    url = 'http://external_app:8003/result'
    params = {
        "cadastre_number": query_data.cadastre_number,
        "latitude": query_data.latitude,
        "longitude": query_data.longitude,
    }
    try:
        request = httpx.get(url=url, params=params)
        request.raise_for_status()
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        response_data = request.json()['response']
    response_data = True
    db_query = save_request(
        db,
        query_data.cadastre_number,
        query_data.latitude,
        query_data.longitude,
        result=response_data
    )
    return {'response': db_query}


@router.get('/history')
def get_all_history(db: Session = Depends(get_db)):
    """Получение истории всех запросов"""
    history = get_all_request_history(db)
    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="База данных пуста",
        )
    return {"history": history}


@router.get('/history/{cadastre_number}')
def get_history(cadastre_number: int, db: Session = Depends(get_db)):
    """Получение истории запросов по кадастровому номеру"""
    history = get_history_by_cadastre_number(db, cadastre_number)
    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Отсутствуют записи с данным кадастровым номером",
        )
    return {"history": history}


@router.get('/ping')
def ping():
    """Проверка на запуск сервера"""
    return {'ping': 'pong'}
