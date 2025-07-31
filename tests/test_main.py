#!/usr/bin/env python3
"""
Tests pour le module main.py
Amélioration de la couverture de code de 10.05% à 80%+
"""

import signal
from unittest.mock import MagicMock, patch

from athalia_core.main import main, menu, safe_input, signal_handler, surveillance_mode


class TestSignalHandler:
    """Tests pour le gestionnaire de signal"""

    def test_signal_handler(self):
        """Test du gestionnaire de signal"""
        # Sauvegarder l'état initial
        import athalia_core.main

        original_running = athalia_core.main.running

        # Test du signal handler
        signal_handler(signal.SIGINT, None)

        # Vérifier que running est mis à False
        assert athalia_core.main.running is False

        # Restaurer l'état
        athalia_core.main.running = original_running


class TestMenu:
    """Tests pour la fonction menu"""

    @patch("builtins.input")
    def test_menu_normal_input(self, mock_input):
        """Test du menu avec entrée normale"""
        mock_input.return_value = "1"

        result = menu()

        assert result == "1"
        mock_input.assert_called_once_with("Choix: ")

    @patch("builtins.input")
    def test_menu_eof_error(self, mock_input):
        """Test du menu avec erreur EOF"""
        mock_input.side_effect = EOFError()

        result = menu()

        assert result == "q"

    @patch("builtins.input")
    def test_menu_keyboard_interrupt(self, mock_input):
        """Test du menu avec interruption clavier"""
        mock_input.side_effect = KeyboardInterrupt()

        result = menu()

        assert result == "q"

    @patch("builtins.input")
    def test_menu_with_whitespace(self, mock_input):
        """Test du menu avec espaces"""
        mock_input.return_value = "  2  "

        result = menu()

        assert result == "2"


class TestSafeInput:
    """Tests pour la fonction safe_input"""

    @patch("builtins.input")
    def test_safe_input_normal(self, mock_input):
        """Test d'entrée sécurisée normale"""
        mock_input.return_value = "test input"

        result = safe_input("Test prompt: ")

        assert result == "test input"
        mock_input.assert_called_once_with("Test prompt: ")

    @patch("builtins.input")
    def test_safe_input_with_whitespace(self, mock_input):
        """Test d'entrée sécurisée avec espaces"""
        mock_input.return_value = "  test input  "

        result = safe_input("Test prompt: ")

        assert result == "test input"

    @patch("builtins.input")
    def test_safe_input_eof_error(self, mock_input):
        """Test d'entrée sécurisée avec erreur EOF"""
        mock_input.side_effect = EOFError()

        result = safe_input("Test prompt: ")

        assert result == ""

    @patch("builtins.input")
    def test_safe_input_keyboard_interrupt(self, mock_input):
        """Test d'entrée sécurisée avec interruption clavier"""
        mock_input.side_effect = KeyboardInterrupt()

        result = safe_input("Test prompt: ")

        assert result == ""


class TestSurveillanceMode:
    """Tests pour le mode surveillance"""

    @patch("time.sleep")
    @patch("builtins.input")
    def test_surveillance_mode_normal(self, mock_input, mock_sleep):
        """Test du mode surveillance normal"""
        # Simuler une interruption après un court délai
        mock_sleep.side_effect = KeyboardInterrupt()

        surveillance_mode()

        mock_sleep.assert_called_with(30)

    @patch("time.sleep")
    def test_surveillance_mode_keyboard_interrupt(self, mock_sleep):
        """Test du mode surveillance avec interruption"""
        mock_sleep.side_effect = KeyboardInterrupt()

        surveillance_mode()

        mock_sleep.assert_called_with(30)


class TestMain:
    """Tests pour la fonction main"""

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    @patch("athalia_core.cleanup.clean_old_tests_and_caches")
    def test_main_cleanup_choice(self, mock_cleanup, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de nettoyage"""
        mock_menu.return_value = "2"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

        mock_cleanup.assert_called_once_with("test_project")

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    @patch("athalia_core.ci.generate_github_ci_yaml")
    @patch("athalia_core.ci.add_coverage_badge")
    def test_main_ci_choice(self, mock_badge, mock_ci, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de CI"""
        mock_menu.return_value = "3"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

        mock_ci.assert_called_once_with("test_project")
        mock_badge.assert_called_once_with("test_project")

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    @patch("athalia_core.onboarding.generate_onboard_cli")
    @patch("athalia_core.onboarding.generate_onboarding_html_advanced")
    def test_main_onboarding_choice(
        self, mock_html, mock_cli, mock_safe_input, mock_menu
    ):
        """Test de la fonction main avec choix d'onboarding"""
        mock_menu.return_value = "5"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

        mock_cli.assert_called_once_with({}, "test_project")
        mock_html.assert_called_once_with({}, "test_project")

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    @patch("athalia_core.security.security_audit_project")
    def test_main_security_choice(self, mock_security, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de sécurité"""
        mock_menu.return_value = "6"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

        mock_security.assert_called_once_with("test_project")

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_scan_choice(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de scan"""
        mock_menu.return_value = "7"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_dry_run_choice(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de dry-run"""
        mock_menu.return_value = "8"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_report_choice(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de rapport"""
        mock_menu.return_value = "9"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_rollback_choice(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de rollback"""
        mock_menu.return_value = "10"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_logs_choice(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix de logs"""
        mock_menu.return_value = "11"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_audit_choice(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec choix d'audit intelligent"""
        mock_menu.return_value = "12"
        mock_safe_input.return_value = "test_project"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    def test_main_quit_choice(self, mock_menu):
        """Test de la fonction main avec choix de quitter"""
        mock_menu.return_value = "13"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    def test_main_surveillance_choice(self, mock_menu):
        """Test de la fonction main avec choix de surveillance"""
        mock_menu.return_value = "14"

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            with patch("athalia_core.main.surveillance_mode") as mock_surveillance:
                main(test_mode=True)

                mock_surveillance.assert_called_once()

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_empty_input(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec entrée vide"""
        mock_menu.return_value = "1"
        mock_safe_input.return_value = ""

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_empty_input_cleanup(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec entrée vide pour nettoyage"""
        mock_menu.return_value = "2"
        mock_safe_input.return_value = ""

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_empty_input_ci(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec entrée vide pour CI"""
        mock_menu.return_value = "3"
        mock_safe_input.return_value = ""

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_empty_input_onboarding(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec entrée vide pour onboarding"""
        mock_menu.return_value = "5"
        mock_safe_input.return_value = ""

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    def test_main_empty_input_security(self, mock_safe_input, mock_menu):
        """Test de la fonction main avec entrée vide pour sécurité"""
        mock_menu.return_value = "6"
        mock_safe_input.return_value = ""

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("psutil.process_iter")
    @patch("psutil.Process")
    def test_main_process_detection(self, mock_process, mock_process_iter):
        """Test de la détection de processus"""
        # Mock des processus
        mock_proc1 = MagicMock()
        mock_proc1.info = {
            "pid": 123,
            "name": "python",
            "cmdline": ["python", "-m", "athalia_core.main"],
        }
        mock_proc2 = MagicMock()
        mock_proc2.info = {
            "pid": 456,
            "name": "python",
            "cmdline": ["python", "-m", "athalia_core.main"],
        }

        mock_process_iter.return_value = [mock_proc1, mock_proc2]

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("psutil.process_iter")
    def test_main_process_detection_no_such_process(self, mock_process_iter):
        """Test de la détection de processus avec erreur NoSuchProcess"""
        # Mock des processus avec erreur
        mock_proc = MagicMock()
        mock_proc.info = {
            "pid": 123,
            "name": "python",
            "cmdline": ["python", "-m", "athalia_core.main"],
        }
        mock_process_iter.return_value = [mock_proc]

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("psutil.process_iter")
    def test_main_process_detection_access_denied(self, mock_process_iter):
        """Test de la détection de processus avec erreur AccessDenied"""
        # Mock des processus avec erreur
        mock_proc = MagicMock()
        mock_proc.info = {
            "pid": 123,
            "name": "python",
            "cmdline": ["python", "-m", "athalia_core.main"],
        }
        mock_process_iter.return_value = [mock_proc]

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)


class TestIntegration:
    """Tests d'intégration pour le module main"""

    @patch("athalia_core.main.menu")
    @patch("athalia_core.main.safe_input")
    @patch("athalia_core.cleanup.clean_old_tests_and_caches")
    @patch("athalia_core.ci.generate_github_ci_yaml")
    @patch("athalia_core.ci.add_coverage_badge")
    def test_main_multiple_choices(
        self, mock_badge, mock_ci, mock_cleanup, mock_safe_input, mock_menu
    ):
        """Test de la fonction main avec plusieurs choix"""
        # Simuler plusieurs choix
        mock_menu.side_effect = ["2", "3", "13"]  # cleanup, ci, quit
        mock_safe_input.side_effect = ["project1", "project2"]

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

        mock_cleanup.assert_called_once_with("project1")
        mock_ci.assert_called_once_with("project2")
        mock_badge.assert_called_once_with("project2")

    def test_main_signal_handling(self):
        """Test de la gestion des signaux dans main"""
        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.athalia_logger")
    def test_main_with_advanced_logging(self, mock_logger):
        """Test de main avec logging avancé"""
        mock_logger.return_value = MagicMock()

        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)

    @patch("athalia_core.main.athalia_logger", None)
    def test_main_without_advanced_logging(self):
        """Test de main sans logging avancé"""
        # Mock pour éviter la boucle infinie
        with patch("athalia_core.main.running", False):
            main(test_mode=True)
