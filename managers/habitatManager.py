import psycopg
from models.models import Habitat

class HabitatManager:
    def agregarHabitat(self, habitat: Habitat, cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO habitats (nombre, id_animal, id_cuidador) VALUES (%s,%s,%s)", (habitat.nombre, habitat.id_animal, habitat.id_cuidador))
        return "Habitat creado."
    
    def obtenerHabitat(self, cursor:psycopg.Cursor):
        res = cursor.execute("SELECT * FROM habitats").fetchall()
        return res
    
    def ActualizarHabitat(self, habitat: Habitat, cursor:psycopg.Cursor):
        cursor.execute("UPDATE habitats SET nombre = %s, id_animal = %s, id_cuidador =%s WHERE id_habitat = %s", (habitat.nombre, habitat.id_animal, habitat.id_cuidador, habitat.id_habitat))
        return "Habitat Actualizado."

    