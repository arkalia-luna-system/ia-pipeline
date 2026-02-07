"""
Tests unitaires générés pour g95
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import g95
except ImportError:
    pytest.skip(f"Module g95 non importable")


def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(g95, 'get_flags')
    assert callable(getattr(g95, 'get_flags'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(g95, 'get_flags_opt')
    assert callable(getattr(g95, 'get_flags_opt'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(g95, 'get_flags_debug')
    assert callable(getattr(g95, 'get_flags_debug'))

class TestG95FCompiler:
    """Tests pour la classe G95FCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(g95, 'G95FCompiler')
        assert isinstance(getattr(g95, 'G95FCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(g95, 'G95FCompiler')
        for method_name in ['get_flags', 'get_flags_opt', 'get_flags_debug']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
