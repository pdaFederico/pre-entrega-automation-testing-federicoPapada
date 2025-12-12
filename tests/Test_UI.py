#Importación
import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from pages.Login_page import LoginPage
from pages.Inventory_page import InventoryPage

#TC-002: Automatización para verificar UI: Título de página, inventario y presencia de elementos criticos

def test_interface(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage (driver)                                 
    login_page.open().login_process("standard_user", "secret_sauce")     
    assert "/inventory.html" in driver.current_url
    expected_title = "Swag Labs"                        
    actual_title = inventory_page.read_title()
    assert actual_title == expected_title, f"Título incorrecto. Esperado: {expected_title}, Actual: {actual_title}"

    product_data = inventory_page.first_product()
    
    # Verifica que haya productos
    assert product_data is not None, "Error: No se encontraron productos en el inventario."

    # Muestra los datos extraídos
    print(f"\nTest OK: Datos del Primer Producto:")
    print(f"    Nombre Producto: {product_data['nombre']}")
    print(f"    Precio del producto: {product_data['precio']}")

    # VALIDACIÓN DE ELEMENTOS CRÍTICOS (Menú, Carrito, Filtros, Footer)
    
    # Usa el método de la página que verifica todos los elementos a la vez
    ui_check = inventory_page.ui_check()
    
    assert ui_check is True, "Error: Faltan elementos críticos de la interfaz (Menú, Carrito, Filtros)."
    
    print("Test OK: Todos los elementos críticos de la interfaz están visibles.")
    