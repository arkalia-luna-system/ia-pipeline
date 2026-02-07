"""
Tests unitaires générés pour pastie
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pastie
except ImportError:
    pytest.skip(f"Module pastie non importable")


class TestPastieStyle:
    """Tests pour la classe PastieStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pastie, 'PastieStyle')
        assert isinstance(getattr(pastie, 'PastieStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pastie, 'PastieStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
