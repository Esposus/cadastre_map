from fastapi import status
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.main import app
from app.src.database import Base, get_db
from app.src.models import CadastreRequest


SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine
)

Base.metadata.create_all(bind=test_engine)


@pytest.fixture(scope='session', autouse=True)
def override_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_db


def test_save_request(override_db: Session):
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
    override_db.add(db_request)
    override_db.commit()
    override_db.refresh(db_request)
    stored_request = (
        override_db.query(CadastreRequest)
        .filter(CadastreRequest.id == db_request.id).first()
    )

    assert stored_request is not None
    assert stored_request.cadastre_number == request_data["cadastre_number"]
    assert stored_request.latitude == request_data["latitude"]
    assert stored_request.longitude == request_data["longitude"]
    assert stored_request.result == request_data["result"]


def test_ping_pong():
    client = TestClient(app)
    response = client.get('ping')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'ping': 'pong'}


# def test_get_all_history():
#     client = TestClient(app)
#     response = client.get("/history")
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.json())
#     assert 'history' in response.json()


# def test_get_history_by_cadastre_number():
#     client = TestClient(app)
#     response = client.get("/history/123")
#     assert response.status_code == status.HTTP_200_OK
#     assert len(response.json())
#     assert 'history' in response.json()
