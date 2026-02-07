"""
Tests unitaires générés pour direct_url
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import direct_url
except ImportError:
    pytest.skip(f"Module direct_url non importable")


def test__get():
    """Test de la fonction _get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_get')
    assert callable(getattr(direct_url, '_get'))

def test__get_required():
    """Test de la fonction _get_required"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_get_required')
    assert callable(getattr(direct_url, '_get_required'))

def test__exactly_one_of():
    """Test de la fonction _exactly_one_of"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_exactly_one_of')
    assert callable(getattr(direct_url, '_exactly_one_of'))

def test__filter_none():
    """Test de la fonction _filter_none"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_filter_none')
    assert callable(getattr(direct_url, '_filter_none'))

def test__from_dict():
    """Test de la fonction _from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_from_dict')
    assert callable(getattr(direct_url, '_from_dict'))

def test__to_dict():
    """Test de la fonction _to_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_to_dict')
    assert callable(getattr(direct_url, '_to_dict'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '__init__')
    assert callable(getattr(direct_url, '__init__'))

def test_hash():
    """Test de la fonction hash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'hash')
    assert callable(getattr(direct_url, 'hash'))

def test_hash():
    """Test de la fonction hash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'hash')
    assert callable(getattr(direct_url, 'hash'))

def test__from_dict():
    """Test de la fonction _from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_from_dict')
    assert callable(getattr(direct_url, '_from_dict'))

def test__to_dict():
    """Test de la fonction _to_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_to_dict')
    assert callable(getattr(direct_url, '_to_dict'))

def test__from_dict():
    """Test de la fonction _from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_from_dict')
    assert callable(getattr(direct_url, '_from_dict'))

def test__to_dict():
    """Test de la fonction _to_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_to_dict')
    assert callable(getattr(direct_url, '_to_dict'))

def test__remove_auth_from_netloc():
    """Test de la fonction _remove_auth_from_netloc"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, '_remove_auth_from_netloc')
    assert callable(getattr(direct_url, '_remove_auth_from_netloc'))

def test_redacted_url():
    """Test de la fonction redacted_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'redacted_url')
    assert callable(getattr(direct_url, 'redacted_url'))

def test_validate():
    """Test de la fonction validate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'validate')
    assert callable(getattr(direct_url, 'validate'))

def test_from_dict():
    """Test de la fonction from_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'from_dict')
    assert callable(getattr(direct_url, 'from_dict'))

def test_to_dict():
    """Test de la fonction to_dict"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'to_dict')
    assert callable(getattr(direct_url, 'to_dict'))

def test_from_json():
    """Test de la fonction from_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'from_json')
    assert callable(getattr(direct_url, 'from_json'))

def test_to_json():
    """Test de la fonction to_json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'to_json')
    assert callable(getattr(direct_url, 'to_json'))

def test_is_local_editable():
    """Test de la fonction is_local_editable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(direct_url, 'is_local_editable')
    assert callable(getattr(direct_url, 'is_local_editable'))

class TestDirectUrlValidationError:
    """Tests pour la classe DirectUrlValidationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(direct_url, 'DirectUrlValidationError')
        assert isinstance(getattr(direct_url, 'DirectUrlValidationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(direct_url, 'DirectUrlValidationError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestVcsInfo:
    """Tests pour la classe VcsInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(direct_url, 'VcsInfo')
        assert isinstance(getattr(direct_url, 'VcsInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(direct_url, 'VcsInfo')
        for method_name in ['_from_dict', '_to_dict']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestArchiveInfo:
    """Tests pour la classe ArchiveInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(direct_url, 'ArchiveInfo')
        assert isinstance(getattr(direct_url, 'ArchiveInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(direct_url, 'ArchiveInfo')
        for method_name in ['__init__', 'hash', 'hash', '_from_dict', '_to_dict']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDirInfo:
    """Tests pour la classe DirInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(direct_url, 'DirInfo')
        assert isinstance(getattr(direct_url, 'DirInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(direct_url, 'DirInfo')
        for method_name in ['_from_dict', '_to_dict']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDirectUrl:
    """Tests pour la classe DirectUrl"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(direct_url, 'DirectUrl')
        assert isinstance(getattr(direct_url, 'DirectUrl'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(direct_url, 'DirectUrl')
        for method_name in ['_remove_auth_from_netloc', 'redacted_url', 'validate', 'from_dict', 'to_dict', 'from_json', 'to_json', 'is_local_editable']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
