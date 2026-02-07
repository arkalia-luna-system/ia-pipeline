"""
Tests unitaires générés pour namespaces
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import namespaces
except ImportError:
    pytest.skip(f"Module namespaces non importable")


def test_install_namespaces():
    """Test de la fonction install_namespaces"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, 'install_namespaces')
    assert callable(getattr(namespaces, 'install_namespaces'))

def test_uninstall_namespaces():
    """Test de la fonction uninstall_namespaces"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, 'uninstall_namespaces')
    assert callable(getattr(namespaces, 'uninstall_namespaces'))

def test__get_nspkg_file():
    """Test de la fonction _get_nspkg_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_get_nspkg_file')
    assert callable(getattr(namespaces, '_get_nspkg_file'))

def test__get_target():
    """Test de la fonction _get_target"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_get_target')
    assert callable(getattr(namespaces, '_get_target'))

def test__get_root():
    """Test de la fonction _get_root"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_get_root')
    assert callable(getattr(namespaces, '_get_root'))

def test__gen_nspkg_line():
    """Test de la fonction _gen_nspkg_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_gen_nspkg_line')
    assert callable(getattr(namespaces, '_gen_nspkg_line'))

def test__get_all_ns_packages():
    """Test de la fonction _get_all_ns_packages"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_get_all_ns_packages')
    assert callable(getattr(namespaces, '_get_all_ns_packages'))

def test__pkg_names():
    """Test de la fonction _pkg_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_pkg_names')
    assert callable(getattr(namespaces, '_pkg_names'))

def test__get_root():
    """Test de la fonction _get_root"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_get_root')
    assert callable(getattr(namespaces, '_get_root'))

def test__get_target():
    """Test de la fonction _get_target"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(namespaces, '_get_target')
    assert callable(getattr(namespaces, '_get_target'))

class TestInstaller:
    """Tests pour la classe Installer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(namespaces, 'Installer')
        assert isinstance(getattr(namespaces, 'Installer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(namespaces, 'Installer')
        for method_name in ['install_namespaces', 'uninstall_namespaces', '_get_nspkg_file', '_get_target', '_get_root', '_gen_nspkg_line', '_get_all_ns_packages', '_pkg_names']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDevelopInstaller:
    """Tests pour la classe DevelopInstaller"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(namespaces, 'DevelopInstaller')
        assert isinstance(getattr(namespaces, 'DevelopInstaller'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(namespaces, 'DevelopInstaller')
        for method_name in ['_get_root', '_get_target']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
