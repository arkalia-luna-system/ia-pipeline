#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from athalia_core.athalia_orchestrator import AthaliaOrchestrator
from pathlib import Path
import os
import sys
import pytest
import shutil
import tempfile

"""
Tests pour l'orchestrateur Athalia
"""

# Ajouter le répertoire athalia_core au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'athalia_core'))


class TestAthaliaOrchestrator:
    """Tests pour l'orchestrateur principal"""

    def setup_method(self):
        """Setup pour chaque test"""
        self.orchestrator = AthaliaOrchestrator()
        self.temp_dir = tempfile.mkdtemp()

        # Créer un projet de test simple
        self.test_project = Path(self.temp_dir) / "projet_test"
        self.test_project.mkdir()

        # Créer quelques fichiers de test
        (self.test_project / "main.py").write_text("""
def main():
    print("Hello world")

if __name__ == "__main__":
    main()
""")

        (self.test_project / "requirements.txt").write_text("pytest\n")

        (self.test_project / "README.md").write_text("# Test Project\n\nA simple test project.")

    def teardown_method(self):
        """Cleanup après chaque test"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_orchestrator_initialization(self):
        """Test l'initialisation de l'orchestrateur"""
        assert self.orchestrator is not None
        assert hasattr(self.orchestrator, 'industrialize_project')
        assert hasattr(self.orchestrator, 'scan_projects')

    def test_industrialize_project_audit_only(self):
        """Test l'industrialisation avec audit seulement"""
        config = {
            "audit": True,
            "clean": False,
            "document": False,
            "test": False,
            "deploy": False,
            "dry_run": True
        }

        results = self.orchestrator.industrialize_project(str(self.test_project), config)

        assert results is not None
        assert "audit" in results
        assert "status" in results["audit"]
        assert results["audit"]["status"]["success"] is True
        assert "issues" in results["audit"]["status"]["details"]

    def test_industrialize_project_documentation_only(self):
        """Test l'industrialisation avec documentation seulement"""
        config = {
            "audit": False,
            "clean": False,
            "document": True,
            "test": False,
            "deploy": False,
            "dry_run": True
        }

        results = self.orchestrator.industrialize_project(str(self.test_project), config)

        assert results is not None
        assert "document" in results
        assert "status" in results["document"]
        assert results["document"]["status"]["success"] is True
        assert "files" in results["document"]

    def test_industrialize_project_complete(self):
        """Test l'industrialisation complète en mode simulation"""
        config = {
            "audit": True,
            "clean": True,
            "document": True,
            "test": True,
            "deploy": True,
            "dry_run": True
        }

        results = self.orchestrator.industrialize_project(str(self.test_project), config)

        assert results is not None
        assert "audit" in results
        assert "clean" in results

        # Vérifier que toutes les étapes sont présentes
        expected_steps = ["audit", "clean", "document", "test", "deploy"]
        for step in expected_steps:
            assert step in results

    def test_scan_projects(self):
        """Test le scan de projets"""
        # Créer quelques projets de test
        project1 = Path(self.temp_dir) / "projet1"
        project1.mkdir()
        (project1 / "main.py").write_text("print('Hello')")

        project2 = Path(self.temp_dir) / "projet2"
        project2.mkdir()
        (project2 / "package.json").write_text('{"name": "test"}')

        projects = self.orchestrator.scan_projects(self.temp_dir)

        assert isinstance(projects, list)
        assert len(projects) >= 2  # Au moins nos 2 projets de test

        # Vérifier la structure des projets détectés
        for project in projects:
            assert "name" in project
            assert "path" in project
            assert "type" in project
            assert "files" in project

    def test_invalid_project_path(self):
        """Test avec un chemin de projet invalide"""
        invalid_path = "/chemin/inexistant/projet"

        with pytest.raises(Exception):
            self.orchestrator.industrialize_project(invalid_path)

    def test_empty_project(self):
        """Test avec un projet vide"""
        empty_project = Path(self.temp_dir) / "projet_vide"
        empty_project.mkdir()

        config = {
            "audit": True,
            "clean": False,
            "document": False,
            "test": False,
            "deploy": False,
            "dry_run": True
        }

        results = self.orchestrator.industrialize_project(str(empty_project), config)

        assert results is not None
        assert "audit" in results
        assert "status" in results["audit"]
        # L'audit devrait fonctionner même sur un projet vide
        assert results["audit"]["status"]["success"] is True

def test_orchestrator_import():
    """Test que l'orchestrateur peut être importé"""
    try:
        orchestrator = AthaliaOrchestrator()
        assert orchestrator is not None
    except ImportError as e:
        pytest.fail(f"Impossible d'importer AthaliaOrchestrator: {e}")

if __name__ == "__main__":
    pytest.main([__file__])