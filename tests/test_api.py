from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)

# test create invite


def test_create_invite():
    response = client.post("/invitation/create",
                           json={"email": "test@example.com"})
    assert response.status_code in [201, 404, 400, 401]
    data = response.json()
    assert "code" in data
    assert data["email"] == "test@example.com"


# test create invite
def test_check_status():
    response = client.get(
        "/invitation/checkstatus?email=haziq@gmail.com&code=0E269925")
    print('response', response)
    assert response.status_code in [200, 404, 400]


# test confirm invite
def test_confirm_invite():
    response = client.patch("/invitation/confirm",
                            json={"email": "test@example.com", "code": "ABC123"})
    assert response.status_code in [200, 404, 400]


# test delete invite
def test_delete_invite():

    response = client.delete(
        "/invitation/delete?email=test@example.com&code=ABC123")
    assert response.status_code in [201, 404, 400, 401]
