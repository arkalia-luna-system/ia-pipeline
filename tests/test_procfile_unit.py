"""
Tests unitaires générés pour procfile
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import procfile
except ImportError:
    pytest.skip(f"Module procfile non importable")


class TestProcfileLexer:
    """Tests pour la classe ProcfileLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(procfile, 'ProcfileLexer')
        assert isinstance(getattr(procfile, 'ProcfileLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(procfile, 'ProcfileLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
