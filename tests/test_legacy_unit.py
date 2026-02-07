"""
Tests unitaires générés pour legacy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import legacy
except ImportError:
    pytest.skip(f"Module legacy non importable")


def test_get_style_guide():
    """Test de la fonction get_style_guide"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'get_style_guide')
    assert callable(getattr(legacy, 'get_style_guide'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, '__init__')
    assert callable(getattr(legacy, '__init__'))

def test_total_errors():
    """Test de la fonction total_errors"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'total_errors')
    assert callable(getattr(legacy, 'total_errors'))

def test_get_statistics():
    """Test de la fonction get_statistics"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'get_statistics')
    assert callable(getattr(legacy, 'get_statistics'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, '__init__')
    assert callable(getattr(legacy, '__init__'))

def test_options():
    """Test de la fonction options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'options')
    assert callable(getattr(legacy, 'options'))

def test_paths():
    """Test de la fonction paths"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'paths')
    assert callable(getattr(legacy, 'paths'))

def test_check_files():
    """Test de la fonction check_files"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'check_files')
    assert callable(getattr(legacy, 'check_files'))

def test_excluded():
    """Test de la fonction excluded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'excluded')
    assert callable(getattr(legacy, 'excluded'))

def test_init_report():
    """Test de la fonction init_report"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'init_report')
    assert callable(getattr(legacy, 'init_report'))

def test_input_file():
    """Test de la fonction input_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'input_file')
    assert callable(getattr(legacy, 'input_file'))

def test_excluded():
    """Test de la fonction excluded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(legacy, 'excluded')
    assert callable(getattr(legacy, 'excluded'))

class TestReport:
    """Tests pour la classe Report"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(legacy, 'Report')
        assert isinstance(getattr(legacy, 'Report'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(legacy, 'Report')
        for method_name in ['__init__', 'total_errors', 'get_statistics']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestStyleGuide:
    """Tests pour la classe StyleGuide"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(legacy, 'StyleGuide')
        assert isinstance(getattr(legacy, 'StyleGuide'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(legacy, 'StyleGuide')
        for method_name in ['__init__', 'options', 'paths', 'check_files', 'excluded', 'init_report', 'input_file']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
