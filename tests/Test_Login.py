#Importación
import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from pages.Login_page import LoginPage

#TC-001: Automatización de Login

def test_login(driver):
    Login_page = LoginPage(driver)
    Login_page.open().login_process("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url  #Verifica que luego del Login se diriga a la URL correcta.
    




