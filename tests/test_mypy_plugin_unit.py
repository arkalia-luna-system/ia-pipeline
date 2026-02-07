"""
Tests unitaires générés pour mypy_plugin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import mypy_plugin
except ImportError:
    pytest.skip(f"Module mypy_plugin non importable")


def test__get_precision_dict():
    """Test de la fonction _get_precision_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, '_get_precision_dict')
    assert callable(getattr(mypy_plugin, '_get_precision_dict'))

def test__get_extended_precision_list():
    """Test de la fonction _get_extended_precision_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, '_get_extended_precision_list')
    assert callable(getattr(mypy_plugin, '_get_extended_precision_list'))

def test__get_c_intp_name():
    """Test de la fonction _get_c_intp_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, '_get_c_intp_name')
    assert callable(getattr(mypy_plugin, '_get_c_intp_name'))

def test__hook():
    """Test de la fonction _hook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, '_hook')
    assert callable(getattr(mypy_plugin, '_hook'))

def test__index():
    """Test de la fonction _index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, '_index')
    assert callable(getattr(mypy_plugin, '_index'))

def test__override_imports():
    """Test de la fonction _override_imports"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, '_override_imports')
    assert callable(getattr(mypy_plugin, '_override_imports'))

def test_plugin():
    """Test de la fonction plugin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, 'plugin')
    assert callable(getattr(mypy_plugin, 'plugin'))

def test_plugin():
    """Test de la fonction plugin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, 'plugin')
    assert callable(getattr(mypy_plugin, 'plugin'))

def test_get_type_analyze_hook():
    """Test de la fonction get_type_analyze_hook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, 'get_type_analyze_hook')
    assert callable(getattr(mypy_plugin, 'get_type_analyze_hook'))

def test_get_additional_deps():
    """Test de la fonction get_additional_deps"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(mypy_plugin, 'get_additional_deps')
    assert callable(getattr(mypy_plugin, 'get_additional_deps'))

class Test_NumpyPlugin:
    """Tests pour la classe _NumpyPlugin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(mypy_plugin, '_NumpyPlugin')
        assert isinstance(getattr(mypy_plugin, '_NumpyPlugin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(mypy_plugin, '_NumpyPlugin')
        for method_name in ['get_type_analyze_hook', 'get_additional_deps']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
