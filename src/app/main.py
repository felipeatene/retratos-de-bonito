from fastapi import FastAPI
from app.routers import photos, people, public, consents, stories

app = FastAPI(
    title="Retratos de Bonito",
    description="API de preservação da memória fotográfica de Bonito-MS",
    version="0.1.0"
)

app.include_router(photos.router)
app.include_router(people.router)
app.include_router(public.router)
app.include_router(consents.router)
app.include_router(stories.router)
