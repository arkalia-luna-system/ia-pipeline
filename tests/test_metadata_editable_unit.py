"""
Tests unitaires générés pour metadata_editable
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import metadata_editable
except ImportError:
    pytest.skip(f"Module metadata_editable non importable")


def test_generate_editable_metadata():
    """Test de la fonction generate_editable_metadata"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(metadata_editable, 'generate_editable_metadata')
    assert callable(getattr(metadata_editable, 'generate_editable_metadata'))

if __name__ == "__main__":
    pytest.main([__file__])
