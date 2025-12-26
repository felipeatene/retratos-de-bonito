from pydantic import BaseModel
from typing import Optional
from app.models.enums import ConsentType


class CreateConsentRequest(BaseModel):
    consent_type: ConsentType
    consent_date: Optional[str] = None
    notes: Optional[str] = None
