import requests
from pages import ReqresPage

# Вынесем заголовки в константу, чтобы не дублировать
# Убедись, что здесь НЕТ русских букв. Вообще.

HEADERS = {
    "x-api-key": "reqres_2b744237b7b34889846a365db5b34174",
    "Content-Type": "application/json"
}

def test_register_success():  # ← убери driver из аргументов
    url = "https://reqres.in/api/register"
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "token" in response.json()

def test_register_missing_password(driver):
    url = "https://reqres.in/api/register"
    payload = {"email": "eve.holt@reqres.in"}

    # Добавляем headers=HEADERS
    response = requests.post(url, json=payload, headers=HEADERS)

    # Теперь сервер пустит нас внутрь, увидит отсутствие пароля и выдаст 400
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"