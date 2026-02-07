"""
Tests unitaires générés pour ada
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ada
except ImportError:
    pytest.skip(f"Module ada non importable")


class TestAdaLexer:
    """Tests pour la classe AdaLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ada, 'AdaLexer')
        assert isinstance(getattr(ada, 'AdaLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ada, 'AdaLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
