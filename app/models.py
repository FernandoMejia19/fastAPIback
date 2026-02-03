from sqlalchemy import Column, String,Integer,Float
from .database import Base

class Matricula(Base):
    __tablename__="matriculas"

    placa=Column(String,primary_key=True,index=True) 
    propietario=Column(String, nullable=False)
    marca=Column(String, nullable=False)
    fabricacion =Column(Integer, nullable=False)
    valor_comercial =Column(Float, nullable=False)
    impuesto =Column(Float, nullable=False)
    codigo_revision =Column(String, nullable=False)

    def _repr_(self):
        return f"<Matricula(placa={self.placa},propietario={self.propietario}),marca={self.marca},fabricacion={self.fabricacion},valor_comercial={self.valor_comercial},impuesto={self.valor_comercial},codigo_revision={self.codigo_revision}"