import unittest
from Backend.app.main import app
from fastapi.testclient import TestClient


class TestUpdateItem(unittest.TestCase):
    def test_invalid_url(self):
        response = TestClient(app=app).put(url="/update/1", json={"text": "Dummy test"})
        assert response.status_code == 404
        assert response.json().get("detail") == "Not Found"

    def test_update_single_item(self):
        client = TestClient(app=app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200
        assert len(response.json().get("items")) == 0

        response = client.post(url="/api/add", json={"text": "First item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 1
        assert response.json().get("items")[0] == {"text": "First item"}

        response = client.put(url="/api/update/0", json={"text": "Updated First item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 1
        assert response.json().get("items")[0] == {"text": "Updated First item"}

        response = client.post(url="/api/add", json={"text": "Second item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 2
        assert response.json().get("items")[1] == {"text": "Second item"}

        response = client.put(url="/api/update/0", json={"text": "New first item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 2
        assert response.json().get("items")[0] == {"text": "New first item"}

    def test_update_item_not_found(self):
        client = TestClient(app=app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200
        assert len(response.json().get("items")) == 0

        response = client.post(url="/api/add", json={"text": "First item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 1
        assert response.json().get("items")[0] == {"text": "First item"}

        response = client.put(url="/api/update/1", json={"text": "Updated first item"})
        assert response.status_code == 404
        assert response.json().get("message") == "Item not found"

