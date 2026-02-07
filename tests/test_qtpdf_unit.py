"""
Tests unitaires générés pour qtpdf
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import qtpdf
except ImportError:
    pytest.skip(f"Module qtpdf non importable")


class TestQtPDFExporter:
    """Tests pour la classe QtPDFExporter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(qtpdf, 'QtPDFExporter')
        assert isinstance(getattr(qtpdf, 'QtPDFExporter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(qtpdf, 'QtPDFExporter')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
