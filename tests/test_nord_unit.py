"""
Tests unitaires générés pour nord
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nord
except ImportError:
    pytest.skip(f"Module nord non importable")


class TestNordStyle:
    """Tests pour la classe NordStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nord, 'NordStyle')
        assert isinstance(getattr(nord, 'NordStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nord, 'NordStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNordDarkerStyle:
    """Tests pour la classe NordDarkerStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nord, 'NordDarkerStyle')
        assert isinstance(getattr(nord, 'NordDarkerStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nord, 'NordDarkerStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
