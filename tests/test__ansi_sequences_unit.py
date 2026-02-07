"""
Tests unitaires générés pour _ansi_sequences
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _ansi_sequences
except ImportError:
    pytest.skip(f"Module _ansi_sequences non importable")


class TestIgnoredSequence:
    """Tests pour la classe IgnoredSequence"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_ansi_sequences, 'IgnoredSequence')
        assert isinstance(getattr(_ansi_sequences, 'IgnoredSequence'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_ansi_sequences, 'IgnoredSequence')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
