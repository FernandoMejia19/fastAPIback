from sqlalchemy.orm import Session
from . import models, schemas
from .repository import MatriculaRepository


class MatriculaService:

    def _init_(self,db:Session):
        self.repo = MatriculaRepository(db)
    
    def get_all(self):
        return self.repo.find_all()
    
    def create(self,matricula_data:schemas.MatriculaCreate):
        matricula=models.Matricula(**matricula_data.model_dump())
        valor=(matricula_data.valor_comercial*2.5)/100
        if(matricula_data.fabricacion<2010):
            adicional=(valor*10)/100
            valor=adicional+valor
        codigo=matricula_data.placa[0]+matricula_data.placa[1]+matricula_data.placa[2]+str(len(matricula_data.propietario))+str(matricula_data.fabricacion[4])
        matricula.impuesto=valor
        matricula.codigo_revision=codigo
        return self.repo.save(matricula)