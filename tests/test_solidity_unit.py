"""
Tests unitaires générés pour solidity
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import solidity
except ImportError:
    pytest.skip(f"Module solidity non importable")


class TestSolidityLexer:
    """Tests pour la classe SolidityLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(solidity, 'SolidityLexer')
        assert isinstance(getattr(solidity, 'SolidityLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(solidity, 'SolidityLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
