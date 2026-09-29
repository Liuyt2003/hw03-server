from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "HW03 server is running"


def test_case_studies():
    response = client.get("/api/case-studies")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_team():
    response = client.get("/api/team")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_blog():
    response = client.get("/api/blog")

    assert response.status_code == 200
    assert isinstance(response.json(), list)