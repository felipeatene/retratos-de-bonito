from app.database import engine, Base
from app.models import (
    collection,
    photo,
    person,
    location,
    event,
    photo_person,
    photo_event,
    consent,
    audit_log
)

Base.metadata.create_all(bind=engine)
print("Banco criado com sucesso.")
