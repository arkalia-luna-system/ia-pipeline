"""
Tests unitaires générés pour _serializers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _serializers
except ImportError:
    pytest.skip(f"Module _serializers non importable")


def test_serialize_sequence_via_list():
    """Test de la fonction serialize_sequence_via_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_serializers, 'serialize_sequence_via_list')
    assert callable(getattr(_serializers, 'serialize_sequence_via_list'))

if __name__ == "__main__":
    pytest.main([__file__])
