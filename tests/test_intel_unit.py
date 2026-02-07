"""
Tests unitaires générés pour intel
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import intel
except ImportError:
    pytest.skip(f"Module intel non importable")


def test_intel_version_match():
    """Test de la fonction intel_version_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'intel_version_match')
    assert callable(getattr(intel, 'intel_version_match'))

def test_update_executables():
    """Test de la fonction update_executables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'update_executables')
    assert callable(getattr(intel, 'update_executables'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'runtime_library_dir_option')
    assert callable(getattr(intel, 'runtime_library_dir_option'))

def test_get_flags_free():
    """Test de la fonction get_flags_free"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_free')
    assert callable(getattr(intel, 'get_flags_free'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags')
    assert callable(getattr(intel, 'get_flags'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_opt')
    assert callable(getattr(intel, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_arch')
    assert callable(getattr(intel, 'get_flags_arch'))

def test_get_flags_linker_so():
    """Test de la fonction get_flags_linker_so"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_linker_so')
    assert callable(getattr(intel, 'get_flags_linker_so'))

def test_update_executables():
    """Test de la fonction update_executables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'update_executables')
    assert callable(getattr(intel, 'update_executables'))

def test_get_flags():
    """Test de la fonction get_flags"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags')
    assert callable(getattr(intel, 'get_flags'))

def test_get_flags_free():
    """Test de la fonction get_flags_free"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_free')
    assert callable(getattr(intel, 'get_flags_free'))

def test_get_flags_debug():
    """Test de la fonction get_flags_debug"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_debug')
    assert callable(getattr(intel, 'get_flags_debug'))

def test_get_flags_opt():
    """Test de la fonction get_flags_opt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_opt')
    assert callable(getattr(intel, 'get_flags_opt'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_arch')
    assert callable(getattr(intel, 'get_flags_arch'))

def test_runtime_library_dir_option():
    """Test de la fonction runtime_library_dir_option"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'runtime_library_dir_option')
    assert callable(getattr(intel, 'runtime_library_dir_option'))

def test_get_flags_arch():
    """Test de la fonction get_flags_arch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(intel, 'get_flags_arch')
    assert callable(getattr(intel, 'get_flags_arch'))

class TestBaseIntelFCompiler:
    """Tests pour la classe BaseIntelFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intel, 'BaseIntelFCompiler')
        assert isinstance(getattr(intel, 'BaseIntelFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intel, 'BaseIntelFCompiler')
        for method_name in ['update_executables', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelFCompiler:
    """Tests pour la classe IntelFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intel, 'IntelFCompiler')
        assert isinstance(getattr(intel, 'IntelFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intel, 'IntelFCompiler')
        for method_name in ['get_flags_free', 'get_flags', 'get_flags_opt', 'get_flags_arch', 'get_flags_linker_so']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelItaniumFCompiler:
    """Tests pour la classe IntelItaniumFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intel, 'IntelItaniumFCompiler')
        assert isinstance(getattr(intel, 'IntelItaniumFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intel, 'IntelItaniumFCompiler')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelEM64TFCompiler:
    """Tests pour la classe IntelEM64TFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intel, 'IntelEM64TFCompiler')
        assert isinstance(getattr(intel, 'IntelEM64TFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intel, 'IntelEM64TFCompiler')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelVisualFCompiler:
    """Tests pour la classe IntelVisualFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intel, 'IntelVisualFCompiler')
        assert isinstance(getattr(intel, 'IntelVisualFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intel, 'IntelVisualFCompiler')
        for method_name in ['update_executables', 'get_flags', 'get_flags_free', 'get_flags_debug', 'get_flags_opt', 'get_flags_arch', 'runtime_library_dir_option']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelItaniumVisualFCompiler:
    """Tests pour la classe IntelItaniumVisualFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intel, 'IntelItaniumVisualFCompiler')
        assert isinstance(getattr(intel, 'IntelItaniumVisualFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intel, 'IntelItaniumVisualFCompiler')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIntelEM64VisualFCompiler:
    """Tests pour la classe IntelEM64VisualFCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(intel, 'IntelEM64VisualFCompiler')
        assert isinstance(getattr(intel, 'IntelEM64VisualFCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(intel, 'IntelEM64VisualFCompiler')
        for method_name in ['get_flags_arch']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
