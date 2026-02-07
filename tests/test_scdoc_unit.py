"""
Tests unitaires générés pour scdoc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import scdoc
except ImportError:
    pytest.skip(f"Module scdoc non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(scdoc, 'analyse_text')
    assert callable(getattr(scdoc, 'analyse_text'))

class TestScdocLexer:
    """Tests pour la classe ScdocLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(scdoc, 'ScdocLexer')
        assert isinstance(getattr(scdoc, 'ScdocLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(scdoc, 'ScdocLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
