import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    service = ChromeService(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=chrome_options)
    driver_instance.implicitly_wait(2)
    yield driver_instance
    
    WAIT_TIME = 5
    print(f"\nVentana abierta por {WAIT_TIME} segundos para revisión...")
    time.sleep(WAIT_TIME)
    
    try:
        driver_instance.quit()
    except Exception as e:
        print(f"Advertencia durante driver.quit(): {e}")

#Carga los datos de prueba desde el JSON

def test_data():
    
    # 🛑 Ajusta la ruta si tu archivo JSON no está en la raíz 🛑
    # Si lo pusiste en 'config/test_data.json', cambia la ruta a 'config/test_data.json'
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'utils/test_data.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        pytest.fail(f"Archivo de datos no encontrado en: {file_path}")
    except json.JSONDecodeError:
        pytest.fail(f"Error al decodificar JSON en: {file_path}")