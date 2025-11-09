from fastapi import APIRouter, Depends
from managers.conexionManagerSupaBase import getCursor
from models.models import Cuidador
from db.db import DB
import psycopg 

db = DB()

router = APIRouter(prefix="/cuidador", tags=["Cuidador"])

@router.post("/agregar_cuidador")
async def agregar_cuidador (cuidador: Cuidador, cursor:psycopg.Cursor=Depends(getCursor)):
    res = db.AgregarCuidador (cuidador, cursor)
    return res

@router.get("/obtener_cuidador")
async def obtener_cuidador (cursor:psycopg.Cursor=Depends(getCursor)):
    res = db.ObtenerCuidador (cursor)
    return res

@router.delete("/eliminar/{id_cuidador}")
async def eliminar_cuidador(id_cuidador: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return db.EliminarCuidador(id_cuidador, cursor)