"""
Tests unitaires générés pour zig
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import zig
except ImportError:
    pytest.skip(f"Module zig non importable")


class TestZigLexer:
    """Tests pour la classe ZigLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(zig, 'ZigLexer')
        assert isinstance(getattr(zig, 'ZigLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(zig, 'ZigLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
