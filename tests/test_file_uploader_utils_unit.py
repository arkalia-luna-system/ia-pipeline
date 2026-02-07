"""
Tests unitaires générés pour file_uploader_utils
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import file_uploader_utils
except ImportError:
    pytest.skip(f"Module file_uploader_utils non importable")


def test_normalize_upload_file_type():
    """Test de la fonction normalize_upload_file_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_uploader_utils, 'normalize_upload_file_type')
    assert callable(getattr(file_uploader_utils, 'normalize_upload_file_type'))

def test_enforce_filename_restriction():
    """Test de la fonction enforce_filename_restriction"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(file_uploader_utils, 'enforce_filename_restriction')
    assert callable(getattr(file_uploader_utils, 'enforce_filename_restriction'))

if __name__ == "__main__":
    pytest.main([__file__])
