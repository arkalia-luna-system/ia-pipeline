"""
Tests unitaires générés pour _doctools
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _doctools
except ImportError:
    pytest.skip(f"Module _doctools non importable")


def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, 'main')
    assert callable(getattr(_doctools, 'main'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, '__init__')
    assert callable(getattr(_doctools, '__init__'))

def test__shape():
    """Test de la fonction _shape"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, '_shape')
    assert callable(getattr(_doctools, '_shape'))

def test__get_cells():
    """Test de la fonction _get_cells"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, '_get_cells')
    assert callable(getattr(_doctools, '_get_cells'))

def test_plot():
    """Test de la fonction plot"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, 'plot')
    assert callable(getattr(_doctools, 'plot'))

def test__conv():
    """Test de la fonction _conv"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, '_conv')
    assert callable(getattr(_doctools, '_conv'))

def test__insert_index():
    """Test de la fonction _insert_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, '_insert_index')
    assert callable(getattr(_doctools, '_insert_index'))

def test__make_table():
    """Test de la fonction _make_table"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_doctools, '_make_table')
    assert callable(getattr(_doctools, '_make_table'))

class TestTablePlotter:
    """Tests pour la classe TablePlotter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_doctools, 'TablePlotter')
        assert isinstance(getattr(_doctools, 'TablePlotter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_doctools, 'TablePlotter')
        for method_name in ['__init__', '_shape', '_get_cells', 'plot', '_conv', '_insert_index', '_make_table']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
