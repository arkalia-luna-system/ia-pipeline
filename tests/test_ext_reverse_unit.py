"""
Tests unitaires générés pour ext_reverse
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ext_reverse
except ImportError:
    pytest.skip(f"Module ext_reverse non importable")


def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ext_reverse, '__getitem__')
    assert callable(getattr(ext_reverse, '__getitem__'))

class TestReversePage:
    """Tests pour la classe ReversePage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ext_reverse, 'ReversePage')
        assert isinstance(getattr(ext_reverse, 'ReversePage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ext_reverse, 'ReversePage')
        for method_name in ['__getitem__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
