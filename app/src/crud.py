from sqlalchemy.orm import Session
from .models import CadastreRequest


def save_request(
        db: Session,
        cadastre_number: int,
        latitude: float,
        longitude: float,
        result: bool
):
    db_query = CadastreRequest(
        cadastre_number=cadastre_number,
        latitude=latitude,
        longitude=longitude,
        result=result
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_request_history(db: Session, cadastre_number: int):
    return (
        db.query(CadastreRequest)
        .filter(CadastreRequest.cadastre_number == cadastre_number).all()
    )


def get_all_request_history(db: Session):
    return db.query(CadastreRequest).all()
