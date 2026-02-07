"""
Tests unitaires générés pour coalescestreams
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import coalescestreams
except ImportError:
    pytest.skip(f"Module coalescestreams non importable")


def test_preprocess_cell():
    """Test de la fonction preprocess_cell"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(coalescestreams, 'preprocess_cell')
    assert callable(getattr(coalescestreams, 'preprocess_cell'))

class TestCoalesceStreamsPreprocessor:
    """Tests pour la classe CoalesceStreamsPreprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(coalescestreams, 'CoalesceStreamsPreprocessor')
        assert isinstance(getattr(coalescestreams, 'CoalesceStreamsPreprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(coalescestreams, 'CoalesceStreamsPreprocessor')
        for method_name in ['preprocess_cell']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
