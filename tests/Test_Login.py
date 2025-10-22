import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import get_driver, login_test

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

#Ingreso al sitio

def test_login(driver):
    login_test(driver)
    assert "inventory" in driver.current_url
    time.sleep(5)