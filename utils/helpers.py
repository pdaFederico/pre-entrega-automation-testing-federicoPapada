import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

URL = 'https://www.saucedemo.com/'
USERNAME = 'visual_user'
PASSWORD = 'secret_sauce'


def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def login_test(driver):
    driver.get(URL)     #Ingresa a la URL
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

