"""
Tests unitaires générés pour _stack
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _stack
except ImportError:
    pytest.skip(f"Module _stack non importable")


def test_top():
    """Test de la fonction top"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_stack, 'top')
    assert callable(getattr(_stack, 'top'))

def test_push():
    """Test de la fonction push"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_stack, 'push')
    assert callable(getattr(_stack, 'push'))

class TestStack:
    """Tests pour la classe Stack"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_stack, 'Stack')
        assert isinstance(getattr(_stack, 'Stack'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_stack, 'Stack')
        for method_name in ['top', 'push']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
