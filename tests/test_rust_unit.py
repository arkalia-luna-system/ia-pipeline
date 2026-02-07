"""
Tests unitaires générés pour rust
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import rust
except ImportError:
    pytest.skip(f"Module rust non importable")


class TestRustLexer:
    """Tests pour la classe RustLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(rust, 'RustLexer')
        assert isinstance(getattr(rust, 'RustLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(rust, 'RustLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
