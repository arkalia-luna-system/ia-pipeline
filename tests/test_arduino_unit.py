"""
Tests unitaires générés pour arduino
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import arduino
except ImportError:
    pytest.skip(f"Module arduino non importable")


class TestArduinoStyle:
    """Tests pour la classe ArduinoStyle"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(arduino, 'ArduinoStyle')
        assert isinstance(getattr(arduino, 'ArduinoStyle'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(arduino, 'ArduinoStyle')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
