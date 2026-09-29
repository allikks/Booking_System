from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.router import api_router
from app.db.base import Base
from app.db.session import engine

import app.db.models.user
import app.db.models.resource
import app.db.models.booking
import app.db.models.booking_history

@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Clinic Booking System", version="1.0.0", lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")