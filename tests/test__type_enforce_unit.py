"""
Tests unitaires générés pour _type_enforce
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _type_enforce
except ImportError:
    pytest.skip(f"Module _type_enforce non importable")


def test_is_value_of_type():
    """Test de la fonction is_value_of_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_type_enforce, 'is_value_of_type')
    assert callable(getattr(_type_enforce, 'is_value_of_type'))

if __name__ == "__main__":
    pytest.main([__file__])
