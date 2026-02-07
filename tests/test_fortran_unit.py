"""
Tests unitaires générés pour fortran
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fortran
except ImportError:
    pytest.skip(f"Module fortran non importable")


def test__lex_fortran():
    """Test de la fonction _lex_fortran"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fortran, '_lex_fortran')
    assert callable(getattr(fortran, '_lex_fortran'))

class TestFortranLexer:
    """Tests pour la classe FortranLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fortran, 'FortranLexer')
        assert isinstance(getattr(fortran, 'FortranLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fortran, 'FortranLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFortranFixedLexer:
    """Tests pour la classe FortranFixedLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fortran, 'FortranFixedLexer')
        assert isinstance(getattr(fortran, 'FortranFixedLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fortran, 'FortranFixedLexer')
        for method_name in ['_lex_fortran']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
