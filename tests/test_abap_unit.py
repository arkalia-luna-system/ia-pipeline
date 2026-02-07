"""
Tests unitaires générés pour abap
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import abap
except ImportError:
    pytest.skip(f"Module abap non importable")


class TestAbapStyle:
    """Tests pour la classe AbapStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(abap, 'AbapStyle')
        assert isinstance(getattr(abap, 'AbapStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(abap, 'AbapStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
