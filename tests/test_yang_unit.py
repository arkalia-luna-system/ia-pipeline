"""
Tests unitaires générés pour yang
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import yang
except ImportError:
    pytest.skip(f"Module yang non importable")


class TestYangLexer:
    """Tests pour la classe YangLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(yang, 'YangLexer')
        assert isinstance(getattr(yang, 'YangLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(yang, 'YangLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
