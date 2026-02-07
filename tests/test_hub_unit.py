"""
Tests unitaires générés pour hub
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import hub
except ImportError:
    pytest.skip(f"Module hub non importable")


def test_ignoring_expected_test_error():
    """Test de la fonction ignoring_expected_test_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hub, 'ignoring_expected_test_error')
    assert callable(getattr(hub, 'ignoring_expected_test_error'))

def test_handle_error():
    """Test de la fonction handle_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hub, 'handle_error')
    assert callable(getattr(hub, 'handle_error'))

def test_print_exception():
    """Test de la fonction print_exception"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(hub, 'print_exception')
    assert callable(getattr(hub, 'print_exception'))

class TestQuietHub:
    """Tests pour la classe QuietHub"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(hub, 'QuietHub')
        assert isinstance(getattr(hub, 'QuietHub'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(hub, 'QuietHub')
        for method_name in ['ignoring_expected_test_error', 'handle_error', 'print_exception']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
