"""
Tests unitaires générés pour dom
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dom
except ImportError:
    pytest.skip(f"Module dom non importable")


def test_getNodeDetails():
    """Test de la fonction getNodeDetails"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dom, 'getNodeDetails')
    assert callable(getattr(dom, 'getNodeDetails'))

def test_getFirstChild():
    """Test de la fonction getFirstChild"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dom, 'getFirstChild')
    assert callable(getattr(dom, 'getFirstChild'))

def test_getNextSibling():
    """Test de la fonction getNextSibling"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dom, 'getNextSibling')
    assert callable(getattr(dom, 'getNextSibling'))

def test_getParentNode():
    """Test de la fonction getParentNode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dom, 'getParentNode')
    assert callable(getattr(dom, 'getParentNode'))

class TestTreeWalker:
    """Tests pour la classe TreeWalker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dom, 'TreeWalker')
        assert isinstance(getattr(dom, 'TreeWalker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dom, 'TreeWalker')
        for method_name in ['getNodeDetails', 'getFirstChild', 'getNextSibling', 'getParentNode']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
