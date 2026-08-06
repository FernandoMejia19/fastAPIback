from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database, service
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Matricula CRUD FastAPI")

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # quién puede acceder
    allow_credentials=True,
    allow_methods=["*"],    # GET, POST, PUT, DELETE
    allow_headers=["*"],    # todos los headers
)


def get_matricula_service(db: Session = Depends(database.get_db)):
    return service.MatriculaService(db)

@app.get("/api/matricula", response_model=List[schemas.MatriculaResponse])
def read_matriculas(service: service.MatriculaService = Depends(get_matricula_service)):
    return service.get_all()

@app.post("/api/matricula", response_model=schemas.Matricula, status_code=status.HTTP_201_CREATED)
def create_matricula(matricula: schemas.MatriculaCreate, service: service.MatriculaService = Depends(get_matricula_service)):
    try:
        return service.create(matricula)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))