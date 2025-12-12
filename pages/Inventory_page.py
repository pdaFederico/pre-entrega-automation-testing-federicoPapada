from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC



class InventoryPage:
    
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_BUTTONS = (By.CSS_SELECTOR, ".inventory_item .btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    FILTER_BUTTON = (By.CLASS_NAME, "product_sort_container") 
    MENU_BUTTON = (By.ID, "react-burger-menu-btn") 
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    def read_title(self):
        
        return self.driver.title
        
    def add_tocart(self):
        """Añade el primer producto disponible al carrito."""
        
        self.driver.find_elements(*self.ADD_BUTTONS)[0].click() 
        return self

    def badge_count(self, expected_value = "1") -> str:
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return badge.text
        except:
            return ""

    def logOut(self):
        """Cierra la sesión del usuario y vuelve a Login."""
        self.driver.find_element(*self.MENU_BUTTON).click()
        # Espera explícita
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
        
        from pages.Login_page import LoginPage
        return LoginPage(self.driver)
    
    def first_product(self) -> dict:
        """
        Verifica la existencia de productos y extrae nombre/precio del primero.
        """
        # 1. Busca todos los productos
        products = self.driver.find_elements(*self.INVENTORY_ITEMS)
        
        # 2. Verifica que haya al menos uno
        if not products:
            return None
        
        # 3. Localización anidada
        first_product = products[0]
        
        name_product = first_product.find_element(*self.PRODUCT_NAME)
        price_product = first_product.find_element(*self.PRODUCT_PRICE)
        
        return {
            "nombre": name_product.text,
            "precio": price_product.text
        }
    
    def ui_check(self) -> bool:
        """
        Verifica la presencia y visibilidad de los elementos clave de la UI.
        Retorna True si todos están visibles, False en caso contrario.
        """
        elements = [
            self.MENU_BUTTON,
            self.ADD_BUTTONS,
            self.FILTER_BUTTON,
        ]
        
        for locator in elements:
            try:
                # Usamos find_element y la verificación is_displayed()
                if not self.driver.find_element(*locator).is_displayed():
                    return False
            except:
                # Si no encuentra el elemento (excepción), la prueba debería fallar
                return False 
        
        return True # Todos los elementos fueron encontrados y están visibles
    
    def go_to_cart(self):
        """Navega a la página del carrito"""
        self.driver.find_element(*self.CART_LINK).click()
        from pages.Checkout_page import CheckoutPage
        return CheckoutPage(self.driver)