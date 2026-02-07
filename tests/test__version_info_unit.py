"""
Tests unitaires générés pour _version_info
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _version_info
except ImportError:
    pytest.skip(f"Module _version_info non importable")


def test__from_version_string():
    """Test de la fonction _from_version_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_version_info, '_from_version_string')
    assert callable(getattr(_version_info, '_from_version_string'))

def test__ensure_tuple():
    """Test de la fonction _ensure_tuple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_version_info, '_ensure_tuple')
    assert callable(getattr(_version_info, '_ensure_tuple'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_version_info, '__eq__')
    assert callable(getattr(_version_info, '__eq__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_version_info, '__lt__')
    assert callable(getattr(_version_info, '__lt__'))

class TestVersionInfo:
    """Tests pour la classe VersionInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_version_info, 'VersionInfo')
        assert isinstance(getattr(_version_info, 'VersionInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_version_info, 'VersionInfo')
        for method_name in ['_from_version_string', '_ensure_tuple', '__eq__', '__lt__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
