from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.repositories.user import UserRepository
from app.services.auth import AuthService
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import Token, LoginRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
async def register(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    service = AuthService(UserRepository(db))
    return await service.register(payload)

@router.post("/login", response_model=Token)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(UserRepository(db))
    return await service.authenticate(payload.email, payload.password)