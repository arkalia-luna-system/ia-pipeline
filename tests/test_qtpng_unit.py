"""
Tests unitaires générés pour qtpng
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import qtpng
except ImportError:
    pytest.skip(f"Module qtpng non importable")


class TestQtPNGExporter:
    """Tests pour la classe QtPNGExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(qtpng, 'QtPNGExporter')
        assert isinstance(getattr(qtpng, 'QtPNGExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(qtpng, 'QtPNGExporter')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
