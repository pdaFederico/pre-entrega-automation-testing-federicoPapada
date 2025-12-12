#Importación
import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from pages.Login_page import LoginPage
from pages.Inventory_page import InventoryPage
import pages.Checkout_page as checkout_module
checkout_page = checkout_module.CheckoutPage

def test_clearcart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # LOGIN Y AÑADIR PRODUCTO
    login_page.open().login_process("standard_user", "secret_sauce")
    inventory_page.add_tocart()
    
    # VERIFICACIÓN: Contar productos (debería ser 1)
    badge_before_remove = inventory_page.badge_count("1")
    assert badge_before_remove == "1", "Error: El producto no se añadió correctamente."
    print("✅ Producto añadido al carrito.")
    
    # NAVEGAR AL CARRITO
    
    checkout_page = inventory_page.go_to_cart()
    
    # ELIMINAR PRODUCTO
    checkout_page.remove_first_item()
    print("✅ Producto eliminado del carrito.")
    
    
    # Verificar que el elemento del producto ya no está presente
    is_present = checkout_page.is_item_present()
    assert is_present is False, "Error: El producto eliminado sigue visible en el carrito."
    
    # Verificar que el badge del carrito desaparezca
    badge_after_remove = inventory_page.badge_count("")
    assert badge_after_remove == "", "Error: El contador del carrito (badge) no se ha actualizado o desaparecido."
    
    print("Test OK: El producto fue eliminado correctamente del carrito.")