"""
Tests unitaires générés pour ucre
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ucre
except ImportError:
    pytest.skip(f"Module ucre non importable")


def test__re_host_terminator():
    """Test de la fonction _re_host_terminator"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ucre, '_re_host_terminator')
    assert callable(getattr(ucre, '_re_host_terminator'))

def test__re_src_path():
    """Test de la fonction _re_src_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ucre, '_re_src_path')
    assert callable(getattr(ucre, '_re_src_path'))

def test_build_re():
    """Test de la fonction build_re"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ucre, 'build_re')
    assert callable(getattr(ucre, 'build_re'))

if __name__ == "__main__":
    pytest.main([__file__])
