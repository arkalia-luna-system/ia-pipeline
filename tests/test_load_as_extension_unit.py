"""
Tests unitaires générés pour load_as_extension
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import load_as_extension
except ImportError:
    pytest.skip(f"Module load_as_extension non importable")


def test_format_data():
    """Test de la fonction format_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(load_as_extension, 'format_data')
    assert callable(getattr(load_as_extension, 'format_data'))

if __name__ == "__main__":
    pytest.main([__file__])
