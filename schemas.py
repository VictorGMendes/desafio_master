from pydantic import BaseModel

class LivroBase(BaseModel):
    nome: str
    autor: str
    paginas: int

class LivroCreate(LivroBase):
    pass

class Livro(LivroBase):
    id: int

    class Config:
        orm_mode = True
