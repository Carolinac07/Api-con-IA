import psycopg
from models.models import Animal, Cuidador, Habitat
from dotenv import load_dotenv

class DB:
    
    def AgregarAnimal(self, animal: Animal, cursor:psycopg.Cursor):
       cursor.execute("INSERT INTO animales (nombre, especie, edad) VALUES (%s,%s,%s)", (animal.nombre, animal.especie, animal.edad))
       return {"msg" : "Animal agregado."}

    def ObtenerAnimal(self, cursor:psycopg.Cursor):
        cursor.execute("SELECT * FROM animales")
        return {"msg" : "Animales obtenidos."}
    
    def EliminarAnimal(self, animal: Animal, cursor:psycopg.Cursor):
        cursor.execute("DELETE FROM animales WHERE nombre = %s AND especie = %s AND edad = %s", (animal.nombre, animal.especie, animal.edad))
        return {"msg" : "Animal eliminado."}



    def AgregarCuidador(self, cuidador: Cuidador, cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO cuidadores (nombre, edad) VALUES (%s,%s)", (cuidador.nombre, cuidador.edad))
        return {"msg" : "Cuidador agregado."}

    def ObtenerCuidador(self, cursor:psycopg.Cursor):
        cursor.execute("SELECT * FROM cuidadores")
        return {"msg" : "Cuidadores obtenidos."}
    
    def EliminarCuidador(self, id_cuidador: int, cursor: psycopg.Cursor):
        cursor.execute("DELETE FROM cuidadores WHERE id_cuidador = %s", (id_cuidador,))
        return {"msg": "Cuidador eliminado."}
    
    

    def AgregarHabitat(self, habitat: Habitat, cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO habitats (nombre, id_animal, id_cuidador) VALUES (%s,%s,%s)", (habitat.nombre, habitat.id_animal, habitat.id_cuidador))
        return {"msg" : "Habitat agregado."}
    
    def ObtenerHabitat(self, cursor:psycopg.Cursor):
        cursor.execute("SELECT * FROM habitats")
        return {"msg" : "Habitats obtenidos."}
    
    def ActualizarHabitat(self, habitat_id: int, habitat: Habitat, cursor: psycopg.Cursor):
        cursor.execute(
        "UPDATE habitats SET nombre = %s, id_animal = %s, id_cuidador = %s WHERE id_habitat = %s",(habitat.nombre, habitat.id_animal, habitat.id_cuidador, habitat_id))
        return {"msg": "Hábitat actualizado."}