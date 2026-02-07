"""
Tests unitaires générés pour _cli
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _cli
except ImportError:
    pytest.skip(f"Module _cli non importable")


def test__output_io():
    """Test de la fonction _output_io"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '_output_io')
    assert callable(getattr(_cli, '_output_io'))

def test__enum_help():
    """Test de la fonction _enum_help"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '_enum_help')
    assert callable(getattr(_cli, '_enum_help'))

def test__fatal():
    """Test de la fonction _fatal"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '_fatal')
    assert callable(getattr(_cli, '_fatal'))

def test__parser():
    """Test de la fonction _parser"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '_parser')
    assert callable(getattr(_cli, '_parser'))

def test__parse_args():
    """Test de la fonction _parse_args"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '_parse_args')
    assert callable(getattr(_cli, '_parse_args'))

def test__dep_source_from_project_path():
    """Test de la fonction _dep_source_from_project_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '_dep_source_from_project_path')
    assert callable(getattr(_cli, '_dep_source_from_project_path'))

def test_audit():
    """Test de la fonction audit"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, 'audit')
    assert callable(getattr(_cli, 'audit'))

def test_to_format():
    """Test de la fonction to_format"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, 'to_format')
    assert callable(getattr(_cli, 'to_format'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '__str__')
    assert callable(getattr(_cli, '__str__'))

def test_to_service():
    """Test de la fonction to_service"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, 'to_service')
    assert callable(getattr(_cli, 'to_service'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '__str__')
    assert callable(getattr(_cli, '__str__'))

def test_to_bool():
    """Test de la fonction to_bool"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, 'to_bool')
    assert callable(getattr(_cli, 'to_bool'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '__str__')
    assert callable(getattr(_cli, '__str__'))

def test_to_bool():
    """Test de la fonction to_bool"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, 'to_bool')
    assert callable(getattr(_cli, 'to_bool'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '__str__')
    assert callable(getattr(_cli, '__str__'))

def test___bool__():
    """Test de la fonction __bool__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '__bool__')
    assert callable(getattr(_cli, '__bool__'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_cli, '__str__')
    assert callable(getattr(_cli, '__str__'))

class TestOutputFormatChoice:
    """Tests pour la classe OutputFormatChoice"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_cli, 'OutputFormatChoice')
        assert isinstance(getattr(_cli, 'OutputFormatChoice'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_cli, 'OutputFormatChoice')
        for method_name in ['to_format', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVulnerabilityServiceChoice:
    """Tests pour la classe VulnerabilityServiceChoice"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_cli, 'VulnerabilityServiceChoice')
        assert isinstance(getattr(_cli, 'VulnerabilityServiceChoice'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_cli, 'VulnerabilityServiceChoice')
        for method_name in ['to_service', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVulnerabilityDescriptionChoice:
    """Tests pour la classe VulnerabilityDescriptionChoice"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_cli, 'VulnerabilityDescriptionChoice')
        assert isinstance(getattr(_cli, 'VulnerabilityDescriptionChoice'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_cli, 'VulnerabilityDescriptionChoice')
        for method_name in ['to_bool', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVulnerabilityAliasChoice:
    """Tests pour la classe VulnerabilityAliasChoice"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_cli, 'VulnerabilityAliasChoice')
        assert isinstance(getattr(_cli, 'VulnerabilityAliasChoice'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_cli, 'VulnerabilityAliasChoice')
        for method_name in ['to_bool', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestProgressSpinnerChoice:
    """Tests pour la classe ProgressSpinnerChoice"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_cli, 'ProgressSpinnerChoice')
        assert isinstance(getattr(_cli, 'ProgressSpinnerChoice'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_cli, 'ProgressSpinnerChoice')
        for method_name in ['__bool__', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
