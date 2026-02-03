from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database, service

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Matricula CRUD FastAPI")


def get_matricual_service(db: Session = Depends(database.get_db)):
    return service.MatriculaService(db)

@app.get("/api/matricula", response_model=List[schemas.Matricula])
def read_matriculas(service: service.MatriculaService = Depends(get_matricual_service)):
    return service.get_all()

@app.post("/api/matricula", response_model=schemas.Matricula, status_code=status.HTTP_201_CREATED)
def create_matricula(matricula: schemas.MatriculaCreate, service: service.MatriculaService = Depends(get_matricual_service)):
    try:
        return service.create(matricula)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))