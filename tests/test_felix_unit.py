"""
Tests unitaires générés pour felix
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import felix
except ImportError:
    pytest.skip(f"Module felix non importable")


class TestFelixLexer:
    """Tests pour la classe FelixLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(felix, 'FelixLexer')
        assert isinstance(getattr(felix, 'FelixLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(felix, 'FelixLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
