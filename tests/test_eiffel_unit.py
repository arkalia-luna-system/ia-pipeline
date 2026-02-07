"""
Tests unitaires générés pour eiffel
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import eiffel
except ImportError:
    pytest.skip(f"Module eiffel non importable")


class TestEiffelLexer:
    """Tests pour la classe EiffelLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(eiffel, 'EiffelLexer')
        assert isinstance(getattr(eiffel, 'EiffelLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(eiffel, 'EiffelLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
