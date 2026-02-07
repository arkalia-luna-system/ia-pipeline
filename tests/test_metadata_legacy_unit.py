"""
Tests unitaires générés pour metadata_legacy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import metadata_legacy
except ImportError:
    pytest.skip(f"Module metadata_legacy non importable")


def test__find_egg_info():
    """Test de la fonction _find_egg_info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(metadata_legacy, '_find_egg_info')
    assert callable(getattr(metadata_legacy, '_find_egg_info'))

def test_generate_metadata():
    """Test de la fonction generate_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(metadata_legacy, 'generate_metadata')
    assert callable(getattr(metadata_legacy, 'generate_metadata'))

if __name__ == "__main__":
    pytest.main([__file__])
