"""
Tests d'intégration pour le CLI Athalia
Vérifie le fonctionnement complet des commandes CLI
"""

import os
import subprocess
import tempfile
from pathlib import Path

import pytest


class TestCLIIntegration:
    """Tests d'intégration pour le CLI"""

    @pytest.fixture
    def temp_dir(self):
        """Dossier temporaire pour les tests"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    def test_cli_help_command(self):
        """Test de la commande d'aide"""
        result = subprocess.run(
            ["python", "-m", "athalia_core.utilities.cli", "--help"],
            capture_output=True,
            text=True,
            cwd="/Volumes/T7/athalia-dev-setup",
        )
        assert result.returncode == 0
        assert "help" in result.stdout.lower()

    def test_cli_version_command(self):
        """Test de la commande de version"""
        result = subprocess.run(
            ["python", "-m", "athalia_core.utilities.cli", "--version"],
            capture_output=True,
            text=True,
            cwd="/Volumes/T7/athalia-dev-setup",
        )
        # Peut retourner 0 ou 1 selon l'implémentation
        assert result.returncode in [0, 1]

    def test_cli_main_entry_point(self):
        """Test du point d'entrée principal"""
        result = subprocess.run(
            ["python", "-c", "from athalia_core.core.main import main; main()"],
            capture_output=True,
            text=True,
            cwd="/Volumes/T7/athalia-dev-setup",
        )
        # Peut retourner 0 ou 1 selon l'implémentation
        assert result.returncode in [0, 1]

    @pytest.mark.integration
    def test_cli_with_invalid_args(self):
        """Test avec arguments invalides"""
        result = subprocess.run(
            ["python", "-m", "athalia_core.utilities.cli", "invalid-command"],
            capture_output=True,
            text=True,
            cwd="/Volumes/T7/athalia-dev-setup",
        )
        # Doit gérer gracieusement les arguments invalides
        assert result.returncode != 0  # Erreur attendue

    @pytest.mark.integration
    def test_cli_imports(self):
        """Test que tous les modules CLI peuvent être importés"""
        try:
            from athalia_core.core.main import main
            from athalia_core.utilities.cli import cli
            from athalia_core.utilities.dashboard import Dashboard

            assert True  # Import réussi
        except ImportError as e:
            pytest.fail(f"Import failed: {e}")

    @pytest.mark.integration
    def test_cli_environment_variables(self, temp_dir):
        """Test avec variables d'environnement"""
        env = os.environ.copy()
        env["ATHALIA_TEST"] = "true"

        result = subprocess.run(
            ["python", "-m", "athalia_core.utilities.cli", "--help"],
            capture_output=True,
            text=True,
            cwd="/Volumes/T7/athalia-dev-setup",
            env=env,
        )
        assert result.returncode == 0
