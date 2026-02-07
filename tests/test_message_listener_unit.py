"""
Tests unitaires générés pour message_listener
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import message_listener
except ImportError:
    pytest.skip(f"Module message_listener non importable")


def test_Modified():
    """Test de la fonction Modified"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(message_listener, 'Modified')
    assert callable(getattr(message_listener, 'Modified'))

def test_Modified():
    """Test de la fonction Modified"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(message_listener, 'Modified')
    assert callable(getattr(message_listener, 'Modified'))

class TestMessageListener:
    """Tests pour la classe MessageListener"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(message_listener, 'MessageListener')
        assert isinstance(getattr(message_listener, 'MessageListener'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(message_listener, 'MessageListener')
        for method_name in ['Modified']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestNullMessageListener:
    """Tests pour la classe NullMessageListener"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(message_listener, 'NullMessageListener')
        assert isinstance(getattr(message_listener, 'NullMessageListener'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(message_listener, 'NullMessageListener')
        for method_name in ['Modified']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
