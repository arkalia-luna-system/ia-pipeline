"""
Tests unitaires générés pour alphabeticalattributes
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import alphabeticalattributes
except ImportError:
    pytest.skip(f"Module alphabeticalattributes non importable")


def test__attr_key():
    """Test de la fonction _attr_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(alphabeticalattributes, '_attr_key')
    assert callable(getattr(alphabeticalattributes, '_attr_key'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(alphabeticalattributes, '__iter__')
    assert callable(getattr(alphabeticalattributes, '__iter__'))

class TestFilter:
    """Tests pour la classe Filter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(alphabeticalattributes, 'Filter')
        assert isinstance(getattr(alphabeticalattributes, 'Filter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(alphabeticalattributes, 'Filter')
        for method_name in ['__iter__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
