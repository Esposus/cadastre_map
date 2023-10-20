from fastapi import status
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_ping_pong():
    response = client.get('ping')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'ping': 'pong'}


def test_get_all_history():
    response = client.get("/history")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json())
    assert 'history' in response.json()


def test_get_history_by_cadastre_number():
    response = client.get("/history/123")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json())
    assert 'history' in response.json()
