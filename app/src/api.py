from fastapi import APIRouter, Depends, HTTPException, status
import httpx
from loguru import logger
from sqlalchemy.orm import Session

from .crud import (
    get_history_by_cadastre_number, get_all_request_history, save_request
)
from .database import get_db
from .exceptions import APIResponseJSONException


router = APIRouter()


@router.get('/query')
def create_query(
    cadastre_number: int,
    latitude: float,
    longitude: float,
    db: Session = Depends(get_db)
):
    """Создание запроса к внешнему сервису"""

    url = 'http://external_app:8003/result'
    params = {
        "cadastre_number": cadastre_number,
        "latitude": latitude,
        "longitude": longitude,
    }
    try:
        request = httpx.get(url=url, params=params)
        request.raise_for_status()
    except httpx.RequestError as e:
        logger.error(f"Ошибка при отправке запроса {e.request.url!r}.")
    except httpx.HTTPStatusError as e:
        logger.error(
            f'Ошибка ответа {e.response.status_code} '
            f'при запросе {e.request.url!r}'
        )
    try:
        response_data = request.json()['response']
    except KeyError:
        logger.error('Ошибка при обращении по ключу "response"')
        raise APIResponseJSONException()
    db_query = save_request(
        db,
        cadastre_number,
        latitude,
        longitude,
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
