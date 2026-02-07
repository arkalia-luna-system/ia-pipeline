"""
Tests unitaires générés pour check
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import check
except ImportError:
    pytest.skip(f"Module check non importable")


def test__parse_content_type():
    """Test de la fonction _parse_content_type"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(check, '_parse_content_type')
    assert callable(getattr(check, '_parse_content_type'))

def test__check_file():
    """Test de la fonction _check_file"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(check, '_check_file')
    assert callable(getattr(check, '_check_file'))

def test_check():
    """Test de la fonction check"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(check, 'check')
    assert callable(getattr(check, 'check'))

def test_main():
    """Test de la fonction main"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(check, 'main')
    assert callable(getattr(check, 'main'))

def test_write():
    """Test de la fonction write"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(check, 'write')
    assert callable(getattr(check, 'write'))

def test___str__():
    """Test de la fonction __str__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(check, '__str__')
    assert callable(getattr(check, '__str__'))

class Test_WarningStream:
    """Tests pour la classe _WarningStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(check, '_WarningStream')
        assert isinstance(getattr(check, '_WarningStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(check, '_WarningStream')
        for method_name in ['write', '__str__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
