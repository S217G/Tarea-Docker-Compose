from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartParking UBB API", version="1.2")

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
# Esto permite que el contenedor del Frontend pueda consultar a este contenedor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, aquí se pone la URL exacta del Frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

estado_estacionamientos = {
    "A1": "DISPONIBLE",
    "A2": "DISPONIBLE",
    "A3": "DISPONIBLE"
}

@app.post("/api/telemetria")
def recibir_datos(plaza_id: str, estado: str):
    if plaza_id in estado_estacionamientos:
        estado_estacionamientos[plaza_id] = estado
        return {"status": "ok", "mensaje": "Estado actualizado"}
    return {"status": "error", "mensaje": "Plaza no existe"}

@app.get("/api/estado")
def obtener_estado():
    return estado_estacionamientos