"""
Tests unitaires générés pour latex
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import latex
except ImportError:
    pytest.skip(f"Module latex non importable")


def test_preprocess():
    """Test de la fonction preprocess"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latex, 'preprocess')
    assert callable(getattr(latex, 'preprocess'))

class TestLatexPreprocessor:
    """Tests pour la classe LatexPreprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(latex, 'LatexPreprocessor')
        assert isinstance(getattr(latex, 'LatexPreprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(latex, 'LatexPreprocessor')
        for method_name in ['preprocess']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
