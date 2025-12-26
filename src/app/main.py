from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import photos, people, public, consents, stories

app = FastAPI(
    title="Retratos de Bonito",
    description="API de preservação da memória fotográfica de Bonito-MS",
    version="0.1.0"
)

# Allow frontend running on localhost:3000 to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(photos.router)
app.include_router(people.router)
app.include_router(public.router)
app.include_router(consents.router)
app.include_router(stories.router)
