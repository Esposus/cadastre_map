from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.src.database import Base, get_db
from app.src.models import CadastreRequest


SQLALCHEMY_DATABASE_URL = "sqlite:///./cadastre.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = db
client = TestClient(app)


def test_save_request(db):
    request_data = {
        'cadastre_number': 123,
        'latitude': 45.678901,
        'longitude': 23.456789,
        'result': True
    }

    db_request = CadastreRequest(
        cadastre_number=request_data['cadastre_number'],
        latitude=request_data['latitude'],
        longitude=request_data['longitude'],
        result=request_data['result']
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    stored_request = (
        db.query(CadastreRequest)
        .filter(CadastreRequest.id == db_request.id).first()
    )

    assert stored_request is not None
    assert stored_request.cadastre_number == request_data["cadastre_number"]
    assert stored_request.latitude == request_data["latitude"]
    assert stored_request.longitude == request_data["longitude"]
    assert stored_request.result == request_data["result"]
