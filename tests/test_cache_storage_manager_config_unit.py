"""
Tests unitaires générés pour cache_storage_manager_config
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cache_storage_manager_config
except ImportError:
    pytest.skip(f"Module cache_storage_manager_config non importable")


def test_create_default_cache_storage_manager():
    """Test de la fonction create_default_cache_storage_manager"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(cache_storage_manager_config, 'create_default_cache_storage_manager')
    assert callable(getattr(cache_storage_manager_config, 'create_default_cache_storage_manager'))

if __name__ == "__main__":
    pytest.main([__file__])
