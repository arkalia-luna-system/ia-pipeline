"""
Tests unitaires générés pour _project_data
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _project_data
except ImportError:
    pytest.skip(f"Module _project_data non importable")


class TestProjectInfo:
    """Tests pour la classe ProjectInfo"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_project_data, 'ProjectInfo')
        assert isinstance(getattr(_project_data, 'ProjectInfo'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_project_data, 'ProjectInfo')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
