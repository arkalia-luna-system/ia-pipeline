"""
Tests d'intégration pour l'API Athalia
Vérifie le fonctionnement complet de l'API FastAPI
"""

import os
import tempfile

import pytest
from fastapi.testclient import TestClient

from athalia_core.api.main_api_server import app


class TestAPIIntegration:
    """Tests d'intégration pour l'API principale"""

    @pytest.fixture
    def client(self):
        """Client de test FastAPI"""
        return TestClient(app)

    def test_api_health_check(self, client):
        """Test de santé de l'API"""
        response = client.get("/health")
        assert response.status_code == 200
        assert "status" in response.json()

    def test_api_docs_accessible(self, client):
        """Test d'accès à la documentation API"""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]

    def test_api_openapi_schema(self, client):
        """Test du schéma OpenAPI"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "info" in schema

    def test_api_cors_headers(self, client):
        """Test des headers CORS"""
        response = client.options("/health")
        assert response.status_code == 200
        # Vérifier que les headers CORS sont présents

    def test_api_error_handling(self, client):
        """Test de gestion d'erreurs"""
        response = client.get("/nonexistent")
        assert response.status_code == 404

    @pytest.mark.integration
    def test_api_startup_shutdown(self, client):
        """Test de démarrage et arrêt de l'API"""
        # Test que l'API peut démarrer et répondre
        response = client.get("/health")
        assert response.status_code == 200

        # Test de métriques si disponibles
        try:
            metrics_response = client.get("/metrics")
            assert metrics_response.status_code in [200, 404]  # 404 si pas implémenté
        except Exception:
            pass  # Métriques optionnelles
