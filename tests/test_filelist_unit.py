"""
Tests unitaires générés pour filelist
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import filelist
except ImportError:
    pytest.skip(f"Module filelist non importable")


def test__find_all_simple():
    """Test de la fonction _find_all_simple"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, '_find_all_simple')
    assert callable(getattr(filelist, '_find_all_simple'))

def test_findall():
    """Test de la fonction findall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'findall')
    assert callable(getattr(filelist, 'findall'))

def test_glob_to_re():
    """Test de la fonction glob_to_re"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'glob_to_re')
    assert callable(getattr(filelist, 'glob_to_re'))

def test_translate_pattern():
    """Test de la fonction translate_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'translate_pattern')
    assert callable(getattr(filelist, 'translate_pattern'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, '__init__')
    assert callable(getattr(filelist, '__init__'))

def test_set_allfiles():
    """Test de la fonction set_allfiles"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'set_allfiles')
    assert callable(getattr(filelist, 'set_allfiles'))

def test_findall():
    """Test de la fonction findall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'findall')
    assert callable(getattr(filelist, 'findall'))

def test_debug_print():
    """Test de la fonction debug_print"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'debug_print')
    assert callable(getattr(filelist, 'debug_print'))

def test_append():
    """Test de la fonction append"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'append')
    assert callable(getattr(filelist, 'append'))

def test_extend():
    """Test de la fonction extend"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'extend')
    assert callable(getattr(filelist, 'extend'))

def test_sort():
    """Test de la fonction sort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'sort')
    assert callable(getattr(filelist, 'sort'))

def test_remove_duplicates():
    """Test de la fonction remove_duplicates"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'remove_duplicates')
    assert callable(getattr(filelist, 'remove_duplicates'))

def test__parse_template_line():
    """Test de la fonction _parse_template_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, '_parse_template_line')
    assert callable(getattr(filelist, '_parse_template_line'))

def test_process_template_line():
    """Test de la fonction process_template_line"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'process_template_line')
    assert callable(getattr(filelist, 'process_template_line'))

def test_include_pattern():
    """Test de la fonction include_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'include_pattern')
    assert callable(getattr(filelist, 'include_pattern'))

def test_include_pattern():
    """Test de la fonction include_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'include_pattern')
    assert callable(getattr(filelist, 'include_pattern'))

def test_include_pattern():
    """Test de la fonction include_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'include_pattern')
    assert callable(getattr(filelist, 'include_pattern'))

def test_include_pattern():
    """Test de la fonction include_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'include_pattern')
    assert callable(getattr(filelist, 'include_pattern'))

def test_exclude_pattern():
    """Test de la fonction exclude_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'exclude_pattern')
    assert callable(getattr(filelist, 'exclude_pattern'))

def test_exclude_pattern():
    """Test de la fonction exclude_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'exclude_pattern')
    assert callable(getattr(filelist, 'exclude_pattern'))

def test_exclude_pattern():
    """Test de la fonction exclude_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'exclude_pattern')
    assert callable(getattr(filelist, 'exclude_pattern'))

def test_exclude_pattern():
    """Test de la fonction exclude_pattern"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'exclude_pattern')
    assert callable(getattr(filelist, 'exclude_pattern'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, '__call__')
    assert callable(getattr(filelist, '__call__'))

def test_filter():
    """Test de la fonction filter"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(filelist, 'filter')
    assert callable(getattr(filelist, 'filter'))

class TestFileList:
    """Tests pour la classe FileList"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(filelist, 'FileList')
        assert isinstance(getattr(filelist, 'FileList'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(filelist, 'FileList')
        for method_name in ['__init__', 'set_allfiles', 'findall', 'debug_print', 'append', 'extend', 'sort', 'remove_duplicates', '_parse_template_line', 'process_template_line', 'include_pattern', 'include_pattern', 'include_pattern', 'include_pattern', 'exclude_pattern', 'exclude_pattern', 'exclude_pattern', 'exclude_pattern']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_UniqueDirs:
    """Tests pour la classe _UniqueDirs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(filelist, '_UniqueDirs')
        assert isinstance(getattr(filelist, '_UniqueDirs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(filelist, '_UniqueDirs')
        for method_name in ['__call__', 'filter']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
