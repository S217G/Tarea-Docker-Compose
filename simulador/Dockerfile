FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# En lugar de levantar un servidor, este contenedor solo ejecuta el script una vez
CMD ["python", "script.py"]