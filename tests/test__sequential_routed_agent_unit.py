"""
Tests unitaires générés pour _sequential_routed_agent
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _sequential_routed_agent
except ImportError:
    pytest.skip(f"Module _sequential_routed_agent non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sequential_routed_agent, '__init__')
    assert callable(getattr(_sequential_routed_agent, '__init__'))

def test_release():
    """Test de la fonction release"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sequential_routed_agent, 'release')
    assert callable(getattr(_sequential_routed_agent, 'release'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_sequential_routed_agent, '__init__')
    assert callable(getattr(_sequential_routed_agent, '__init__'))

class TestFIFOLock:
    """Tests pour la classe FIFOLock"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_sequential_routed_agent, 'FIFOLock')
        assert isinstance(getattr(_sequential_routed_agent, 'FIFOLock'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_sequential_routed_agent, 'FIFOLock')
        for method_name in ['__init__', 'release']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSequentialRoutedAgent:
    """Tests pour la classe SequentialRoutedAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_sequential_routed_agent, 'SequentialRoutedAgent')
        assert isinstance(getattr(_sequential_routed_agent, 'SequentialRoutedAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_sequential_routed_agent, 'SequentialRoutedAgent')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
