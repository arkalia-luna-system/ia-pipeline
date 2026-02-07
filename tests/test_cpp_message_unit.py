"""
Tests unitaires générés pour cpp_message
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import cpp_message
except ImportError:
    pytest.skip(f"Module cpp_message non importable")


class TestGeneratedProtocolMessageType:
    """Tests pour la classe GeneratedProtocolMessageType"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(cpp_message, 'GeneratedProtocolMessageType')
        assert isinstance(getattr(cpp_message, 'GeneratedProtocolMessageType'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(cpp_message, 'GeneratedProtocolMessageType')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
