"""
Tests unitaires générés pour html
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import html
except ImportError:
    pytest.skip(f"Module html non importable")


def test_find_lab_theme():
    """Test de la fonction find_lab_theme"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'find_lab_theme')
    assert callable(getattr(html, 'find_lab_theme'))

def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, '_file_extension_default')
    assert callable(getattr(html, '_file_extension_default'))

def test__template_name_default():
    """Test de la fonction _template_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, '_template_name_default')
    assert callable(getattr(html, '_template_name_default'))

def test_default_config():
    """Test de la fonction default_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'default_config')
    assert callable(getattr(html, 'default_config'))

def test__valid_language_code():
    """Test de la fonction _valid_language_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, '_valid_language_code')
    assert callable(getattr(html, '_valid_language_code'))

def test_markdown2html():
    """Test de la fonction markdown2html"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'markdown2html')
    assert callable(getattr(html, 'markdown2html'))

def test_default_filters():
    """Test de la fonction default_filters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'default_filters')
    assert callable(getattr(html, 'default_filters'))

def test_from_notebook_node():
    """Test de la fonction from_notebook_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'from_notebook_node')
    assert callable(getattr(html, 'from_notebook_node'))

def test__init_resources():
    """Test de la fonction _init_resources"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, '_init_resources')
    assert callable(getattr(html, '_init_resources'))

def test_resources_include_css():
    """Test de la fonction resources_include_css"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'resources_include_css')
    assert callable(getattr(html, 'resources_include_css'))

def test_resources_include_lab_theme():
    """Test de la fonction resources_include_lab_theme"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'resources_include_lab_theme')
    assert callable(getattr(html, 'resources_include_lab_theme'))

def test_resources_include_js():
    """Test de la fonction resources_include_js"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'resources_include_js')
    assert callable(getattr(html, 'resources_include_js'))

def test_resources_include_url():
    """Test de la fonction resources_include_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(html, 'resources_include_url')
    assert callable(getattr(html, 'resources_include_url'))

class TestHTMLExporter:
    """Tests pour la classe HTMLExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(html, 'HTMLExporter')
        assert isinstance(getattr(html, 'HTMLExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(html, 'HTMLExporter')
        for method_name in ['_file_extension_default', '_template_name_default', 'default_config', '_valid_language_code', 'markdown2html', 'default_filters', 'from_notebook_node', '_init_resources']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
