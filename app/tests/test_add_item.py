import unittest
from fastapi.testclient import TestClient

from Backend.app.main import app


class TestAddItems(unittest.TestCase):

    def test_validation_error(self):
        client = TestClient(app=app)
        response = client.post(url="/api/add", json={"body": "First item"})
        assert response.status_code == 422
        assert response.json().get("detail")[0].get("msg") == "field required"

    def test_invalid_url(self):
        client = TestClient(app=app)
        response = client.post(url="/add", json={"text": "First item"})
        assert response.status_code == 404

    def test_add_single_item(self):
        client = TestClient(app=app)
        response = client.post(url="/api/add", json={"text": "First item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 1
        assert len(client.get(url="/api/list").json().get("items")) == 1

    def test_multiple_add_items(self):
        client = TestClient(app=app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200
        assert response.json().get("status") == "Items cleared successfully"
        response = client.post(url="/api/add", json={"text": "First item"})
        print(response.json())
        assert response.status_code == 200
        assert len(response.json().get("items")) == 1
        response = client.post(url="/api/add", json={"text": "Second item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 2
        response = client.post(url="/api/add", json={"text": "Third item"})
        assert response.status_code == 200
        assert len(response.json().get("items")) == 3
