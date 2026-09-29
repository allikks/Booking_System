from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.schemas.booking import BookingCreate, BookingResponse
from app.repositories.booking import BookingRepository
from app.repositories.resource import ResourceRepository
from app.services.booking import BookingService
from app.core.dependencies import get_current_user
from app.db.models.user import User

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingResponse)
async def create_booking(
    payload: BookingCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    service = BookingService(
        booking_repo=BookingRepository(db),
        resource_repo=ResourceRepository(db)
    )
    return await service.make_appointment(user_id=current_user.id, data=payload)

@router.get("/my", response_model=List[BookingResponse])
async def get_my_bookings(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    repo = BookingRepository(db)
    return await repo.get_user_bookings(current_user.id)