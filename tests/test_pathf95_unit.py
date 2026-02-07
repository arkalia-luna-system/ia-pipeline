"""
Tests unitaires générés pour pathf95
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pathf95
except ImportError:
    pytest.skip(f"Module pathf95 non importable")


def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathf95, 'get_flags_opt')
    assert callable(getattr(pathf95, 'get_flags_opt'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathf95, 'get_flags_debug')
    assert callable(getattr(pathf95, 'get_flags_debug'))

class TestPathScaleFCompiler:
    """Tests pour la classe PathScaleFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pathf95, 'PathScaleFCompiler')
        assert isinstance(getattr(pathf95, 'PathScaleFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pathf95, 'PathScaleFCompiler')
        for method_name in ['get_flags_opt', 'get_flags_debug']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
