from datetime import datetime, timezone
from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Text, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    resource_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)

    start_time: Mapped[datetime] = mapped_column(DateTime(timezone = True), nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone = True), nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)

    user = relationship("User", back_populates="bookings")
    resource = relationship("Resource", back_populates="bookings")
    history = relationship("History", back_populates="bookings")