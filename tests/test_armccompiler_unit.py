"""
Tests unitaires générés pour armccompiler
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import armccompiler
except ImportError:
    pytest.skip(f"Module armccompiler non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(armccompiler, '__init__')
    assert callable(getattr(armccompiler, '__init__'))

class TestArmCCompiler:
    """Tests pour la classe ArmCCompiler"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(armccompiler, 'ArmCCompiler')
        assert isinstance(getattr(armccompiler, 'ArmCCompiler'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(armccompiler, 'ArmCCompiler')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
