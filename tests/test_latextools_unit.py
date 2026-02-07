"""
Tests unitaires générés pour latextools
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import latextools
except ImportError:
    pytest.skip(f"Module latextools non importable")


def test_latex_to_png():
    """Test de la fonction latex_to_png"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latextools, 'latex_to_png')
    assert callable(getattr(latextools, 'latex_to_png'))

def test_latex_to_png_mpl():
    """Test de la fonction latex_to_png_mpl"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latextools, 'latex_to_png_mpl')
    assert callable(getattr(latextools, 'latex_to_png_mpl'))

def test_latex_to_png_dvipng():
    """Test de la fonction latex_to_png_dvipng"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latextools, 'latex_to_png_dvipng')
    assert callable(getattr(latextools, 'latex_to_png_dvipng'))

def test_kpsewhich():
    """Test de la fonction kpsewhich"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latextools, 'kpsewhich')
    assert callable(getattr(latextools, 'kpsewhich'))

def test_genelatex():
    """Test de la fonction genelatex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latextools, 'genelatex')
    assert callable(getattr(latextools, 'genelatex'))

def test_latex_to_html():
    """Test de la fonction latex_to_html"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latextools, 'latex_to_html')
    assert callable(getattr(latextools, 'latex_to_html'))

def test__config_default():
    """Test de la fonction _config_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(latextools, '_config_default')
    assert callable(getattr(latextools, '_config_default'))

class TestLaTeXTool:
    """Tests pour la classe LaTeXTool"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(latextools, 'LaTeXTool')
        assert isinstance(getattr(latextools, 'LaTeXTool'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(latextools, 'LaTeXTool')
        for method_name in ['_config_default']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
