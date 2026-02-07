"""
Tests unitaires générés pour series_list
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import series_list
except ImportError:
    pytest.skip(f"Module series_list non importable")


def test_len():
    """Test de la fonction len"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_list, 'len')
    assert callable(getattr(series_list, 'len'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_list, 'get')
    assert callable(getattr(series_list, 'get'))

class TestPandasLikeSeriesListNamespace:
    """Tests pour la classe PandasLikeSeriesListNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(series_list, 'PandasLikeSeriesListNamespace')
        assert isinstance(getattr(series_list, 'PandasLikeSeriesListNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(series_list, 'PandasLikeSeriesListNamespace')
        for method_name in ['len', 'get']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
