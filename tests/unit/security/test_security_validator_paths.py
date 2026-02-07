"""Tests pour vérifier l'absence de chemins absolus spécifiques à macOS."""

from pathlib import Path

import pytest

from athalia_core.validation.security_validator import CommandSecurityValidator


class TestCommandSecurityValidatorPaths:
    """Tests pour la validation des chemins de sécurité."""

    def test_no_macos_specific_paths(self):
        """Vérifie qu'aucun chemin macOS hardcodé n'est présent (sys.executable autorisé)."""
        import sys

        validator = CommandSecurityValidator()
        current_executable = sys.executable or ""

        # Chemins macOS hardcodés à éviter (le validateur ajoute sys.executable dynamiquement)
        forbidden_paths = [
            "/opt/homebrew/opt/pyenv/versions/3.10.14/bin/python",
            "/opt/homebrew/opt/pyenv/versions/3.10.14/bin/python3",
        ]
        for forbidden_path in forbidden_paths:
            if forbidden_path == current_executable:
                continue
            assert forbidden_path not in validator.allowed_commands, (
                f"Chemin macOS interdit trouvé: {forbidden_path}"
            )

    def test_python_paths_are_dynamic(self):
        """Vérifie que les chemins Python sont détectés dynamiquement."""
        validator = CommandSecurityValidator()

        # Vérifier que sys.executable est dans les commandes autorisées
        import sys

        if sys.executable:
            assert sys.executable in validator.allowed_commands, (
                "L'exécutable Python actuel doit être autorisé"
            )

    def test_relative_paths_are_present(self):
        """Vérifie que les chemins relatifs sont présents."""
        validator = CommandSecurityValidator()

        # Chemins relatifs qui doivent être présents
        required_relative_paths = [
            "bin/ath-lint.py",
            "bin/ath-test.py",
            "bin/ath-coverage.py",
        ]

        for relative_path in required_relative_paths:
            assert relative_path in validator.allowed_commands, (
                f"Chemin relatif requis manquant: {relative_path}"
            )

    def test_no_absolute_paths_in_whitelist(self):
        """Vérifie qu'aucun chemin absolu hardcodé n'est présent (sys.executable autorisé)."""
        import sys

        validator = CommandSecurityValidator()
        current_executable = sys.executable or ""

        for command in validator.allowed_commands:
            if (
                "/opt/homebrew/opt/pyenv/versions/" in command
                and command != current_executable
            ):
                pytest.fail(f"Chemin absolu macOS trouvé dans la whitelist: {command}")

    def test_security_validator_initialization(self):
        """Vérifie que le validateur s'initialise correctement."""
        validator = CommandSecurityValidator()

        # Vérifications de base
        assert hasattr(validator, "allowed_commands")
        assert hasattr(validator, "safe_directories")
        assert isinstance(validator.allowed_commands, set)
        assert isinstance(validator.safe_directories, list)

        # Vérifier que les commandes de base sont présentes
        basic_commands = ["python", "python3", "pip", "git"]
        for cmd in basic_commands:
            assert cmd in validator.allowed_commands, (
                f"Commande de base manquante: {cmd}"
            )
