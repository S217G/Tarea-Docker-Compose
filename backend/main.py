from fastapi import FastAPI

app = FastAPI(title="SmartParking UBB API (Version Dockerfile)", version="1.0")

@app.get("/")
def read_root():
    return {"mensaje": "¡Servidor SmartParking UBB en línea desde un contenedor individual!"}

@app.post("/api/telemetria")
def recibir_datos(plaza_id: str, estado: str):
    # En el futuro aquí irá el código de PostgreSQL
    return {
        "status": "ok", 
        "plaza": plaza_id, 
        "estado": estado, 
        "mensaje": "Datos recibidos en memoria"
    }