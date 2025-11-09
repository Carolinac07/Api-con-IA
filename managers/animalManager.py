import psycopg
from models.models import Animal

class AnimalManager:
    def agregarAnimal(self, animal: Animal, cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO animales (nombre, especie, edad) VALUES (%s,%s,%s)", (animal.nombre, animal.especie, animal.edad))
        return "Animal creado."
    
    def obtenerAnimal(self, cursor:psycopg.Cursor):
        res = cursor.execute("SELECT id_animal, nombre, especie, edad FROM animales").fetchall()
        return [{"id": row [0], "nombre":row [1], "especie": row [2], "edad": row[3]} for row in res]
    
    def eliminarAnimal(self, nombre: str, cursor:psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM animales WHERE nombre = %s", (nombre,))
        return "Animal eliminado."