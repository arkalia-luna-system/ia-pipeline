"""
Tests unitaires générés pour slides
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import slides
except ImportError:
    pytest.skip(f"Module slides non importable")


def test_preprocess():
    """Test de la fonction preprocess"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(slides, 'preprocess')
    assert callable(getattr(slides, 'preprocess'))

def test__template_name_default():
    """Test de la fonction _template_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(slides, '_template_name_default')
    assert callable(getattr(slides, '_template_name_default'))

def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(slides, '_file_extension_default')
    assert callable(getattr(slides, '_file_extension_default'))

def test__template_extension_default():
    """Test de la fonction _template_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(slides, '_template_extension_default')
    assert callable(getattr(slides, '_template_extension_default'))

def test__reveal_url_prefix_default():
    """Test de la fonction _reveal_url_prefix_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(slides, '_reveal_url_prefix_default')
    assert callable(getattr(slides, '_reveal_url_prefix_default'))

def test__init_resources():
    """Test de la fonction _init_resources"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(slides, '_init_resources')
    assert callable(getattr(slides, '_init_resources'))

class Test_RevealMetadataPreprocessor:
    """Tests pour la classe _RevealMetadataPreprocessor"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(slides, '_RevealMetadataPreprocessor')
        assert isinstance(getattr(slides, '_RevealMetadataPreprocessor'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(slides, '_RevealMetadataPreprocessor')
        for method_name in ['preprocess']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSlidesExporter:
    """Tests pour la classe SlidesExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(slides, 'SlidesExporter')
        assert isinstance(getattr(slides, 'SlidesExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(slides, 'SlidesExporter')
        for method_name in ['_template_name_default', '_file_extension_default', '_template_extension_default', '_reveal_url_prefix_default', '_init_resources']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
