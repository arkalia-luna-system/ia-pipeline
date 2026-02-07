"""
Tests unitaires générés pour McIdasImagePlugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import McIdasImagePlugin
except ImportError:
    pytest.skip(f"Module McIdasImagePlugin non importable")


def test__accept():
    """Test de la fonction _accept"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(McIdasImagePlugin, '_accept')
    assert callable(getattr(McIdasImagePlugin, '_accept'))

def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(McIdasImagePlugin, '_open')
    assert callable(getattr(McIdasImagePlugin, '_open'))

class TestMcIdasImageFile:
    """Tests pour la classe McIdasImageFile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(McIdasImagePlugin, 'McIdasImageFile')
        assert isinstance(getattr(McIdasImagePlugin, 'McIdasImageFile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(McIdasImagePlugin, 'McIdasImageFile')
        for method_name in ['_open']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
