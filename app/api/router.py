from fastapi import APIRouter
from app.api.routers import auth, users, resources, bookings

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(resources.router)
api_router.include_router(bookings.router)