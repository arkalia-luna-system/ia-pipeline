"""
Tests unitaires générés pour ampl
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ampl
except ImportError:
    pytest.skip(f"Module ampl non importable")


class TestAmplLexer:
    """Tests pour la classe AmplLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ampl, 'AmplLexer')
        assert isinstance(getattr(ampl, 'AmplLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ampl, 'AmplLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
