from fastapi import FastAPI
from app.routers import photos

app = FastAPI(
    title="Retratos de Bonito",
    description="API de preservação da memória fotográfica de Bonito-MS",
    version="0.1.0"
)

app.include_router(photos.router)
