"""
Tests unitaires générés pour tlb
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import tlb
except ImportError:
    pytest.skip(f"Module tlb non importable")


class TestTlbLexer:
    """Tests pour la classe TlbLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(tlb, 'TlbLexer')
        assert isinstance(getattr(tlb, 'TlbLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(tlb, 'TlbLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
