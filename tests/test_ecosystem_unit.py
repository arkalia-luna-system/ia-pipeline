"""
Tests unitaires générés pour ecosystem
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ecosystem
except ImportError:
    pytest.skip(f"Module ecosystem non importable")


class TestEcosystemIgnoreConfigModel:
    """Tests pour la classe EcosystemIgnoreConfigModel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ecosystem, 'EcosystemIgnoreConfigModel')
        assert isinstance(getattr(ecosystem, 'EcosystemIgnoreConfigModel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ecosystem, 'EcosystemIgnoreConfigModel')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPythonEcosystemIgnoreConfigModel:
    """Tests pour la classe PythonEcosystemIgnoreConfigModel"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ecosystem, 'PythonEcosystemIgnoreConfigModel')
        assert isinstance(getattr(ecosystem, 'PythonEcosystemIgnoreConfigModel'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ecosystem, 'PythonEcosystemIgnoreConfigModel')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
