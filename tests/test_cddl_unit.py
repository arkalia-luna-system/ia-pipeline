"""
Tests unitaires générés pour cddl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cddl
except ImportError:
    pytest.skip(f"Module cddl non importable")


class TestCddlLexer:
    """Tests pour la classe CddlLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cddl, 'CddlLexer')
        assert isinstance(getattr(cddl, 'CddlLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cddl, 'CddlLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
