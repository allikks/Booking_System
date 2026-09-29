from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from datetime import datetime
from app.db.models.booking import Booking
from app.utils.enums import BookingStatus

class BookingRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def has_conflict(self, resource_id: int, start: datetime, end: datetime) -> bool:
        # Проверяем, свободен ли специалист на этот интервал
        query = select(Booking).where(
            and_(
                Booking.resource_id == resource_id,
                Booking.status != BookingStatus.CANCELLED,
                Booking.start_time < end,
                Booking.end_time > start
            )
        )
        result = await self.db.execute(query)
        return result.scalars().first() is not None

    async def create(self, user_id: int, resource_id: int, start: datetime, end: datetime):
        booking = Booking(
            user_id=user_id,
            resource_id=resource_id,
            start_time=start,
            end_time=end,
            status=BookingStatus.CONFIRMED
        )
        self.db.add(booking)
        await self.db.commit()
        await self.db.refresh(booking)
        return booking

    async def get_user_bookings(self, user_id: int):
        result = await self.db.execute(select(Booking).where(Booking.user_id == user_id))
        return result.scalars().all()