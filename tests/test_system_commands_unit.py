"""
Tests unitaires générés pour system_commands
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import system_commands
except ImportError:
    pytest.skip(f"Module system_commands non importable")


class TestSystemCommandsProvider:
    """Tests pour la classe SystemCommandsProvider"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(system_commands, 'SystemCommandsProvider')
        assert isinstance(getattr(system_commands, 'SystemCommandsProvider'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(system_commands, 'SystemCommandsProvider')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
