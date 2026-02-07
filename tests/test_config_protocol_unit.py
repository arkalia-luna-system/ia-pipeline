"""
Tests unitaires générés pour config_protocol
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import config_protocol
except ImportError:
    pytest.skip(f"Module config_protocol non importable")


def test_as_v30():
    """Test de la fonction as_v30"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_protocol, 'as_v30')
    assert callable(getattr(config_protocol, 'as_v30'))

def test_from_v30():
    """Test de la fonction from_v30"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(config_protocol, 'from_v30')
    assert callable(getattr(config_protocol, 'from_v30'))

class TestConfigConvertible:
    """Tests pour la classe ConfigConvertible"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(config_protocol, 'ConfigConvertible')
        assert isinstance(getattr(config_protocol, 'ConfigConvertible'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(config_protocol, 'ConfigConvertible')
        for method_name in ['as_v30', 'from_v30']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
