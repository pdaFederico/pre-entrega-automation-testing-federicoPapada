import time
import pytest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

#Importación de fixtures

from utils.helpers import get_driver, login_test, wait_time


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    print("\nMantener ventana abierta para revisión...")
    time.sleep(5)
    driver.quit()

#TC-002: Automatización para verificar UI: Título de página, inventario y presencia de elementos criticos

def test_interface(driver):
    login_test(driver)                                  #Inicia sesión
    wait_time(driver)                                   #Espera explicita
    assert "/inventory.html" in driver.current_url      #Verifica titulo en URL

    #Verifica titulo del sitio y devuelve un mensaje en consola
    expected_title = "Swag Labs"                        
    assert driver.title == expected_title, f"Título de página incorrecto. Esperado: {expected_title}, Actual: {driver.title}"

    #Verifica que exista al menos un producto en el inventario, extrae su nombre y precio para mostrarlos en consola
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products)> 0
    first_product = products [0]
    product_name = first_product.find_element(By.CLASS_NAME, 'inventory_item_name')
    product_name = product_name.text
    print(f"    Nombre Producto: {product_name}")
    product_price = first_product.find_element(By.CLASS_NAME, 'inventory_item_price')
    product_price = product_price.text
    print(f"    Precio del producto: {product_price}")

    #Verifica existencia del menú hamburguesa
    buttonMenu = driver.find_element(By.ID, 'react-burger-menu-btn')

    #Verifica existencia del carrito de compras
    cartLink = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')

    #Verifica existencia del filtro de búsqueda
    searchFilter = driver.find_element(By.CLASS_NAME, 'product_sort_container') 
    