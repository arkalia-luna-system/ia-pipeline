"""
Tests unitaires générés pour enabled
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import enabled
except ImportError:
    pytest.skip(f"Module enabled non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(enabled, '__init__')
    assert callable(getattr(enabled, '__init__'))

def test__load_one_plugin():
    """Test de la fonction _load_one_plugin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(enabled, '_load_one_plugin')
    assert callable(getattr(enabled, '_load_one_plugin'))

class TestEnabledExtensionManager:
    """Tests pour la classe EnabledExtensionManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(enabled, 'EnabledExtensionManager')
        assert isinstance(getattr(enabled, 'EnabledExtensionManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(enabled, 'EnabledExtensionManager')
        for method_name in ['__init__', '_load_one_plugin']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
