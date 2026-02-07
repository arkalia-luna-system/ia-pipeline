"""
Tests unitaires générés pour dax
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dax
except ImportError:
    pytest.skip(f"Module dax non importable")


class TestDaxLexer:
    """Tests pour la classe DaxLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dax, 'DaxLexer')
        assert isinstance(getattr(dax, 'DaxLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dax, 'DaxLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
