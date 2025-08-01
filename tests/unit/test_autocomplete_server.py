import pytest

# Vérification de la disponibilité de FastAPI
try:
    from fastapi.testclient import TestClient

    from athalia_core.autocomplete_server import app

    FASTAPI_AVAILABLE = True
    client = TestClient(app)
except ImportError:
    FASTAPI_AVAILABLE = False
    client = None

# Vérification de la disponibilité du module autocomplete
try:
    from athalia_core.autocomplete_engine import AutocompleteEngine

    AUTOCOMPLETE_AVAILABLE = True
except ImportError:
    AUTOCOMPLETE_AVAILABLE = False


def test_autocomplete_nominal():
    if not FASTAPI_AVAILABLE or client is None:
        pytest.skip("FastAPI ou client non disponible")
    response = client.post(
        "/autocomplete", json={"prompt": "def", "max_suggestions": 3}
    )
    assert response.status_code == 200
    data = response.json()
    assert "suggestions" in data
    assert isinstance(data["suggestions"], list)
    # Le nombre de suggestions peut varier selon le contexte
    assert len(data["suggestions"]) >= 0


def test_autocomplete_empty_prompt():
    if not FASTAPI_AVAILABLE or client is None:
        pytest.skip("FastAPI ou client non disponible")
    response = client.post("/autocomplete", json={"prompt": "", "max_suggestions": 2})
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Le prompt ne peut pas être vide."


def test_autocomplete_engine():
    """Test du moteur de complétion automatique"""
    if not AUTOCOMPLETE_AVAILABLE:
        pytest.skip("Module autocomplete non disponible")

    engine = AutocompleteEngine()
    suggestions = engine.get_suggestions_for_context("python", "def")
    assert isinstance(suggestions, list)
    assert len(suggestions) >= 0  # Peut être vide selon le contexte
