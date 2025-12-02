from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_payment_success():
    response = client.post("/pay", json={"user": "arun", "amount": 100})
    assert response.json()["status"] == "success"

def test_payment_fail():
    response = client.post("/pay", json={"user": "arun", "amount": -50})
    assert response.json()["status"] == "fail"

