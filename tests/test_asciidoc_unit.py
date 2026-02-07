"""
Tests unitaires générés pour asciidoc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import asciidoc
except ImportError:
    pytest.skip(f"Module asciidoc non importable")


def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asciidoc, '_file_extension_default')
    assert callable(getattr(asciidoc, '_file_extension_default'))

def test__template_name_default():
    """Test de la fonction _template_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asciidoc, '_template_name_default')
    assert callable(getattr(asciidoc, '_template_name_default'))

def test__raw_mimetypes_default():
    """Test de la fonction _raw_mimetypes_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asciidoc, '_raw_mimetypes_default')
    assert callable(getattr(asciidoc, '_raw_mimetypes_default'))

def test_default_config():
    """Test de la fonction default_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(asciidoc, 'default_config')
    assert callable(getattr(asciidoc, 'default_config'))

class TestASCIIDocExporter:
    """Tests pour la classe ASCIIDocExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(asciidoc, 'ASCIIDocExporter')
        assert isinstance(getattr(asciidoc, 'ASCIIDocExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(asciidoc, 'ASCIIDocExporter')
        for method_name in ['_file_extension_default', '_template_name_default', '_raw_mimetypes_default', 'default_config']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
