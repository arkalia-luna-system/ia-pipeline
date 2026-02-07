"""
Tests unitaires générés pour toml_document
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import toml_document
except ImportError:
    pytest.skip(f"Module toml_document non importable")


class TestTOMLDocument:
    """Tests pour la classe TOMLDocument"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(toml_document, 'TOMLDocument')
        assert isinstance(getattr(toml_document, 'TOMLDocument'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(toml_document, 'TOMLDocument')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
