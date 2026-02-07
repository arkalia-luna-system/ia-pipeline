"""
Tests unitaires générés pour qt_loaders
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import qt_loaders
except ImportError:
    pytest.skip(f"Module qt_loaders non importable")


def test_commit_api():
    """Test de la fonction commit_api"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'commit_api')
    assert callable(getattr(qt_loaders, 'commit_api'))

def test_loaded_api():
    """Test de la fonction loaded_api"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'loaded_api')
    assert callable(getattr(qt_loaders, 'loaded_api'))

def test_has_binding():
    """Test de la fonction has_binding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'has_binding')
    assert callable(getattr(qt_loaders, 'has_binding'))

def test_qtapi_version():
    """Test de la fonction qtapi_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'qtapi_version')
    assert callable(getattr(qt_loaders, 'qtapi_version'))

def test_can_import():
    """Test de la fonction can_import"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'can_import')
    assert callable(getattr(qt_loaders, 'can_import'))

def test_import_pyqt4():
    """Test de la fonction import_pyqt4"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'import_pyqt4')
    assert callable(getattr(qt_loaders, 'import_pyqt4'))

def test_import_pyqt5():
    """Test de la fonction import_pyqt5"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'import_pyqt5')
    assert callable(getattr(qt_loaders, 'import_pyqt5'))

def test_import_pyqt6():
    """Test de la fonction import_pyqt6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'import_pyqt6')
    assert callable(getattr(qt_loaders, 'import_pyqt6'))

def test_import_pyside():
    """Test de la fonction import_pyside"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'import_pyside')
    assert callable(getattr(qt_loaders, 'import_pyside'))

def test_import_pyside2():
    """Test de la fonction import_pyside2"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'import_pyside2')
    assert callable(getattr(qt_loaders, 'import_pyside2'))

def test_import_pyside6():
    """Test de la fonction import_pyside6"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'import_pyside6')
    assert callable(getattr(qt_loaders, 'import_pyside6'))

def test_load_qt():
    """Test de la fonction load_qt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'load_qt')
    assert callable(getattr(qt_loaders, 'load_qt'))

def test_enum_factory():
    """Test de la fonction enum_factory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'enum_factory')
    assert callable(getattr(qt_loaders, 'enum_factory'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, '__init__')
    assert callable(getattr(qt_loaders, '__init__'))

def test_forbid():
    """Test de la fonction forbid"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'forbid')
    assert callable(getattr(qt_loaders, 'forbid'))

def test_find_spec():
    """Test de la fonction find_spec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, 'find_spec')
    assert callable(getattr(qt_loaders, 'find_spec'))

def test__enum():
    """Test de la fonction _enum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(qt_loaders, '_enum')
    assert callable(getattr(qt_loaders, '_enum'))

class TestImportDenier:
    """Tests pour la classe ImportDenier"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(qt_loaders, 'ImportDenier')
        assert isinstance(getattr(qt_loaders, 'ImportDenier'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(qt_loaders, 'ImportDenier')
        for method_name in ['__init__', 'forbid', 'find_spec']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
