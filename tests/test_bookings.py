import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_and_read_booking(client: AsyncClient, auth_headers: dict):

    doc_res = await client.post("/api/v1/resources/", json={
        "name": "Олена Костенко",
        "specialization": "психолог",
        "room_number": "5"
    })
    doc_id = doc_res.json()["id"]


    booking_data = {
        "resource_id": doc_id,
        "start_time": "2026-11-10T14:00:00",
        "end_time": "2026-11-10T15:00:00"
    }
    book_res = await client.post("/api/v1/bookings/", headers=auth_headers, json=booking_data)
    assert book_res.status_code == 200
    assert book_res.json()["status"] == "confirmed"


    my_bookings = await client.get("/api/v1/bookings/my", headers=auth_headers)
    assert my_bookings.status_code == 200
    assert len(my_bookings.json()) >= 1