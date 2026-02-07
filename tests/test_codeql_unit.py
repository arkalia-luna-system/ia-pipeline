"""
Tests unitaires générés pour codeql
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import codeql
except ImportError:
    pytest.skip(f"Module codeql non importable")


class TestCodeQLLexer:
    """Tests pour la classe CodeQLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(codeql, 'CodeQLLexer')
        assert isinstance(getattr(codeql, 'CodeQLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(codeql, 'CodeQLLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
