import json
import random
import time

from fastapi import APIRouter, Depends, HTTPException
import requests
from sqlalchemy.orm import Session

from .crud import get_request_history, get_all_request_history, save_request
from .database import get_db


router = APIRouter()


@router.post('/query')
def create_query(cadastre_number: int,
                 latitude: float,
                 longitude: float,
                 db: Session = Depends(get_db)):
    """Создание запроса"""
    url = 'http://external_app:8003/result'
    # response = emulate_external_server()
    data = {
        "cadastre_number": cadastre_number,
        "latitude": latitude,
        "longitude": longitude
    }
    data = json.dumps(data).encode("utf-8")
    request = requests.post(url=url)
    response_data = request.json()['response']
    db_query = save_request(
        db, cadastre_number, latitude, longitude, response=response_data
    )

    return {'response': db_query}


@router.get('/history')
def get_all_history(db: Session = Depends(get_db)):
    """Получение истории всех запросов"""
    history = get_all_request_history(db)
    if not history:
        raise HTTPException(
            status_code=404,
            detail="Данные отсутствуют в базе"
        )

    return {"history": history}


@router.get('/history/{cadastre_number}')
def get_history(cadastre_number: int, db: Session = Depends(get_db)):
    """Получение истории запросов по кадастровому номеру"""
    history = get_request_history(db, cadastre_number)
    if not history:
        raise HTTPException(
            status_code=404,
            detail="Отсутствуют записи с данным кадастровым номером"
        )

    return {"history": history}


@router.get('/ping')
def ping():
    """Проверка на запуск сервера"""
    return {'ping': 'pong'}


@router.get('/result')
def emulate_external_server():
    """Эмуляция внешнего сервиса"""
    time.sleep(random.uniform(0, 2))
    return random.choice([True, False])
