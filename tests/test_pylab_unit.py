"""
Tests unitaires générés pour pylab
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pylab
except ImportError:
    pytest.skip(f"Module pylab non importable")


def test_matplotlib():
    """Test de la fonction matplotlib"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pylab, 'matplotlib')
    assert callable(getattr(pylab, 'matplotlib'))

def test_pylab():
    """Test de la fonction pylab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pylab, 'pylab')
    assert callable(getattr(pylab, 'pylab'))

def test__show_matplotlib_backend():
    """Test de la fonction _show_matplotlib_backend"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pylab, '_show_matplotlib_backend')
    assert callable(getattr(pylab, '_show_matplotlib_backend'))

class TestPylabMagics:
    """Tests pour la classe PylabMagics"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pylab, 'PylabMagics')
        assert isinstance(getattr(pylab, 'PylabMagics'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pylab, 'PylabMagics')
        for method_name in ['matplotlib', 'pylab', '_show_matplotlib_backend']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
