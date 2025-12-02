import json
from app import app

def test_health():
    tester = app.test_client()
    response = tester.get("/health")
    assert response.status_code == 200

def test_login_success():
    tester = app.test_client()
    response = tester.post("/login",
        data=json.dumps({"username": "admin", "password": "admin123"}),
        content_type="application/json"
    )
    assert response.status_code == 200

def test_login_failure():
    tester = app.test_client()
    response = tester.post("/login",
        data=json.dumps({"username": "wrong", "password": "test"}),
        content_type="application/json"
    )
    assert response.status_code == 401

