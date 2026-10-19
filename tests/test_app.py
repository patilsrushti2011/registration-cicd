
from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Create an Account" in response.data


def test_registration():
    client = app.test_client()

    response = client.post(
        "/",
        data={"name": "Test User", "email": "test@example.com"}
    )

    assert response.status_code == 200
    assert b"Thank you for registering, Test User!" in response.data
