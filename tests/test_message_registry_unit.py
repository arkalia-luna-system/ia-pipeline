"""
Tests unitaires générés pour message_registry
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import message_registry
except ImportError:
    pytest.skip(f"Module message_registry non importable")


def test_format():
    """Test de la fonction format"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(message_registry, 'format')
    assert callable(getattr(message_registry, 'format'))

def test_with_additional_msg():
    """Test de la fonction with_additional_msg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(message_registry, 'with_additional_msg')
    assert callable(getattr(message_registry, 'with_additional_msg'))

class TestErrorMessage:
    """Tests pour la classe ErrorMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(message_registry, 'ErrorMessage')
        assert isinstance(getattr(message_registry, 'ErrorMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(message_registry, 'ErrorMessage')
        for method_name in ['format', 'with_additional_msg']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
