import pytest
from datetime import datetime, timedelta


@pytest.mark.asyncio
async def test_overlapping_booking_conflict(client, auth_headers):

    doc_res = await client.post("/api/v1/resources/", json={
        "name": "Анна Сергеевна",
        "specialization": "логопед",
        "room_number": "101"
    })
    doc_id = doc_res.json()["id"]


    start1 = datetime(2026, 10, 15, 10, 0, 0).isoformat()
    end1 = datetime(2026, 10, 15, 11, 0, 0).isoformat()

    res1 = await client.post("/api/v1/bookings/", headers=auth_headers, json={
        "resource_id": doc_id,
        "start_time": start1,
        "end_time": end1
    })
    assert res1.status_code == 200


    start2 = datetime(2026, 10, 15, 10, 30, 0).isoformat()
    end2 = datetime(2026, 10, 15, 11, 30, 0).isoformat()

    res2 = await client.post("/api/v1/bookings/", headers=auth_headers, json={
        "resource_id": doc_id,
        "start_time": start2,
        "end_time": end2
    })
    assert res2.status_code == 409
    assert res2.json()["detail"] == "У специалиста это время уже занято"