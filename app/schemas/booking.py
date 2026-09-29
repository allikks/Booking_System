from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.utils.enums import BookingStatus

class BookingCreate(BaseModel):
    resource_id: int
    start_time: datetime
    end_time: datetime

class BookingResponse(BaseModel):
    id: int
    user_id: int
    resource_id: int
    start_time: datetime
    end_time: datetime
    status: BookingStatus

    model_config = ConfigDict(from_attributes=True)