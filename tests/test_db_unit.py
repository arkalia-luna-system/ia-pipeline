"""
Tests unitaires générés pour db
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import db
except ImportError:
    pytest.skip(f"Module db non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(db, '__init__')
    assert callable(getattr(db, '__init__'))

def test_info():
    """Test de la fonction info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(db, 'info')
    assert callable(getattr(db, 'info'))

def test_stream():
    """Test de la fonction stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(db, 'stream')
    assert callable(getattr(db, 'stream'))

def test_partial_to_complete_sha_hex():
    """Test de la fonction partial_to_complete_sha_hex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(db, 'partial_to_complete_sha_hex')
    assert callable(getattr(db, 'partial_to_complete_sha_hex'))

class TestGitCmdObjectDB:
    """Tests pour la classe GitCmdObjectDB"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(db, 'GitCmdObjectDB')
        assert isinstance(getattr(db, 'GitCmdObjectDB'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(db, 'GitCmdObjectDB')
        for method_name in ['__init__', 'info', 'stream', 'partial_to_complete_sha_hex']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
