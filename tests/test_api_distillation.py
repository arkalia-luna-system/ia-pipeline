from fastapi.testclient import TestClient
from setup.api_distillation import app

def test_feedback():
    client = TestClient(app)
    response = client.post("/feedback", json={"prompt": "Test feedback"})
    assert response.status_code == 200
    assert response.json()["status"] == "ok" 