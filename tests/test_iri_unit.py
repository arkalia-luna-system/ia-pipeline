"""
Tests unitaires générés pour iri
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import iri
except ImportError:
    pytest.skip(f"Module iri non importable")


def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(iri, '__new__')
    assert callable(getattr(iri, '__new__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(iri, '__eq__')
    assert callable(getattr(iri, '__eq__'))

def test__match_subauthority():
    """Test de la fonction _match_subauthority"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(iri, '_match_subauthority')
    assert callable(getattr(iri, '_match_subauthority'))

def test_from_string():
    """Test de la fonction from_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(iri, 'from_string')
    assert callable(getattr(iri, 'from_string'))

def test_encode():
    """Test de la fonction encode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(iri, 'encode')
    assert callable(getattr(iri, 'encode'))

def test_idna_encoder():
    """Test de la fonction idna_encoder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(iri, 'idna_encoder')
    assert callable(getattr(iri, 'idna_encoder'))

class TestIRIReference:
    """Tests pour la classe IRIReference"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(iri, 'IRIReference')
        assert isinstance(getattr(iri, 'IRIReference'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(iri, 'IRIReference')
        for method_name in ['__new__', '__eq__', '_match_subauthority', 'from_string', 'encode']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
