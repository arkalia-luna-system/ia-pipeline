"""
Tests unitaires générés pour nbjson
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nbjson
except ImportError:
    pytest.skip(f"Module nbjson non importable")


def test_default():
    """Test de la fonction default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbjson, 'default')
    assert callable(getattr(nbjson, 'default'))

def test_reads():
    """Test de la fonction reads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbjson, 'reads')
    assert callable(getattr(nbjson, 'reads'))

def test_to_notebook():
    """Test de la fonction to_notebook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbjson, 'to_notebook')
    assert callable(getattr(nbjson, 'to_notebook'))

def test_writes():
    """Test de la fonction writes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbjson, 'writes')
    assert callable(getattr(nbjson, 'writes'))

class TestBytesEncoder:
    """Tests pour la classe BytesEncoder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nbjson, 'BytesEncoder')
        assert isinstance(getattr(nbjson, 'BytesEncoder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nbjson, 'BytesEncoder')
        for method_name in ['default']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestJSONReader:
    """Tests pour la classe JSONReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nbjson, 'JSONReader')
        assert isinstance(getattr(nbjson, 'JSONReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nbjson, 'JSONReader')
        for method_name in ['reads', 'to_notebook']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestJSONWriter:
    """Tests pour la classe JSONWriter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nbjson, 'JSONWriter')
        assert isinstance(getattr(nbjson, 'JSONWriter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nbjson, 'JSONWriter')
        for method_name in ['writes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
