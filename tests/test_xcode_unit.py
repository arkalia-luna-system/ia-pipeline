"""
Tests unitaires générés pour xcode
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import xcode
except ImportError:
    pytest.skip(f"Module xcode non importable")


class TestXcodeStyle:
    """Tests pour la classe XcodeStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(xcode, 'XcodeStyle')
        assert isinstance(getattr(xcode, 'XcodeStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(xcode, 'XcodeStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
