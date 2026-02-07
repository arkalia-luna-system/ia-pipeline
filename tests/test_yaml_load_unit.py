"""
Tests unitaires générés pour yaml_load
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import yaml_load
except ImportError:
    pytest.skip(f"Module yaml_load non importable")


def test_yaml_load():
    """Test de la fonction yaml_load"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(yaml_load, 'yaml_load')
    assert callable(getattr(yaml_load, 'yaml_load'))

if __name__ == "__main__":
    pytest.main([__file__])
