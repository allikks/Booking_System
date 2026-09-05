from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTErro, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import AsyncSessionn