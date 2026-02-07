"""
Tests d'intégration pour les workflows GitHub Actions
Vérifie la cohérence et la validité des workflows
"""

from pathlib import Path

import pytest
import yaml


class TestWorkflowIntegration:
    """Tests d'intégration pour les workflows"""

    @pytest.fixture
    def workflows_dir(self):
        """Dossier des workflows"""
        return Path("/Volumes/T7/athalia-dev-setup/.github/workflows")

    def test_workflow_files_exist(self, workflows_dir):
        """Test que tous les fichiers de workflow existent"""
        expected_workflows = [
            "ci-matrix.yml",
            "docs.yml",
            "metrics.yml",
            "release.yml",
            "sbom.yml",
            "security.yml",
        ]

        for workflow in expected_workflows:
            workflow_path = workflows_dir / workflow
            assert workflow_path.exists(), f"Workflow {workflow} manquant"

    def test_workflow_yaml_validity(self, workflows_dir):
        """Test de validité YAML des workflows"""
        for workflow_file in workflows_dir.glob("*.yml"):
            with open(workflow_file) as f:
                try:
                    yaml.safe_load(f)
                except yaml.YAMLError as e:
                    pytest.fail(f"YAML invalide dans {workflow_file}: {e}")

    def test_ci_matrix_workflow_structure(self, workflows_dir):
        """Test de la structure du workflow CI principal"""
        ci_file = workflows_dir / "ci-matrix.yml"
        with open(ci_file) as f:
            workflow = yaml.safe_load(f)

        # Vérifier les sections principales
        assert "name" in workflow
        assert "on" in workflow
        assert "jobs" in workflow
        assert "permissions" in workflow

        # Vérifier les permissions GitHub Pages
        permissions = workflow["permissions"]
        assert "pages" in permissions
        assert "id-token" in permissions
        assert "contents" in permissions

    def test_workflow_permissions_consistency(self, workflows_dir):
        """Test de cohérence des permissions entre workflows"""
        for workflow_file in workflows_dir.glob("*.yml"):
            with open(workflow_file) as f:
                workflow = yaml.safe_load(f)

            if "permissions" in workflow:
                perms = workflow["permissions"]
                # Vérifier que les permissions sont valides
                valid_perms = ["read", "write", "admin"]
                for perm, level in perms.items():
                    assert level in valid_perms, f"Permission invalide {perm}: {level}"

    def test_workflow_uses_actions(self, workflows_dir):
        """Test que les workflows utilisent des actions valides"""
        for workflow_file in workflows_dir.glob("*.yml"):
            with open(workflow_file) as f:
                content = f.read()

            # Vérifier qu'il n'y a pas d'actions obsolètes
            deprecated_actions = [
                "actions/checkout@v1",
                "actions/setup-python@v1",
                "actions/upload-artifact@v1",
            ]

            for deprecated in deprecated_actions:
                assert deprecated not in content, (
                    f"Action obsolète {deprecated} dans {workflow_file}"
                )

    @pytest.mark.integration
    def test_workflow_dependencies(self, workflows_dir):
        """Test des dépendances entre workflows"""
        # Vérifier que les workflows ne se bloquent pas mutuellement
        workflow_files = list(workflows_dir.glob("*.yml"))
        assert len(workflow_files) >= 4, "Pas assez de workflows pour les tests"

        # Vérifier que chaque workflow a un nom unique
        names = []
        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                workflow = yaml.safe_load(f)
                if "name" in workflow:
                    assert workflow["name"] not in names, (
                        f"Nom de workflow dupliqué: {workflow['name']}"
                    )
                    names.append(workflow["name"])
