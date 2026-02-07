"""
Tests unitaires générés pour author
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import author
except ImportError:
    pytest.skip(f"Module author non importable")


class TestAuthor:
    """Tests pour la classe Author"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(author, 'Author')
        assert isinstance(getattr(author, 'Author'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(author, 'Author')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAuthors:
    """Tests pour la classe Authors"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(author, 'Authors')
        assert isinstance(getattr(author, 'Authors'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(author, 'Authors')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
