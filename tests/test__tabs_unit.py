"""
Tests unitaires générés pour _tabs
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _tabs
except ImportError:
    pytest.skip(f"Module _tabs non importable")


def test__highlight_range():
    """Test de la fonction _highlight_range"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_highlight_range')
    assert callable(getattr(_tabs, '_highlight_range'))

def test_render():
    """Test de la fonction render"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'render')
    assert callable(getattr(_tabs, 'render'))

def test__on_click():
    """Test de la fonction _on_click"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_click')
    assert callable(getattr(_tabs, '_on_click'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '__init__')
    assert callable(getattr(_tabs, '__init__'))

def test_label():
    """Test de la fonction label"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'label')
    assert callable(getattr(_tabs, 'label'))

def test_label():
    """Test de la fonction label"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'label')
    assert callable(getattr(_tabs, 'label'))

def test_update():
    """Test de la fonction update"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'update')
    assert callable(getattr(_tabs, 'update'))

def test_label_text():
    """Test de la fonction label_text"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'label_text')
    assert callable(getattr(_tabs, 'label_text'))

def test__on_click():
    """Test de la fonction _on_click"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_click')
    assert callable(getattr(_tabs, '_on_click'))

def test__watch_disabled():
    """Test de la fonction _watch_disabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_watch_disabled')
    assert callable(getattr(_tabs, '_watch_disabled'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '__init__')
    assert callable(getattr(_tabs, '__init__'))

def test__auto_tab_id():
    """Test de la fonction _auto_tab_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_auto_tab_id')
    assert callable(getattr(_tabs, '_auto_tab_id'))

def test__new_tab_id():
    """Test de la fonction _new_tab_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_new_tab_id')
    assert callable(getattr(_tabs, '_new_tab_id'))

def test_tab_count():
    """Test de la fonction tab_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'tab_count')
    assert callable(getattr(_tabs, 'tab_count'))

def test__potentially_active_tabs():
    """Test de la fonction _potentially_active_tabs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_potentially_active_tabs')
    assert callable(getattr(_tabs, '_potentially_active_tabs'))

def test__next_active():
    """Test de la fonction _next_active"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_next_active')
    assert callable(getattr(_tabs, '_next_active'))

def test_add_tab():
    """Test de la fonction add_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'add_tab')
    assert callable(getattr(_tabs, 'add_tab'))

def test_clear():
    """Test de la fonction clear"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'clear')
    assert callable(getattr(_tabs, 'clear'))

def test_remove_tab():
    """Test de la fonction remove_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'remove_tab')
    assert callable(getattr(_tabs, 'remove_tab'))

def test_validate_active():
    """Test de la fonction validate_active"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'validate_active')
    assert callable(getattr(_tabs, 'validate_active'))

def test_active_tab():
    """Test de la fonction active_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'active_tab')
    assert callable(getattr(_tabs, 'active_tab'))

def test__on_mount():
    """Test de la fonction _on_mount"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_mount')
    assert callable(getattr(_tabs, '_on_mount'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'compose')
    assert callable(getattr(_tabs, 'compose'))

def test_watch_active():
    """Test de la fonction watch_active"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'watch_active')
    assert callable(getattr(_tabs, 'watch_active'))

def test__highlight_active():
    """Test de la fonction _highlight_active"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_highlight_active')
    assert callable(getattr(_tabs, '_highlight_active'))

def test__activate_tab():
    """Test de la fonction _activate_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_activate_tab')
    assert callable(getattr(_tabs, '_activate_tab'))

def test__on_underline_clicked():
    """Test de la fonction _on_underline_clicked"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_underline_clicked')
    assert callable(getattr(_tabs, '_on_underline_clicked'))

def test__scroll_active_tab():
    """Test de la fonction _scroll_active_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_scroll_active_tab')
    assert callable(getattr(_tabs, '_scroll_active_tab'))

def test__on_resize():
    """Test de la fonction _on_resize"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_resize')
    assert callable(getattr(_tabs, '_on_resize'))

def test_action_next_tab():
    """Test de la fonction action_next_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'action_next_tab')
    assert callable(getattr(_tabs, 'action_next_tab'))

def test_action_previous_tab():
    """Test de la fonction action_previous_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'action_previous_tab')
    assert callable(getattr(_tabs, 'action_previous_tab'))

def test__move_tab():
    """Test de la fonction _move_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_move_tab')
    assert callable(getattr(_tabs, '_move_tab'))

def test__on_tab_disabled():
    """Test de la fonction _on_tab_disabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_tab_disabled')
    assert callable(getattr(_tabs, '_on_tab_disabled'))

def test__on_tab_enabled():
    """Test de la fonction _on_tab_enabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_tab_enabled')
    assert callable(getattr(_tabs, '_on_tab_enabled'))

def test__on_tab_relabelled():
    """Test de la fonction _on_tab_relabelled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '_on_tab_relabelled')
    assert callable(getattr(_tabs, '_on_tab_relabelled'))

def test_disable():
    """Test de la fonction disable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'disable')
    assert callable(getattr(_tabs, 'disable'))

def test_enable():
    """Test de la fonction enable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'enable')
    assert callable(getattr(_tabs, 'enable'))

def test_hide():
    """Test de la fonction hide"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'hide')
    assert callable(getattr(_tabs, 'hide'))

def test_show():
    """Test de la fonction show"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'show')
    assert callable(getattr(_tabs, 'show'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '__init__')
    assert callable(getattr(_tabs, '__init__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'control')
    assert callable(getattr(_tabs, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '__init__')
    assert callable(getattr(_tabs, '__init__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'control')
    assert callable(getattr(_tabs, 'control'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '__rich_repr__')
    assert callable(getattr(_tabs, '__rich_repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '__init__')
    assert callable(getattr(_tabs, '__init__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'control')
    assert callable(getattr(_tabs, 'control'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, '__rich_repr__')
    assert callable(getattr(_tabs, '__rich_repr__'))

def test_move_underline():
    """Test de la fonction move_underline"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabs, 'move_underline')
    assert callable(getattr(_tabs, 'move_underline'))

class TestUnderline:
    """Tests pour la classe Underline"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Underline')
        assert isinstance(getattr(_tabs, 'Underline'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Underline')
        for method_name in ['_highlight_range', 'render', '_on_click']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTab:
    """Tests pour la classe Tab"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Tab')
        assert isinstance(getattr(_tabs, 'Tab'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Tab')
        for method_name in ['__init__', 'label', 'label', 'update', 'label_text', '_on_click', '_watch_disabled']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabs:
    """Tests pour la classe Tabs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Tabs')
        assert isinstance(getattr(_tabs, 'Tabs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Tabs')
        for method_name in ['__init__', '_auto_tab_id', '_new_tab_id', 'tab_count', '_potentially_active_tabs', '_next_active', 'add_tab', 'clear', 'remove_tab', 'validate_active', 'active_tab', '_on_mount', 'compose', 'watch_active', '_highlight_active', '_activate_tab', '_on_underline_clicked', '_scroll_active_tab', '_on_resize', 'action_next_tab', 'action_previous_tab', '_move_tab', '_on_tab_disabled', '_on_tab_enabled', '_on_tab_relabelled', 'disable', 'enable', 'hide', 'show']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestClicked:
    """Tests pour la classe Clicked"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Clicked')
        assert isinstance(getattr(_tabs, 'Clicked'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Clicked')
        for method_name in ['__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabMessage:
    """Tests pour la classe TabMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabMessage')
        assert isinstance(getattr(_tabs, 'TabMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabMessage')
        for method_name in ['control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestClicked:
    """Tests pour la classe Clicked"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Clicked')
        assert isinstance(getattr(_tabs, 'Clicked'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Clicked')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDisabled:
    """Tests pour la classe Disabled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Disabled')
        assert isinstance(getattr(_tabs, 'Disabled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Disabled')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestEnabled:
    """Tests pour la classe Enabled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Enabled')
        assert isinstance(getattr(_tabs, 'Enabled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Enabled')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestRelabelled:
    """Tests pour la classe Relabelled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Relabelled')
        assert isinstance(getattr(_tabs, 'Relabelled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Relabelled')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabError:
    """Tests pour la classe TabError"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabError')
        assert isinstance(getattr(_tabs, 'TabError'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabError')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabMessage:
    """Tests pour la classe TabMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabMessage')
        assert isinstance(getattr(_tabs, 'TabMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabMessage')
        for method_name in ['__init__', 'control', '__rich_repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabActivated:
    """Tests pour la classe TabActivated"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabActivated')
        assert isinstance(getattr(_tabs, 'TabActivated'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabActivated')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabDisabled:
    """Tests pour la classe TabDisabled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabDisabled')
        assert isinstance(getattr(_tabs, 'TabDisabled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabDisabled')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabEnabled:
    """Tests pour la classe TabEnabled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabEnabled')
        assert isinstance(getattr(_tabs, 'TabEnabled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabEnabled')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabHidden:
    """Tests pour la classe TabHidden"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabHidden')
        assert isinstance(getattr(_tabs, 'TabHidden'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabHidden')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabShown:
    """Tests pour la classe TabShown"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'TabShown')
        assert isinstance(getattr(_tabs, 'TabShown'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'TabShown')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCleared:
    """Tests pour la classe Cleared"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabs, 'Cleared')
        assert isinstance(getattr(_tabs, 'Cleared'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabs, 'Cleared')
        for method_name in ['__init__', 'control', '__rich_repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
