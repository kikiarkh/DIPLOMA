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
        self.browser.find_element(By.CSS_SELECTOR, '[id="formSearchMain"]>[value="поиск"]').click()
        result = self.browser.find_element(By.CSS_SELECTOR, ".text-blue").text
        return result

    @allure.step("Произвести поиск фильмов по актеру")
    def Searc_by_actor(self, actor):
        self.browser.find_element(By.CSS_SELECTOR, "#country").send_keys("США")
        self.browser.find_element(By.CSS_SELECTOR, "input.text:nth-child(14)").send_keys(actor)
        self.browser.find_element(By.CSS_SELECTOR, '[id="formSearchMain"]>[value="поиск"]').click()
        result = self.browser.find_elements(By.CSS_SELECTOR, "div:nth-child(3) > span:nth-child(4) > a:nth-child(1)")
        for item in result:
            print(item.text)
            return result
        
    @allure.step("Произвести поиск фильмов по названию")
    def Search_by_name(self, name):
        self.browser.find_element(By.CSS_SELECTOR, "#find_film").send_keys(name)
        self.browser.find_element(By.CSS_SELECTOR, '[id="formSearchMain"]>[value="поиск"]').click()
        result = self.browser.find_element(By.CSS_SELECTOR, "div.element:nth-child(2) > div:nth-child(3) > p:nth-child(1) > a:nth-child(1)").text
        return result


    @allure.step("Произвести поиск фильмов по годовому интервалу")
    def Search_by_interval(self, from_year, to_year):
        self.browser.find_element(By.CSS_SELECTOR, "#from_year").send_keys(from_year)
        self.browser.find_element(By.CSS_SELECTOR, "#to_year").send_keys(to_year)
        self.browser.find_element(By.CSS_SELECTOR, '[id="formSearchMain"]>[value="поиск"]').click()
        self.browser.find_element(By.CSS_SELECTOR, '.show_all > a:nth-child(1)').click()
        self.browser.find_element(By.CSS_SELECTOR, '.sorts > dd:nth-child(4) > a:nth-child(1)').click()
        result = self.browser.find_element(By.CSS_SELECTOR, "div.element:nth-child(4) > div:nth-child(3) > p:nth-child(1) > span:nth-child(2)").text
        return result
    
        
    @allure.step("Произвести поиск по рейтингу IMDB")
    def Search_by_best_films(self, rating_min, rating_max):
        self.browser.find_element(By.CSS_SELECTOR, ".block_left_pad > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > h1:nth-child(1) > a:nth-child(1)").click()
        self.browser.find_element(By.CSS_SELECTOR, "#ex_rating_min").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#ex_rating_min").send_keys(rating_min)
        self.browser.find_element(By.CSS_SELECTOR, "#ex_rating_max").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#ex_rating_max").send_keys(rating_max)
        self.browser.find_element(By.CSS_SELECTOR, "input.nice_button:nth-child(45)").click()
        result = self.browser.find_element(By.CSS_SELECTOR, "div.imdb").text
        return result 

        
    
        
        
    



        

    