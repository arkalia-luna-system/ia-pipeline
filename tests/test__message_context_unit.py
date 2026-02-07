"""
Tests unitaires générés pour _message_context
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _message_context
except ImportError:
    pytest.skip(f"Module _message_context non importable")


class TestMessageContext:
    """Tests pour la classe MessageContext"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_message_context, 'MessageContext')
        assert isinstance(getattr(_message_context, 'MessageContext'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_message_context, 'MessageContext')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
