import unittest
from fastapi.testclient import TestClient
from Backend.app.main import app


class TestClearItems(unittest.TestCase):
    def test_invalid_request(self):
        response = TestClient(app=app).delete(url="/clear")
        assert response.status_code == 404
        assert response.json().get("detail") == "Not Found"

    def test_clear_items(self):
        response = TestClient(app=app).delete(url="/api/clear")
        assert response.status_code == 200
        assert response.json().get("status") == "Items cleared successfully"
        assert len(response.json().get("items")) == 0

