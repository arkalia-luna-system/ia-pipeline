"""
Tests unitaires générés pour blob
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import blob
except ImportError:
    pytest.skip(f"Module blob non importable")


def test_mime_type():
    """Test de la fonction mime_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(blob, 'mime_type')
    assert callable(getattr(blob, 'mime_type'))

class TestBlob:
    """Tests pour la classe Blob"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(blob, 'Blob')
        assert isinstance(getattr(blob, 'Blob'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(blob, 'Blob')
        for method_name in ['mime_type']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
