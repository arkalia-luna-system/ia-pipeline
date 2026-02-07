"""
Tests unitaires générés pour _files
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _files
except ImportError:
    pytest.skip(f"Module _files non importable")


def test_generate_datetime_filename():
    """Test de la fonction generate_datetime_filename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_files, 'generate_datetime_filename')
    assert callable(getattr(_files, 'generate_datetime_filename'))

if __name__ == "__main__":
    pytest.main([__file__])
