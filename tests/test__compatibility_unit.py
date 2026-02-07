"""
Tests unitaires générés pour _compatibility
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _compatibility
except ImportError:
    pytest.skip(f"Module _compatibility non importable")


def test_pickle_load():
    """Test de la fonction pickle_load"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compatibility, 'pickle_load')
    assert callable(getattr(_compatibility, 'pickle_load'))

def test_pickle_dump():
    """Test de la fonction pickle_dump"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compatibility, 'pickle_dump')
    assert callable(getattr(_compatibility, 'pickle_dump'))

def test_find_class():
    """Test de la fonction find_class"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_compatibility, 'find_class')
    assert callable(getattr(_compatibility, 'find_class'))

class TestUnpickler:
    """Tests pour la classe Unpickler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_compatibility, 'Unpickler')
        assert isinstance(getattr(_compatibility, 'Unpickler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_compatibility, 'Unpickler')
        for method_name in ['find_class']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
