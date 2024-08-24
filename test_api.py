import requests
import pytest
import allure
from Data.constans import Base_URL, token

@allure.title("Проверка поиска фильма по жанру")
def test_search_by_genre():
    with allure.step("Произвести поиск по жанру и в заголовках передать токен"):
        resp = requests.get(Base_URL + '/movie?page=1&limit=10&genres.name=драма', headers={"X-API-KEY": token})
    with allure.step("Проверить, что статус код равен 200"):
        assert resp.status_code == 200
    with allure.step("Проверить, что полученный список фильмов не пустой"):
        data = resp.json() 
        assert len(data) is not 0  

@allure.title("Проверка поиска фильма по дата премьеры в мире")
def test_search_by_premiere():
    with allure.step("Произвести поиск по дате премьеры и в заголовках передать токен"):
        resp = requests.get(Base_URL + '/movie?page=1&limit=10&premiere.world=01.01.2020-31.12.2020', headers={"X-API-KEY": token})
    with allure.step("Проверить, что статус код равен 200"):
        assert resp.status_code == 200 
    with allure.step("Проверить, что полученный список фильмов не пустой"):
        data = resp.json() 
        assert len(data) is not 0  

@allure.title("Проверка поиска фильма по рейтингу imdb")
def test_search_by_imdb():
    with allure.step("Произвести поиск по рейтингу imdb и в заголовках передать токен"):
        resp = requests.get(Base_URL + '/movie?page=1&limit=10&rating.imdb=7-9&premiere.world=01.01.2022-05.05.2024', headers={"X-API-KEY": token})
    with allure.step("Проверить, что статус код равен 200"):
        assert resp.status_code == 200
    with allure.step("Проверить, что полученный список фильмов не пустой"):
        data = resp.json() 
        assert len(data) is not 0  

@allure.title("Невалидная првоерка поиска по дате релиза")
def test_negative_search_by_release():
    with allure.step("Произвести поиск по несуществующей дате релиза и в заголовках передать токен"):
        resp = requests.get(Base_URL + '/movie?page=1&limit=10&releaseYears.start=1800', headers={"X-API-KEY": token})
    with allure.step("Проверить, что статус код равен 400"):
        assert resp.status_code == 400
    with allure.step("Проверить, что в теле запроса ошибка"):
        data = resp.json() 
        assert data["error"] == "Bad Request"

@allure.title("Невалидная првоерка поиска по актеру")
def test_negative_search_by_actor():
    with allure.step("Произвести поиск по несуществующему актеру и в заголовках передать токен"):
        resp = requests.get(Base_URL + '/person/search?page=1&limit=10&query=РайанГосуслуг', headers={"X-API-KEY": token})
    with allure.step("Проверить, что статус код равен 200"):
        assert resp.status_code == 200
    with allure.step("Проверить, что список пустой"):
        data = resp.json()
        assert data["docs"] == []


#pytest test_api.py


