# Importación
import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from pages.Login_page import LoginPage
from pages.Inventory_page import InventoryPage
import pages.Checkout_page as checkout_module
checkout_page = checkout_module.CheckoutPage 

def test_finish_purchase(driver,):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Datos de prueba de ejemplo
    TEST_USER_DATA = {
        "nombre": "Test",
        "apellido": "UserTT",
        "cp": "C100"
    }

    login_page.open().login_process("standard_user", "secret_sauce")
    inventory_page.add_tocart()

    print("\n✅ Producto añadido. Iniciando Checkout...")

    # Navegar al Carrito y obtener la instancia de CheckoutPage
    checkout_page = inventory_page.go_to_cart()

    # Iniciar Checkout 
    checkout_page.navegar_al_checkout()

    # Ingresar Información del Usuario
    checkout_page.user_info(
        TEST_USER_DATA["nombre"],
        TEST_USER_DATA["apellido"],
        TEST_USER_DATA["cp"]
    )

    # Finalizar la Compra
    checkout_page.finalizar_compra()
