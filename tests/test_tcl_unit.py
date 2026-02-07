"""
Tests unitaires générés pour tcl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tcl
except ImportError:
    pytest.skip(f"Module tcl non importable")


def test__gen_command_rules():
    """Test de la fonction _gen_command_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcl, '_gen_command_rules')
    assert callable(getattr(tcl, '_gen_command_rules'))

def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tcl, 'analyse_text')
    assert callable(getattr(tcl, 'analyse_text'))

class TestTclLexer:
    """Tests pour la classe TclLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tcl, 'TclLexer')
        assert isinstance(getattr(tcl, 'TclLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tcl, 'TclLexer')
        for method_name in ['_gen_command_rules', 'analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
