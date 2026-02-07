"""
Tests unitaires générés pour game
"""

import pytest
from pathlib import Path
import sys

# Ajouter le chemin du projet au PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import game
except ImportError:
    pytest.skip(f"Module game non importable")


def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, '__init__')
    assert callable(getattr(game, '__init__'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'compose')
    assert callable(getattr(game, 'compose'))

def test_on_mount():
    """Test de la fonction on_mount"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'on_mount')
    assert callable(getattr(game, 'on_mount'))

def test_watch_position():
    """Test de la fonction watch_position"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'watch_position')
    assert callable(getattr(game, 'watch_position'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'compose')
    assert callable(getattr(game, 'compose'))

def test_on_button_pressed():
    """Test de la fonction on_button_pressed"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'on_button_pressed')
    assert callable(getattr(game, 'on_button_pressed'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'compose')
    assert callable(getattr(game, 'compose'))

def test___init__():
    """Test de la fonction __init__"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, '__init__')
    assert callable(getattr(game, '__init__'))

def test_check_win():
    """Test de la fonction check_win"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'check_win')
    assert callable(getattr(game, 'check_win'))

def test_watch_dimensions():
    """Test de la fonction watch_dimensions"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'watch_dimensions')
    assert callable(getattr(game, 'watch_dimensions'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'compose')
    assert callable(getattr(game, 'compose'))

def test_update_clock():
    """Test de la fonction update_clock"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'update_clock')
    assert callable(getattr(game, 'update_clock'))

def test_watch_play_time():
    """Test de la fonction watch_play_time"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'watch_play_time')
    assert callable(getattr(game, 'watch_play_time'))

def test_watch_state():
    """Test de la fonction watch_state"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'watch_state')
    assert callable(getattr(game, 'watch_state'))

def test_get_tile():
    """Test de la fonction get_tile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'get_tile')
    assert callable(getattr(game, 'get_tile'))

def test_get_tile_at():
    """Test de la fonction get_tile_at"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'get_tile_at')
    assert callable(getattr(game, 'get_tile_at'))

def test_move_tile():
    """Test de la fonction move_tile"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'move_tile')
    assert callable(getattr(game, 'move_tile'))

def test_can_move():
    """Test de la fonction can_move"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'can_move')
    assert callable(getattr(game, 'can_move'))

def test_action_move():
    """Test de la fonction action_move"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'action_move')
    assert callable(getattr(game, 'action_move'))

def test_get_legal_moves():
    """Test de la fonction get_legal_moves"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'get_legal_moves')
    assert callable(getattr(game, 'get_legal_moves'))

def test_on_tile_clicked():
    """Test de la fonction on_tile_clicked"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'on_tile_clicked')
    assert callable(getattr(game, 'on_tile_clicked'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'compose')
    assert callable(getattr(game, 'compose'))

def test_compose():
    """Test de la fonction compose"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'compose')
    assert callable(getattr(game, 'compose'))

def test_action_shuffle():
    """Test de la fonction action_shuffle"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'action_shuffle')
    assert callable(getattr(game, 'action_shuffle'))

def test_action_new_game():
    """Test de la fonction action_new_game"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'action_new_game')
    assert callable(getattr(game, 'action_new_game'))

def test_check_action():
    """Test de la fonction check_action"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'check_action')
    assert callable(getattr(game, 'check_action'))

def test_get_default_screen():
    """Test de la fonction get_default_screen"""
    # TODO: Implémenter les tests spécifiques
    assert hasattr(game, 'get_default_screen')
    assert callable(getattr(game, 'get_default_screen'))

class TestNewGame:
    """Tests pour la classe NewGame"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'NewGame')
        assert isinstance(getattr(game, 'NewGame'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'NewGame')
        for method_name in []:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestTile:
    """Tests pour la classe Tile"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'Tile')
        assert isinstance(getattr(game, 'Tile'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'Tile')
        for method_name in ['__init__', 'compose', 'on_mount', 'watch_position']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGameDialog:
    """Tests pour la classe GameDialog"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'GameDialog')
        assert isinstance(getattr(game, 'GameDialog'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'GameDialog')
        for method_name in ['compose', 'on_button_pressed']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGameDialogScreen:
    """Tests pour la classe GameDialogScreen"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'GameDialogScreen')
        assert isinstance(getattr(game, 'GameDialogScreen'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'GameDialogScreen')
        for method_name in ['compose']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGame:
    """Tests pour la classe Game"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'Game')
        assert isinstance(getattr(game, 'Game'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'Game')
        for method_name in ['__init__', 'check_win', 'watch_dimensions', 'compose', 'update_clock', 'watch_play_time', 'watch_state', 'get_tile', 'get_tile_at', 'move_tile', 'can_move', 'action_move', 'get_legal_moves', 'on_tile_clicked']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGameInstructions:
    """Tests pour la classe GameInstructions"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'GameInstructions')
        assert isinstance(getattr(game, 'GameInstructions'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'GameInstructions')
        for method_name in ['compose']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGameScreen:
    """Tests pour la classe GameScreen"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'GameScreen')
        assert isinstance(getattr(game, 'GameScreen'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'GameScreen')
        for method_name in ['compose', 'action_shuffle', 'action_new_game', 'check_action']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

class TestGameApp:
    """Tests pour la classe GameApp"""

    def test_class_exists(self):
        """Vérifie que la classe existe"""
        assert hasattr(game, 'GameApp')
        assert isinstance(getattr(game, 'GameApp'), type)

    def test_class_methods(self):
        """Vérifie les méthodes de la classe"""
        cls = getattr(game, 'GameApp')
        for method_name in ['get_default_screen']:
            assert hasattr(cls, method_name)
            assert callable(getattr(cls, method_name))

if __name__ == "__main__":
    pytest.main([__file__])
