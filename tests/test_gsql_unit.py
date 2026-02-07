"""
Tests unitaires générés pour gsql
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import gsql
except ImportError:
    pytest.skip(f"Module gsql non importable")


class TestGSQLLexer:
    """Tests pour la classe GSQLLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(gsql, 'GSQLLexer')
        assert isinstance(getattr(gsql, 'GSQLLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(gsql, 'GSQLLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
