"""
Tests unitaires générés pour _importhook
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _importhook
except ImportError:
    pytest.skip(f"Module _importhook non importable")


def test__call_with_frames_removed():
    """Test de la fonction _call_with_frames_removed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, '_call_with_frames_removed')
    assert callable(getattr(_importhook, '_call_with_frames_removed'))

def test_optimized_cache_from_source():
    """Test de la fonction optimized_cache_from_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, 'optimized_cache_from_source')
    assert callable(getattr(_importhook, 'optimized_cache_from_source'))

def test_install_import_hook():
    """Test de la fonction install_import_hook"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, 'install_import_hook')
    assert callable(getattr(_importhook, 'install_import_hook'))

def test_source_to_code():
    """Test de la fonction source_to_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, 'source_to_code')
    assert callable(getattr(_importhook, 'source_to_code'))

def test_exec_module():
    """Test de la fonction exec_module"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, 'exec_module')
    assert callable(getattr(_importhook, 'exec_module'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, '__init__')
    assert callable(getattr(_importhook, '__init__'))

def test_find_spec():
    """Test de la fonction find_spec"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, 'find_spec')
    assert callable(getattr(_importhook, 'find_spec'))

def test_should_instrument():
    """Test de la fonction should_instrument"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, 'should_instrument')
    assert callable(getattr(_importhook, 'should_instrument'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, '__init__')
    assert callable(getattr(_importhook, '__init__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, '__enter__')
    assert callable(getattr(_importhook, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, '__exit__')
    assert callable(getattr(_importhook, '__exit__'))

def test_uninstall():
    """Test de la fonction uninstall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_importhook, 'uninstall')
    assert callable(getattr(_importhook, 'uninstall'))

class TestTypeguardLoader:
    """Tests pour la classe TypeguardLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_importhook, 'TypeguardLoader')
        assert isinstance(getattr(_importhook, 'TypeguardLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_importhook, 'TypeguardLoader')
        for method_name in ['source_to_code', 'exec_module']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTypeguardFinder:
    """Tests pour la classe TypeguardFinder"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_importhook, 'TypeguardFinder')
        assert isinstance(getattr(_importhook, 'TypeguardFinder'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_importhook, 'TypeguardFinder')
        for method_name in ['__init__', 'find_spec', 'should_instrument']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestImportHookManager:
    """Tests pour la classe ImportHookManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_importhook, 'ImportHookManager')
        assert isinstance(getattr(_importhook, 'ImportHookManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_importhook, 'ImportHookManager')
        for method_name in ['__init__', '__enter__', '__exit__', 'uninstall']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
