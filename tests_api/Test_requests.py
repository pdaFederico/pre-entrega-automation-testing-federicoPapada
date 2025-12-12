import pytest
import requests
import json
import time
from datetime import datetime

BASE_URL = "https://jsonplaceholder.typicode.com/"

# Datos fijos
POST_PAYLOAD = {
    'title': 'TT Automatización - Post de Prueba Proyecto Final',
    'body': 'Generado para validar métodos.',
    'userId': 99
}

class TestJSONPlaceholder:

    pytestmark = pytest.mark.api

# --- 1: GET (Obtener recurso) ---

    def test_get_single_post(self):
        """
        Verifica obtención exitosa del Post ID 1
        """
        post_id = 1
        url = f"{BASE_URL}posts/{post_id}"

        # Solicitud
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        # Validación
        assert response.status_code == 200, \
            f"Error: Esperado 200, obtenido {response.status_code}"

        # Validación de Cabeceras
        assert 'application/json' in response.headers.get('Content-Type', ''), \
            "Error de Cabecera: Content-Type no es application/json."

        # Convertir a JSON
        body = response.json()

        # Validación de Contenido y Estructura
        expected_keys = {'id', 'title', 'body', 'userId'}
        assert expected_keys.issubset(set(body.keys())), \
            "Error de Estructura: Faltan claves esenciales en la respuesta JSON."
            
        assert body['id'] == post_id, \
            f"Error de Contenido: ID esperado {post_id}, obtenido {body['id']}"

        # Validación de Tiempo de Respuesta
        response_time = end_time - start_time
        assert response_time < 1.0, \
            f"Error de Performance: El tiempo de respuesta ({response_time:.3f}s) excede el límite de 1.0s."

        print(f"\n✅ Test GET exitoso para Post ID {post_id}.")

# --- 2: POST (Crear recurso) ---

    def test_post_create_resource(self):
        """
        Verifica la creación exitosa de un nuevo post, validando el código 201 y los datos reflejados.
        """
        url = f"{BASE_URL}posts"
        
        # Solicitud
        start_time = time.time()
        response = requests.post(url, json=POST_PAYLOAD)
        end_time = time.time()
        
        # Validación de Código
        assert response.status_code == 201, \
            f"Error: Esperado 201, obtenido {response.status_code}"
            
        # Validación de Cabeceras
        assert 'application/json' in response.headers.get('Content-Type', ''), \
            "Error de Cabecera: Content-Type no es application/json."
            
        # Convertir a JSON
        new_post = response.json()
        
        # Validación de Contenido y Estructura
        
        assert new_post['title'] == POST_PAYLOAD['title'], \
            "Error: El título en la respuesta no coincide con el enviado."
        
        # Verificar generación del nuevo ID
        assert 'id' in new_post and isinstance(new_post['id'], int), \
            "Error: No se generó un ID válido para el nuevo post."
            
        # 5. Validación tiempo respuesta
        response_time = end_time - start_time
        assert response_time < 1.5, \
            f"Error: Tiempo de respuesta ({response_time:.3f}s) excede el límite de 1.5s."

        print(f"✅ Test POST exitoso. Nuevo recurso creado con ID: {new_post.get('id')}.")

# --- 3: DELETE (Eliminar recurso) ---

    def test_delete_resource(self):
        """
        Verifica la eliminación exitosa
        """
        post_id_to_delete = 1
        url = f"{BASE_URL}posts/{post_id_to_delete}"
        
        # Solicitud
        start_time = time.time()
        response = requests.delete(url)
        end_time = time.time()
        
        # Validación de Código de Estado
        assert response.status_code in [200, 204], \
            f"Error: Esperado 200 o 204, obtenido {response.status_code}"
            
        # Validación de Cabeceras
        if response.status_code == 204:
            assert response.text == "", "El cuerpo de la respuesta 204 debe estar vacío."
        elif response.status_code == 200:
            # JSONPlaceholder devuelve un cuerpo JSON vacío {} con 200
            assert response.json() == {}, "El cuerpo de la respuesta 200 debe ser un JSON vacío {}."

        # Validación tiempo de respuesta
        response_time = end_time - start_time
        assert response_time < 0.8, \
            f"Error: El tiempo de respuesta ({response_time:.3f}s) excede el límite de 0.8s."
            
        print(f"✅ Test DELETE exitoso para Post ID {post_id_to_delete}.")