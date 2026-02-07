"""
Tests unitaires générés pour templateexporter
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import templateexporter
except ImportError:
    pytest.skip(f"Module templateexporter non importable")


def test_recursive_update():
    """Test de la fonction recursive_update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'recursive_update')
    assert callable(getattr(templateexporter, 'recursive_update'))

def test_deprecated():
    """Test de la fonction deprecated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'deprecated')
    assert callable(getattr(templateexporter, 'deprecated'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '__init__')
    assert callable(getattr(templateexporter, '__init__'))

def test_get_source():
    """Test de la fonction get_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'get_source')
    assert callable(getattr(templateexporter, 'get_source'))

def test_list_templates():
    """Test de la fonction list_templates"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'list_templates')
    assert callable(getattr(templateexporter, 'list_templates'))

def test__invalidate_template_cache():
    """Test de la fonction _invalidate_template_cache"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_invalidate_template_cache')
    assert callable(getattr(templateexporter, '_invalidate_template_cache'))

def test_template():
    """Test de la fonction template"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'template')
    assert callable(getattr(templateexporter, 'template'))

def test__invalidate_environment_cache():
    """Test de la fonction _invalidate_environment_cache"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_invalidate_environment_cache')
    assert callable(getattr(templateexporter, '_invalidate_environment_cache'))

def test_environment():
    """Test de la fonction environment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'environment')
    assert callable(getattr(templateexporter, 'environment'))

def test_default_config():
    """Test de la fonction default_config"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'default_config')
    assert callable(getattr(templateexporter, 'default_config'))

def test__template_name_validate():
    """Test de la fonction _template_name_validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_template_name_validate')
    assert callable(getattr(templateexporter, '_template_name_validate'))

def test__template_file_changed():
    """Test de la fonction _template_file_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_template_file_changed')
    assert callable(getattr(templateexporter, '_template_file_changed'))

def test__template_file_default():
    """Test de la fonction _template_file_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_template_file_default')
    assert callable(getattr(templateexporter, '_template_file_default'))

def test__raw_template_changed():
    """Test de la fonction _raw_template_changed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_raw_template_changed')
    assert callable(getattr(templateexporter, '_raw_template_changed'))

def test__default_extra_template_basedirs():
    """Test de la fonction _default_extra_template_basedirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_default_extra_template_basedirs')
    assert callable(getattr(templateexporter, '_default_extra_template_basedirs'))

def test__template_extension_default():
    """Test de la fonction _template_extension_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_template_extension_default')
    assert callable(getattr(templateexporter, '_template_extension_default'))

def test__raw_mimetypes_default():
    """Test de la fonction _raw_mimetypes_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_raw_mimetypes_default')
    assert callable(getattr(templateexporter, '_raw_mimetypes_default'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '__init__')
    assert callable(getattr(templateexporter, '__init__'))

def test__load_template():
    """Test de la fonction _load_template"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_load_template')
    assert callable(getattr(templateexporter, '_load_template'))

def test_from_filename():
    """Test de la fonction from_filename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'from_filename')
    assert callable(getattr(templateexporter, 'from_filename'))

def test_from_file():
    """Test de la fonction from_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'from_file')
    assert callable(getattr(templateexporter, 'from_file'))

def test_from_notebook_node():
    """Test de la fonction from_notebook_node"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'from_notebook_node')
    assert callable(getattr(templateexporter, 'from_notebook_node'))

def test__register_filter():
    """Test de la fonction _register_filter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_register_filter')
    assert callable(getattr(templateexporter, '_register_filter'))

def test_register_filter():
    """Test de la fonction register_filter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'register_filter')
    assert callable(getattr(templateexporter, 'register_filter'))

def test_default_filters():
    """Test de la fonction default_filters"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'default_filters')
    assert callable(getattr(templateexporter, 'default_filters'))

def test__create_environment():
    """Test de la fonction _create_environment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_create_environment')
    assert callable(getattr(templateexporter, '_create_environment'))

def test__init_preprocessors():
    """Test de la fonction _init_preprocessors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_init_preprocessors')
    assert callable(getattr(templateexporter, '_init_preprocessors'))

def test__get_conf():
    """Test de la fonction _get_conf"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_get_conf')
    assert callable(getattr(templateexporter, '_get_conf'))

def test__template_paths():
    """Test de la fonction _template_paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_template_paths')
    assert callable(getattr(templateexporter, '_template_paths'))

def test_get_compatibility_base_template_conf():
    """Test de la fonction get_compatibility_base_template_conf"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'get_compatibility_base_template_conf')
    assert callable(getattr(templateexporter, 'get_compatibility_base_template_conf'))

def test_get_template_names():
    """Test de la fonction get_template_names"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'get_template_names')
    assert callable(getattr(templateexporter, 'get_template_names'))

def test_get_prefix_root_dirs():
    """Test de la fonction get_prefix_root_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, 'get_prefix_root_dirs')
    assert callable(getattr(templateexporter, 'get_prefix_root_dirs'))

def test__init_resources():
    """Test de la fonction _init_resources"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(templateexporter, '_init_resources')
    assert callable(getattr(templateexporter, '_init_resources'))

class TestExtensionTolerantLoader:
    """Tests pour la classe ExtensionTolerantLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(templateexporter, 'ExtensionTolerantLoader')
        assert isinstance(getattr(templateexporter, 'ExtensionTolerantLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(templateexporter, 'ExtensionTolerantLoader')
        for method_name in ['__init__', 'get_source', 'list_templates']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTemplateExporter:
    """Tests pour la classe TemplateExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(templateexporter, 'TemplateExporter')
        assert isinstance(getattr(templateexporter, 'TemplateExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(templateexporter, 'TemplateExporter')
        for method_name in ['_invalidate_template_cache', 'template', '_invalidate_environment_cache', 'environment', 'default_config', '_template_name_validate', '_template_file_changed', '_template_file_default', '_raw_template_changed', '_default_extra_template_basedirs', '_template_extension_default', '_raw_mimetypes_default', '__init__', '_load_template', 'from_filename', 'from_file', 'from_notebook_node', '_register_filter', 'register_filter', 'default_filters', '_create_environment', '_init_preprocessors', '_get_conf', '_template_paths', 'get_compatibility_base_template_conf', 'get_template_names', 'get_prefix_root_dirs', '_init_resources']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
