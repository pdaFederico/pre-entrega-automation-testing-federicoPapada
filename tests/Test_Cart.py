#Importaciones
import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from pages.Login_page import LoginPage
from pages.Inventory_page import InventoryPage


#TC-003: Automatización del flujo de compra: Añadir elementos al carrito y verificar presencia

def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.open().login_process("standard_user", "secret_sauce")
    inventory_page.add_tocart()
    badge = inventory_page.badge_count("1")
    assert badge == "1"
    print(f"Test OK: Productos en el carrito: {badge}")
