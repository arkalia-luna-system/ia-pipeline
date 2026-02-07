"""
Tests unitaires générés pour kafka_manager
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import kafka_manager
except ImportError:
    pytest.skip(f"Module kafka_manager non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(kafka_manager, '__init__')
    assert callable(getattr(kafka_manager, '__init__'))

def test__publish():
    """Test de la fonction _publish"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(kafka_manager, '_publish')
    assert callable(getattr(kafka_manager, '_publish'))

def test__kafka_listen():
    """Test de la fonction _kafka_listen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(kafka_manager, '_kafka_listen')
    assert callable(getattr(kafka_manager, '_kafka_listen'))

def test__listen():
    """Test de la fonction _listen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(kafka_manager, '_listen')
    assert callable(getattr(kafka_manager, '_listen'))

class TestKafkaManager:
    """Tests pour la classe KafkaManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(kafka_manager, 'KafkaManager')
        assert isinstance(getattr(kafka_manager, 'KafkaManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(kafka_manager, 'KafkaManager')
        for method_name in ['__init__', '_publish', '_kafka_listen', '_listen']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
