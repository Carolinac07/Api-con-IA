from fastapi import FastAPI
from routers.animal import router as animal_router
from routers.cuidador import router as cuidador_router
from routers.habitat import router as habitat_router

app = FastAPI()

app.include_router(animal_router)
app.include_router(cuidador_router)
app.include_router(habitat_router)