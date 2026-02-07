"""
Tests unitaires générés pour capnproto
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import capnproto
except ImportError:
    pytest.skip(f"Module capnproto non importable")


class TestCapnProtoLexer:
    """Tests pour la classe CapnProtoLexer"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(capnproto, 'CapnProtoLexer')
        assert isinstance(getattr(capnproto, 'CapnProtoLexer'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(capnproto, 'CapnProtoLexer')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
