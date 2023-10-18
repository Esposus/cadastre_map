# from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Request


def save_request(
        db: Session,
        cadastre_number: int,
        latitude: float,
        longitude: float,
        response: bool
):
    db_query = Request(
        cadastre_number=cadastre_number,
        latitude=latitude,
        longitude=longitude,
        response=response
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_request_history(db: Session, cadastre_number: int):
    return db.query(Request).filter(Request.cadastre_number == cadastre_number).all()


# def save_result(db: Session, result: bool, query_id: int):
#     """Обрабатывает ответ от внешнего сервера"""
#     db_query = db.query(Request).filter(Request.id == query_id).first()
#     if db_query:
#         db_query.result = result
#         db.commit()
#         db.refresh(db_query)
#         return {"message": "Ответ от внешнего сервера обработан"}
#     else:
#         raise HTTPException(status_code=404, detail="МашаЛлах!")


# def create_user(db: Session, username: str):
#     db_query = User(username=username)
#     db.add(db_query)
#     db.commit()
#     db.refresh(db_query)
#     return db_query
