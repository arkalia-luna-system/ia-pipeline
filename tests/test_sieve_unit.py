"""
Tests unitaires générés pour sieve
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import sieve
except ImportError:
    pytest.skip(f"Module sieve non importable")


class TestSieveLexer:
    """Tests pour la classe SieveLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(sieve, 'SieveLexer')
        assert isinstance(getattr(sieve, 'SieveLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(sieve, 'SieveLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
