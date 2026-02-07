"""
Tests unitaires générés pour autumn
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import autumn
except ImportError:
    pytest.skip(f"Module autumn non importable")


class TestAutumnStyle:
    """Tests pour la classe AutumnStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(autumn, 'AutumnStyle')
        assert isinstance(getattr(autumn, 'AutumnStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(autumn, 'AutumnStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
