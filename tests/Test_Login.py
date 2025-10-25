import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

#Importación de fixtures

from utils.helpers import get_driver, login_test, wait_time


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    print(" \rMantener ventana abierta para revisión...")
    time.sleep(5)
    driver.quit()

#TC-001: Automatización de Login

def test_login(driver):
    login_test(driver)  #Inicia sesión
    assert "/inventory.html" in driver.current_url  #Verifica titulo en la URL al que fue dirigido luego del login
    wait_time(driver)

