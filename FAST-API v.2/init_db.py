from db import get_connection

def crear_tablas():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        email VARCHAR(100)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(200),
        autor VARCHAR(100)
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Tablas creadas correctamente")

if __name__ == "__main__":
    crear_tablas()
