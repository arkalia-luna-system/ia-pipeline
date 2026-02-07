"""
Tests unitaires générés pour ImtImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ImtImagePlugin
except ImportError:
    pytest.skip(f"Module ImtImagePlugin non importable")


def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ImtImagePlugin, '_open')
    assert callable(getattr(ImtImagePlugin, '_open'))

class TestImtImageFile:
    """Tests pour la classe ImtImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ImtImagePlugin, 'ImtImageFile')
        assert isinstance(getattr(ImtImagePlugin, 'ImtImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ImtImagePlugin, 'ImtImageFile')
        for method_name in ['_open']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
