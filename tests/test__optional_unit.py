"""
Tests unitaires générés pour _optional
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _optional
except ImportError:
    pytest.skip(f"Module _optional non importable")


def test_get_version():
    """Test de la fonction get_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_optional, 'get_version')
    assert callable(getattr(_optional, 'get_version'))

def test_import_optional_dependency():
    """Test de la fonction import_optional_dependency"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_optional, 'import_optional_dependency')
    assert callable(getattr(_optional, 'import_optional_dependency'))

if __name__ == "__main__":
    pytest.main([__file__])
