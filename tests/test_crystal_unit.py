"""
Tests unitaires générés pour crystal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import crystal
except ImportError:
    pytest.skip(f"Module crystal non importable")


def test_heredoc_callback():
    """Test de la fonction heredoc_callback"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(crystal, 'heredoc_callback')
    assert callable(getattr(crystal, 'heredoc_callback'))

def test_gen_crystalstrings_rules():
    """Test de la fonction gen_crystalstrings_rules"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(crystal, 'gen_crystalstrings_rules')
    assert callable(getattr(crystal, 'gen_crystalstrings_rules'))

class TestCrystalLexer:
    """Tests pour la classe CrystalLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(crystal, 'CrystalLexer')
        assert isinstance(getattr(crystal, 'CrystalLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(crystal, 'CrystalLexer')
        for method_name in ['heredoc_callback', 'gen_crystalstrings_rules']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
