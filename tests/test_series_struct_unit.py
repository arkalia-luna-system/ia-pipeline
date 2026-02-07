"""
Tests unitaires générés pour series_struct
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import series_struct
except ImportError:
    pytest.skip(f"Module series_struct non importable")


def test_field():
    """Test de la fonction field"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_struct, 'field')
    assert callable(getattr(series_struct, 'field'))

class TestPandasLikeSeriesStructNamespace:
    """Tests pour la classe PandasLikeSeriesStructNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(series_struct, 'PandasLikeSeriesStructNamespace')
        assert isinstance(getattr(series_struct, 'PandasLikeSeriesStructNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(series_struct, 'PandasLikeSeriesStructNamespace')
        for method_name in ['field']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
