"""
Tests unitaires générés pour forgetful
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import forgetful
except ImportError:
    pytest.skip(f"Module forgetful non importable")


def test_set_cookie():
    """Test de la fonction set_cookie"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(forgetful, 'set_cookie')
    assert callable(getattr(forgetful, 'set_cookie'))

class TestForgetfulCookieJar:
    """Tests pour la classe ForgetfulCookieJar"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(forgetful, 'ForgetfulCookieJar')
        assert isinstance(getattr(forgetful, 'ForgetfulCookieJar'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(forgetful, 'ForgetfulCookieJar')
        for method_name in ['set_cookie']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
