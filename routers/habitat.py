from fastapi import APIRouter, Depends
import psycopg 
from db.db import DB
from managers.conexionManagerSupaBase import getCursor
from models.models import Habitat 

db = DB()

router = APIRouter(prefix="/habitat", tags=["Habitat"])

@router.post("/crear_habitat")
async def crear_habitat(habitat: Habitat, cursor: psycopg.Cursor = Depends(getCursor)):
    return db.AgregarHabitat(habitat, cursor)


@router.get("/obtener_habitats")
async def obtener_habitats(cursor:psycopg.Cursor = Depends (getCursor)):
    return db.ObtenerHabitat(cursor)

@router.put("/actualizar_habitat/{habitat_id}")
async def actualizar_habitat(habitat_id: int, habitat: Habitat, cursor: psycopg.Cursor = Depends(getCursor)):
    return db.ActualizarHabitat(habitat_id, habitat, cursor)