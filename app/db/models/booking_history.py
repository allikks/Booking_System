from datetime import datetime, timezone
from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Booking(Base):
    __tablename__ = "booking_history"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
