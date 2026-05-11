# 1. Usar una imagen oficial de Python ligera
FROM python:3.11-slim

# 2. Crear y establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requerimientos
COPY requirements.txt .

# 4. Instalar las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código fuente (main.py) al contenedor
COPY . .

# 6. Exponer el puerto que usará FastAPI
EXPOSE 8000

# 7. Comando para arrancar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]