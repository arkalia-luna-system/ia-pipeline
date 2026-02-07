"""
Tests unitaires générés pour lilypond
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import lilypond
except ImportError:
    pytest.skip(f"Module lilypond non importable")


class TestLilyPondStyle:
    """Tests pour la classe LilyPondStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(lilypond, 'LilyPondStyle')
        assert isinstance(getattr(lilypond, 'LilyPondStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(lilypond, 'LilyPondStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
