"""
Tests unitaires générés pour win
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import win
except ImportError:
    pytest.skip(f"Module win non importable")


def test__settzkeyname():
    """Test de la fonction _settzkeyname"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '_settzkeyname')
    assert callable(getattr(win, '_settzkeyname'))

def test_picknthweekday():
    """Test de la fonction picknthweekday"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, 'picknthweekday')
    assert callable(getattr(win, 'picknthweekday'))

def test_valuestodict():
    """Test de la fonction valuestodict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, 'valuestodict')
    assert callable(getattr(win, 'valuestodict'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__init__')
    assert callable(getattr(win, '__init__'))

def test_load_name():
    """Test de la fonction load_name"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, 'load_name')
    assert callable(getattr(win, 'load_name'))

def test_name_from_string():
    """Test de la fonction name_from_string"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, 'name_from_string')
    assert callable(getattr(win, 'name_from_string'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__init__')
    assert callable(getattr(win, '__init__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__eq__')
    assert callable(getattr(win, '__eq__'))

def test_list():
    """Test de la fonction list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, 'list')
    assert callable(getattr(win, 'list'))

def test_display():
    """Test de la fonction display"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, 'display')
    assert callable(getattr(win, 'display'))

def test_transitions():
    """Test de la fonction transitions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, 'transitions')
    assert callable(getattr(win, 'transitions'))

def test__get_hasdst():
    """Test de la fonction _get_hasdst"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '_get_hasdst')
    assert callable(getattr(win, '_get_hasdst'))

def test__dst_base_offset():
    """Test de la fonction _dst_base_offset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '_dst_base_offset')
    assert callable(getattr(win, '_dst_base_offset'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__init__')
    assert callable(getattr(win, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__repr__')
    assert callable(getattr(win, '__repr__'))

def test___reduce__():
    """Test de la fonction __reduce__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__reduce__')
    assert callable(getattr(win, '__reduce__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__init__')
    assert callable(getattr(win, '__init__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__repr__')
    assert callable(getattr(win, '__repr__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__str__')
    assert callable(getattr(win, '__str__'))

def test___reduce__():
    """Test de la fonction __reduce__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win, '__reduce__')
    assert callable(getattr(win, '__reduce__'))

class Testtzres:
    """Tests pour la classe tzres"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(win, 'tzres')
        assert isinstance(getattr(win, 'tzres'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(win, 'tzres')
        for method_name in ['__init__', 'load_name', 'name_from_string']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Testtzwinbase:
    """Tests pour la classe tzwinbase"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(win, 'tzwinbase')
        assert isinstance(getattr(win, 'tzwinbase'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(win, 'tzwinbase')
        for method_name in ['__init__', '__eq__', 'list', 'display', 'transitions', '_get_hasdst', '_dst_base_offset']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Testtzwin:
    """Tests pour la classe tzwin"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(win, 'tzwin')
        assert isinstance(getattr(win, 'tzwin'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(win, 'tzwin')
        for method_name in ['__init__', '__repr__', '__reduce__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Testtzwinlocal:
    """Tests pour la classe tzwinlocal"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(win, 'tzwinlocal')
        assert isinstance(getattr(win, 'tzwinlocal'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(win, 'tzwinlocal')
        for method_name in ['__init__', '__repr__', '__str__', '__reduce__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
