from My_page.search import Search
from Data.data import *
from Data.conftest import *
from Data.constans import *
import requests
import pytest
import allure

@allure.title("Проверка поиска фильмов по актеру")
def test_search_by_actor(chrome_browser):
    search = Search(chrome_browser)
    result = search.Searc_by_actor(actor)
    with allure.step("Проверить, что в полученных фильмах есть запрашиваемый актер"):
        assert result_actor in [item.text for item in result]

@allure.title("Проверка поиска фильмов по названию")
def test_search_by_name(chrome_browser):
    search = Search(chrome_browser)
    result = search.Search_by_name(name)
    with allure.step("Проверить совпадает ли название фильма с полученным результатом"):
        assert result == result_name

@allure.title("Проверка поиска фильмов по годовому интервалу")
def test_search_by_interval(chrome_browser):
    search = Search(chrome_browser)
    result = search.Search_by_interval(from_year, to_year)
    with allure.step("Проверить, что первый в списке фильм совпадает с выбранным интервалом"):
        assert result == result_to_year

@allure.title("Проверка поиска фильмов по рейтингу IMDB")
def test_search_by_best_films(chrome_browser):
    search = Search(chrome_browser)
    result = search.Search_by_best_films(rating_min, rating_max)
    with allure.step("Проверить что рейтинг первого фильма выше или равен минимальному рейтингу"):
        assert result >= rating_min

