from pydantic import BaseModel, EmailStr, ConfigDict
from app.utils.enums import UserRole

class UserBase(BaseModel):
    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.CLIENT

class UserResponse(UserBase):
    id: int
    role: UserRole

    model_config = ConfigDict(from_attributes=True)