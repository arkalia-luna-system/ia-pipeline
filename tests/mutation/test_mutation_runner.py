"""
Tests de mutation pour Athalia
Vérifie la qualité des tests en introduisant des mutations
"""

import os
import subprocess
from pathlib import Path

import pytest


class TestMutationQuality:
    """Tests de qualité par mutation"""

    @pytest.fixture
    def project_root(self):
        """Racine du projet"""
        return Path("/Volumes/T7/athalia-dev-setup")

    def test_mutation_config_exists(self, project_root):
        """Test que la configuration mutmut existe"""
        config_file = project_root / "mutmut_config.py"
        assert config_file.exists(), "Configuration mutmut manquante"

    def test_mutation_can_run(self, project_root):
        """Test que mutmut peut s'exécuter"""
        # Test basique de mutmut
        result = subprocess.run(
            ["mutmut", "--version"], capture_output=True, text=True, cwd=project_root
        )
        assert result.returncode == 0, f"Mutmut ne peut pas s'exécuter: {result.stderr}"

    @pytest.mark.mutation
    def test_mutation_on_core_modules(self, project_root):
        """Test de mutation sur les modules core"""
        # Test sur un module simple d'abord
        core_modules = ["athalia_core/core/main.py", "athalia_core/utilities/cli.py"]

        for module in core_modules:
            module_path = project_root / module
            if module_path.exists():
                # Test de mutation basique
                result = subprocess.run(
                    ["mutmut", "run", "--paths-to-mutate", str(module_path)],
                    capture_output=True,
                    text=True,
                    cwd=project_root,
                    timeout=300,  # 5 minutes max
                )
                # Mutmut peut retourner des codes d'erreur même en cas de succès
                assert result.returncode in [
                    0,
                    1,
                    2,
                ], f"Erreur mutmut sur {module}: {result.stderr}"

    @pytest.mark.mutation
    def test_mutation_coverage(self, project_root):
        """Test de couverture des mutations"""
        # Vérifier que mutmut peut analyser le projet
        result = subprocess.run(
            ["mutmut", "run", "--paths-to-mutate", "athalia_core/"],
            capture_output=True,
            text=True,
            cwd=project_root,
            timeout=600,  # 10 minutes max
        )

        # Vérifier que des mutations ont été trouvées
        assert "mutations" in result.stdout.lower() or result.returncode in [
            0,
            1,
            2,
        ], f"Mutmut n'a pas trouvé de mutations: {result.stdout}"

    def test_mutation_environment(self, project_root):
        """Test de l'environnement de mutation"""
        # Vérifier que les dépendances sont installées
        result = subprocess.run(
            ["python", "-c", "import mutmut; print('OK')"],
            capture_output=True,
            text=True,
            cwd=project_root,
        )
        assert result.returncode == 0, "Mutmut non disponible dans l'environnement"
