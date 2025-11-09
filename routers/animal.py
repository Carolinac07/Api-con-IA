from fastapi import APIRouter,Depends
import psycopg
from managers.conexionManagerSupaBase import getCursor
from models.models import Animal
from db.db import DB


db = DB()

router= APIRouter (prefix="/animal", tags=["Animales"])

@router.post ("/crear_animal")
async def crear_animal (animal: Animal, cursor:psycopg.Cursor=Depends(getCursor)):
    res = db.AgregarAnimal(animal, cursor)
    return res

@router.get("/obtener_animal")
async def obtener_animales(cursor: psycopg.Cursor = Depends(getCursor)):
    return db.ObtenerAnimal(cursor)


@router.delete("/eliminar_animal/{id_animal}")
async def eliminar_animal(id_animal: int, cursor: psycopg.Cursor = Depends(getCursor)):
    cursor.execute("DELETE FROM animales WHERE id_animal = %s", (id_animal,))
    return {"msg": "Animal eliminado."}