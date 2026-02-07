"""
Tests unitaires générés pour state_core
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import state_core
except ImportError:
    pytest.skip(f"Module state_core non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(state_core, '__init__')
    assert callable(getattr(state_core, '__init__'))

class TestStateCore:
    """Tests pour la classe StateCore"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(state_core, 'StateCore')
        assert isinstance(getattr(state_core, 'StateCore'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(state_core, 'StateCore')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
