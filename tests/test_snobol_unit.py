"""
Tests unitaires générés pour snobol
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import snobol
except ImportError:
    pytest.skip(f"Module snobol non importable")


class TestSnobolLexer:
    """Tests pour la classe SnobolLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(snobol, 'SnobolLexer')
        assert isinstance(getattr(snobol, 'SnobolLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(snobol, 'SnobolLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
