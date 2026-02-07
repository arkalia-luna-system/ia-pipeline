"""
Tests unitaires générés pour object_array
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import object_array
except ImportError:
    pytest.skip(f"Module object_array non importable")


def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '__len__')
    assert callable(getattr(object_array, '__len__'))

def test__str_map():
    """Test de la fonction _str_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_map')
    assert callable(getattr(object_array, '_str_map'))

def test__str_count():
    """Test de la fonction _str_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_count')
    assert callable(getattr(object_array, '_str_count'))

def test__str_pad():
    """Test de la fonction _str_pad"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_pad')
    assert callable(getattr(object_array, '_str_pad'))

def test__str_contains():
    """Test de la fonction _str_contains"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_contains')
    assert callable(getattr(object_array, '_str_contains'))

def test__str_startswith():
    """Test de la fonction _str_startswith"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_startswith')
    assert callable(getattr(object_array, '_str_startswith'))

def test__str_endswith():
    """Test de la fonction _str_endswith"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_endswith')
    assert callable(getattr(object_array, '_str_endswith'))

def test__str_replace():
    """Test de la fonction _str_replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_replace')
    assert callable(getattr(object_array, '_str_replace'))

def test__str_repeat():
    """Test de la fonction _str_repeat"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_repeat')
    assert callable(getattr(object_array, '_str_repeat'))

def test__str_match():
    """Test de la fonction _str_match"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_match')
    assert callable(getattr(object_array, '_str_match'))

def test__str_fullmatch():
    """Test de la fonction _str_fullmatch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_fullmatch')
    assert callable(getattr(object_array, '_str_fullmatch'))

def test__str_encode():
    """Test de la fonction _str_encode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_encode')
    assert callable(getattr(object_array, '_str_encode'))

def test__str_find():
    """Test de la fonction _str_find"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_find')
    assert callable(getattr(object_array, '_str_find'))

def test__str_rfind():
    """Test de la fonction _str_rfind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_rfind')
    assert callable(getattr(object_array, '_str_rfind'))

def test__str_find_():
    """Test de la fonction _str_find_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_find_')
    assert callable(getattr(object_array, '_str_find_'))

def test__str_findall():
    """Test de la fonction _str_findall"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_findall')
    assert callable(getattr(object_array, '_str_findall'))

def test__str_get():
    """Test de la fonction _str_get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_get')
    assert callable(getattr(object_array, '_str_get'))

def test__str_index():
    """Test de la fonction _str_index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_index')
    assert callable(getattr(object_array, '_str_index'))

def test__str_rindex():
    """Test de la fonction _str_rindex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_rindex')
    assert callable(getattr(object_array, '_str_rindex'))

def test__str_join():
    """Test de la fonction _str_join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_join')
    assert callable(getattr(object_array, '_str_join'))

def test__str_partition():
    """Test de la fonction _str_partition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_partition')
    assert callable(getattr(object_array, '_str_partition'))

def test__str_rpartition():
    """Test de la fonction _str_rpartition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_rpartition')
    assert callable(getattr(object_array, '_str_rpartition'))

def test__str_len():
    """Test de la fonction _str_len"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_len')
    assert callable(getattr(object_array, '_str_len'))

def test__str_slice():
    """Test de la fonction _str_slice"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_slice')
    assert callable(getattr(object_array, '_str_slice'))

def test__str_slice_replace():
    """Test de la fonction _str_slice_replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_slice_replace')
    assert callable(getattr(object_array, '_str_slice_replace'))

def test__str_split():
    """Test de la fonction _str_split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_split')
    assert callable(getattr(object_array, '_str_split'))

def test__str_rsplit():
    """Test de la fonction _str_rsplit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_rsplit')
    assert callable(getattr(object_array, '_str_rsplit'))

def test__str_translate():
    """Test de la fonction _str_translate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_translate')
    assert callable(getattr(object_array, '_str_translate'))

def test__str_wrap():
    """Test de la fonction _str_wrap"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_wrap')
    assert callable(getattr(object_array, '_str_wrap'))

def test__str_get_dummies():
    """Test de la fonction _str_get_dummies"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_get_dummies')
    assert callable(getattr(object_array, '_str_get_dummies'))

def test__str_upper():
    """Test de la fonction _str_upper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_upper')
    assert callable(getattr(object_array, '_str_upper'))

def test__str_isalnum():
    """Test de la fonction _str_isalnum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_isalnum')
    assert callable(getattr(object_array, '_str_isalnum'))

def test__str_isalpha():
    """Test de la fonction _str_isalpha"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_isalpha')
    assert callable(getattr(object_array, '_str_isalpha'))

def test__str_isdecimal():
    """Test de la fonction _str_isdecimal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_isdecimal')
    assert callable(getattr(object_array, '_str_isdecimal'))

def test__str_isdigit():
    """Test de la fonction _str_isdigit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_isdigit')
    assert callable(getattr(object_array, '_str_isdigit'))

def test__str_islower():
    """Test de la fonction _str_islower"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_islower')
    assert callable(getattr(object_array, '_str_islower'))

def test__str_isnumeric():
    """Test de la fonction _str_isnumeric"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_isnumeric')
    assert callable(getattr(object_array, '_str_isnumeric'))

def test__str_isspace():
    """Test de la fonction _str_isspace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_isspace')
    assert callable(getattr(object_array, '_str_isspace'))

def test__str_istitle():
    """Test de la fonction _str_istitle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_istitle')
    assert callable(getattr(object_array, '_str_istitle'))

def test__str_isupper():
    """Test de la fonction _str_isupper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_isupper')
    assert callable(getattr(object_array, '_str_isupper'))

def test__str_capitalize():
    """Test de la fonction _str_capitalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_capitalize')
    assert callable(getattr(object_array, '_str_capitalize'))

def test__str_casefold():
    """Test de la fonction _str_casefold"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_casefold')
    assert callable(getattr(object_array, '_str_casefold'))

def test__str_title():
    """Test de la fonction _str_title"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_title')
    assert callable(getattr(object_array, '_str_title'))

def test__str_swapcase():
    """Test de la fonction _str_swapcase"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_swapcase')
    assert callable(getattr(object_array, '_str_swapcase'))

def test__str_lower():
    """Test de la fonction _str_lower"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_lower')
    assert callable(getattr(object_array, '_str_lower'))

def test__str_normalize():
    """Test de la fonction _str_normalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_normalize')
    assert callable(getattr(object_array, '_str_normalize'))

def test__str_strip():
    """Test de la fonction _str_strip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_strip')
    assert callable(getattr(object_array, '_str_strip'))

def test__str_lstrip():
    """Test de la fonction _str_lstrip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_lstrip')
    assert callable(getattr(object_array, '_str_lstrip'))

def test__str_rstrip():
    """Test de la fonction _str_rstrip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_rstrip')
    assert callable(getattr(object_array, '_str_rstrip'))

def test__str_removeprefix():
    """Test de la fonction _str_removeprefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_removeprefix')
    assert callable(getattr(object_array, '_str_removeprefix'))

def test__str_removesuffix():
    """Test de la fonction _str_removesuffix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_removesuffix')
    assert callable(getattr(object_array, '_str_removesuffix'))

def test__str_extract():
    """Test de la fonction _str_extract"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_str_extract')
    assert callable(getattr(object_array, '_str_extract'))

def test_f():
    """Test de la fonction f"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'f')
    assert callable(getattr(object_array, 'f'))

def test_f():
    """Test de la fonction f"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'f')
    assert callable(getattr(object_array, 'f'))

def test__isin():
    """Test de la fonction _isin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, '_isin')
    assert callable(getattr(object_array, '_isin'))

def test_removeprefix():
    """Test de la fonction removeprefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'removeprefix')
    assert callable(getattr(object_array, 'removeprefix'))

def test_f():
    """Test de la fonction f"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'f')
    assert callable(getattr(object_array, 'f'))

def test_scalar_rep():
    """Test de la fonction scalar_rep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'scalar_rep')
    assert callable(getattr(object_array, 'scalar_rep'))

def test_rep():
    """Test de la fonction rep"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'rep')
    assert callable(getattr(object_array, 'rep'))

def test_g():
    """Test de la fonction g"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'g')
    assert callable(getattr(object_array, 'g'))

def test_g():
    """Test de la fonction g"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(object_array, 'g')
    assert callable(getattr(object_array, 'g'))

class TestObjectStringArrayMixin:
    """Tests pour la classe ObjectStringArrayMixin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(object_array, 'ObjectStringArrayMixin')
        assert isinstance(getattr(object_array, 'ObjectStringArrayMixin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(object_array, 'ObjectStringArrayMixin')
        for method_name in ['__len__', '_str_map', '_str_count', '_str_pad', '_str_contains', '_str_startswith', '_str_endswith', '_str_replace', '_str_repeat', '_str_match', '_str_fullmatch', '_str_encode', '_str_find', '_str_rfind', '_str_find_', '_str_findall', '_str_get', '_str_index', '_str_rindex', '_str_join', '_str_partition', '_str_rpartition', '_str_len', '_str_slice', '_str_slice_replace', '_str_split', '_str_rsplit', '_str_translate', '_str_wrap', '_str_get_dummies', '_str_upper', '_str_isalnum', '_str_isalpha', '_str_isdecimal', '_str_isdigit', '_str_islower', '_str_isnumeric', '_str_isspace', '_str_istitle', '_str_isupper', '_str_capitalize', '_str_casefold', '_str_title', '_str_swapcase', '_str_lower', '_str_normalize', '_str_strip', '_str_lstrip', '_str_rstrip', '_str_removeprefix', '_str_removesuffix', '_str_extract']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
