import time
import pytest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import get_driver, login_test, wait_time

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    print("\nMantener ventana abierta para revisión...")
    time.sleep(5)
    driver.quit()

def test_interface(driver):
    login_test(driver)
    wait_time(driver)
    assert "/inventory.html" in driver.current_url
    expected_title = "Swag Labs"
    assert driver.title == expected_title, f"Título de página incorrecto. Esperado: {expected_title}, Actual: {driver.title}"
    products = driver.find_elements(By.CLASS_NAME, 'inventory_list')
    assert len(products)> 0