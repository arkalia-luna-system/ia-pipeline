"""
Tests unitaires générés pour webpdf
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import webpdf
except ImportError:
    pytest.skip(f"Module webpdf non importable")


def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(webpdf, '_file_extension_default')
    assert callable(getattr(webpdf, '_file_extension_default'))

def test__template_name_default():
    """Test de la fonction _template_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(webpdf, '_template_name_default')
    assert callable(getattr(webpdf, '_template_name_default'))

def test_run_playwright():
    """Test de la fonction run_playwright"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(webpdf, 'run_playwright')
    assert callable(getattr(webpdf, 'run_playwright'))

def test_from_notebook_node():
    """Test de la fonction from_notebook_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(webpdf, 'from_notebook_node')
    assert callable(getattr(webpdf, 'from_notebook_node'))

def test_run_coroutine():
    """Test de la fonction run_coroutine"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(webpdf, 'run_coroutine')
    assert callable(getattr(webpdf, 'run_coroutine'))

class TestWebPDFExporter:
    """Tests pour la classe WebPDFExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(webpdf, 'WebPDFExporter')
        assert isinstance(getattr(webpdf, 'WebPDFExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(webpdf, 'WebPDFExporter')
        for method_name in ['_file_extension_default', '_template_name_default', 'run_playwright', 'from_notebook_node']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
