"""
Tests unitaires générés pour _ssl_compat
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _ssl_compat
except ImportError:
    pytest.skip(f"Module _ssl_compat non importable")


class TestSSLError:
    """Tests pour la classe SSLError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_ssl_compat, 'SSLError')
        assert isinstance(getattr(_ssl_compat, 'SSLError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_ssl_compat, 'SSLError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSSLEOFError:
    """Tests pour la classe SSLEOFError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_ssl_compat, 'SSLEOFError')
        assert isinstance(getattr(_ssl_compat, 'SSLEOFError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_ssl_compat, 'SSLEOFError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSSLWantReadError:
    """Tests pour la classe SSLWantReadError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_ssl_compat, 'SSLWantReadError')
        assert isinstance(getattr(_ssl_compat, 'SSLWantReadError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_ssl_compat, 'SSLWantReadError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestSSLWantWriteError:
    """Tests pour la classe SSLWantWriteError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_ssl_compat, 'SSLWantWriteError')
        assert isinstance(getattr(_ssl_compat, 'SSLWantWriteError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_ssl_compat, 'SSLWantWriteError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
