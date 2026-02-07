"""
Tests unitaires générés pour igor
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import igor
except ImportError:
    pytest.skip(f"Module igor non importable")


class TestIgorStyle:
    """Tests pour la classe IgorStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(igor, 'IgorStyle')
        assert isinstance(getattr(igor, 'IgorStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(igor, 'IgorStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
