from sqlalchemy import Column, Integer, String
from database import Base

class Livro(Base):
    __tablename__ = "livros"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    autor = Column(String, index=True)
    paginas = Column(Integer)
