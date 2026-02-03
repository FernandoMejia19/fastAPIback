from sqlalchemy.orm import Session
from .import models

class MatriculaRepository:
    def _init_(self,db:Session):
        self.db = db

    def find_all(self):
        return self.db.query(models.Matricula).all()

    def save(self, matricula: models.Matricula):
        self.db.add(matricula)
        self.db.commit()
        self.db.refresh(matricula)
        return matricula
