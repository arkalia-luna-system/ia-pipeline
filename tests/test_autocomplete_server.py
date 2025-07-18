import pytest
from fastapi.testclient import TestClient
from athalia_core.autocomplete_server import app
from athalia_core.autocomplete_engine import OllamaAutocompleteEngine
import requests
from unittest.mock import patch


client = TestClient(app)

def test_autocomplete_nominal():
    response = client.post("/autocomplete", json={"prompt": "test", "max_suggestions": 3})
    assert response.status_code == 200
    data = response.json()
    assert "suggestions" in data
    assert len(data["suggestions"]) == 3
    assert all(s.startswith("test_auto_") for s in data["suggestions"])

def test_autocomplete_empty_prompt():
    response = client.post("/autocomplete", json={"prompt": "", "max_suggestions": 2})
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Le prompt ne peut pas être vide."

def test_ollama_autocomplete_engine(monkeypatch):
    # Mock de la réponse Ollama
    class MockResp:
        def raise_for_status(self):
            pass
        def json(self):
            return {"response": "sugg1\nsugg2\nsugg3"}
    def mock_post(*args, **kwargs):
        return MockResp()
    with patch.object(requests, "post", mock_post):
        engine = OllamaAutocompleteEngine()
        suggestions = engine.suggest("test", 3)
        assert suggestions == ["sugg1", "sugg2", "sugg3"] 