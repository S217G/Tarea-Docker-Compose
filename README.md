#  SmartParking UBB - Sistema de Gestión y Predicción Vehicular

Este proyecto es un Sistema de Información Distribuido basado en Edge Computing y Visión Computacional para monitorear la disponibilidad de los estacionamientos en el Campus Concepción de la Universidad del Bío-Bío.

##  Arquitectura del Proyecto (Prototipo Local)

Actualmente, el sistema está orquestado mediante **Docker Compose** y se divide en 3 microservicios principales:

1.  **Frontend (Nginx):** Interfaz web interactiva para visualizar el estado de los estacionamientos en tiempo real.
2.  **Backend (FastAPI):** API RESTful que recibe, procesa y sirve los datos de telemetría.
3.  **Simulador Edge (Python):** Script que emula el comportamiento de una cámara OAK-D enviando datos de ocupación aleatorios.

---

##  Guía de Instalación y Uso (Quickstart)

### Requisitos Previos
* Tener instalado [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/).
* Asegurarse de que el motor de Docker esté corriendo ("Engine running").

### Pasos para Ejecutar
1.  Abre tu terminal en la carpeta principal del proyecto (donde está este archivo).
2.  Ejecuta el siguiente comando para construir y levantar todos los servicios:
    ```bash
    docker-compose up --build
    ```
3.  Espera unos segundos a que la terminal muestre que los servicios están listos.

---

##  Accesos Directos (Links)

Una vez que el sistema esté corriendo, puedes acceder a las diferentes capas mediante los siguientes enlaces:

###  1. Panel de Control (Frontend)
Aquí podrás ver la simulación en vivo de los estacionamientos cambiando de estado.
👉 **[http://localhost:8080](http://localhost:8080)**

### ⚙️ 2. Documentación de la API (Backend)
Interfaz de Swagger UI autogenerada por FastAPI. Aquí puedes ver los "endpoints" y probar envíos manuales de datos.
👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

##  Cómo detener el sistema
Para apagar los servidores y liberar los puertos de tu computadora, presiona `Ctrl + C` en la terminal donde se está ejecutando, o abre una nueva terminal en esta misma carpeta y ejecuta:
```bash
docker-compose down