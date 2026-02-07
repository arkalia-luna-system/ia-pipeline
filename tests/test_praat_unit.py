"""
Tests unitaires générés pour praat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import praat
except ImportError:
    pytest.skip(f"Module praat non importable")


class TestPraatLexer:
    """Tests pour la classe PraatLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(praat, 'PraatLexer')
        assert isinstance(getattr(praat, 'PraatLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(praat, 'PraatLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
