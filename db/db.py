import psycopg
from models.models import Animal, Cuidador, Habitat
from dotenv import load_dotenv

class DB:
    
    def AgregarAnimal(self, animal: Animal, cursor:psycopg.Cursor):
       cursor.execute("INSERT INTO animales (nombre, especie, edad) VALUES (%s,%s,%s)", (animal.nombre, animal.especie, animal.edad))
       return {"msg" : "Animal agregado."}
    
    def ObtenerAnimal(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT id_animal, nombre, especie, edad FROM animales")
        rows = cursor.fetchall()
        return [
        {
            "id_animal": row[0],
            "nombre": row[1],
            "especie": row[2],
            "edad": row[3]
        }
        for row in rows
    ]
    
    def EliminarAnimal(self, animal: Animal, cursor:psycopg.Cursor):
        cursor.execute("DELETE FROM animales WHERE nombre = %s AND especie = %s AND edad = %s", (animal.nombre, animal.especie, animal.edad))
        return {"msg" : "Animal eliminado."}



    def AgregarCuidador(self, cuidador: Cuidador, cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO cuidadores (nombre, edad) VALUES (%s,%s)", (cuidador.nombre, cuidador.edad))
        return {"msg" : "Cuidador agregado."}
    
    def ObtenerCuidador(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT id_cuidador, nombre, edad FROM cuidadores")
        rows = cursor.fetchall()
        return [
        {
            "id_cuidador": row[0],
            "nombre": row[1],
            "edad": row[2]
        }
        for row in rows
    ]
    
    def EliminarCuidador(self, id_cuidador: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM cuidadores WHERE id_cuidador = %s", (id_cuidador,))
        return {"msg": "Cuidador eliminado."}
    
    

    def AgregarHabitat(self, habitat: Habitat, cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO habitats (nombre, id_animal, id_cuidador) VALUES (%s,%s,%s)", (habitat.nombre, habitat.id_animal, habitat.id_cuidador))
        return {"msg" : "Habitat agregado."}
    
    def ObtenerHabitat(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT id_habitat, nombre, id_animal, id_cuidador FROM habitats")
        rows = cursor.fetchall()
        return [
        {
            "id_habitat": row[0],
            "nombre": row[1],
            "id_animal": row[2],
            "id_cuidador": row[3]
        }
        for row in rows
    ]
    
    def ActualizarHabitat(self, habitat_id: int, habitat: Habitat, cursor: psycopg.Cursor):
        cursor.execute(
        "UPDATE habitats SET nombre = %s, id_animal = %s, id_cuidador = %s WHERE id_habitat = %s",(habitat.nombre, habitat.id_animal, habitat.id_cuidador, habitat_id))
        return {"msg": "Hábitat actualizado."}