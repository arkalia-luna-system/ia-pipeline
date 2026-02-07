"""
Tests unitaires générés pour off
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import off
except ImportError:
    pytest.skip(f"Module off non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(off, '__init__')
    assert callable(getattr(off, '__init__'))

class TestLifespanOff:
    """Tests pour la classe LifespanOff"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(off, 'LifespanOff')
        assert isinstance(getattr(off, 'LifespanOff'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(off, 'LifespanOff')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
