"""
Tests unitaires générés pour dirtools
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dirtools
except ImportError:
    pytest.skip(f"Module dirtools non importable")


def test_dir_to_zipfile():
    """Test de la fonction dir_to_zipfile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dirtools, 'dir_to_zipfile')
    assert callable(getattr(dirtools, 'dir_to_zipfile'))

if __name__ == "__main__":
    pytest.main([__file__])
