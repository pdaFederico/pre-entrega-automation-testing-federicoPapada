import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import get_driver, login_test, wait_time

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    print("\nMantener ventana abierta para revisión...")
    time.sleep(5)
    driver.quit()

#Ingreso al sitio

def test_login(driver):
    login_test(driver)
    assert "/inventory.html" in driver.current_url
    wait_time(driver)

