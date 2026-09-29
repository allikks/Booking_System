from sqlalchemy import Integer, String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.utils.enums import SpecialistType

class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)  # ФИО специалиста, напр. "Иванова А.С."
    specialization: Mapped[SpecialistType] = mapped_column(SQLEnum(SpecialistType), nullable=False)
    room_number: Mapped[str] = mapped_column(String, nullable=True)  # Кабинет №4

    bookings = relationship("Booking", back_populates="resource")