import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_and_get_specialist(client: AsyncClient):
    # Создать врача
    new_doc = {
        "name": "Елена Викторовна",
        "specialization": "логопед",
        "room_number": "12"
    }
    create_res = await client.post("/api/v1/resources/", json=new_doc)
    assert create_res.status_code == 200
    assert create_res.json()["name"] == "Елена Викторовна"

    # список врачей
    list_res = await client.get("/api/v1/resources/")
    assert list_res.status_code == 200
    assert len(list_res.json()) > 0