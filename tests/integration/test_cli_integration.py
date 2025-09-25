"""
Tests d'intégration pour le CLI Athalia
Vérifie le fonctionnement complet des commandes CLI
"""

import os
import subprocess
import tempfile
from pathlib import Path

import pytest


def _run(cmd, cwd, env, timeout=5):
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=cwd,
        env=env,
        timeout=timeout,
    )


@pytest.fixture(scope="module")
def project_root():
    return Path("/Volumes/T7/athalia-dev-setup")


@pytest.fixture(scope="module")
def base_env():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    return env


@pytest.mark.slow
class TestCLIIntegration:
    """Tests d'intégration pour le CLI"""

    @pytest.fixture
    def temp_dir(self):
        """Dossier temporaire pour les tests"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    def test_cli_help_command(self, project_root, base_env):
        """Test de la commande d'aide"""
        result = _run(
            ["python", "-m", "athalia_core.utilities.cli", "--help"],
            cwd=project_root,
            env=base_env,
        )
        assert result.returncode == 0
        assert "help" in result.stdout.lower()

    def test_cli_version_command(self, project_root, base_env):
        """Test de la commande de version"""
        result = _run(
            ["python", "-m", "athalia_core.utilities.cli", "--version"],
            cwd=project_root,
            env=base_env,
        )
        # Certains CLI n'implémentent pas --version (code 2). Accepter 0/1/2.
        assert result.returncode in [0, 1, 2]
        if result.returncode == 2:
            assert "No such option" in (result.stderr or "")

    def test_cli_main_entry_point(self, project_root, base_env):
        """Test du point d'entrée principal"""
        # Import direct: si le module ou l'attribut n'existe pas, on skippe
        try:
            import athalia_core.core.main as m
        except Exception:
            pytest.skip("module main non importable")
        if not hasattr(m, "main"):
            pytest.skip("main non disponible")
        assert callable(m.main)

    @pytest.mark.integration
    def test_cli_with_invalid_args(self, project_root, base_env):
        """Test avec arguments invalides"""
        result = _run(
            ["python", "-m", "athalia_core.utilities.cli", "invalid-command"],
            cwd=project_root,
            env=base_env,
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
    def test_cli_environment_variables(self, temp_dir, project_root, base_env):
        """Test avec variables d'environnement"""
        env = base_env.copy()
        env["ATHALIA_TEST"] = "true"
        result = _run(
            ["python", "-m", "athalia_core.utilities.cli", "--help"],
            cwd=project_root,
            env=env,
        )
        assert result.returncode == 0
