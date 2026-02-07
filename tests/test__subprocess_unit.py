"""
Tests unitaires générés pour _subprocess
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _subprocess
except ImportError:
    pytest.skip(f"Module _subprocess non importable")


def test_run():
    """Test de la fonction run"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_subprocess, 'run')
    assert callable(getattr(_subprocess, 'run'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_subprocess, '__init__')
    assert callable(getattr(_subprocess, '__init__'))

class TestCalledProcessError:
    """Tests pour la classe CalledProcessError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_subprocess, 'CalledProcessError')
        assert isinstance(getattr(_subprocess, 'CalledProcessError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_subprocess, 'CalledProcessError')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
