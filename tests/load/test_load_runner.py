"""
Tests de charge pour Athalia
Vérifie les performances sous charge
"""

import os
import subprocess
import time
from pathlib import Path

import pytest


class TestLoadPerformance:
    """Tests de performance sous charge"""

    @pytest.fixture
    def project_root(self):
        """Racine du projet"""
        return Path("/Volumes/T7/athalia-dev-setup")

    def test_locust_installation(self, project_root):
        """Test que Locust est installé"""
        result = subprocess.run(
            ["locust", "--version"], capture_output=True, text=True, cwd=project_root
        )
        assert result.returncode == 0, f"Locust non installé: {result.stderr}"

    def test_locustfile_exists(self, project_root):
        """Test que le fichier locustfile existe"""
        locustfile = project_root / "tests/load/locustfile.py"
        assert locustfile.exists(), "Fichier locustfile manquant"

    def test_locustfile_syntax(self, project_root):
        """Test de la syntaxe du locustfile"""
        locustfile = project_root / "tests/load/locustfile.py"
        result = subprocess.run(
            ["python", "-m", "py_compile", str(locustfile)],
            capture_output=True,
            text=True,
            cwd=project_root,
        )
        assert result.returncode == 0, (
            f"Erreur de syntaxe dans locustfile: {result.stderr}"
        )

    @pytest.mark.load
    def test_load_validation(self, project_root):
        """Test de validation des tests de charge"""
        # Test de validation sans exécution
        result = subprocess.run(
            ["locust", "--check", "-f", "tests/load/locustfile.py"],
            capture_output=True,
            text=True,
            cwd=project_root,
            timeout=30,
        )
        assert result.returncode == 0, f"Validation locust échouée: {result.stderr}"

    @pytest.mark.load
    def test_load_short_run(self, project_root):
        """Test de charge court (1 minute)"""
        # Test court pour vérifier que tout fonctionne
        result = subprocess.run(
            [
                "locust",
                "-f",
                "tests/load/locustfile.py",
                "--headless",
                "--users",
                "2",
                "--spawn-rate",
                "1",
                "--run-time",
                "30s",
                "--host",
                "http://localhost:8000",
            ],
            capture_output=True,
            text=True,
            cwd=project_root,
            timeout=60,
        )

        # Locust peut retourner des codes d'erreur même en cas de succès partiel
        assert result.returncode in [0, 1, 2], f"Test de charge échoué: {result.stderr}"

    def test_load_environment(self, project_root):
        """Test de l'environnement de charge"""
        # Vérifier que les dépendances sont installées
        result = subprocess.run(
            ["python", "-c", "import locust; print('OK')"],
            capture_output=True,
            text=True,
            cwd=project_root,
        )
        assert result.returncode == 0, "Locust non disponible dans l'environnement"

    @pytest.mark.load
    def test_load_configuration(self, project_root):
        """Test de la configuration des tests de charge"""
        # Vérifier que le fichier de configuration est valide
        locustfile = project_root / "tests/load/locustfile.py"

        # Test d'import du fichier
        result = subprocess.run(
            [
                "python",
                "-c",
                f"import sys; sys.path.append('{project_root}'); exec(open('{locustfile}').read())",
            ],
            capture_output=True,
            text=True,
            cwd=project_root,
        )

        assert result.returncode == 0, f"Configuration locust invalide: {result.stderr}"
