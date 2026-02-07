"""
Tests unitaires générés pour _windows_color
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _windows_color
except ImportError:
    pytest.skip(f"Module _windows_color non importable")


def test__enable():
    """Test de la fonction _enable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_windows_color, '_enable')
    assert callable(getattr(_windows_color, '_enable'))

def test_bool_errcheck():
    """Test de la fonction bool_errcheck"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_windows_color, 'bool_errcheck')
    assert callable(getattr(_windows_color, 'bool_errcheck'))

if __name__ == "__main__":
    pytest.main([__file__])
