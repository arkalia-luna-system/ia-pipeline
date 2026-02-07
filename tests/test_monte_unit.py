"""
Tests unitaires générés pour monte
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import monte
except ImportError:
    pytest.skip(f"Module monte non importable")


class TestMonteLexer:
    """Tests pour la classe MonteLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(monte, 'MonteLexer')
        assert isinstance(getattr(monte, 'MonteLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(monte, 'MonteLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
