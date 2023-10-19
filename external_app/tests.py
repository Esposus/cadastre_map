from fastapi.testclient import TestClient
from app.external_server import external_app


# client = TestClient(external_app)


# def test_emulate_external_server():
#     response = client.post('/emulate_external_server')
#     assert response.status_code == 200
#     assert 'response' in response.json()
#     assert response.json()['response'] in (True, False)


# Опциональный тест для проверки внешнего сервера
def test_emulate_external_server():
    # Подготавливаем клиент для внешнего сервера
    external_client = TestClient(external_app)

    # Отправляем запрос на эмуляцию обработки
    response = external_client.post("/emulate_external_server", json={"cadastre_number": 1, "latitude": 1.0, "longitude": 2.0})
    
    assert response in [True, False]
