"""
Tests unitaires générés pour glob
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import glob
except ImportError:
    pytest.skip(f"Module glob non importable")


def test_separate():
    """Test de la fonction separate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'separate')
    assert callable(getattr(glob, 'separate'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, '__init__')
    assert callable(getattr(glob, '__init__'))

def test_translate():
    """Test de la fonction translate"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'translate')
    assert callable(getattr(glob, 'translate'))

def test_extend():
    """Test de la fonction extend"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'extend')
    assert callable(getattr(glob, 'extend'))

def test_match_dirs():
    """Test de la fonction match_dirs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'match_dirs')
    assert callable(getattr(glob, 'match_dirs'))

def test_translate_core():
    """Test de la fonction translate_core"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'translate_core')
    assert callable(getattr(glob, 'translate_core'))

def test_replace():
    """Test de la fonction replace"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'replace')
    assert callable(getattr(glob, 'replace'))

def test_restrict_rglob():
    """Test de la fonction restrict_rglob"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'restrict_rglob')
    assert callable(getattr(glob, 'restrict_rglob'))

def test_star_not_empty():
    """Test de la fonction star_not_empty"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'star_not_empty')
    assert callable(getattr(glob, 'star_not_empty'))

def test_handle_segment():
    """Test de la fonction handle_segment"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(glob, 'handle_segment')
    assert callable(getattr(glob, 'handle_segment'))

class TestTranslator:
    """Tests pour la classe Translator"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(glob, 'Translator')
        assert isinstance(getattr(glob, 'Translator'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(glob, 'Translator')
        for method_name in ['__init__', 'translate', 'extend', 'match_dirs', 'translate_core', 'replace', 'restrict_rglob', 'star_not_empty']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
