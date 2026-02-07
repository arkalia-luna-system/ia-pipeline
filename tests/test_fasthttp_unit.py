"""
Tests unitaires générés pour fasthttp
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import fasthttp
except ImportError:
    pytest.skip(f"Module fasthttp non importable")


def test__construct_basic_auth_str():
    """Test de la fonction _construct_basic_auth_str"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '_construct_basic_auth_str')
    assert callable(getattr(fasthttp, '_construct_basic_auth_str'))

def test_insecure_ssl_context_factory():
    """Test de la fonction insecure_ssl_context_factory"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'insecure_ssl_context_factory')
    assert callable(getattr(fasthttp, 'insecure_ssl_context_factory'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__init__')
    assert callable(getattr(fasthttp, '__init__'))

def test__build_url():
    """Test de la fonction _build_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '_build_url')
    assert callable(getattr(fasthttp, '_build_url'))

def test__send_request_safe_mode():
    """Test de la fonction _send_request_safe_mode"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '_send_request_safe_mode')
    assert callable(getattr(fasthttp, '_send_request_safe_mode'))

def test_request():
    """Test de la fonction request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'request')
    assert callable(getattr(fasthttp, 'request'))

def test_delete():
    """Test de la fonction delete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'delete')
    assert callable(getattr(fasthttp, 'delete'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'get')
    assert callable(getattr(fasthttp, 'get'))

def test_iter_lines():
    """Test de la fonction iter_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'iter_lines')
    assert callable(getattr(fasthttp, 'iter_lines'))

def test_head():
    """Test de la fonction head"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'head')
    assert callable(getattr(fasthttp, 'head'))

def test_options():
    """Test de la fonction options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'options')
    assert callable(getattr(fasthttp, 'options'))

def test_patch():
    """Test de la fonction patch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'patch')
    assert callable(getattr(fasthttp, 'patch'))

def test_post():
    """Test de la fonction post"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'post')
    assert callable(getattr(fasthttp, 'post'))

def test_put():
    """Test de la fonction put"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'put')
    assert callable(getattr(fasthttp, 'put'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__init__')
    assert callable(getattr(fasthttp, '__init__'))

def test_rest():
    """Test de la fonction rest"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'rest')
    assert callable(getattr(fasthttp, 'rest'))

def test_rest_():
    """Test de la fonction rest_"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'rest_')
    assert callable(getattr(fasthttp, 'rest_'))

def test_body():
    """Test de la fonction body"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'body')
    assert callable(getattr(fasthttp, 'body'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__init__')
    assert callable(getattr(fasthttp, '__init__'))

def test_text():
    """Test de la fonction text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'text')
    assert callable(getattr(fasthttp, 'text'))

def test_url():
    """Test de la fonction url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'url')
    assert callable(getattr(fasthttp, 'url'))

def test_json():
    """Test de la fonction json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'json')
    assert callable(getattr(fasthttp, 'json'))

def test_raise_for_status():
    """Test de la fonction raise_for_status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'raise_for_status')
    assert callable(getattr(fasthttp, 'raise_for_status'))

def test_status_code():
    """Test de la fonction status_code"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'status_code')
    assert callable(getattr(fasthttp, 'status_code'))

def test_ok():
    """Test de la fonction ok"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'ok')
    assert callable(getattr(fasthttp, 'ok'))

def test__content():
    """Test de la fonction _content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '_content')
    assert callable(getattr(fasthttp, '_content'))

def test_success():
    """Test de la fonction success"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'success')
    assert callable(getattr(fasthttp, 'success'))

def test_failure():
    """Test de la fonction failure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'failure')
    assert callable(getattr(fasthttp, 'failure'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__init__')
    assert callable(getattr(fasthttp, '__init__'))

def test_raise_for_status():
    """Test de la fonction raise_for_status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'raise_for_status')
    assert callable(getattr(fasthttp, 'raise_for_status'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__repr__')
    assert callable(getattr(fasthttp, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__init__')
    assert callable(getattr(fasthttp, '__init__'))

def test__urlopen():
    """Test de la fonction _urlopen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '_urlopen')
    assert callable(getattr(fasthttp, '_urlopen'))

def test__verify_status():
    """Test de la fonction _verify_status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '_verify_status')
    assert callable(getattr(fasthttp, '_verify_status'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__init__')
    assert callable(getattr(fasthttp, '__init__'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__enter__')
    assert callable(getattr(fasthttp, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '__exit__')
    assert callable(getattr(fasthttp, '__exit__'))

def test__report_request():
    """Test de la fonction _report_request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, '_report_request')
    assert callable(getattr(fasthttp, '_report_request'))

def test_success():
    """Test de la fonction success"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'success')
    assert callable(getattr(fasthttp, 'success'))

def test_failure():
    """Test de la fonction failure"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'failure')
    assert callable(getattr(fasthttp, 'failure'))

def test_raise_for_status():
    """Test de la fonction raise_for_status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(fasthttp, 'raise_for_status')
    assert callable(getattr(fasthttp, 'raise_for_status'))

class TestFastHttpSession:
    """Tests pour la classe FastHttpSession"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'FastHttpSession')
        assert isinstance(getattr(fasthttp, 'FastHttpSession'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'FastHttpSession')
        for method_name in ['__init__', '_build_url', '_send_request_safe_mode', 'request', 'delete', 'get', 'iter_lines', 'head', 'options', 'patch', 'post', 'put']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFastHttpUser:
    """Tests pour la classe FastHttpUser"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'FastHttpUser')
        assert isinstance(getattr(fasthttp, 'FastHttpUser'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'FastHttpUser')
        for method_name in ['__init__', 'rest', 'rest_']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFastRequest:
    """Tests pour la classe FastRequest"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'FastRequest')
        assert isinstance(getattr(fasthttp, 'FastRequest'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'FastRequest')
        for method_name in ['body']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFastResponse:
    """Tests pour la classe FastResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'FastResponse')
        assert isinstance(getattr(fasthttp, 'FastResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'FastResponse')
        for method_name in ['__init__', 'text', 'url', 'json', 'raise_for_status', 'status_code', 'ok', '_content', 'success', 'failure']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestErrorResponse:
    """Tests pour la classe ErrorResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'ErrorResponse')
        assert isinstance(getattr(fasthttp, 'ErrorResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'ErrorResponse')
        for method_name in ['__init__', 'raise_for_status']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLocustBadStatusCode:
    """Tests pour la classe LocustBadStatusCode"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'LocustBadStatusCode')
        assert isinstance(getattr(fasthttp, 'LocustBadStatusCode'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'LocustBadStatusCode')
        for method_name in ['__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestLocustUserAgent:
    """Tests pour la classe LocustUserAgent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'LocustUserAgent')
        assert isinstance(getattr(fasthttp, 'LocustUserAgent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'LocustUserAgent')
        for method_name in ['__init__', '_urlopen', '_verify_status']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestResponseContextManager:
    """Tests pour la classe ResponseContextManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'ResponseContextManager')
        assert isinstance(getattr(fasthttp, 'ResponseContextManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'ResponseContextManager')
        for method_name in ['__init__', '__enter__', '__exit__', '_report_request', 'success', 'failure', 'raise_for_status']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRestResponseContextManager:
    """Tests pour la classe RestResponseContextManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'RestResponseContextManager')
        assert isinstance(getattr(fasthttp, 'RestResponseContextManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'RestResponseContextManager')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPostKwargs:
    """Tests pour la classe PostKwargs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'PostKwargs')
        assert isinstance(getattr(fasthttp, 'PostKwargs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'PostKwargs')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPutKwargs:
    """Tests pour la classe PutKwargs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'PutKwargs')
        assert isinstance(getattr(fasthttp, 'PutKwargs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'PutKwargs')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestPatchKwargs:
    """Tests pour la classe PatchKwargs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'PatchKwargs')
        assert isinstance(getattr(fasthttp, 'PatchKwargs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'PatchKwargs')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRESTKwargs:
    """Tests pour la classe RESTKwargs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(fasthttp, 'RESTKwargs')
        assert isinstance(getattr(fasthttp, 'RESTKwargs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(fasthttp, 'RESTKwargs')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
