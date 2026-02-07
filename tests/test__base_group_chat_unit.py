"""
Tests unitaires générés pour _base_group_chat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _base_group_chat
except ImportError:
    pytest.skip(f"Module _base_group_chat non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_group_chat, '__init__')
    assert callable(getattr(_base_group_chat, '__init__'))

def test_name():
    """Test de la fonction name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_group_chat, 'name')
    assert callable(getattr(_base_group_chat, 'name'))

def test_description():
    """Test de la fonction description"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_group_chat, 'description')
    assert callable(getattr(_base_group_chat, 'description'))

def test__create_group_chat_manager_factory():
    """Test de la fonction _create_group_chat_manager_factory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_group_chat, '_create_group_chat_manager_factory')
    assert callable(getattr(_base_group_chat, '_create_group_chat_manager_factory'))

def test__create_participant_factory():
    """Test de la fonction _create_participant_factory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_group_chat, '_create_participant_factory')
    assert callable(getattr(_base_group_chat, '_create_participant_factory'))

def test__factory():
    """Test de la fonction _factory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_base_group_chat, '_factory')
    assert callable(getattr(_base_group_chat, '_factory'))

class TestBaseGroupChat:
    """Tests pour la classe BaseGroupChat"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_base_group_chat, 'BaseGroupChat')
        assert isinstance(getattr(_base_group_chat, 'BaseGroupChat'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_base_group_chat, 'BaseGroupChat')
        for method_name in ['__init__', 'name', 'description', '_create_group_chat_manager_factory', '_create_participant_factory']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
