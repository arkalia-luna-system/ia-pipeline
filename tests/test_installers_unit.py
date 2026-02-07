"""
Tests unitaires générés pour installers
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import installers
except ImportError:
    pytest.skip(f"Module installers non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(installers, 'analyse_text')
    assert callable(getattr(installers, 'analyse_text'))

class TestNSISLexer:
    """Tests pour la classe NSISLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(installers, 'NSISLexer')
        assert isinstance(getattr(installers, 'NSISLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(installers, 'NSISLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRPMSpecLexer:
    """Tests pour la classe RPMSpecLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(installers, 'RPMSpecLexer')
        assert isinstance(getattr(installers, 'RPMSpecLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(installers, 'RPMSpecLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDebianSourcesLexer:
    """Tests pour la classe DebianSourcesLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(installers, 'DebianSourcesLexer')
        assert isinstance(getattr(installers, 'DebianSourcesLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(installers, 'DebianSourcesLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSourcesListLexer:
    """Tests pour la classe SourcesListLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(installers, 'SourcesListLexer')
        assert isinstance(getattr(installers, 'SourcesListLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(installers, 'SourcesListLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDebianControlLexer:
    """Tests pour la classe DebianControlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(installers, 'DebianControlLexer')
        assert isinstance(getattr(installers, 'DebianControlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(installers, 'DebianControlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
