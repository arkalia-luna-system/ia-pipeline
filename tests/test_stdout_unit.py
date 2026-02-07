"""
Tests unitaires générés pour stdout
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import stdout
except ImportError:
    pytest.skip(f"Module stdout non importable")


def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(stdout, 'write')
    assert callable(getattr(stdout, 'write'))

class TestStdoutWriter:
    """Tests pour la classe StdoutWriter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(stdout, 'StdoutWriter')
        assert isinstance(getattr(stdout, 'StdoutWriter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(stdout, 'StdoutWriter')
        for method_name in ['write']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
