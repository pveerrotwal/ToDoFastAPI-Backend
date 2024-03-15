import unittest
from fastapi.testclient import TestClient
from Backend.app.main import app


class TestDeleteItem(unittest.TestCase):

    def test_item_not_in_storage(self):
        client = TestClient(app=app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200
        assert response.json().get("status") == "Items cleared successfully"

        response = client.delete(url="/api/delete/1")
        assert response.status_code == 404
        assert response.json().get("message") == "Item not found"

    def test_invalid_request(self):
        client = TestClient(app=app)
        response = client.delete(url="/delete/1")
        assert response.status_code == 404
        assert response.json().get("detail") == "Not Found"

    def test_delete_single_item(self):
        client = TestClient(app=app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200

        response = client.post(url="/api/add", json={"text": "First item"})
        assert response.status_code == 200
        assert response.json().get("status") == "Item added successfully"
        assert len(response.json().get("items")) == 1

        response = client.delete(url="/api/delete/0")
        assert response.status_code == 200
        assert response.json().get("status") == "Item #1 deleted successfully"
        assert len(response.json().get("items")) == 0

    def test_delete_multiple_items(self):
        client = TestClient(app=app)
        response = client.delete(url="/api/clear")
        assert response.status_code == 200

        response = client.post(url="/api/add", json={"text": "First item"})
        assert response.status_code == 200
        assert response.json().get("status") == "Item added successfully"
        assert len(response.json().get("items")) == 1

        response = client.post(url="/api/add", json={"text": "Second item"})
        assert response.status_code == 200
        assert response.json().get("status") == "Item added successfully"
        assert len(response.json().get("items")) == 2

        response = client.delete(url="/api/delete/1")
        assert response.status_code == 200
        assert response.json().get("status") == "Item #2 deleted successfully"
        assert len(response.json().get("items")) == 1

        response = client.delete(url="/api/delete/0")
        assert response.status_code == 200
        assert response.json().get("status") == "Item #1 deleted successfully"
        assert len(response.json().get("items")) == 0
