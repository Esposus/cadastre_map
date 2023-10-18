from fastapi import APIRouter, Depends, HTTPException
import requests
from sqlalchemy.orm import Session

from .crud import get_request_history, save_request
from .database import get_db


router = APIRouter()


# URL_EXTERNAL_SERVER = "http://127.0.0.1:8003/result"


@router.post('/query')
def create_query(cadastre_number: int,
                 latitude: float,
                 longitude: float,
                 db: Session = Depends(get_db)):
    """Создание запроса"""

    url = "http://127.0.0.1:8003/result"
    params = {
        "cadastre_number": cadastre_number,
        "latitude": latitude,
        "longitude": longitude
    }
    response = requests.post(url=url, params=params)
    response = response.json()["response"]
    db_query = save_request(
        db, cadastre_number, latitude, longitude, response=response
    )

    return {'response': db_query}


@router.get('/history')
def get_history(cadastre_number: str, db: Session = Depends(get_db)):
    """Получение истории запросов по кадастровому номеру"""
    history = get_request_history(db, cadastre_number)
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    return {"history": history}


@router.get('/ping')
def ping():
    return {'ping': 'pong'}


"""@router.get('/result')
def emulate_external_server(cadastre_number: int, latitude: float, longitude: float):
    time.sleep(random.uniform(0, 2))
    response_data = {'response': random.choice([True, False])}
    return response_data"""
