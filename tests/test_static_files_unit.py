"""
Tests unitaires générés pour static_files
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import static_files
except ImportError:
    pytest.skip(f"Module static_files non importable")


def test_get_static_file():
    """Test de la fonction get_static_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(static_files, 'get_static_file')
    assert callable(getattr(static_files, 'get_static_file'))

if __name__ == "__main__":
    pytest.main([__file__])
