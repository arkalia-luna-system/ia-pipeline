"""
Tests unitaires générés pour ecl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ecl
except ImportError:
    pytest.skip(f"Module ecl non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(ecl, 'analyse_text')
    assert callable(getattr(ecl, 'analyse_text'))

class TestECLLexer:
    """Tests pour la classe ECLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ecl, 'ECLLexer')
        assert isinstance(getattr(ecl, 'ECLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ecl, 'ECLLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
