"""
Tests unitaires générés pour nbpy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import nbpy
except ImportError:
    pytest.skip(f"Module nbpy non importable")


def test_reads():
    """Test de la fonction reads"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbpy, 'reads')
    assert callable(getattr(nbpy, 'reads'))

def test_to_notebook():
    """Test de la fonction to_notebook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbpy, 'to_notebook')
    assert callable(getattr(nbpy, 'to_notebook'))

def test_new_cell():
    """Test de la fonction new_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbpy, 'new_cell')
    assert callable(getattr(nbpy, 'new_cell'))

def test__remove_comments():
    """Test de la fonction _remove_comments"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbpy, '_remove_comments')
    assert callable(getattr(nbpy, '_remove_comments'))

def test_split_lines_into_blocks():
    """Test de la fonction split_lines_into_blocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbpy, 'split_lines_into_blocks')
    assert callable(getattr(nbpy, 'split_lines_into_blocks'))

def test_writes():
    """Test de la fonction writes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(nbpy, 'writes')
    assert callable(getattr(nbpy, 'writes'))

class TestPyReaderError:
    """Tests pour la classe PyReaderError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nbpy, 'PyReaderError')
        assert isinstance(getattr(nbpy, 'PyReaderError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nbpy, 'PyReaderError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPyReader:
    """Tests pour la classe PyReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nbpy, 'PyReader')
        assert isinstance(getattr(nbpy, 'PyReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nbpy, 'PyReader')
        for method_name in ['reads', 'to_notebook', 'new_cell', '_remove_comments', 'split_lines_into_blocks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPyWriter:
    """Tests pour la classe PyWriter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(nbpy, 'PyWriter')
        assert isinstance(getattr(nbpy, 'PyWriter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(nbpy, 'PyWriter')
        for method_name in ['writes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
