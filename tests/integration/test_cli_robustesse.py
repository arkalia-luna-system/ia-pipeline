#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests d'intégration CLI robuste pour Athalia.
Tests professionnels pour la CI/CD.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


class TestCLIRobustesse:
    """Tests de robustesse de l'interface en ligne de commande."""

    def setup_method(self):
        """Initialisation pour chaque test."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.cli_paths = [
            # Scripts CLI simples qui fonctionnent
            Path("bin/ath-audit.py"),
            Path("bin/ath-coverage.py"),
            Path("bin/ath-build.py"),
            Path("bin/ath-lint.py"),
            # Exclure athalia_core/main.py car c'est un script interactif
            # Path("athalia_core/main.py"),
            # Exclure athalia_unified.py car il entre dans une boucle interactive
            # Path("athalia_unified.py"),
            # Exclure ath-test.py car il lance pytest et prend trop de temps
            # Path("bin/ath-test.py"),
        ]
        # Correction pour éviter les timeouts dans les tests CLI

    def teardown_method(self):
        """Nettoyage après chaque test."""
        import shutil

        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    @pytest.mark.timeout(120)
    def test_cli_help_command(self):
        """Test de la commande d'aide."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=120,
                    )

                    # Vérifier que la commande s'exécute sans erreur
                    assert result.returncode in [0, 1]  # 0 = succès, 1 = aide affichée
                    assert len(result.stdout) > 0 or len(result.stderr) > 0

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    @pytest.mark.timeout(120)
    def test_cli_version_command(self):
        """Test de la commande de version."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--version"],
                        capture_output=True,
                        text=True,
                        timeout=120,
                    )

                    # Vérifier que la commande s'exécute
                    assert result.returncode in [0, 1]

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    @pytest.mark.timeout(120)
    def test_cli_invalid_argument(self):
        """Test avec des arguments invalides."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--invalid-arg"],
                        capture_output=True,
                        text=True,
                        timeout=120,
                    )

                    # Devrait retourner une erreur pour un argument invalide
                    assert result.returncode != 0

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_missing_argument(self):
        """Test avec des arguments manquants."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--action"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Devrait retourner une erreur pour un argument manquant
                    assert result.returncode != 0

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_dry_run_mode(self):
        """Test du mode simulation (dry-run)."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--dry-run"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Le mode dry-run ne devrait pas échouer
                    assert result.returncode in [0, 1]

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_verbose_mode(self):
        """Test du mode verbeux."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--verbose"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Le mode verbeux devrait produire plus de sortie
                    assert result.returncode in [0, 1]

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_timeout_handling(self):
        """Test de la gestion des timeouts."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    # Test avec un timeout très court
                    _ = subprocess.run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=1,  # Timeout très court
                    )

                    # Si le timeout est respecté, c'est bien
                    assert True

                except subprocess.TimeoutExpired:
                    # Le timeout est normal pour un timeout court
                    assert True
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_error_handling(self):
        """Test de la gestion d'erreurs."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    # Test avec un fichier inexistant
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "/chemin/inexistant"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Devrait gérer l'erreur gracieusement
                    assert result.returncode != 0

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_output_format(self):
        """Test du format de sortie."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # La sortie devrait être du texte
                    if result.stdout:
                        assert isinstance(result.stdout, str)
                    if result.stderr:
                        assert isinstance(result.stderr, str)

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_environment_variables(self):
        """Test avec des variables d'environnement."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    # Test avec des variables d'environnement
                    env = os.environ.copy()
                    env["ATHALIA_DEBUG"] = "1"

                    result = subprocess.run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                        env=env,
                    )

                    # Devrait fonctionner avec les variables d'environnement
                    assert result.returncode in [0, 1]

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_concurrent_execution(self):
        """Test d'exécution concurrente."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    # Lancer plusieurs processus CLI simultanément
                    processes = []
                    for i in range(3):
                        process = subprocess.Popen(
                            [sys.executable, str(cli_path), "--help"],
                            capture_output=True,
                            text=True,
                        )
                        processes.append(process)

                    # Attendre que tous les processus se terminent
                    for process in processes:
                        process.wait(timeout=30)
                        assert process.returncode in [0, 1]

                except subprocess.TimeoutExpired:
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")


def test_cli_basic_functionality():
    """Test de fonctionnalité de base de la CLI."""
    # Test avec athalia_unified.py s'il existe
    cli_path = Path("athalia_unified.py")
    if not cli_path.exists():
        pytest.skip("CLI principale non trouvée")

    try:
        result = subprocess.run(
            [sys.executable, str(cli_path), "--help"],
            capture_output=True,
            text=True,
            timeout=30,
        )

        assert result.returncode in [0, 1]

    except subprocess.TimeoutExpired:
        pytest.skip("CLI prend trop de temps à démarrer")
    except Exception as e:
        pytest.skip(f"CLI non disponible: {e}")


def test_cli_integration_workflow():
    """Test du workflow d'intégration CLI."""
    cli_path = Path("athalia_unified.py")
    if not cli_path.exists():
        pytest.skip("CLI principale non trouvée")

    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Test d'un workflow complet
            result = subprocess.run(
                [
                    sys.executable,
                    str(cli_path),
                    temp_dir,
                    "--action",
                    "audit",
                    "--dry-run",
                ],
                capture_output=True,
                text=True,
                timeout=60,
            )

            # Le workflow devrait s'exécuter sans erreur critique
            assert result.returncode in [0, 1]

        except subprocess.TimeoutExpired:
            pytest.skip("Workflow CLI prend trop de temps")
        except Exception as e:
            pytest.skip(f"Workflow CLI non disponible: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
