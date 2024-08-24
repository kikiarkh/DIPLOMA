from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data.data import *
import allure

class Search:
    
    def __init__(self,browser):
        self.browser = browser
        self.browser.get("https://www.kinopoisk.ru/s/")
        self.browser.implicitly_wait(4)

    @allure.step("Произвести поиск фильмов по стране")
    def Search_by_country(self, country):
        self.browser.find_element(By.CSS_SELECTOR, "#country").send_keys(country)
        self.browser.find_element(By.CSS_SELECTOR, ".el_18").click()

    @allure.step("Произвести поиск фильмов по актеру")
    def Searc_by_actor(self, actor):
        self.browser.find_element(By.CSS_SELECTOR, "#country").send_keys("США")
        self.browser.find_element(By.CSS_SELECTOR, "input.text:nth-child(14)").send_keys(actor)
        self.browser.find_element(By.CSS_SELECTOR, ".el_18").click()
        
    @allure.step("Произвести поиск фильмов по названию")
    def Search_by_name(self, name):
        self.browser.find_element(By.CSS_SELECTOR, "#find_film").send_keys(name)
        self.browser.find_element(By.CSS_SELECTOR, ".el_18").click()

    @allure.step("Произвести поиск фильмов по годовому интервалу")
    def Search_by_interval(self, from_year, to_year):
        self.browser.find_element(By.CSS_SELECTOR, "#from_year").send_keys(from_year)
        self.browser.find_element(By.CSS_SELECTOR, "#to_year").send_keys(to_year)
        self.browser.find_element(By.CSS_SELECTOR, ".el_18").click()

    @allure.step("Произвести поиск фильмов по премьере")
    def Search_by_premiere(self, prem_month):
        self.browser.find_element(By.CSS_SELECTOR, "#prem_month").send_keys(prem_month)
        self.browser.find_element(By.CSS_SELECTOR, ".el_18").click()




        

        

    