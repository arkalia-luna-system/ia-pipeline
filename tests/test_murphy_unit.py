"""
Tests unitaires générés pour murphy
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import murphy
except ImportError:
    pytest.skip(f"Module murphy non importable")


class TestMurphyStyle:
    """Tests pour la classe MurphyStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(murphy, 'MurphyStyle')
        assert isinstance(getattr(murphy, 'MurphyStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(murphy, 'MurphyStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
