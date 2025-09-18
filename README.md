# 🚀 Proyecto FastAPI - Usuarios y Libros

Este proyecto es una **API RESTful simple** creada con **FastAPI**, que maneja **Usuarios** y **Libros** con operaciones CRUD usando **SQLite** como base de datos.

---

## 📌 Requisitos

- Python 3.10 o superior  
- pip  
- Git  
- (Opcional para producción) Node.js y pm2  

---

## ⚙️ Instalación y Ejecución en un solo script Bash

```bash
#!/bin/bash
# ==========================
# Proyecto FastAPI - Setup
# ==========================

# Paso 1: Clonar el repositorio
# ------------------------------
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

# Paso 2: Crear y activar entorno virtual
# ---------------------------------------
python3 -m venv venv             # crea el entorno virtual llamado 'venv'
source venv/bin/activate         # activa el entorno virtual en Linux/WSL
# En Windows PowerShell usar: venv\Scripts\Activate.ps1
# Para desactivar después usar: deactivate

# Paso 3: Instalar dependencias
# ------------------------------
pip install -r requirements.txt

# Paquetes principales:
# - fastapi     → framework para crear la API
# - uvicorn     → servidor ASGI para ejecutar la API
# - sqlmodel    → maneja modelos y consultas a la base de datos
# - sqlalchemy  → ORM para interactuar con SQLite

# Paso 4: Ejecutar la API localmente
# ----------------------------------
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# La API estará disponible en:
# - http://localhost:8000
# - Documentación automática: http://localhost:8000/docs

# Nota: El archivo database.db (SQLite) se crea automáticamente al iniciar la API.


# ==========================
# OPCIONAL: Mantener API activa en segundo plano con PM2
# ==========================

# Paso 5.1: Instalar Node.js y pm2
# --------------------------------
sudo apt update
sudo apt install nodejs npm -y
sudo npm install -g pm2

# Paso 5.2: Iniciar la API con pm2
# --------------------------------
pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000" --name fastapi-api

# Paso 5.3: Comandos útiles de pm2
# --------------------------------
pm2 status               # muestra estado de todas las apps
pm2 logs                 # muestra los registros en tiempo real
pm2 restart fastapi-api  # reinicia el proceso
pm2 stop fastapi-api     # detiene el proceso
pm2 delete fastapi-api   # elimina el proceso de pm2

# Paso 5.4: Arranque automático al reiniciar la máquina
# -----------------------------------------------------
pm2 save
pm2 startup
