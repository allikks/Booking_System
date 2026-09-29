from fastapi import HTTPException
from app.repositories.booking import BookingRepository
from app.repositories.resource import ResourceRepository
from app.schemas.booking import BookingCreate

class BookingService:
    def __init__(self, booking_repo: BookingRepository, resource_repo: ResourceRepository):
        self.booking_repo = booking_repo
        self.resource_repo = resource_repo

    async def make_appointment(self, user_id: int, data: BookingCreate):
        if data.start_time >= data.end_time:
            raise HTTPException(status_code=400, detail="Время начала должно быть раньше времени окончания")


        doctor = await self.resource_repo.get_by_id(data.resource_id)
        if not doctor:
            raise HTTPException(status_code=404, detail="Специалист не найден")


        conflict = await self.booking_repo.has_conflict(data.resource_id, data.start_time, data.end_time)
        if conflict:
            raise HTTPException(status_code=409, detail="У специалиста это время уже занято")

        return await self.booking_repo.create(
            user_id=user_id,
            resource_id=data.resource_id,
            start=data.start_time,
            end=data.end_time
        )