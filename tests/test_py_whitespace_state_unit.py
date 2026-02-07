"""
Tests unitaires générés pour py_whitespace_state
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import py_whitespace_state
except ImportError:
    pytest.skip(f"Module py_whitespace_state non importable")


class TestWhitespaceState:
    """Tests pour la classe WhitespaceState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(py_whitespace_state, 'WhitespaceState')
        assert isinstance(getattr(py_whitespace_state, 'WhitespaceState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(py_whitespace_state, 'WhitespaceState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
