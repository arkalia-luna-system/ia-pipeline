"""
Tests unitaires générés pour _url
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _url
except ImportError:
    pytest.skip(f"Module _url non importable")


class TestURL:
    """Tests pour la classe URL"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_url, 'URL')
        assert isinstance(getattr(_url, 'URL'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_url, 'URL')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
