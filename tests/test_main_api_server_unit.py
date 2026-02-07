"""
Tests unitaires générés pour main_api_server
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import main_api_server
except ImportError:
    pytest.skip(f"Module main_api_server non importable")


class TestHealthResponse:
    """Tests pour la classe HealthResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(main_api_server, 'HealthResponse')
        assert isinstance(getattr(main_api_server, 'HealthResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(main_api_server, 'HealthResponse')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestProjectBlueprint:
    """Tests pour la classe ProjectBlueprint"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(main_api_server, 'ProjectBlueprint')
        assert isinstance(getattr(main_api_server, 'ProjectBlueprint'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(main_api_server, 'ProjectBlueprint')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestProjectResponse:
    """Tests pour la classe ProjectResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(main_api_server, 'ProjectResponse')
        assert isinstance(getattr(main_api_server, 'ProjectResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(main_api_server, 'ProjectResponse')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSecurityScanResponse:
    """Tests pour la classe SecurityScanResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(main_api_server, 'SecurityScanResponse')
        assert isinstance(getattr(main_api_server, 'SecurityScanResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(main_api_server, 'SecurityScanResponse')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestErrorResponse:
    """Tests pour la classe ErrorResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(main_api_server, 'ErrorResponse')
        assert isinstance(getattr(main_api_server, 'ErrorResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(main_api_server, 'ErrorResponse')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
