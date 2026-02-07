"""
Tests unitaires générés pour blocking
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import blocking
except ImportError:
    pytest.skip(f"Module blocking non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(blocking, '__init__')
    assert callable(getattr(blocking, '__init__'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(blocking, 'close')
    assert callable(getattr(blocking, 'close'))

class TestResolver:
    """Tests pour la classe Resolver"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(blocking, 'Resolver')
        assert isinstance(getattr(blocking, 'Resolver'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(blocking, 'Resolver')
        for method_name in ['__init__', 'close']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
