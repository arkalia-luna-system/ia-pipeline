"""
Tests unitaires générés pour tal
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tal
except ImportError:
    pytest.skip(f"Module tal non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(tal, 'analyse_text')
    assert callable(getattr(tal, 'analyse_text'))

class TestTalLexer:
    """Tests pour la classe TalLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tal, 'TalLexer')
        assert isinstance(getattr(tal, 'TalLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tal, 'TalLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
