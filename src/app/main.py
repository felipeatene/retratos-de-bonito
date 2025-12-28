from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import photos, people, public, consents, stories, auth
from app.database import SessionLocal
from app.repositories.user_repository import ensure_default_roles


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicialização e finalização da aplicação."""
    # Startup: garantir que papéis padrão existam
    db = SessionLocal()
    try:
        ensure_default_roles(db)
    finally:
        db.close()
    
    yield
    
    # Shutdown: limpeza se necessário


app = FastAPI(
    title="Retratos de Bonito",
    description="API de preservação da memória fotográfica de Bonito-MS",
    version="0.1.0",
    lifespan=lifespan
)

# Allow frontend running on localhost:3000 to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(photos.router)
app.include_router(people.router)
app.include_router(public.router)
app.include_router(consents.router)
app.include_router(stories.router)
