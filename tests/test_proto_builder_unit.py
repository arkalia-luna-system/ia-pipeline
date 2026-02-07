"""
Tests unitaires générés pour proto_builder
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import proto_builder
except ImportError:
    pytest.skip(f"Module proto_builder non importable")


def test__GetMessageFromFactory():
    """Test de la fonction _GetMessageFromFactory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(proto_builder, '_GetMessageFromFactory')
    assert callable(getattr(proto_builder, '_GetMessageFromFactory'))

def test_MakeSimpleProtoClass():
    """Test de la fonction MakeSimpleProtoClass"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(proto_builder, 'MakeSimpleProtoClass')
    assert callable(getattr(proto_builder, 'MakeSimpleProtoClass'))

def test__MakeFileDescriptorProto():
    """Test de la fonction _MakeFileDescriptorProto"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(proto_builder, '_MakeFileDescriptorProto')
    assert callable(getattr(proto_builder, '_MakeFileDescriptorProto'))

if __name__ == "__main__":
    pytest.main([__file__])
