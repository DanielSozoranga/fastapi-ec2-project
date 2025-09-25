from fastapi import FastAPI
from db import get_connection

app = FastAPI(title="API FastAPI + PostgreSQL RDS")

# -----------------
# RUTA DE PRUEBA
# -----------------
@app.get("/")
def root():
    return {"msg": "🚀 API FastAPI conectada a PostgreSQL en RDS"}

# -----------------
# CRUD USUARIOS
# -----------------
@app.post("/usuarios/")
def crear_usuario(nombre: str, email: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO usuarios (nombre, email) VALUES (%s, %s) RETURNING *;",
        (nombre, email)
    )
    nuevo = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"usuario": nuevo}

@app.get("/usuarios/")
def listar_usuarios():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios;")
    usuarios = cur.fetchall()
    cur.close()
    conn.close()
    return {"usuarios": usuarios}

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = %s;", (usuario_id,))
    usuario = cur.fetchone()
    cur.close()
    conn.close()
    if usuario:
        return {"usuario": usuario}
    return {"error": "Usuario no encontrado"}

@app.delete("/usuarios/{usuario_id}")
def borrar_usuario(usuario_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s RETURNING *;", (usuario_id,))
    eliminado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if eliminado:
        return {"usuario_eliminado": eliminado}
    return {"error": "Usuario no encontrado"}

# -----------------
# CRUD LIBROS
# -----------------
@app.post("/libros/")
def crear_libro(titulo: str, autor: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO libros (titulo, autor) VALUES (%s, %s) RETURNING *;",
        (titulo, autor)
    )
    nuevo = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"libro": nuevo}

@app.get("/libros/")
def listar_libros():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM libros;")
    libros = cur.fetchall()
    cur.close()
    conn.close()
    return {"libros": libros}
