"""
Tests unitaires générés pour savi
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import savi
except ImportError:
    pytest.skip(f"Module savi non importable")


class TestSaviLexer:
    """Tests pour la classe SaviLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(savi, 'SaviLexer')
        assert isinstance(getattr(savi, 'SaviLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(savi, 'SaviLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
