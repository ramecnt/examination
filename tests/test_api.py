import pytest
from app import app
from utils import load_by_pk

def test_api_all():
    """ Тест по проверки работы api со всеми даннами """
    # Получаем данные из api
    responce = app.test_client().get("/api/routes")
    # Проверка статус кода
    assert responce.status_code == 200
    # Проверка того что возвращается список
    assert isinstance(responce.json, list)
    # Проверка того что список не пустой
    assert len(responce.json) > 0

def test_api_first():
    """ Тест по проверки работы api с данными 1 элемента """
    # Получаем данные из api
    responce = app.test_client().get("/api/routes/1")
    # Проверка статус кода
    assert responce.status_code == 200
    # Проверка того что возвращается словарь
    assert isinstance(responce.json, dict)
    # Проверка того что возвращается список равный нашим данным
    assert responce.json == load_by_pk(1)
