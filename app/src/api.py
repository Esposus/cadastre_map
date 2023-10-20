from fastapi import APIRouter, Depends, HTTPException, status
import requests
from sqlalchemy.orm import Session

from .crud import get_request_history, get_all_request_history, save_request
from .database import get_db


router = APIRouter()


@router.get('/query')
def create_query(cadastre_number: int,
                 latitude: float,
                 longitude: float,
                 db: Session = Depends(get_db)):
    """Создание запроса к внешнему сервису"""

    url = 'http://external_app:8003/result'
    params = {
        "cadastre_number": cadastre_number,
        "latitude": latitude,
        "longitude": longitude,
    }
    try:
        request = requests.get(url=url, params=params)
        response_data = request.json()['response']
        db_query = save_request(
            db, cadastre_number, latitude, longitude, result=response_data
        )
        return {'response': db_query}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


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
    history_by_cadastre_number = get_request_history(db, cadastre_number)
    if not history_by_cadastre_number:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Отсутствуют записи с данным кадастровым номером",
        )
    return {"history": history_by_cadastre_number}


@router.get('/ping')
def ping():
    """Проверка на запуск сервера"""
    return {'ping': 'pong'}
