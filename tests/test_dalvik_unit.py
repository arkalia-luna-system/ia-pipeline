"""
Tests unitaires générés pour dalvik
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import dalvik
except ImportError:
    pytest.skip(f"Module dalvik non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(dalvik, 'analyse_text')
    assert callable(getattr(dalvik, 'analyse_text'))

class TestSmaliLexer:
    """Tests pour la classe SmaliLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(dalvik, 'SmaliLexer')
        assert isinstance(getattr(dalvik, 'SmaliLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(dalvik, 'SmaliLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
