import pytest
from src.router import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_dynamic_routing(client):
    response = client.post("/route", json={
        "text": "Write a detailed essay on quantum mechanics.",
        "metrics": {"latency": 180, "cost": 0.3, "accuracy": 0.92}
    })
    assert response.status_code == 200
    assert response.json["routed_model"] in ["gpt-4", "gpt-3.5", "opt-66b"]
