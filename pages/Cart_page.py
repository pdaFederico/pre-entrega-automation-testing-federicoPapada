from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)

#Añade al carrito el primer producto del inventario

def add_tocart(self):
    self.driver.find_elements(*self._ADD_BUTTONS)[0].click() 
    return self