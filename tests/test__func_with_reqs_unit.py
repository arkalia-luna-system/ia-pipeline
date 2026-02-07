"""
Tests unitaires générés pour _func_with_reqs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _func_with_reqs
except ImportError:
    pytest.skip(f"Module _func_with_reqs non importable")


def test__to_code():
    """Test de la fonction _to_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, '_to_code')
    assert callable(getattr(_func_with_reqs, '_to_code'))

def test__import_to_str():
    """Test de la fonction _import_to_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, '_import_to_str')
    assert callable(getattr(_func_with_reqs, '_import_to_str'))

def test_with_requirements():
    """Test de la fonction with_requirements"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'with_requirements')
    assert callable(getattr(_func_with_reqs, 'with_requirements'))

def test_build_python_functions_file():
    """Test de la fonction build_python_functions_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'build_python_functions_file')
    assert callable(getattr(_func_with_reqs, 'build_python_functions_file'))

def test_to_stub():
    """Test de la fonction to_stub"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'to_stub')
    assert callable(getattr(_func_with_reqs, 'to_stub'))

def test_to_code():
    """Test de la fonction to_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'to_code')
    assert callable(getattr(_func_with_reqs, 'to_code'))

def test_import_to_str():
    """Test de la fonction import_to_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'import_to_str')
    assert callable(getattr(_func_with_reqs, 'import_to_str'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, '__init__')
    assert callable(getattr(_func_with_reqs, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, '__init__')
    assert callable(getattr(_func_with_reqs, '__init__'))

def test_get_source():
    """Test de la fonction get_source"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'get_source')
    assert callable(getattr(_func_with_reqs, 'get_source'))

def test_get_data():
    """Test de la fonction get_data"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'get_data')
    assert callable(getattr(_func_with_reqs, 'get_data'))

def test_get_filename():
    """Test de la fonction get_filename"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'get_filename')
    assert callable(getattr(_func_with_reqs, 'get_filename'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, '__init__')
    assert callable(getattr(_func_with_reqs, '__init__'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, '__call__')
    assert callable(getattr(_func_with_reqs, '__call__'))

def test_from_callable():
    """Test de la fonction from_callable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'from_callable')
    assert callable(getattr(_func_with_reqs, 'from_callable'))

def test_from_str():
    """Test de la fonction from_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'from_str')
    assert callable(getattr(_func_with_reqs, 'from_str'))

def test___call__():
    """Test de la fonction __call__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, '__call__')
    assert callable(getattr(_func_with_reqs, '__call__'))

def test_wrapper():
    """Test de la fonction wrapper"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'wrapper')
    assert callable(getattr(_func_with_reqs, 'wrapper'))

def test_to_str():
    """Test de la fonction to_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_func_with_reqs, 'to_str')
    assert callable(getattr(_func_with_reqs, 'to_str'))

class TestAlias:
    """Tests pour la classe Alias"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_func_with_reqs, 'Alias')
        assert isinstance(getattr(_func_with_reqs, 'Alias'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_func_with_reqs, 'Alias')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestImportFromModule:
    """Tests pour la classe ImportFromModule"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_func_with_reqs, 'ImportFromModule')
        assert isinstance(getattr(_func_with_reqs, 'ImportFromModule'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_func_with_reqs, 'ImportFromModule')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_StringLoader:
    """Tests pour la classe _StringLoader"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_func_with_reqs, '_StringLoader')
        assert isinstance(getattr(_func_with_reqs, '_StringLoader'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_func_with_reqs, '_StringLoader')
        for method_name in ['__init__', 'get_source', 'get_data', 'get_filename']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFunctionWithRequirementsStr:
    """Tests pour la classe FunctionWithRequirementsStr"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_func_with_reqs, 'FunctionWithRequirementsStr')
        assert isinstance(getattr(_func_with_reqs, 'FunctionWithRequirementsStr'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_func_with_reqs, 'FunctionWithRequirementsStr')
        for method_name in ['__init__', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFunctionWithRequirements:
    """Tests pour la classe FunctionWithRequirements"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_func_with_reqs, 'FunctionWithRequirements')
        assert isinstance(getattr(_func_with_reqs, 'FunctionWithRequirements'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_func_with_reqs, 'FunctionWithRequirements')
        for method_name in ['from_callable', 'from_str', '__call__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
