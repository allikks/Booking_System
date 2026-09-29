from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.schemas.resource import ResourceCreate, ResourceResponse
from app.repositories.resource import ResourceRepository

router = APIRouter(prefix="/resources", tags=["Specialists"])

@router.get("/", response_model=List[ResourceResponse])
async def list_specialists(db: AsyncSession = Depends(get_db)):
    repo = ResourceRepository(db)
    return await repo.get_all()

@router.post("/", response_model=ResourceResponse)
async def add_specialist(payload: ResourceCreate, db: AsyncSession = Depends(get_db)):
    repo = ResourceRepository(db)
    return await repo.create(payload)