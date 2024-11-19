from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar 
@app.post("/livros/", response_model=schemas.Livro)
def criar_livro(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    db_livro = models.Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

# Listar 
@app.get("/livros/", response_model=list[schemas.Livro])
def listar_livros(db: Session = Depends(get_db)):
    return db.query(models.Livro).all()

# Pegar pelo ID
@app.get("/livros/{livro_id}", response_model=schemas.Livro)
def obter_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    return livro

# Atualizar 
@app.put("/livros/{livro_id}", response_model=schemas.Livro)
def atualizar_livro(livro_id: int, livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    for key, value in livro.dict().items():
        setattr(db_livro, key, value)

    db.commit()
    db.refresh(db_livro)
    return db_livro

# Excluir
@app.delete("/livros/{livro_id}")
def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
    db_livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()

    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    db.delete(db_livro)
    db.commit()
    return {"message": "Livro excluído com sucesso"}