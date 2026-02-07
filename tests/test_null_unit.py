"""
Tests unitaires générés pour null
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import null
except ImportError:
    pytest.skip(f"Module null non importable")


def test_priority():
    """Test de la fonction priority"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(null, 'priority')
    assert callable(getattr(null, 'priority'))

def test_get_password():
    """Test de la fonction get_password"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(null, 'get_password')
    assert callable(getattr(null, 'get_password'))

class TestKeyring:
    """Tests pour la classe Keyring"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(null, 'Keyring')
        assert isinstance(getattr(null, 'Keyring'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(null, 'Keyring')
        for method_name in ['priority', 'get_password']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
