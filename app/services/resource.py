from app.repositories.resource import ResourceRepository
from app.schemas.resource import ResourceCreate

class ResourceService:
    def __init__(self, resource_repo: ResourceRepository):
        self.resource_repo = resource_repo

    async def get_all_specialists(self):
        return await self.resource_repo.get_all()

    async def add_specialist(self, data: ResourceCreate):
        return await self.resource_repo.create(data)