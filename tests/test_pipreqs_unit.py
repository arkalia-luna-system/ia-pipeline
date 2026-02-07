"""
Tests unitaires générés pour pipreqs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pipreqs
except ImportError:
    pytest.skip(f"Module pipreqs non importable")


def test__open():
    """Test de la fonction _open"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, '_open')
    assert callable(getattr(pipreqs, '_open'))

def test_get_all_imports():
    """Test de la fonction get_all_imports"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'get_all_imports')
    assert callable(getattr(pipreqs, 'get_all_imports'))

def test_get_file_extensions():
    """Test de la fonction get_file_extensions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'get_file_extensions')
    assert callable(getattr(pipreqs, 'get_file_extensions'))

def test_read_file_content():
    """Test de la fonction read_file_content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'read_file_content')
    assert callable(getattr(pipreqs, 'read_file_content'))

def test_file_ext_is_allowed():
    """Test de la fonction file_ext_is_allowed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'file_ext_is_allowed')
    assert callable(getattr(pipreqs, 'file_ext_is_allowed'))

def test_ipynb_2_py():
    """Test de la fonction ipynb_2_py"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'ipynb_2_py')
    assert callable(getattr(pipreqs, 'ipynb_2_py'))

def test_generate_requirements_file():
    """Test de la fonction generate_requirements_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'generate_requirements_file')
    assert callable(getattr(pipreqs, 'generate_requirements_file'))

def test_output_requirements():
    """Test de la fonction output_requirements"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'output_requirements')
    assert callable(getattr(pipreqs, 'output_requirements'))

def test_get_imports_info():
    """Test de la fonction get_imports_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'get_imports_info')
    assert callable(getattr(pipreqs, 'get_imports_info'))

def test_get_locally_installed_packages():
    """Test de la fonction get_locally_installed_packages"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'get_locally_installed_packages')
    assert callable(getattr(pipreqs, 'get_locally_installed_packages'))

def test_get_import_local():
    """Test de la fonction get_import_local"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'get_import_local')
    assert callable(getattr(pipreqs, 'get_import_local'))

def test_get_pkg_names():
    """Test de la fonction get_pkg_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'get_pkg_names')
    assert callable(getattr(pipreqs, 'get_pkg_names'))

def test_get_name_without_alias():
    """Test de la fonction get_name_without_alias"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'get_name_without_alias')
    assert callable(getattr(pipreqs, 'get_name_without_alias'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'join')
    assert callable(getattr(pipreqs, 'join'))

def test_parse_requirements():
    """Test de la fonction parse_requirements"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'parse_requirements')
    assert callable(getattr(pipreqs, 'parse_requirements'))

def test_compare_modules():
    """Test de la fonction compare_modules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'compare_modules')
    assert callable(getattr(pipreqs, 'compare_modules'))

def test_diff():
    """Test de la fonction diff"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'diff')
    assert callable(getattr(pipreqs, 'diff'))

def test_clean():
    """Test de la fonction clean"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'clean')
    assert callable(getattr(pipreqs, 'clean'))

def test_dynamic_versioning():
    """Test de la fonction dynamic_versioning"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'dynamic_versioning')
    assert callable(getattr(pipreqs, 'dynamic_versioning'))

def test_handle_scan_noteboooks():
    """Test de la fonction handle_scan_noteboooks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'handle_scan_noteboooks')
    assert callable(getattr(pipreqs, 'handle_scan_noteboooks'))

def test_init():
    """Test de la fonction init"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'init')
    assert callable(getattr(pipreqs, 'init'))

def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, 'main')
    assert callable(getattr(pipreqs, 'main'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pipreqs, '__init__')
    assert callable(getattr(pipreqs, '__init__'))

class TestNbconvertNotInstalled:
    """Tests pour la classe NbconvertNotInstalled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pipreqs, 'NbconvertNotInstalled')
        assert isinstance(getattr(pipreqs, 'NbconvertNotInstalled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pipreqs, 'NbconvertNotInstalled')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
