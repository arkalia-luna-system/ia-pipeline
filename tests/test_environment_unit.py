"""
Tests unitaires générés pour environment
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import environment
except ImportError:
    pytest.skip(f"Module environment non importable")


def test_is_type_checking():
    """Test de la fonction is_type_checking"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(environment, 'is_type_checking')
    assert callable(getattr(environment, 'is_type_checking'))

if __name__ == "__main__":
    pytest.main([__file__])
