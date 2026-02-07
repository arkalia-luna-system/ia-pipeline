"""
Tests unitaires générés pour debug
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import debug
except ImportError:
    pytest.skip(f"Module debug non importable")


def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(debug, 'write')
    assert callable(getattr(debug, 'write'))

class TestDebugWriter:
    """Tests pour la classe DebugWriter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(debug, 'DebugWriter')
        assert isinstance(getattr(debug, 'DebugWriter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(debug, 'DebugWriter')
        for method_name in ['write']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
