"""
Tests unitaires générés pour envbuild
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import envbuild
except ImportError:
    pytest.skip(f"Module envbuild non importable")


def test__load_pyproject():
    """Test de la fonction _load_pyproject"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(envbuild, '_load_pyproject')
    assert callable(getattr(envbuild, '_load_pyproject'))

def test_build_wheel():
    """Test de la fonction build_wheel"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(envbuild, 'build_wheel')
    assert callable(getattr(envbuild, 'build_wheel'))

def test_build_sdist():
    """Test de la fonction build_sdist"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(envbuild, 'build_sdist')
    assert callable(getattr(envbuild, 'build_sdist'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(envbuild, '__init__')
    assert callable(getattr(envbuild, '__init__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(envbuild, '__enter__')
    assert callable(getattr(envbuild, '__enter__'))

def test_pip_install():
    """Test de la fonction pip_install"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(envbuild, 'pip_install')
    assert callable(getattr(envbuild, 'pip_install'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(envbuild, '__exit__')
    assert callable(getattr(envbuild, '__exit__'))

class TestBuildEnvironment:
    """Tests pour la classe BuildEnvironment"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(envbuild, 'BuildEnvironment')
        assert isinstance(getattr(envbuild, 'BuildEnvironment'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(envbuild, 'BuildEnvironment')
        for method_name in ['__init__', '__enter__', 'pip_install', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
