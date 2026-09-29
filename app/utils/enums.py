from enum import Enum

class UserRole(str, Enum):
    CLIENT = "client"
    ADMIN = "admin"
    SPECIALIST = "specialist"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class SpecialistType(str, Enum):
    LOGOPEDIST = "логопед"
    NEUROPSYCHOLOGIST = "нейропсихолог"
    PSYCHOLOGIST = "психолог"
    DEFECTOLOGIST = "дефектолог"