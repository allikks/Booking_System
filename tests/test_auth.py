import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_and_login(client: AsyncClient):
    # Регистрация
    reg_response = await client.post("/api/v1/auth/register", json={
        "full_name": "Иван Иванов",
        "email": "ivan@example.com",
        "password": "password123",
        "role": "client"
    })
    assert reg_response.status_code == 200
    data = reg_response.json()
    assert data["email"] == "ivan@example.com"
    assert "id" in data

    # Вход
    login_response = await client.post("/api/v1/auth/login", json={
        "email": "ivan@example.com",
        "password": "password123"
    })
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
