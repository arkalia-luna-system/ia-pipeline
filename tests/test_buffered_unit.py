"""
Tests unitaires générés pour buffered
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import buffered
except ImportError:
    pytest.skip(f"Module buffered non importable")


def test_buffer():
    """Test de la fonction buffer"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffered, 'buffer')
    assert callable(getattr(buffered, 'buffer'))

def test_extra_attributes():
    """Test de la fonction extra_attributes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(buffered, 'extra_attributes')
    assert callable(getattr(buffered, 'extra_attributes'))

class TestBufferedByteReceiveStream:
    """Tests pour la classe BufferedByteReceiveStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(buffered, 'BufferedByteReceiveStream')
        assert isinstance(getattr(buffered, 'BufferedByteReceiveStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(buffered, 'BufferedByteReceiveStream')
        for method_name in ['buffer', 'extra_attributes']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
