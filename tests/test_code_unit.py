"""
Tests unitaires générés pour code
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import code
except ImportError:
    pytest.skip(f"Module code non importable")


def test_code():
    """Test de la fonction code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(code, 'code')
    assert callable(getattr(code, 'code'))

def test_dg():
    """Test de la fonction dg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(code, 'dg')
    assert callable(getattr(code, 'dg'))

class TestCodeMixin:
    """Tests pour la classe CodeMixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(code, 'CodeMixin')
        assert isinstance(getattr(code, 'CodeMixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(code, 'CodeMixin')
        for method_name in ['code', 'dg']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
