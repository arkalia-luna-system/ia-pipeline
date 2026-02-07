"""
Tests unitaires générés pour async_aiopika_manager
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import async_aiopika_manager
except ImportError:
    pytest.skip(f"Module async_aiopika_manager non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(async_aiopika_manager, '__init__')
    assert callable(getattr(async_aiopika_manager, '__init__'))

class TestAsyncAioPikaManager:
    """Tests pour la classe AsyncAioPikaManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(async_aiopika_manager, 'AsyncAioPikaManager')
        assert isinstance(getattr(async_aiopika_manager, 'AsyncAioPikaManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(async_aiopika_manager, 'AsyncAioPikaManager')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
