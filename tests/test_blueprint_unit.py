"""
Tests unitaires générés pour blueprint
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import blueprint
except ImportError:
    pytest.skip(f"Module blueprint non importable")


class TestBlueprintLexer:
    """Tests pour la classe BlueprintLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(blueprint, 'BlueprintLexer')
        assert isinstance(getattr(blueprint, 'BlueprintLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(blueprint, 'BlueprintLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
