from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    CART_CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    THANK_YOU_HEADER = (By.CLASS_NAME, "complete-header")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".cart_item button[name^='remove-']")

    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    def navegar_al_checkout(self):
        """Hace clic en el botón 'Checkout' desde la vista del carrito."""
        self.wait.until(EC.element_to_be_clickable(self.CART_CHECKOUT_BUTTON)).click()
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        return self

    def user_info(self, nombre, apellido, cp):
        """Llena los campos de información de envío."""
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(nombre)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(apellido)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(cp)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def finalizar_compra(self):
        """Hace clic en el botón 'Finish' en la página de resumen."""
        self.driver.find_element(*self.FINISH_BUTTON).click()
        return self

    def obtener_mensaje_confirmacion(self) -> str:
        """Obtiene el mensaje de agradecimiento de la compra finalizada."""
        return self.driver.find_element(*self.THANK_YOU_HEADER).text
    
    def remove_first_item(self):
        """Elimina el primer producto que se encuentra en el carrito."""
        
        # En el carrito, busca todos los botones de remover y hace clic en el primero
        self.driver.find_elements(*self.REMOVE_BUTTON)[0].click()
        return self
    
    def is_item_present(self) -> bool:
        """Verifica si todavía hay productos en el carrito."""
        # Intenta encontrar cualquier elemento de producto en el carrito.
        # En SauceDemo, si el producto se elimina, el elemento desaparece.
        try:
            item = self.driver.find_element(By.CLASS_NAME, "cart_item")
            return item.is_displayed()
        except:
            return False # Si no se encuentra el elemento, no hay productos.