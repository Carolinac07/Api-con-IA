from pydantic import BaseModel

class Animal(BaseModel):
    nombre: str
    especie: str
    edad: int
    
class Cuidador(BaseModel):
    nombre: str
    edad: int
    
class Habitat(BaseModel):
    nombre: str
    id_animal: int
    id_cuidador: int