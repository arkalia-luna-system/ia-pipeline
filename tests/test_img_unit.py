"""
Tests unitaires générés pour img
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import img
except ImportError:
    pytest.skip(f"Module img non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '__init__')
    assert callable(getattr(img, '__init__'))

def test__get_nix_font_path():
    """Test de la fonction _get_nix_font_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_nix_font_path')
    assert callable(getattr(img, '_get_nix_font_path'))

def test__create_nix():
    """Test de la fonction _create_nix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_create_nix')
    assert callable(getattr(img, '_create_nix'))

def test__get_mac_font_path():
    """Test de la fonction _get_mac_font_path"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_mac_font_path')
    assert callable(getattr(img, '_get_mac_font_path'))

def test__create_mac():
    """Test de la fonction _create_mac"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_create_mac')
    assert callable(getattr(img, '_create_mac'))

def test__lookup_win():
    """Test de la fonction _lookup_win"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_lookup_win')
    assert callable(getattr(img, '_lookup_win'))

def test__create_win():
    """Test de la fonction _create_win"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_create_win')
    assert callable(getattr(img, '_create_win'))

def test_get_char_size():
    """Test de la fonction get_char_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, 'get_char_size')
    assert callable(getattr(img, 'get_char_size'))

def test_get_text_size():
    """Test de la fonction get_text_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, 'get_text_size')
    assert callable(getattr(img, 'get_text_size'))

def test_get_font():
    """Test de la fonction get_font"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, 'get_font')
    assert callable(getattr(img, 'get_font'))

def test_get_style():
    """Test de la fonction get_style"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, 'get_style')
    assert callable(getattr(img, 'get_style'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '__init__')
    assert callable(getattr(img, '__init__'))

def test_get_style_defs():
    """Test de la fonction get_style_defs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, 'get_style_defs')
    assert callable(getattr(img, 'get_style_defs'))

def test__get_line_height():
    """Test de la fonction _get_line_height"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_line_height')
    assert callable(getattr(img, '_get_line_height'))

def test__get_line_y():
    """Test de la fonction _get_line_y"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_line_y')
    assert callable(getattr(img, '_get_line_y'))

def test__get_char_width():
    """Test de la fonction _get_char_width"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_char_width')
    assert callable(getattr(img, '_get_char_width'))

def test__get_char_x():
    """Test de la fonction _get_char_x"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_char_x')
    assert callable(getattr(img, '_get_char_x'))

def test__get_text_pos():
    """Test de la fonction _get_text_pos"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_text_pos')
    assert callable(getattr(img, '_get_text_pos'))

def test__get_linenumber_pos():
    """Test de la fonction _get_linenumber_pos"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_linenumber_pos')
    assert callable(getattr(img, '_get_linenumber_pos'))

def test__get_text_color():
    """Test de la fonction _get_text_color"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_text_color')
    assert callable(getattr(img, '_get_text_color'))

def test__get_text_bg_color():
    """Test de la fonction _get_text_bg_color"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_text_bg_color')
    assert callable(getattr(img, '_get_text_bg_color'))

def test__get_style_font():
    """Test de la fonction _get_style_font"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_style_font')
    assert callable(getattr(img, '_get_style_font'))

def test__get_image_size():
    """Test de la fonction _get_image_size"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_get_image_size')
    assert callable(getattr(img, '_get_image_size'))

def test__draw_linenumber():
    """Test de la fonction _draw_linenumber"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_draw_linenumber')
    assert callable(getattr(img, '_draw_linenumber'))

def test__draw_text():
    """Test de la fonction _draw_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_draw_text')
    assert callable(getattr(img, '_draw_text'))

def test__create_drawables():
    """Test de la fonction _create_drawables"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_create_drawables')
    assert callable(getattr(img, '_create_drawables'))

def test__draw_line_numbers():
    """Test de la fonction _draw_line_numbers"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_draw_line_numbers')
    assert callable(getattr(img, '_draw_line_numbers'))

def test__paint_line_number_bg():
    """Test de la fonction _paint_line_number_bg"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, '_paint_line_number_bg')
    assert callable(getattr(img, '_paint_line_number_bg'))

def test_format():
    """Test de la fonction format"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(img, 'format')
    assert callable(getattr(img, 'format'))

class TestPilNotAvailable:
    """Tests pour la classe PilNotAvailable"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(img, 'PilNotAvailable')
        assert isinstance(getattr(img, 'PilNotAvailable'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(img, 'PilNotAvailable')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFontNotFound:
    """Tests pour la classe FontNotFound"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(img, 'FontNotFound')
        assert isinstance(getattr(img, 'FontNotFound'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(img, 'FontNotFound')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFontManager:
    """Tests pour la classe FontManager"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(img, 'FontManager')
        assert isinstance(getattr(img, 'FontManager'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(img, 'FontManager')
        for method_name in ['__init__', '_get_nix_font_path', '_create_nix', '_get_mac_font_path', '_create_mac', '_lookup_win', '_create_win', 'get_char_size', 'get_text_size', 'get_font', 'get_style']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestImageFormatter:
    """Tests pour la classe ImageFormatter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(img, 'ImageFormatter')
        assert isinstance(getattr(img, 'ImageFormatter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(img, 'ImageFormatter')
        for method_name in ['__init__', 'get_style_defs', '_get_line_height', '_get_line_y', '_get_char_width', '_get_char_x', '_get_text_pos', '_get_linenumber_pos', '_get_text_color', '_get_text_bg_color', '_get_style_font', '_get_image_size', '_draw_linenumber', '_draw_text', '_create_drawables', '_draw_line_numbers', '_paint_line_number_bg', 'format']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGifImageFormatter:
    """Tests pour la classe GifImageFormatter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(img, 'GifImageFormatter')
        assert isinstance(getattr(img, 'GifImageFormatter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(img, 'GifImageFormatter')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestJpgImageFormatter:
    """Tests pour la classe JpgImageFormatter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(img, 'JpgImageFormatter')
        assert isinstance(getattr(img, 'JpgImageFormatter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(img, 'JpgImageFormatter')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestBmpImageFormatter:
    """Tests pour la classe BmpImageFormatter"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(img, 'BmpImageFormatter')
        assert isinstance(getattr(img, 'BmpImageFormatter'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(img, 'BmpImageFormatter')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
