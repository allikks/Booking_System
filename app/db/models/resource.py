from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Resource(Base):
    __tablename__ = 'resource'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String) # имя специалиста
    capacity: Mapped[int] = mapped_column(Integer, default=1, nullable=False) #по умолчанию один клиент

    bookings = relationship("Booking", back_populates="resource")
