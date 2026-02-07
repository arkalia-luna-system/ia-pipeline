"""
Tests unitaires générés pour _tabbed_content
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import _tabbed_content
except ImportError:
    pytest.skip(f"Module _tabbed_content non importable")


def test_add_prefix():
    """Test de la fonction add_prefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'add_prefix')
    assert callable(getattr(_tabbed_content, 'add_prefix'))

def test_sans_prefix():
    """Test de la fonction sans_prefix"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'sans_prefix')
    assert callable(getattr(_tabbed_content, 'sans_prefix'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '__init__')
    assert callable(getattr(_tabbed_content, '__init__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '__init__')
    assert callable(getattr(_tabbed_content, '__init__'))

def test_get_content_tab():
    """Test de la fonction get_content_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'get_content_tab')
    assert callable(getattr(_tabbed_content, 'get_content_tab'))

def test_disable():
    """Test de la fonction disable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'disable')
    assert callable(getattr(_tabbed_content, 'disable'))

def test_enable():
    """Test de la fonction enable"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'enable')
    assert callable(getattr(_tabbed_content, 'enable'))

def test_hide():
    """Test de la fonction hide"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'hide')
    assert callable(getattr(_tabbed_content, 'hide'))

def test_show():
    """Test de la fonction show"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'show')
    assert callable(getattr(_tabbed_content, 'show'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '__init__')
    assert callable(getattr(_tabbed_content, '__init__'))

def test__watch_disabled():
    """Test de la fonction _watch_disabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_watch_disabled')
    assert callable(getattr(_tabbed_content, '_watch_disabled'))

def test__on_descendant_focus():
    """Test de la fonction _on_descendant_focus"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_descendant_focus')
    assert callable(getattr(_tabbed_content, '_on_descendant_focus'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '__init__')
    assert callable(getattr(_tabbed_content, '__init__'))

def test_active_pane():
    """Test de la fonction active_pane"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'active_pane')
    assert callable(getattr(_tabbed_content, 'active_pane'))

def test__set_id():
    """Test de la fonction _set_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_set_id')
    assert callable(getattr(_tabbed_content, '_set_id'))

def test__generate_tab_id():
    """Test de la fonction _generate_tab_id"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_generate_tab_id')
    assert callable(getattr(_tabbed_content, '_generate_tab_id'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'compose')
    assert callable(getattr(_tabbed_content, 'compose'))

def test_add_pane():
    """Test de la fonction add_pane"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'add_pane')
    assert callable(getattr(_tabbed_content, 'add_pane'))

def test_remove_pane():
    """Test de la fonction remove_pane"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'remove_pane')
    assert callable(getattr(_tabbed_content, 'remove_pane'))

def test_clear_panes():
    """Test de la fonction clear_panes"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'clear_panes')
    assert callable(getattr(_tabbed_content, 'clear_panes'))

def test_compose_add_child():
    """Test de la fonction compose_add_child"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'compose_add_child')
    assert callable(getattr(_tabbed_content, 'compose_add_child'))

def test__on_tabs_tab_activated():
    """Test de la fonction _on_tabs_tab_activated"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_tabs_tab_activated')
    assert callable(getattr(_tabbed_content, '_on_tabs_tab_activated'))

def test__on_tab_pane_focused():
    """Test de la fonction _on_tab_pane_focused"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_tab_pane_focused')
    assert callable(getattr(_tabbed_content, '_on_tab_pane_focused'))

def test__on_tabs_cleared():
    """Test de la fonction _on_tabs_cleared"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_tabs_cleared')
    assert callable(getattr(_tabbed_content, '_on_tabs_cleared'))

def test__is_associated_tabs():
    """Test de la fonction _is_associated_tabs"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_is_associated_tabs')
    assert callable(getattr(_tabbed_content, '_is_associated_tabs'))

def test__watch_active():
    """Test de la fonction _watch_active"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_watch_active')
    assert callable(getattr(_tabbed_content, '_watch_active'))

def test_tab_count():
    """Test de la fonction tab_count"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'tab_count')
    assert callable(getattr(_tabbed_content, 'tab_count'))

def test_get_tab():
    """Test de la fonction get_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'get_tab')
    assert callable(getattr(_tabbed_content, 'get_tab'))

def test_get_pane():
    """Test de la fonction get_pane"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'get_pane')
    assert callable(getattr(_tabbed_content, 'get_pane'))

def test__on_tabs_tab_disabled():
    """Test de la fonction _on_tabs_tab_disabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_tabs_tab_disabled')
    assert callable(getattr(_tabbed_content, '_on_tabs_tab_disabled'))

def test__on_tab_pane_disabled():
    """Test de la fonction _on_tab_pane_disabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_tab_pane_disabled')
    assert callable(getattr(_tabbed_content, '_on_tab_pane_disabled'))

def test__on_tabs_tab_enabled():
    """Test de la fonction _on_tabs_tab_enabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_tabs_tab_enabled')
    assert callable(getattr(_tabbed_content, '_on_tabs_tab_enabled'))

def test__on_tab_pane_enabled():
    """Test de la fonction _on_tab_pane_enabled"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '_on_tab_pane_enabled')
    assert callable(getattr(_tabbed_content, '_on_tab_pane_enabled'))

def test_disable_tab():
    """Test de la fonction disable_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'disable_tab')
    assert callable(getattr(_tabbed_content, 'disable_tab'))

def test_enable_tab():
    """Test de la fonction enable_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'enable_tab')
    assert callable(getattr(_tabbed_content, 'enable_tab'))

def test_hide_tab():
    """Test de la fonction hide_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'hide_tab')
    assert callable(getattr(_tabbed_content, 'hide_tab'))

def test_show_tab():
    """Test de la fonction show_tab"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'show_tab')
    assert callable(getattr(_tabbed_content, 'show_tab'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'control')
    assert callable(getattr(_tabbed_content, 'control'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '__init__')
    assert callable(getattr(_tabbed_content, '__init__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'control')
    assert callable(getattr(_tabbed_content, 'control'))

def test___rich_repr__():
    """Test de la fonction __rich_repr__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '__rich_repr__')
    assert callable(getattr(_tabbed_content, '__rich_repr__'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, '__init__')
    assert callable(getattr(_tabbed_content, '__init__'))

def test_control():
    """Test de la fonction control"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(_tabbed_content, 'control')
    assert callable(getattr(_tabbed_content, 'control'))

class TestContentTab:
    """Tests pour la classe ContentTab"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'ContentTab')
        assert isinstance(getattr(_tabbed_content, 'ContentTab'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'ContentTab')
        for method_name in ['add_prefix', 'sans_prefix', '__init__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestContentTabs:
    """Tests pour la classe ContentTabs"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'ContentTabs')
        assert isinstance(getattr(_tabbed_content, 'ContentTabs'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'ContentTabs')
        for method_name in ['__init__', 'get_content_tab', 'disable', 'enable', 'hide', 'show']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabPane:
    """Tests pour la classe TabPane"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'TabPane')
        assert isinstance(getattr(_tabbed_content, 'TabPane'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'TabPane')
        for method_name in ['__init__', '_watch_disabled', '_on_descendant_focus']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabbedContent:
    """Tests pour la classe TabbedContent"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'TabbedContent')
        assert isinstance(getattr(_tabbed_content, 'TabbedContent'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'TabbedContent')
        for method_name in ['__init__', 'active_pane', '_set_id', '_generate_tab_id', 'compose', 'add_pane', 'remove_pane', 'clear_panes', 'compose_add_child', '_on_tabs_tab_activated', '_on_tab_pane_focused', '_on_tabs_cleared', '_is_associated_tabs', '_watch_active', 'tab_count', 'get_tab', 'get_pane', '_on_tabs_tab_disabled', '_on_tab_pane_disabled', '_on_tabs_tab_enabled', '_on_tab_pane_enabled', 'disable_tab', 'enable_tab', 'hide_tab', 'show_tab']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabPaneMessage:
    """Tests pour la classe TabPaneMessage"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'TabPaneMessage')
        assert isinstance(getattr(_tabbed_content, 'TabPaneMessage'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'TabPaneMessage')
        for method_name in ['control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestDisabled:
    """Tests pour la classe Disabled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'Disabled')
        assert isinstance(getattr(_tabbed_content, 'Disabled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'Disabled')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestEnabled:
    """Tests pour la classe Enabled"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'Enabled')
        assert isinstance(getattr(_tabbed_content, 'Enabled'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'Enabled')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestFocused:
    """Tests pour la classe Focused"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'Focused')
        assert isinstance(getattr(_tabbed_content, 'Focused'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'Focused')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTabActivated:
    """Tests pour la classe TabActivated"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'TabActivated')
        assert isinstance(getattr(_tabbed_content, 'TabActivated'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'TabActivated')
        for method_name in ['__init__', 'control', '__rich_repr__']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestCleared:
    """Tests pour la classe Cleared"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(_tabbed_content, 'Cleared')
        assert isinstance(getattr(_tabbed_content, 'Cleared'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(_tabbed_content, 'Cleared')
        for method_name in ['__init__', 'control']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
