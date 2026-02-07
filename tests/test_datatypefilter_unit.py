"""
Tests unitaires générés pour datatypefilter
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import datatypefilter
except ImportError:
    pytest.skip(f"Module datatypefilter non importable")


def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(datatypefilter, '__call__')
    assert callable(getattr(datatypefilter, '__call__'))

class TestDataTypeFilter:
    """Tests pour la classe DataTypeFilter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(datatypefilter, 'DataTypeFilter')
        assert isinstance(getattr(datatypefilter, 'DataTypeFilter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(datatypefilter, 'DataTypeFilter')
        for method_name in ['__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
