import psycopg
from models.models import Cuidador

class CuidadorManager:
    def agregarCuidador(self, cuidador: Cuidador, cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO cuidadores (nombre, edad) VALUES (%s,%s)", (cuidador.nombre, cuidador.edad))
        return "Cuidador creado."
    
    def obtenerCuidador(self, cursor:psycopg.Cursor):
        res = cursor.execute("SELECT id_cuidador, nombre, edad FROM cuidadores").fetchall()
        return [{"id": row [0], "nombre":row [1]} for row in res]
    
    def eliminarCuidador(self,id: int, cursor:psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM cuidadores WHERE id_cuidador = %s", (id,))
        return "Cuidador eliminado."