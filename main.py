# main.py (archivo único, simple y funcional)
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select

DATABASE_URL = "sqlite:///./database.db"
# SQLite necesita check_same_thread=False cuando se usa desde uvicorn (hilos)
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(title="API mínima - Usuarios y Libros")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- CRUD Usuarios ---
@app.post("/usuarios/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.get("/usuarios/", response_model=List[User])
def list_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()

@app.get("/usuarios/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@app.put("/usuarios/{user_id}", response_model=User)
def update_user(user_id: int, updated: User, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    user.name = updated.name
    user.email = updated.email
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.delete("/usuarios/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    session.delete(user)
    session.commit()
    return {"ok": True}

# --- CRUD Libros ---
@app.post("/libros/", response_model=Book)
def create_book(book: Book, session: Session = Depends(get_session)):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@app.get("/libros/", response_model=List[Book])
def list_books(session: Session = Depends(get_session)):
    return session.exec(select(Book)).all()

@app.get("/libros/{book_id}", response_model=Book)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return book

@app.put("/libros/{book_id}", response_model=Book)
def update_book(book_id: int, updated: Book, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    book.title = updated.title
    book.author = updated.author
    book.owner_id = updated.owner_id
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@app.delete("/libros/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    session.delete(book)
    session.commit()
    return {"ok": True}
