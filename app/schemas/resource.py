from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.utils.enums import SpecialistType

class ResourceBase(BaseModel):
    name: str
    specialization: SpecialistType
    room_number: Optional[str] = None

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)