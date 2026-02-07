"""
Tests unitaires générés pour namespace
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import namespace
except ImportError:
    pytest.skip(f"Module namespace non importable")


def test_pinfo():
    """Test de la fonction pinfo"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'pinfo')
    assert callable(getattr(namespace, 'pinfo'))

def test_pinfo2():
    """Test de la fonction pinfo2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'pinfo2')
    assert callable(getattr(namespace, 'pinfo2'))

def test_pdef():
    """Test de la fonction pdef"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'pdef')
    assert callable(getattr(namespace, 'pdef'))

def test_pdoc():
    """Test de la fonction pdoc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'pdoc')
    assert callable(getattr(namespace, 'pdoc'))

def test_psource():
    """Test de la fonction psource"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'psource')
    assert callable(getattr(namespace, 'psource'))

def test_pfile():
    """Test de la fonction pfile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'pfile')
    assert callable(getattr(namespace, 'pfile'))

def test_psearch():
    """Test de la fonction psearch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'psearch')
    assert callable(getattr(namespace, 'psearch'))

def test_who_ls():
    """Test de la fonction who_ls"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'who_ls')
    assert callable(getattr(namespace, 'who_ls'))

def test_who():
    """Test de la fonction who"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'who')
    assert callable(getattr(namespace, 'who'))

def test_whos():
    """Test de la fonction whos"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'whos')
    assert callable(getattr(namespace, 'whos'))

def test_reset():
    """Test de la fonction reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'reset')
    assert callable(getattr(namespace, 'reset'))

def test_reset_selective():
    """Test de la fonction reset_selective"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'reset_selective')
    assert callable(getattr(namespace, 'reset_selective'))

def test_xdel():
    """Test de la fonction xdel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'xdel')
    assert callable(getattr(namespace, 'xdel'))

def test_type_name():
    """Test de la fonction type_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespace, 'type_name')
    assert callable(getattr(namespace, 'type_name'))

class TestNamespaceMagics:
    """Tests pour la classe NamespaceMagics"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(namespace, 'NamespaceMagics')
        assert isinstance(getattr(namespace, 'NamespaceMagics'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(namespace, 'NamespaceMagics')
        for method_name in ['pinfo', 'pinfo2', 'pdef', 'pdoc', 'psource', 'pfile', 'psearch', 'who_ls', 'who', 'whos', 'reset', 'reset_selective', 'xdel']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
