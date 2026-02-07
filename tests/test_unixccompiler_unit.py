"""
Tests unitaires générés pour unixccompiler
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import unixccompiler
except ImportError:
    pytest.skip(f"Module unixccompiler non importable")


def test_UnixCCompiler__compile():
    """Test de la fonction UnixCCompiler__compile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unixccompiler, 'UnixCCompiler__compile')
    assert callable(getattr(unixccompiler, 'UnixCCompiler__compile'))

def test_UnixCCompiler_create_static_lib():
    """Test de la fonction UnixCCompiler_create_static_lib"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(unixccompiler, 'UnixCCompiler_create_static_lib')
    assert callable(getattr(unixccompiler, 'UnixCCompiler_create_static_lib'))

if __name__ == "__main__":
    pytest.main([__file__])
