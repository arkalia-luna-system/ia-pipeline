"""
Tests unitaires générés pour _models
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _models
except ImportError:
    pytest.skip(f"Module _models non importable")


def test__is_known_encoding():
    """Test de la fonction _is_known_encoding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_is_known_encoding')
    assert callable(getattr(_models, '_is_known_encoding'))

def test__normalize_header_key():
    """Test de la fonction _normalize_header_key"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_normalize_header_key')
    assert callable(getattr(_models, '_normalize_header_key'))

def test__normalize_header_value():
    """Test de la fonction _normalize_header_value"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_normalize_header_value')
    assert callable(getattr(_models, '_normalize_header_value'))

def test__parse_content_type_charset():
    """Test de la fonction _parse_content_type_charset"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_parse_content_type_charset')
    assert callable(getattr(_models, '_parse_content_type_charset'))

def test__parse_header_links():
    """Test de la fonction _parse_header_links"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_parse_header_links')
    assert callable(getattr(_models, '_parse_header_links'))

def test__obfuscate_sensitive_headers():
    """Test de la fonction _obfuscate_sensitive_headers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_obfuscate_sensitive_headers')
    assert callable(getattr(_models, '_obfuscate_sensitive_headers'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__init__')
    assert callable(getattr(_models, '__init__'))

def test_encoding():
    """Test de la fonction encoding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'encoding')
    assert callable(getattr(_models, 'encoding'))

def test_encoding():
    """Test de la fonction encoding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'encoding')
    assert callable(getattr(_models, 'encoding'))

def test_raw():
    """Test de la fonction raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'raw')
    assert callable(getattr(_models, 'raw'))

def test_keys():
    """Test de la fonction keys"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'keys')
    assert callable(getattr(_models, 'keys'))

def test_values():
    """Test de la fonction values"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'values')
    assert callable(getattr(_models, 'values'))

def test_items():
    """Test de la fonction items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'items')
    assert callable(getattr(_models, 'items'))

def test_multi_items():
    """Test de la fonction multi_items"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'multi_items')
    assert callable(getattr(_models, 'multi_items'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'get')
    assert callable(getattr(_models, 'get'))

def test_get_list():
    """Test de la fonction get_list"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'get_list')
    assert callable(getattr(_models, 'get_list'))

def test_update():
    """Test de la fonction update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'update')
    assert callable(getattr(_models, 'update'))

def test_copy():
    """Test de la fonction copy"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'copy')
    assert callable(getattr(_models, 'copy'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__getitem__')
    assert callable(getattr(_models, '__getitem__'))

def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__setitem__')
    assert callable(getattr(_models, '__setitem__'))

def test___delitem__():
    """Test de la fonction __delitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__delitem__')
    assert callable(getattr(_models, '__delitem__'))

def test___contains__():
    """Test de la fonction __contains__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__contains__')
    assert callable(getattr(_models, '__contains__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__iter__')
    assert callable(getattr(_models, '__iter__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__len__')
    assert callable(getattr(_models, '__len__'))

def test___eq__():
    """Test de la fonction __eq__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__eq__')
    assert callable(getattr(_models, '__eq__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__repr__')
    assert callable(getattr(_models, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__init__')
    assert callable(getattr(_models, '__init__'))

def test__prepare():
    """Test de la fonction _prepare"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_prepare')
    assert callable(getattr(_models, '_prepare'))

def test_content():
    """Test de la fonction content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'content')
    assert callable(getattr(_models, 'content'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'read')
    assert callable(getattr(_models, 'read'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__repr__')
    assert callable(getattr(_models, '__repr__'))

def test___getstate__():
    """Test de la fonction __getstate__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__getstate__')
    assert callable(getattr(_models, '__getstate__'))

def test___setstate__():
    """Test de la fonction __setstate__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__setstate__')
    assert callable(getattr(_models, '__setstate__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__init__')
    assert callable(getattr(_models, '__init__'))

def test__prepare():
    """Test de la fonction _prepare"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_prepare')
    assert callable(getattr(_models, '_prepare'))

def test_elapsed():
    """Test de la fonction elapsed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'elapsed')
    assert callable(getattr(_models, 'elapsed'))

def test_elapsed():
    """Test de la fonction elapsed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'elapsed')
    assert callable(getattr(_models, 'elapsed'))

def test_request():
    """Test de la fonction request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'request')
    assert callable(getattr(_models, 'request'))

def test_request():
    """Test de la fonction request"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'request')
    assert callable(getattr(_models, 'request'))

def test_http_version():
    """Test de la fonction http_version"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'http_version')
    assert callable(getattr(_models, 'http_version'))

def test_reason_phrase():
    """Test de la fonction reason_phrase"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'reason_phrase')
    assert callable(getattr(_models, 'reason_phrase'))

def test_url():
    """Test de la fonction url"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'url')
    assert callable(getattr(_models, 'url'))

def test_content():
    """Test de la fonction content"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'content')
    assert callable(getattr(_models, 'content'))

def test_text():
    """Test de la fonction text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'text')
    assert callable(getattr(_models, 'text'))

def test_encoding():
    """Test de la fonction encoding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'encoding')
    assert callable(getattr(_models, 'encoding'))

def test_encoding():
    """Test de la fonction encoding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'encoding')
    assert callable(getattr(_models, 'encoding'))

def test_charset_encoding():
    """Test de la fonction charset_encoding"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'charset_encoding')
    assert callable(getattr(_models, 'charset_encoding'))

def test__get_content_decoder():
    """Test de la fonction _get_content_decoder"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '_get_content_decoder')
    assert callable(getattr(_models, '_get_content_decoder'))

def test_is_informational():
    """Test de la fonction is_informational"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'is_informational')
    assert callable(getattr(_models, 'is_informational'))

def test_is_success():
    """Test de la fonction is_success"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'is_success')
    assert callable(getattr(_models, 'is_success'))

def test_is_redirect():
    """Test de la fonction is_redirect"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'is_redirect')
    assert callable(getattr(_models, 'is_redirect'))

def test_is_client_error():
    """Test de la fonction is_client_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'is_client_error')
    assert callable(getattr(_models, 'is_client_error'))

def test_is_server_error():
    """Test de la fonction is_server_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'is_server_error')
    assert callable(getattr(_models, 'is_server_error'))

def test_is_error():
    """Test de la fonction is_error"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'is_error')
    assert callable(getattr(_models, 'is_error'))

def test_has_redirect_location():
    """Test de la fonction has_redirect_location"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'has_redirect_location')
    assert callable(getattr(_models, 'has_redirect_location'))

def test_raise_for_status():
    """Test de la fonction raise_for_status"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'raise_for_status')
    assert callable(getattr(_models, 'raise_for_status'))

def test_json():
    """Test de la fonction json"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'json')
    assert callable(getattr(_models, 'json'))

def test_cookies():
    """Test de la fonction cookies"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'cookies')
    assert callable(getattr(_models, 'cookies'))

def test_links():
    """Test de la fonction links"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'links')
    assert callable(getattr(_models, 'links'))

def test_num_bytes_downloaded():
    """Test de la fonction num_bytes_downloaded"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'num_bytes_downloaded')
    assert callable(getattr(_models, 'num_bytes_downloaded'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__repr__')
    assert callable(getattr(_models, '__repr__'))

def test___getstate__():
    """Test de la fonction __getstate__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__getstate__')
    assert callable(getattr(_models, '__getstate__'))

def test___setstate__():
    """Test de la fonction __setstate__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__setstate__')
    assert callable(getattr(_models, '__setstate__'))

def test_read():
    """Test de la fonction read"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'read')
    assert callable(getattr(_models, 'read'))

def test_iter_bytes():
    """Test de la fonction iter_bytes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'iter_bytes')
    assert callable(getattr(_models, 'iter_bytes'))

def test_iter_text():
    """Test de la fonction iter_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'iter_text')
    assert callable(getattr(_models, 'iter_text'))

def test_iter_lines():
    """Test de la fonction iter_lines"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'iter_lines')
    assert callable(getattr(_models, 'iter_lines'))

def test_iter_raw():
    """Test de la fonction iter_raw"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'iter_raw')
    assert callable(getattr(_models, 'iter_raw'))

def test_close():
    """Test de la fonction close"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'close')
    assert callable(getattr(_models, 'close'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__init__')
    assert callable(getattr(_models, '__init__'))

def test_extract_cookies():
    """Test de la fonction extract_cookies"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'extract_cookies')
    assert callable(getattr(_models, 'extract_cookies'))

def test_set_cookie_header():
    """Test de la fonction set_cookie_header"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'set_cookie_header')
    assert callable(getattr(_models, 'set_cookie_header'))

def test_set():
    """Test de la fonction set"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'set')
    assert callable(getattr(_models, 'set'))

def test_get():
    """Test de la fonction get"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'get')
    assert callable(getattr(_models, 'get'))

def test_delete():
    """Test de la fonction delete"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'delete')
    assert callable(getattr(_models, 'delete'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'clear')
    assert callable(getattr(_models, 'clear'))

def test_update():
    """Test de la fonction update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'update')
    assert callable(getattr(_models, 'update'))

def test___setitem__():
    """Test de la fonction __setitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__setitem__')
    assert callable(getattr(_models, '__setitem__'))

def test___getitem__():
    """Test de la fonction __getitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__getitem__')
    assert callable(getattr(_models, '__getitem__'))

def test___delitem__():
    """Test de la fonction __delitem__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__delitem__')
    assert callable(getattr(_models, '__delitem__'))

def test___len__():
    """Test de la fonction __len__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__len__')
    assert callable(getattr(_models, '__len__'))

def test___iter__():
    """Test de la fonction __iter__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__iter__')
    assert callable(getattr(_models, '__iter__'))

def test___bool__():
    """Test de la fonction __bool__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__bool__')
    assert callable(getattr(_models, '__bool__'))

def test___repr__():
    """Test de la fonction __repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__repr__')
    assert callable(getattr(_models, '__repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__init__')
    assert callable(getattr(_models, '__init__'))

def test_add_unredirected_header():
    """Test de la fonction add_unredirected_header"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'add_unredirected_header')
    assert callable(getattr(_models, 'add_unredirected_header'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, '__init__')
    assert callable(getattr(_models, '__init__'))

def test_info():
    """Test de la fonction info"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_models, 'info')
    assert callable(getattr(_models, 'info'))

class TestHeaders:
    """Tests pour la classe Headers"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_models, 'Headers')
        assert isinstance(getattr(_models, 'Headers'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_models, 'Headers')
        for method_name in ['__init__', 'encoding', 'encoding', 'raw', 'keys', 'values', 'items', 'multi_items', 'get', 'get_list', 'update', 'copy', '__getitem__', '__setitem__', '__delitem__', '__contains__', '__iter__', '__len__', '__eq__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRequest:
    """Tests pour la classe Request"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_models, 'Request')
        assert isinstance(getattr(_models, 'Request'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_models, 'Request')
        for method_name in ['__init__', '_prepare', 'content', 'read', '__repr__', '__getstate__', '__setstate__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestResponse:
    """Tests pour la classe Response"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_models, 'Response')
        assert isinstance(getattr(_models, 'Response'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_models, 'Response')
        for method_name in ['__init__', '_prepare', 'elapsed', 'elapsed', 'request', 'request', 'http_version', 'reason_phrase', 'url', 'content', 'text', 'encoding', 'encoding', 'charset_encoding', '_get_content_decoder', 'is_informational', 'is_success', 'is_redirect', 'is_client_error', 'is_server_error', 'is_error', 'has_redirect_location', 'raise_for_status', 'json', 'cookies', 'links', 'num_bytes_downloaded', '__repr__', '__getstate__', '__setstate__', 'read', 'iter_bytes', 'iter_text', 'iter_lines', 'iter_raw', 'close']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCookies:
    """Tests pour la classe Cookies"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_models, 'Cookies')
        assert isinstance(getattr(_models, 'Cookies'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_models, 'Cookies')
        for method_name in ['__init__', 'extract_cookies', 'set_cookie_header', 'set', 'get', 'delete', 'clear', 'update', '__setitem__', '__getitem__', '__delitem__', '__len__', '__iter__', '__bool__', '__repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_CookieCompatRequest:
    """Tests pour la classe _CookieCompatRequest"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_models, '_CookieCompatRequest')
        assert isinstance(getattr(_models, '_CookieCompatRequest'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_models, '_CookieCompatRequest')
        for method_name in ['__init__', 'add_unredirected_header']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class Test_CookieCompatResponse:
    """Tests pour la classe _CookieCompatResponse"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_models, '_CookieCompatResponse')
        assert isinstance(getattr(_models, '_CookieCompatResponse'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_models, '_CookieCompatResponse')
        for method_name in ['__init__', 'info']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
