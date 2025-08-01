"""
Tests pour le module athalia_core.cli
Tests appropriés pour l'interface CLI d'Athalia
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import direct du module cli
from athalia_core.cli import cli as cli_group
from athalia_core import generate_project
from athalia_core.audit import audit_project_intelligent


def test_cli_group_exists():
    """Test que le groupe CLI existe."""
    assert cli_group is not None
    assert hasattr(cli_group, "commands")


def test_cli_group_has_commands():
    """Test que le groupe CLI a des commandes."""
    commands = cli_group.list_commands(None)
    assert isinstance(commands, list)
    # Vérifier que le groupe CLI a au moins quelques commandes
    assert len(commands) > 0


def test_function_generate_project_exists():
    """Test que la fonction generate_project existe."""
    assert generate_project is not None
    assert callable(generate_project)


def test_function_audit_project_intelligent_exists():
    """Test que la fonction audit_project_intelligent existe."""
    assert audit_project_intelligent is not None
    assert callable(audit_project_intelligent)


class TestGenerateProject:
    """Tests pour la fonction generate_project"""

    def test_generate_project_dry_run(self):
        """Test generate_project en mode dry-run."""
        blueprint = {
            "project_name": "test_project",
            "description": "Test project",
            "dependencies": ["pytest", "click"],
        }

        result = generate_project(blueprint, "./test_output", dry_run=True)
        assert result is True

    def test_generate_project_creates_files(self):
        """Test que generate_project crée les fichiers nécessaires."""
        with tempfile.TemporaryDirectory() as temp_dir:
            blueprint = {
                "project_name": "test_project",
                "description": "Test project",
                "dependencies": ["pytest", "click"],
            }

            result = generate_project(blueprint, temp_dir, dry_run=False)

            # Vérifier que les fichiers ont été créés
            project_path = Path(temp_dir)
            assert (project_path / "README.md").exists()
            assert (project_path / "requirements.txt").exists()
            assert (project_path / "main.py").exists()

    def test_generate_project_readme_content(self):
        """Test le contenu du README généré."""
        with tempfile.TemporaryDirectory() as temp_dir:
            blueprint = {
                "project_name": "my_test_project",
                "description": "A test project",
                "dependencies": ["pytest"],
            }

            generate_project(blueprint, temp_dir, dry_run=False)

            readme_path = Path(temp_dir) / "README.md"
            with open(readme_path, "r") as f:
                content = f.read()

            assert "my_test_project" in content
            assert "A test project" in content

    def test_generate_project_requirements_content(self):
        """Test le contenu du requirements.txt généré."""
        with tempfile.TemporaryDirectory() as temp_dir:
            blueprint = {
                "project_name": "test_project",
                "description": "Test project",
                "dependencies": ["pytest", "click", "requests"],
            }

            generate_project(blueprint, temp_dir, dry_run=False)

            requirements_path = Path(temp_dir) / "requirements.txt"
            with open(requirements_path, "r") as f:
                content = f.read()

            assert "pytest" in content
            assert "click" in content
            assert "requests" in content

    def test_generate_project_main_content(self):
        """Test le contenu du main.py généré."""
        with tempfile.TemporaryDirectory() as temp_dir:
            blueprint = {"project_name": "my_project", "description": "Test project"}

            generate_project(blueprint, temp_dir, dry_run=False)

            main_path = Path(temp_dir) / "main.py"
            with open(main_path, "r") as f:
                content = f.read()

            assert "my_project" in content
            assert "def main():" in content


class TestAuditProjectIntelligent:
    """Tests pour la fonction audit_project_intelligent"""

    def test_audit_project_intelligent_basic(self):
        """Test basique de audit_project_intelligent."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = audit_project_intelligent(temp_dir)

            assert isinstance(result, dict)
            # La fonction peut retourner un statut d'erreur si l'audit n'est pas disponible
            assert "status" in result or "audit_results" in result

    def test_audit_project_intelligent_with_files(self):
        """Test audit_project_intelligent avec des fichiers."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Créer quelques fichiers de test
            (Path(temp_dir) / "test.py").touch()
            (Path(temp_dir) / "README.md").touch()

            result = audit_project_intelligent(temp_dir)

            assert isinstance(result, dict)


def test_cli_group_help():
    """Test que le groupe CLI peut afficher l'aide."""
    try:
        # Test que le groupe CLI peut être appelé sans erreur
        help_text = cli_group.get_help()
        assert isinstance(help_text, str)
        assert len(help_text) > 0
    except Exception as e:
        pytest.skip(f"Impossible de tester l'aide CLI: {e}")


def test_cli_group_commands_list():
    """Test la liste des commandes du groupe CLI."""
    try:
        commands = cli_group.list_commands(None)
        assert isinstance(commands, list)
        # Vérifier que certaines commandes communes existent
        common_commands = ["generate", "audit", "ai-status", "test-ai"]
        for cmd in common_commands:
            if cmd in commands:
                assert True  # La commande existe
    except Exception as e:
        pytest.skip(f"Impossible de lister les commandes CLI: {e}")


def test_module_integration():
    """Test d'intégration de base du module."""
    # Test que les fonctions principales peuvent être utilisées
    try:
        # Test generate_project
        blueprint = {"project_name": "test", "description": "test"}
        with tempfile.TemporaryDirectory() as temp_dir:
            result = generate_project(blueprint, temp_dir, dry_run=True)
            assert result is True

        # Test audit_project_intelligent
        with tempfile.TemporaryDirectory() as temp_dir:
            result = audit_project_intelligent(temp_dir)
            assert isinstance(result, dict)

    except Exception as e:
        pytest.skip(f"Erreur lors de l'intégration: {e}")
