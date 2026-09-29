from fastapi import HTTPException, status
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.core.security import verify_password, create_access_token


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register(self, user_data: UserCreate):
        existing_user = await self.user_repo.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пользователь с таким email уже зарегистрирован"
            )
        return await self.user_repo.create(user_data)

    async def authenticate(self, email: str, password: str):
        user = await self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный email или пароль"
            )

        token = create_access_token(data={"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer"}