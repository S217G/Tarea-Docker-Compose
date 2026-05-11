import requests
import time

print("Iniciando Simulador de Nodo Perimetral (Raspberry Pi)...")
time.sleep(3) # Esperamos 3 segundos para asegurar que el servidor esté listo

# ¡Aquí ocurre la magia! Usamos el NOMBRE del otro contenedor como dirección web
url_servidor = "http://mi-servidor-ubb:8000/api/telemetria?plaza_id=A1&estado=OCUPADO"

try:
    print(f"Enviando datos a {url_servidor}...")
    respuesta = requests.post(url_servidor)
    print("Respuesta del servidor:", respuesta.json())
except Exception as e:
    print("Error de conexión:", e)