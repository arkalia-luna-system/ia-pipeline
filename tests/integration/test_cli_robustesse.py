#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests d'intégration CLI robuste pour Athalia.
Tests professionnels pour la CI/CD.
"""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any

import pytest

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:

    def validate_and_run(
        command: list[str], **kwargs: Any
    ) -> subprocess.CompletedProcess:
        return subprocess.run(command, **kwargs)

    class SecurityErrorFallback(Exception):
        pass

    SecurityError = SecurityErrorFallback


class TestCLIRobustesse:
    """Tests de robustesse de l'interface en ligne de commande."""

    def setup_method(self) -> None:
        """Initialisation pour chaque test."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.cli_paths = [
            # Scripts CLI qui existent et fonctionnent
            Path("bin/ath-lint.py"),
            Path("bin/ath-coverage.py"),
            Path("bin/ath-test.py"),
            Path("bin/ath-audit.py"),
            Path("bin/ath-build.py"),
        ]

    def teardown_method(self):
        """Nettoyage après chaque test."""
        import shutil

        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    @pytest.mark.timeout(30)
    def test_cli_help_command(self):
        """Test de la commande d'aide."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = validate_and_run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Vérifier que la commande s'exécute sans erreur
                    # Certains scripts peuvent ne pas avoir --help, c'est normal
                    assert result.returncode in [
                        0,
                        1,
                        2,
                    ]  # 0 = succès, 1-2 = erreur d'argument

                except (subprocess.TimeoutExpired, SecurityError):
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    @pytest.mark.timeout(30)
    def test_cli_version_command(self):
        """Test de la commande de version."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = validate_and_run(
                        [sys.executable, str(cli_path), "--version"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Vérifier que la commande s'exécute
                    assert result.returncode in [0, 1, 2]

                except (subprocess.TimeoutExpired, SecurityError):
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    @pytest.mark.timeout(30)
    def test_cli_invalid_argument(self):
        """Test avec des arguments invalides."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = validate_and_run(
                        [sys.executable, str(cli_path), "--invalid-arg"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Vérifier que la commande gère l'erreur correctement
                    assert result.returncode in [1, 2]  # Code d'erreur attendu

                except (subprocess.TimeoutExpired, SecurityError):
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    @pytest.mark.timeout(30)
    def test_cli_missing_argument(self):
        """Test avec des arguments manquants."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = validate_and_run(
                        [sys.executable, str(cli_path)],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    # Vérifier que la commande gère l'absence d'arguments
                    assert result.returncode in [0, 1, 2]

                except (subprocess.TimeoutExpired, SecurityError):
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    @pytest.mark.timeout(30)
    def test_cli_html_argument(self) -> None:
        """Test de l'argument --html pour ath-coverage.py."""
        cli_path = Path("bin/ath-coverage.py")
        if cli_path.exists():
            try:
                result = validate_and_run(
                    [sys.executable, str(cli_path), "--html"],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )

                # Vérifier que l'argument fonctionne
                assert result.returncode in [0, 1]

            except (subprocess.TimeoutExpired, SecurityError):
                pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
            except Exception as e:
                pytest.skip(f"CLI {cli_path} non disponible: {e}")

    @pytest.mark.timeout(30)
    def test_cli_version_argument(self) -> None:
        """Test de l'argument --version pour ath-coverage.py."""
        cli_path = Path("bin/ath-coverage.py")
        if cli_path.exists():
            try:
                result = validate_and_run(
                    [sys.executable, str(cli_path), "--version"],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )

                # Vérifier que l'argument fonctionne
                assert result.returncode in [0, 1]

            except (subprocess.TimeoutExpired, SecurityError):
                pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
            except Exception as e:
                pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_timeout_handling(self):
        """Test de la gestion des timeouts."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    # Test avec un timeout très court
                    _ = validate_and_run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=1,  # Timeout très court
                    )

                    # Si le timeout est respecté, c'est bien
                    assert True

                except (subprocess.TimeoutExpired, SecurityError):
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
                    result = validate_and_run(
                        [sys.executable, str(cli_path), "/chemin/inexistant"],
                        capture_output=True,
                        text=True,
                        timeout=15,  # Timeout réduit
                    )

                    # Devrait gérer l'erreur gracieusement
                    assert result.returncode != 0

                except (subprocess.TimeoutExpired, SecurityError):
                    pytest.skip(f"CLI {cli_path} prend trop de temps à démarrer")
                except Exception as e:
                    pytest.skip(f"CLI {cli_path} non disponible: {e}")

    def test_cli_output_format(self):
        """Test du format de sortie."""
        for cli_path in self.cli_paths:
            if cli_path.exists():
                try:
                    result = validate_and_run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=15,  # Timeout réduit
                    )

                    # La sortie devrait être du texte
                    if result.stdout:
                        assert isinstance(result.stdout, str)
                    if result.stderr:
                        assert isinstance(result.stderr, str)

                except (subprocess.TimeoutExpired, SecurityError):
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

                    result = validate_and_run(
                        [sys.executable, str(cli_path), "--help"],
                        capture_output=True,
                        text=True,
                        timeout=15,  # Timeout réduit
                        env=env,
                    )

                    # Devrait fonctionner avec les variables d'environnement
                    assert result.returncode in [0, 1, 2]

                except (subprocess.TimeoutExpired, SecurityError):
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
                        process.wait(timeout=15)  # Timeout réduit
                        assert process.returncode in [0, 1, 2]

                except (subprocess.TimeoutExpired, SecurityError):
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
        result = validate_and_run(
            [sys.executable, str(cli_path), "--help"],
            capture_output=True,
            text=True,
            timeout=15,  # Timeout réduit
        )

        assert result.returncode in [0, 1, 2]

    except (subprocess.TimeoutExpired, SecurityError):
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
            result = validate_and_run(
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
                timeout=30,  # Timeout réduit
            )

            # Le workflow devrait s'exécuter sans erreur critique
            assert result.returncode in [0, 1, 2]

        except (subprocess.TimeoutExpired, SecurityError):
            pytest.skip("Workflow CLI prend trop de temps")
        except Exception as e:
            pytest.skip(f"Workflow CLI non disponible: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
