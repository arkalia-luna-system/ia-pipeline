"""
Tests unitaires générés pour teraterm
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import teraterm
except ImportError:
    pytest.skip(f"Module teraterm non importable")


def test_analyse_text():
    """Test de la fonction analyse_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(teraterm, 'analyse_text')
    assert callable(getattr(teraterm, 'analyse_text'))

class TestTeraTermLexer:
    """Tests pour la classe TeraTermLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(teraterm, 'TeraTermLexer')
        assert isinstance(getattr(teraterm, 'TeraTermLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(teraterm, 'TeraTermLexer')
        for method_name in ['analyse_text']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
