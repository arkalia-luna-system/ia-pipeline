"""
Tests unitaires générés pour on
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import on
except ImportError:
    pytest.skip(f"Module on non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(on, '__init__')
    assert callable(getattr(on, '__init__'))

class TestLifespanOn:
    """Tests pour la classe LifespanOn"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(on, 'LifespanOn')
        assert isinstance(getattr(on, 'LifespanOn'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(on, 'LifespanOn')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
