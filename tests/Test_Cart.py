import time
import pytest
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import get_driver, login_test, wait_time, product_search

#Importación de fixtures

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    print("\nMantener ventana abierta para revisión...")
    time.sleep(5)
    driver.quit()

#TC-003: Automatización del flujo de compra: Añadir elementos al carrito y verificar presencia

def test_cart(driver):
    login_test(driver)  #Inicia sesión
    wait_time(driver)   #Espera explicita
    product_search(driver)  #Busca el primer producto del inventario y lo añade al carrito

    #Valida que el producto se haya agregado correctamente al carrito y devuelve un mensaje en consola
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')   
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1"))
    badge = badge.text
    assert badge == "1"
    print(f"Test OK: Productos en el carrito: {badge}")