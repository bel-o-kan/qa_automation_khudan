import requests

# Тест для GET-запиту
def test_get_request():
    url = "https://api.example.com/data"
    response = requests.get(url)
    assert response.status_code == 200
    # Додаткові перевірки, якщо необхідно


# Тест для POST-запиту
def test_post_request():
    url = "https://api.example.com/data"
    data = {"name": "John", "age": 30}
    response = requests.post(url, json=data)
    assert response.status_code == 201
    # Додаткові перевірки, якщо необхідно


# Тест для PUT-запиту
def test_put_request():
    url = "https://api.example.com/data/1"
    data = {"name": "John", "age": 35}
    response = requests.put(url, json=data)
    assert response.status_code == 200
    # Додаткові перевірки, якщо необхідно


# Тест для PATCH-запиту
def test_patch_request():
    url = "https://api.example.com/data/1"
    data = {"age": 40}
    response = requests.patch(url, json=data)
    assert response.status_code == 200
    # Додаткові перевірки, якщо необхідно


# Запуск тестів
test_get_request()
test_post_request()
test_put_request()
test_patch_request()
