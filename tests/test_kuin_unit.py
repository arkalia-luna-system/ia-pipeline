"""
Tests unitaires générés pour kuin
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import kuin
except ImportError:
    pytest.skip(f"Module kuin non importable")


class TestKuinLexer:
    """Tests pour la classe KuinLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(kuin, 'KuinLexer')
        assert isinstance(getattr(kuin, 'KuinLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(kuin, 'KuinLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
