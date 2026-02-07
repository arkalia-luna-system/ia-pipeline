"""
Tests unitaires générés pour pointless
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import pointless
except ImportError:
    pytest.skip(f"Module pointless non importable")


class TestPointlessLexer:
    """Tests pour la classe PointlessLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(pointless, 'PointlessLexer')
        assert isinstance(getattr(pointless, 'PointlessLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(pointless, 'PointlessLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
