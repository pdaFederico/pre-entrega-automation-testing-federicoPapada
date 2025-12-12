from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#Proceso de Login

class LoginPage:
    URL = 'https://www.saucedemo.com/'
    USER_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def login_process(self, user, password):
        self.driver.find_element(*self.USER_INPUT).send_keys(user)
        self.driver.find_element(*self.PASS_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

