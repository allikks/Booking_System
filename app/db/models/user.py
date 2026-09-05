from datetime import datetime, timezone
from sqlalchemy import Boolean, DateTime, Enum, Integer, string, Column, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.base import Base
from app.utils.enums import UserRole


class User(Base):
    __tablename__ = "user"

    id: int = mapped_column(Column(Integer, primary_key=True, autoincrement=True))
    username: str = mapped_column(Column(String, unique=True))
    email: str = mapped_column(Column(String, unique=True))
    password: str = mapped_column(Column(String(55), unique=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc)
    )

    bookings = relationship("Booking", back_populates="user")