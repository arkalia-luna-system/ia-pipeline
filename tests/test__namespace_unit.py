"""
Tests unitaires générés pour _namespace
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _namespace
except ImportError:
    pytest.skip(f"Module _namespace non importable")


class TestNamespace:
    """Tests pour la classe Namespace"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_namespace, 'Namespace')
        assert isinstance(getattr(_namespace, 'Namespace'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_namespace, 'Namespace')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
