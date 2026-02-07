"""
Tests unitaires générés pour series_cat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import series_cat
except ImportError:
    pytest.skip(f"Module series_cat non importable")


def test_get_categories():
    """Test de la fonction get_categories"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(series_cat, 'get_categories')
    assert callable(getattr(series_cat, 'get_categories'))

class TestPandasLikeSeriesCatNamespace:
    """Tests pour la classe PandasLikeSeriesCatNamespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(series_cat, 'PandasLikeSeriesCatNamespace')
        assert isinstance(getattr(series_cat, 'PandasLikeSeriesCatNamespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(series_cat, 'PandasLikeSeriesCatNamespace')
        for method_name in ['get_categories']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
