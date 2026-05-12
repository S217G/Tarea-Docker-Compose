import requests
import time
import random

print("Iniciando Simulador de Nodos (Cámaras OAK-D)...")
time.sleep(3) # Esperar a que la API inicie

plazas = ["A1", "A2", "A3"]
estados = ["OCUPADO", "DISPONIBLE"]

while True:
    # Elegir una plaza y un estado al azar
    plaza_elegida = random.choice(plazas)
    estado_elegido = random.choice(estados)
    
    url_servidor = f"http://mi-servidor-ubb:8000/api/telemetria?plaza_id={plaza_elegida}&estado={estado_elegido}"
    
    try:
        print(f"Camara detecta: {plaza_elegida} -> {estado_elegido}")
        requests.post(url_servidor)
    except Exception as e:
        print("Error de conexión...", e)
        
    # Esperar 4 segundos antes del siguiente escaneo simulado
    time.sleep(4)