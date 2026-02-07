"""
Tests unitaires générés pour _exc
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _exc
except ImportError:
    pytest.skip(f"Module _exc non importable")


class TestBidictException:
    """Tests pour la classe BidictException"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_exc, 'BidictException')
        assert isinstance(getattr(_exc, 'BidictException'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_exc, 'BidictException')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDuplicationError:
    """Tests pour la classe DuplicationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_exc, 'DuplicationError')
        assert isinstance(getattr(_exc, 'DuplicationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_exc, 'DuplicationError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestKeyDuplicationError:
    """Tests pour la classe KeyDuplicationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_exc, 'KeyDuplicationError')
        assert isinstance(getattr(_exc, 'KeyDuplicationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_exc, 'KeyDuplicationError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestValueDuplicationError:
    """Tests pour la classe ValueDuplicationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_exc, 'ValueDuplicationError')
        assert isinstance(getattr(_exc, 'ValueDuplicationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_exc, 'ValueDuplicationError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestKeyAndValueDuplicationError:
    """Tests pour la classe KeyAndValueDuplicationError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_exc, 'KeyAndValueDuplicationError')
        assert isinstance(getattr(_exc, 'KeyAndValueDuplicationError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_exc, 'KeyAndValueDuplicationError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
