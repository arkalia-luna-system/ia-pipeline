"""
Tests unitaires générés pour rst
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rst
except ImportError:
    pytest.skip(f"Module rst non importable")


def test__file_extension_default():
    """Test de la fonction _file_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rst, '_file_extension_default')
    assert callable(getattr(rst, '_file_extension_default'))

def test__template_name_default():
    """Test de la fonction _template_name_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rst, '_template_name_default')
    assert callable(getattr(rst, '_template_name_default'))

def test__raw_mimetypes_default():
    """Test de la fonction _raw_mimetypes_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rst, '_raw_mimetypes_default')
    assert callable(getattr(rst, '_raw_mimetypes_default'))

def test_default_filters():
    """Test de la fonction default_filters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rst, 'default_filters')
    assert callable(getattr(rst, 'default_filters'))

def test_default_config():
    """Test de la fonction default_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(rst, 'default_config')
    assert callable(getattr(rst, 'default_config'))

class TestRSTExporter:
    """Tests pour la classe RSTExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rst, 'RSTExporter')
        assert isinstance(getattr(rst, 'RSTExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rst, 'RSTExporter')
        for method_name in ['_file_extension_default', '_template_name_default', '_raw_mimetypes_default', 'default_filters', 'default_config']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
