from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.resource import Resource
from app.schemas.resource import ResourceCreate

class ResourceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(select(Resource))
        return result.scalars().all()

    async def get_by_id(self, resource_id: int):
        result = await self.db.execute(select(Resource).where(Resource.id == resource_id))
        return result.scalar_one_or_none()

    async def create(self, data: ResourceCreate):
        new_resource = Resource(**data.model_dump())
        self.db.add(new_resource)
        await self.db.commit()
        await self.db.refresh(new_resource)
        return new_resource