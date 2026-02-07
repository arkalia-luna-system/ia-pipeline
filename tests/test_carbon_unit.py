"""
Tests unitaires générés pour carbon
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import carbon
except ImportError:
    pytest.skip(f"Module carbon non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(carbon, 'analyse_text')
    assert callable(getattr(carbon, 'analyse_text'))

class TestCarbonLexer:
    """Tests pour la classe CarbonLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(carbon, 'CarbonLexer')
        assert isinstance(getattr(carbon, 'CarbonLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(carbon, 'CarbonLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
