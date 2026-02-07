"""
Tests unitaires générés pour template
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import template
except ImportError:
    pytest.skip(f"Module template non importable")


def test_filter_whitespace():
    """Test de la fonction filter_whitespace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'filter_whitespace')
    assert callable(getattr(template, 'filter_whitespace'))

def test__format_code():
    """Test de la fonction _format_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '_format_code')
    assert callable(getattr(template, '_format_code'))

def test__parse():
    """Test de la fonction _parse"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '_parse')
    assert callable(getattr(template, '_parse'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test__generate_python():
    """Test de la fonction _generate_python"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '_generate_python')
    assert callable(getattr(template, '_generate_python'))

def test__get_ancestors():
    """Test de la fonction _get_ancestors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '_get_ancestors')
    assert callable(getattr(template, '_get_ancestors'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_reset():
    """Test de la fonction reset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'reset')
    assert callable(getattr(template, 'reset'))

def test_resolve_path():
    """Test de la fonction resolve_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'resolve_path')
    assert callable(getattr(template, 'resolve_path'))

def test_load():
    """Test de la fonction load"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'load')
    assert callable(getattr(template, 'load'))

def test__create_template():
    """Test de la fonction _create_template"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '_create_template')
    assert callable(getattr(template, '_create_template'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_resolve_path():
    """Test de la fonction resolve_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'resolve_path')
    assert callable(getattr(template, 'resolve_path'))

def test__create_template():
    """Test de la fonction _create_template"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '_create_template')
    assert callable(getattr(template, '_create_template'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_resolve_path():
    """Test de la fonction resolve_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'resolve_path')
    assert callable(getattr(template, 'resolve_path'))

def test__create_template():
    """Test de la fonction _create_template"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '_create_template')
    assert callable(getattr(template, '_create_template'))

def test_each_child():
    """Test de la fonction each_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'each_child')
    assert callable(getattr(template, 'each_child'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test_find_named_blocks():
    """Test de la fonction find_named_blocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'find_named_blocks')
    assert callable(getattr(template, 'find_named_blocks'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test_each_child():
    """Test de la fonction each_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'each_child')
    assert callable(getattr(template, 'each_child'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test_each_child():
    """Test de la fonction each_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'each_child')
    assert callable(getattr(template, 'each_child'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_each_child():
    """Test de la fonction each_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'each_child')
    assert callable(getattr(template, 'each_child'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test_find_named_blocks():
    """Test de la fonction find_named_blocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'find_named_blocks')
    assert callable(getattr(template, 'find_named_blocks'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_find_named_blocks():
    """Test de la fonction find_named_blocks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'find_named_blocks')
    assert callable(getattr(template, 'find_named_blocks'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_each_child():
    """Test de la fonction each_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'each_child')
    assert callable(getattr(template, 'each_child'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_each_child():
    """Test de la fonction each_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'each_child')
    assert callable(getattr(template, 'each_child'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_generate():
    """Test de la fonction generate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'generate')
    assert callable(getattr(template, 'generate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__str__')
    assert callable(getattr(template, '__str__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_indent_size():
    """Test de la fonction indent_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'indent_size')
    assert callable(getattr(template, 'indent_size'))

def test_indent():
    """Test de la fonction indent"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'indent')
    assert callable(getattr(template, 'indent'))

def test_include():
    """Test de la fonction include"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'include')
    assert callable(getattr(template, 'include'))

def test_write_line():
    """Test de la fonction write_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'write_line')
    assert callable(getattr(template, 'write_line'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__init__')
    assert callable(getattr(template, '__init__'))

def test_find():
    """Test de la fonction find"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'find')
    assert callable(getattr(template, 'find'))

def test_consume():
    """Test de la fonction consume"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'consume')
    assert callable(getattr(template, 'consume'))

def test_remaining():
    """Test de la fonction remaining"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'remaining')
    assert callable(getattr(template, 'remaining'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__len__')
    assert callable(getattr(template, '__len__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__getitem__')
    assert callable(getattr(template, '__getitem__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__str__')
    assert callable(getattr(template, '__str__'))

def test_raise_parse_error():
    """Test de la fonction raise_parse_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, 'raise_parse_error')
    assert callable(getattr(template, 'raise_parse_error'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__enter__')
    assert callable(getattr(template, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__exit__')
    assert callable(getattr(template, '__exit__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__enter__')
    assert callable(getattr(template, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(template, '__exit__')
    assert callable(getattr(template, '__exit__'))

class Test_UnsetMarker:
    """Tests pour la classe _UnsetMarker"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_UnsetMarker')
        assert isinstance(getattr(template, '_UnsetMarker'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_UnsetMarker')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTemplate:
    """Tests pour la classe Template"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, 'Template')
        assert isinstance(getattr(template, 'Template'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, 'Template')
        for method_name in ['__init__', 'generate', '_generate_python', '_get_ancestors']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseLoader:
    """Tests pour la classe BaseLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, 'BaseLoader')
        assert isinstance(getattr(template, 'BaseLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, 'BaseLoader')
        for method_name in ['__init__', 'reset', 'resolve_path', 'load', '_create_template']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLoader:
    """Tests pour la classe Loader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, 'Loader')
        assert isinstance(getattr(template, 'Loader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, 'Loader')
        for method_name in ['__init__', 'resolve_path', '_create_template']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDictLoader:
    """Tests pour la classe DictLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, 'DictLoader')
        assert isinstance(getattr(template, 'DictLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, 'DictLoader')
        for method_name in ['__init__', 'resolve_path', '_create_template']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Node:
    """Tests pour la classe _Node"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_Node')
        assert isinstance(getattr(template, '_Node'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_Node')
        for method_name in ['each_child', 'generate', 'find_named_blocks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_File:
    """Tests pour la classe _File"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_File')
        assert isinstance(getattr(template, '_File'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_File')
        for method_name in ['__init__', 'generate', 'each_child']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_ChunkList:
    """Tests pour la classe _ChunkList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_ChunkList')
        assert isinstance(getattr(template, '_ChunkList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_ChunkList')
        for method_name in ['__init__', 'generate', 'each_child']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_NamedBlock:
    """Tests pour la classe _NamedBlock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_NamedBlock')
        assert isinstance(getattr(template, '_NamedBlock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_NamedBlock')
        for method_name in ['__init__', 'each_child', 'generate', 'find_named_blocks']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_ExtendsBlock:
    """Tests pour la classe _ExtendsBlock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_ExtendsBlock')
        assert isinstance(getattr(template, '_ExtendsBlock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_ExtendsBlock')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_IncludeBlock:
    """Tests pour la classe _IncludeBlock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_IncludeBlock')
        assert isinstance(getattr(template, '_IncludeBlock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_IncludeBlock')
        for method_name in ['__init__', 'find_named_blocks', 'generate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_ApplyBlock:
    """Tests pour la classe _ApplyBlock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_ApplyBlock')
        assert isinstance(getattr(template, '_ApplyBlock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_ApplyBlock')
        for method_name in ['__init__', 'each_child', 'generate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_ControlBlock:
    """Tests pour la classe _ControlBlock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_ControlBlock')
        assert isinstance(getattr(template, '_ControlBlock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_ControlBlock')
        for method_name in ['__init__', 'each_child', 'generate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_IntermediateControlBlock:
    """Tests pour la classe _IntermediateControlBlock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_IntermediateControlBlock')
        assert isinstance(getattr(template, '_IntermediateControlBlock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_IntermediateControlBlock')
        for method_name in ['__init__', 'generate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Statement:
    """Tests pour la classe _Statement"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_Statement')
        assert isinstance(getattr(template, '_Statement'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_Statement')
        for method_name in ['__init__', 'generate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Expression:
    """Tests pour la classe _Expression"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_Expression')
        assert isinstance(getattr(template, '_Expression'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_Expression')
        for method_name in ['__init__', 'generate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Module:
    """Tests pour la classe _Module"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_Module')
        assert isinstance(getattr(template, '_Module'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_Module')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_Text:
    """Tests pour la classe _Text"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_Text')
        assert isinstance(getattr(template, '_Text'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_Text')
        for method_name in ['__init__', 'generate']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestParseError:
    """Tests pour la classe ParseError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, 'ParseError')
        assert isinstance(getattr(template, 'ParseError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, 'ParseError')
        for method_name in ['__init__', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_CodeWriter:
    """Tests pour la classe _CodeWriter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_CodeWriter')
        assert isinstance(getattr(template, '_CodeWriter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_CodeWriter')
        for method_name in ['__init__', 'indent_size', 'indent', 'include', 'write_line']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_TemplateReader:
    """Tests pour la classe _TemplateReader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, '_TemplateReader')
        assert isinstance(getattr(template, '_TemplateReader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, '_TemplateReader')
        for method_name in ['__init__', 'find', 'consume', 'remaining', '__len__', '__getitem__', '__str__', 'raise_parse_error']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIndenter:
    """Tests pour la classe Indenter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, 'Indenter')
        assert isinstance(getattr(template, 'Indenter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, 'Indenter')
        for method_name in ['__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestIncludeTemplate:
    """Tests pour la classe IncludeTemplate"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(template, 'IncludeTemplate')
        assert isinstance(getattr(template, 'IncludeTemplate'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(template, 'IncludeTemplate')
        for method_name in ['__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
