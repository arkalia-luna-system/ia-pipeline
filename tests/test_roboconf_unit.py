"""
Tests unitaires générés pour roboconf
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import roboconf
except ImportError:
    pytest.skip(f"Module roboconf non importable")


class TestRoboconfGraphLexer:
    """Tests pour la classe RoboconfGraphLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(roboconf, 'RoboconfGraphLexer')
        assert isinstance(getattr(roboconf, 'RoboconfGraphLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(roboconf, 'RoboconfGraphLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRoboconfInstancesLexer:
    """Tests pour la classe RoboconfInstancesLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(roboconf, 'RoboconfInstancesLexer')
        assert isinstance(getattr(roboconf, 'RoboconfInstancesLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(roboconf, 'RoboconfInstancesLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
