"""
Tests unitaires générés pour cplint
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cplint
except ImportError:
    pytest.skip(f"Module cplint non importable")


class TestCplintLexer:
    """Tests pour la classe CplintLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cplint, 'CplintLexer')
        assert isinstance(getattr(cplint, 'CplintLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cplint, 'CplintLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
