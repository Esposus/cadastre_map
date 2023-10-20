from http import HTTPStatus

from fastapi.testclient import TestClient

from external_app.main import app


ENDPOINT = '/result'
TEST_PARAMS = {
    "cadastre_number": 1,
    "latitude": 12.345678,
    "longitude": 87.654321,
}


def test_status_code_is_200():
    client = TestClient(app)
    response = client.get(ENDPOINT, params=TEST_PARAMS)
    assert response.status_code == HTTPStatus.OK, 'Массаракш!'


def test_json_is_correct():
    client = TestClient(app)
    response = client.get(ENDPOINT, params=TEST_PARAMS)
    assert 'response' in response.json()
    assert response.json()['response'] in (True, False)
