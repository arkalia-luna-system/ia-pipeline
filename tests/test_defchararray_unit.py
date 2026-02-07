"""
Tests unitaires générés pour defchararray
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import defchararray
except ImportError:
    pytest.skip(f"Module defchararray non importable")


def test__binary_op_dispatcher():
    """Test de la fonction _binary_op_dispatcher"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '_binary_op_dispatcher')
    assert callable(getattr(defchararray, '_binary_op_dispatcher'))

def test_equal():
    """Test de la fonction equal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'equal')
    assert callable(getattr(defchararray, 'equal'))

def test_not_equal():
    """Test de la fonction not_equal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'not_equal')
    assert callable(getattr(defchararray, 'not_equal'))

def test_greater_equal():
    """Test de la fonction greater_equal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'greater_equal')
    assert callable(getattr(defchararray, 'greater_equal'))

def test_less_equal():
    """Test de la fonction less_equal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'less_equal')
    assert callable(getattr(defchararray, 'less_equal'))

def test_greater():
    """Test de la fonction greater"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'greater')
    assert callable(getattr(defchararray, 'greater'))

def test_less():
    """Test de la fonction less"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'less')
    assert callable(getattr(defchararray, 'less'))

def test_multiply():
    """Test de la fonction multiply"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'multiply')
    assert callable(getattr(defchararray, 'multiply'))

def test_partition():
    """Test de la fonction partition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'partition')
    assert callable(getattr(defchararray, 'partition'))

def test_rpartition():
    """Test de la fonction rpartition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'rpartition')
    assert callable(getattr(defchararray, 'rpartition'))

def test_array():
    """Test de la fonction array"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'array')
    assert callable(getattr(defchararray, 'array'))

def test_asarray():
    """Test de la fonction asarray"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'asarray')
    assert callable(getattr(defchararray, 'asarray'))

def test___new__():
    """Test de la fonction __new__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__new__')
    assert callable(getattr(defchararray, '__new__'))

def test___array_wrap__():
    """Test de la fonction __array_wrap__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__array_wrap__')
    assert callable(getattr(defchararray, '__array_wrap__'))

def test___array_finalize__():
    """Test de la fonction __array_finalize__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__array_finalize__')
    assert callable(getattr(defchararray, '__array_finalize__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__getitem__')
    assert callable(getattr(defchararray, '__getitem__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__eq__')
    assert callable(getattr(defchararray, '__eq__'))

def test___ne__():
    """Test de la fonction __ne__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__ne__')
    assert callable(getattr(defchararray, '__ne__'))

def test___ge__():
    """Test de la fonction __ge__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__ge__')
    assert callable(getattr(defchararray, '__ge__'))

def test___le__():
    """Test de la fonction __le__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__le__')
    assert callable(getattr(defchararray, '__le__'))

def test___gt__():
    """Test de la fonction __gt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__gt__')
    assert callable(getattr(defchararray, '__gt__'))

def test___lt__():
    """Test de la fonction __lt__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__lt__')
    assert callable(getattr(defchararray, '__lt__'))

def test___add__():
    """Test de la fonction __add__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__add__')
    assert callable(getattr(defchararray, '__add__'))

def test___radd__():
    """Test de la fonction __radd__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__radd__')
    assert callable(getattr(defchararray, '__radd__'))

def test___mul__():
    """Test de la fonction __mul__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__mul__')
    assert callable(getattr(defchararray, '__mul__'))

def test___rmul__():
    """Test de la fonction __rmul__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__rmul__')
    assert callable(getattr(defchararray, '__rmul__'))

def test___mod__():
    """Test de la fonction __mod__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__mod__')
    assert callable(getattr(defchararray, '__mod__'))

def test___rmod__():
    """Test de la fonction __rmod__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, '__rmod__')
    assert callable(getattr(defchararray, '__rmod__'))

def test_argsort():
    """Test de la fonction argsort"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'argsort')
    assert callable(getattr(defchararray, 'argsort'))

def test_capitalize():
    """Test de la fonction capitalize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'capitalize')
    assert callable(getattr(defchararray, 'capitalize'))

def test_center():
    """Test de la fonction center"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'center')
    assert callable(getattr(defchararray, 'center'))

def test_count():
    """Test de la fonction count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'count')
    assert callable(getattr(defchararray, 'count'))

def test_decode():
    """Test de la fonction decode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'decode')
    assert callable(getattr(defchararray, 'decode'))

def test_encode():
    """Test de la fonction encode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'encode')
    assert callable(getattr(defchararray, 'encode'))

def test_endswith():
    """Test de la fonction endswith"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'endswith')
    assert callable(getattr(defchararray, 'endswith'))

def test_expandtabs():
    """Test de la fonction expandtabs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'expandtabs')
    assert callable(getattr(defchararray, 'expandtabs'))

def test_find():
    """Test de la fonction find"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'find')
    assert callable(getattr(defchararray, 'find'))

def test_index():
    """Test de la fonction index"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'index')
    assert callable(getattr(defchararray, 'index'))

def test_isalnum():
    """Test de la fonction isalnum"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'isalnum')
    assert callable(getattr(defchararray, 'isalnum'))

def test_isalpha():
    """Test de la fonction isalpha"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'isalpha')
    assert callable(getattr(defchararray, 'isalpha'))

def test_isdigit():
    """Test de la fonction isdigit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'isdigit')
    assert callable(getattr(defchararray, 'isdigit'))

def test_islower():
    """Test de la fonction islower"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'islower')
    assert callable(getattr(defchararray, 'islower'))

def test_isspace():
    """Test de la fonction isspace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'isspace')
    assert callable(getattr(defchararray, 'isspace'))

def test_istitle():
    """Test de la fonction istitle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'istitle')
    assert callable(getattr(defchararray, 'istitle'))

def test_isupper():
    """Test de la fonction isupper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'isupper')
    assert callable(getattr(defchararray, 'isupper'))

def test_join():
    """Test de la fonction join"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'join')
    assert callable(getattr(defchararray, 'join'))

def test_ljust():
    """Test de la fonction ljust"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'ljust')
    assert callable(getattr(defchararray, 'ljust'))

def test_lower():
    """Test de la fonction lower"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'lower')
    assert callable(getattr(defchararray, 'lower'))

def test_lstrip():
    """Test de la fonction lstrip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'lstrip')
    assert callable(getattr(defchararray, 'lstrip'))

def test_partition():
    """Test de la fonction partition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'partition')
    assert callable(getattr(defchararray, 'partition'))

def test_replace():
    """Test de la fonction replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'replace')
    assert callable(getattr(defchararray, 'replace'))

def test_rfind():
    """Test de la fonction rfind"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'rfind')
    assert callable(getattr(defchararray, 'rfind'))

def test_rindex():
    """Test de la fonction rindex"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'rindex')
    assert callable(getattr(defchararray, 'rindex'))

def test_rjust():
    """Test de la fonction rjust"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'rjust')
    assert callable(getattr(defchararray, 'rjust'))

def test_rpartition():
    """Test de la fonction rpartition"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'rpartition')
    assert callable(getattr(defchararray, 'rpartition'))

def test_rsplit():
    """Test de la fonction rsplit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'rsplit')
    assert callable(getattr(defchararray, 'rsplit'))

def test_rstrip():
    """Test de la fonction rstrip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'rstrip')
    assert callable(getattr(defchararray, 'rstrip'))

def test_split():
    """Test de la fonction split"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'split')
    assert callable(getattr(defchararray, 'split'))

def test_splitlines():
    """Test de la fonction splitlines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'splitlines')
    assert callable(getattr(defchararray, 'splitlines'))

def test_startswith():
    """Test de la fonction startswith"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'startswith')
    assert callable(getattr(defchararray, 'startswith'))

def test_strip():
    """Test de la fonction strip"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'strip')
    assert callable(getattr(defchararray, 'strip'))

def test_swapcase():
    """Test de la fonction swapcase"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'swapcase')
    assert callable(getattr(defchararray, 'swapcase'))

def test_title():
    """Test de la fonction title"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'title')
    assert callable(getattr(defchararray, 'title'))

def test_translate():
    """Test de la fonction translate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'translate')
    assert callable(getattr(defchararray, 'translate'))

def test_upper():
    """Test de la fonction upper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'upper')
    assert callable(getattr(defchararray, 'upper'))

def test_zfill():
    """Test de la fonction zfill"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'zfill')
    assert callable(getattr(defchararray, 'zfill'))

def test_isnumeric():
    """Test de la fonction isnumeric"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'isnumeric')
    assert callable(getattr(defchararray, 'isnumeric'))

def test_isdecimal():
    """Test de la fonction isdecimal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(defchararray, 'isdecimal')
    assert callable(getattr(defchararray, 'isdecimal'))

class Testchararray:
    """Tests pour la classe chararray"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(defchararray, 'chararray')
        assert isinstance(getattr(defchararray, 'chararray'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(defchararray, 'chararray')
        for method_name in ['__new__', '__array_wrap__', '__array_finalize__', '__getitem__', '__eq__', '__ne__', '__ge__', '__le__', '__gt__', '__lt__', '__add__', '__radd__', '__mul__', '__rmul__', '__mod__', '__rmod__', 'argsort', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill', 'isnumeric', 'isdecimal']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
