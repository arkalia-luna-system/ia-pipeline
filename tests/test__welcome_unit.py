"""
Tests unitaires générés pour _welcome
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _welcome
except ImportError:
    pytest.skip(f"Module _welcome non importable")


def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_welcome, 'compose')
    assert callable(getattr(_welcome, 'compose'))

class TestWelcome:
    """Tests pour la classe Welcome"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_welcome, 'Welcome')
        assert isinstance(getattr(_welcome, 'Welcome'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_welcome, 'Welcome')
        for method_name in ['compose']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
