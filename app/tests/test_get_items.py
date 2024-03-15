import unittest
from fastapi.testclient import TestClient

from Backend.app.main import app


class TestGetItems(unittest.TestCase):

    def test_invalid_url(self):
        response = TestClient(app=app).get("/list")
        assert response.status_code == 404
        assert response.json().get("detail") == "Not Found"

    def test_empty_items(self):
        client = TestClient(app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200
        assert response.json().get("status") == "Items cleared successfully"
        response = TestClient(app).get("/api/list")
        assert response.status_code == 200
        assert response.json().get("status") == "No todo items"
        assert len(response.json().get("items")) == 0

    def test_get_single_item(self):
        client = TestClient(app)
        client.post("/api/add", json={"text": "First item"})
        response = client.get(url="/api/list")
        assert response.status_code == 200
        response_data = response.json()
        assert response_data.get("status") == "Items loaded successfully"
        assert response_data.get("items")[0] == {"text": "First item"}

    def test_get_multiple_items(self):
        client = TestClient(app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200
        assert response.json().get("status") == "Items cleared successfully"

        client.post(url="/api/add", json={"text": "First item"})
        client.post(url="/api/add", json={"text": "Second item"})
        response = client.post(url="/api/add", json={"text": "Third item"})
        assert response.status_code == 200
        assert response.json().get("status") == "Item added successfully"
        assert len(response.json().get("items")) == 3
        response = client.get("/api/list")
        assert response.status_code == 200
        assert response.json().get("status") == "Items loaded successfully"
        assert len(response.json().get("items")) == 3
