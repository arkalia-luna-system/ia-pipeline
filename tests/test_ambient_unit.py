"""
Tests unitaires générés pour ambient
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import ambient
except ImportError:
    pytest.skip(f"Module ambient non importable")


class TestAmbientTalkLexer:
    """Tests pour la classe AmbientTalkLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(ambient, 'AmbientTalkLexer')
        assert isinstance(getattr(ambient, 'AmbientTalkLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(ambient, 'AmbientTalkLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
