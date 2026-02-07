"""
Tests unitaires générés pour pathccompiler
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pathccompiler
except ImportError:
    pytest.skip(f"Module pathccompiler non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(pathccompiler, '__init__')
    assert callable(getattr(pathccompiler, '__init__'))

class TestPathScaleCCompiler:
    """Tests pour la classe PathScaleCCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pathccompiler, 'PathScaleCCompiler')
        assert isinstance(getattr(pathccompiler, 'PathScaleCCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pathccompiler, 'PathScaleCCompiler')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
