"""
Tests unitaires générés pour sophia
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sophia
except ImportError:
    pytest.skip(f"Module sophia non importable")


class TestSophiaLexer:
    """Tests pour la classe SophiaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sophia, 'SophiaLexer')
        assert isinstance(getattr(sophia, 'SophiaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sophia, 'SophiaLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
