from My_page.search import Search
from Data.data import *
from Data.conftest import *
from Data.constans import *
import requests
import pytest
import allure

@allure.title("Проверка поиска фильмов по стране")
def test_search_by_country(chrome_browser):
    search = Search(chrome_browser)
    result = search.Search_by_country(country)


@allure.title("Проверка поиска фильмов по актеру")
def test_search_by_actor(chrome_browser):
    search = Search(chrome_browser)
    result = search.Searc_by_actor(actor)

@allure.title("Проверка поиска фильмов по названию")
def test_search_by_name(chrome_browser):
    search = Search(chrome_browser)
    result = search.Search_by_name(name)

@allure.title("Проверка поиска фильмов по годовому интервалу")
def test_search_by_interval(chrome_browser):
    search = Search(chrome_browser)
    result = search.Search_by_interval(from_year, to_year)

@allure.title("Проверка поиска фильмов по премьере")
def test_search_by_premiere(chrome_browser):
    search = Search(chrome_browser)
    result = search.Search_by_premiere(prem_month)

#pytest test_ui.py
