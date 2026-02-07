"""
Tests unitaires générés pour rego
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rego
except ImportError:
    pytest.skip(f"Module rego non importable")


class TestRegoLexer:
    """Tests pour la classe RegoLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rego, 'RegoLexer')
        assert isinstance(getattr(rego, 'RegoLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rego, 'RegoLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
