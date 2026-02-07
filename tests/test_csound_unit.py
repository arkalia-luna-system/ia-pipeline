"""
Tests unitaires générés pour csound
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import csound
except ImportError:
    pytest.skip(f"Module csound non importable")


def test_opcode_name_callback():
    """Test de la fonction opcode_name_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(csound, 'opcode_name_callback')
    assert callable(getattr(csound, 'opcode_name_callback'))

def test_name_callback():
    """Test de la fonction name_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(csound, 'name_callback')
    assert callable(getattr(csound, 'name_callback'))

class TestCsoundLexer:
    """Tests pour la classe CsoundLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(csound, 'CsoundLexer')
        assert isinstance(getattr(csound, 'CsoundLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(csound, 'CsoundLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCsoundScoreLexer:
    """Tests pour la classe CsoundScoreLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(csound, 'CsoundScoreLexer')
        assert isinstance(getattr(csound, 'CsoundScoreLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(csound, 'CsoundScoreLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCsoundOrchestraLexer:
    """Tests pour la classe CsoundOrchestraLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(csound, 'CsoundOrchestraLexer')
        assert isinstance(getattr(csound, 'CsoundOrchestraLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(csound, 'CsoundOrchestraLexer')
        for method_name in ['opcode_name_callback', 'name_callback']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCsoundDocumentLexer:
    """Tests pour la classe CsoundDocumentLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(csound, 'CsoundDocumentLexer')
        assert isinstance(getattr(csound, 'CsoundDocumentLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(csound, 'CsoundDocumentLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
