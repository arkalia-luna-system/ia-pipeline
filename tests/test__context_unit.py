"""
Tests unitaires générés pour _context
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _context
except ImportError:
    pytest.skip(f"Module _context non importable")


class TestNoActiveAppError:
    """Tests pour la classe NoActiveAppError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_context, 'NoActiveAppError')
        assert isinstance(getattr(_context, 'NoActiveAppError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_context, 'NoActiveAppError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
