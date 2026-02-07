"""
Tests unitaires générés pour win_interrupt
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import win_interrupt
except ImportError:
    pytest.skip(f"Module win_interrupt non importable")


def test_create_interrupt_event():
    """Test de la fonction create_interrupt_event"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win_interrupt, 'create_interrupt_event')
    assert callable(getattr(win_interrupt, 'create_interrupt_event'))

def test_send_interrupt():
    """Test de la fonction send_interrupt"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(win_interrupt, 'send_interrupt')
    assert callable(getattr(win_interrupt, 'send_interrupt'))

class TestSECURITY_ATTRIBUTES:
    """Tests pour la classe SECURITY_ATTRIBUTES"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(win_interrupt, 'SECURITY_ATTRIBUTES')
        assert isinstance(getattr(win_interrupt, 'SECURITY_ATTRIBUTES'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(win_interrupt, 'SECURITY_ATTRIBUTES')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
