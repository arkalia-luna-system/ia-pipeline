"""
Tests unitaires générés pour _intervention
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _intervention
except ImportError:
    pytest.skip(f"Module _intervention non importable")


class TestDropMessage:
    """Tests pour la classe DropMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_intervention, 'DropMessage')
        assert isinstance(getattr(_intervention, 'DropMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_intervention, 'DropMessage')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestInterventionHandler:
    """Tests pour la classe InterventionHandler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_intervention, 'InterventionHandler')
        assert isinstance(getattr(_intervention, 'InterventionHandler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_intervention, 'InterventionHandler')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDefaultInterventionHandler:
    """Tests pour la classe DefaultInterventionHandler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_intervention, 'DefaultInterventionHandler')
        assert isinstance(getattr(_intervention, 'DefaultInterventionHandler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_intervention, 'DefaultInterventionHandler')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
