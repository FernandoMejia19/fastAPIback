from pydantic import BaseModel
from typing import Optional

class MatriculaBase (BaseModel):
    placa:str
    propietario:str
    marca:str
    fabricacion:int
    valor_comercial:float

class MatriculaCreate(MatriculaBase):
    pass

class Matricula (MatriculaBase):
    pass

class Config:
    from_attributes=True