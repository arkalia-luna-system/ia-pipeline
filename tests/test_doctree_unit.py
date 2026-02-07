"""
Tests unitaires générés pour doctree
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import doctree
except ImportError:
    pytest.skip(f"Module doctree non importable")


def test_parse():
    """Test de la fonction parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(doctree, 'parse')
    assert callable(getattr(doctree, 'parse'))

class TestReader:
    """Tests pour la classe Reader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(doctree, 'Reader')
        assert isinstance(getattr(doctree, 'Reader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(doctree, 'Reader')
        for method_name in ['parse']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
