"""
Tests unitaires générés pour _client
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _client
except ImportError:
    pytest.skip(f"Module _client non importable")


def test__is_https_redirect():
    """Test de la fonction _is_https_redirect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_is_https_redirect')
    assert callable(getattr(_client, '_is_https_redirect'))

def test__port_or_default():
    """Test de la fonction _port_or_default"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_port_or_default')
    assert callable(getattr(_client, '_port_or_default'))

def test__same_origin():
    """Test de la fonction _same_origin"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_same_origin')
    assert callable(getattr(_client, '_same_origin'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__init__')
    assert callable(getattr(_client, '__init__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__iter__')
    assert callable(getattr(_client, '__iter__'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'close')
    assert callable(getattr(_client, 'close'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__init__')
    assert callable(getattr(_client, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__init__')
    assert callable(getattr(_client, '__init__'))

def test_is_closed():
    """Test de la fonction is_closed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'is_closed')
    assert callable(getattr(_client, 'is_closed'))

def test_trust_env():
    """Test de la fonction trust_env"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'trust_env')
    assert callable(getattr(_client, 'trust_env'))

def test__enforce_trailing_slash():
    """Test de la fonction _enforce_trailing_slash"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_enforce_trailing_slash')
    assert callable(getattr(_client, '_enforce_trailing_slash'))

def test__get_proxy_map():
    """Test de la fonction _get_proxy_map"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_get_proxy_map')
    assert callable(getattr(_client, '_get_proxy_map'))

def test_timeout():
    """Test de la fonction timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'timeout')
    assert callable(getattr(_client, 'timeout'))

def test_timeout():
    """Test de la fonction timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'timeout')
    assert callable(getattr(_client, 'timeout'))

def test_event_hooks():
    """Test de la fonction event_hooks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'event_hooks')
    assert callable(getattr(_client, 'event_hooks'))

def test_event_hooks():
    """Test de la fonction event_hooks"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'event_hooks')
    assert callable(getattr(_client, 'event_hooks'))

def test_auth():
    """Test de la fonction auth"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'auth')
    assert callable(getattr(_client, 'auth'))

def test_auth():
    """Test de la fonction auth"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'auth')
    assert callable(getattr(_client, 'auth'))

def test_base_url():
    """Test de la fonction base_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'base_url')
    assert callable(getattr(_client, 'base_url'))

def test_base_url():
    """Test de la fonction base_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'base_url')
    assert callable(getattr(_client, 'base_url'))

def test_headers():
    """Test de la fonction headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'headers')
    assert callable(getattr(_client, 'headers'))

def test_headers():
    """Test de la fonction headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'headers')
    assert callable(getattr(_client, 'headers'))

def test_cookies():
    """Test de la fonction cookies"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'cookies')
    assert callable(getattr(_client, 'cookies'))

def test_cookies():
    """Test de la fonction cookies"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'cookies')
    assert callable(getattr(_client, 'cookies'))

def test_params():
    """Test de la fonction params"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'params')
    assert callable(getattr(_client, 'params'))

def test_params():
    """Test de la fonction params"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'params')
    assert callable(getattr(_client, 'params'))

def test_build_request():
    """Test de la fonction build_request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'build_request')
    assert callable(getattr(_client, 'build_request'))

def test__merge_url():
    """Test de la fonction _merge_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_merge_url')
    assert callable(getattr(_client, '_merge_url'))

def test__merge_cookies():
    """Test de la fonction _merge_cookies"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_merge_cookies')
    assert callable(getattr(_client, '_merge_cookies'))

def test__merge_headers():
    """Test de la fonction _merge_headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_merge_headers')
    assert callable(getattr(_client, '_merge_headers'))

def test__merge_queryparams():
    """Test de la fonction _merge_queryparams"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_merge_queryparams')
    assert callable(getattr(_client, '_merge_queryparams'))

def test__build_auth():
    """Test de la fonction _build_auth"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_build_auth')
    assert callable(getattr(_client, '_build_auth'))

def test__build_request_auth():
    """Test de la fonction _build_request_auth"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_build_request_auth')
    assert callable(getattr(_client, '_build_request_auth'))

def test__build_redirect_request():
    """Test de la fonction _build_redirect_request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_build_redirect_request')
    assert callable(getattr(_client, '_build_redirect_request'))

def test__redirect_method():
    """Test de la fonction _redirect_method"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_redirect_method')
    assert callable(getattr(_client, '_redirect_method'))

def test__redirect_url():
    """Test de la fonction _redirect_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_redirect_url')
    assert callable(getattr(_client, '_redirect_url'))

def test__redirect_headers():
    """Test de la fonction _redirect_headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_redirect_headers')
    assert callable(getattr(_client, '_redirect_headers'))

def test__redirect_stream():
    """Test de la fonction _redirect_stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_redirect_stream')
    assert callable(getattr(_client, '_redirect_stream'))

def test__set_timeout():
    """Test de la fonction _set_timeout"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_set_timeout')
    assert callable(getattr(_client, '_set_timeout'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__init__')
    assert callable(getattr(_client, '__init__'))

def test__init_transport():
    """Test de la fonction _init_transport"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_init_transport')
    assert callable(getattr(_client, '_init_transport'))

def test__init_proxy_transport():
    """Test de la fonction _init_proxy_transport"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_init_proxy_transport')
    assert callable(getattr(_client, '_init_proxy_transport'))

def test__transport_for_url():
    """Test de la fonction _transport_for_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_transport_for_url')
    assert callable(getattr(_client, '_transport_for_url'))

def test_request():
    """Test de la fonction request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'request')
    assert callable(getattr(_client, 'request'))

def test_stream():
    """Test de la fonction stream"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'stream')
    assert callable(getattr(_client, 'stream'))

def test_send():
    """Test de la fonction send"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'send')
    assert callable(getattr(_client, 'send'))

def test__send_handling_auth():
    """Test de la fonction _send_handling_auth"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_send_handling_auth')
    assert callable(getattr(_client, '_send_handling_auth'))

def test__send_handling_redirects():
    """Test de la fonction _send_handling_redirects"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_send_handling_redirects')
    assert callable(getattr(_client, '_send_handling_redirects'))

def test__send_single_request():
    """Test de la fonction _send_single_request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_send_single_request')
    assert callable(getattr(_client, '_send_single_request'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'get')
    assert callable(getattr(_client, 'get'))

def test_options():
    """Test de la fonction options"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'options')
    assert callable(getattr(_client, 'options'))

def test_head():
    """Test de la fonction head"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'head')
    assert callable(getattr(_client, 'head'))

def test_post():
    """Test de la fonction post"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'post')
    assert callable(getattr(_client, 'post'))

def test_put():
    """Test de la fonction put"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'put')
    assert callable(getattr(_client, 'put'))

def test_patch():
    """Test de la fonction patch"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'patch')
    assert callable(getattr(_client, 'patch'))

def test_delete():
    """Test de la fonction delete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'delete')
    assert callable(getattr(_client, 'delete'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, 'close')
    assert callable(getattr(_client, 'close'))

def test___enter__():
    """Test de la fonction __enter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__enter__')
    assert callable(getattr(_client, '__enter__'))

def test___exit__():
    """Test de la fonction __exit__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__exit__')
    assert callable(getattr(_client, '__exit__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '__init__')
    assert callable(getattr(_client, '__init__'))

def test__init_transport():
    """Test de la fonction _init_transport"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_init_transport')
    assert callable(getattr(_client, '_init_transport'))

def test__init_proxy_transport():
    """Test de la fonction _init_proxy_transport"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_init_proxy_transport')
    assert callable(getattr(_client, '_init_proxy_transport'))

def test__transport_for_url():
    """Test de la fonction _transport_for_url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_client, '_transport_for_url')
    assert callable(getattr(_client, '_transport_for_url'))

class TestUseClientDefault:
    """Tests pour la classe UseClientDefault"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_client, 'UseClientDefault')
        assert isinstance(getattr(_client, 'UseClientDefault'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_client, 'UseClientDefault')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestClientState:
    """Tests pour la classe ClientState"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_client, 'ClientState')
        assert isinstance(getattr(_client, 'ClientState'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_client, 'ClientState')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBoundSyncStream:
    """Tests pour la classe BoundSyncStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_client, 'BoundSyncStream')
        assert isinstance(getattr(_client, 'BoundSyncStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_client, 'BoundSyncStream')
        for method_name in ['__init__', '__iter__', 'close']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBoundAsyncStream:
    """Tests pour la classe BoundAsyncStream"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_client, 'BoundAsyncStream')
        assert isinstance(getattr(_client, 'BoundAsyncStream'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_client, 'BoundAsyncStream')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBaseClient:
    """Tests pour la classe BaseClient"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_client, 'BaseClient')
        assert isinstance(getattr(_client, 'BaseClient'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_client, 'BaseClient')
        for method_name in ['__init__', 'is_closed', 'trust_env', '_enforce_trailing_slash', '_get_proxy_map', 'timeout', 'timeout', 'event_hooks', 'event_hooks', 'auth', 'auth', 'base_url', 'base_url', 'headers', 'headers', 'cookies', 'cookies', 'params', 'params', 'build_request', '_merge_url', '_merge_cookies', '_merge_headers', '_merge_queryparams', '_build_auth', '_build_request_auth', '_build_redirect_request', '_redirect_method', '_redirect_url', '_redirect_headers', '_redirect_stream', '_set_timeout']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestClient:
    """Tests pour la classe Client"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_client, 'Client')
        assert isinstance(getattr(_client, 'Client'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_client, 'Client')
        for method_name in ['__init__', '_init_transport', '_init_proxy_transport', '_transport_for_url', 'request', 'stream', 'send', '_send_handling_auth', '_send_handling_redirects', '_send_single_request', 'get', 'options', 'head', 'post', 'put', 'patch', 'delete', 'close', '__enter__', '__exit__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestAsyncClient:
    """Tests pour la classe AsyncClient"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_client, 'AsyncClient')
        assert isinstance(getattr(_client, 'AsyncClient'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_client, 'AsyncClient')
        for method_name in ['__init__', '_init_transport', '_init_proxy_transport', '_transport_for_url']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
