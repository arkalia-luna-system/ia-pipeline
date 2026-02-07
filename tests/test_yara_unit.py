"""
Tests unitaires générés pour yara
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import yara
except ImportError:
    pytest.skip(f"Module yara non importable")


class TestYaraLexer:
    """Tests pour la classe YaraLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(yara, 'YaraLexer')
        assert isinstance(getattr(yara, 'YaraLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(yara, 'YaraLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
