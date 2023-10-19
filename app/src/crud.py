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
    return (
        db.query(Request)
        .filter(Request.cadastre_number == cadastre_number).all()
    )


def get_all_request_history(db: Session):
    return db.query(Request).all()
