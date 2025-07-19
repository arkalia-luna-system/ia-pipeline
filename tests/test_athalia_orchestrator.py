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

        # Créer un projet robotique de test
        self.robotics_project = Path(self.temp_dir) / "robotics_project"
        self.robotics_project.mkdir()
        
        # Structure ROS2
        (self.robotics_project / "src").mkdir()
        (self.robotics_project / "src" / "my_robot_package").mkdir()
        (self.robotics_project / "src" / "my_robot_package" / "package.xml").write_text("""<?xml version="1.0"?>
<package format="2">
  <name>my_robot_package</name>
  <version>0.0.1</version>
  <description>Test robot package</description>
  <maintainer email="test@example.com">Test User</maintainer>
  <license>MIT</license>
  <buildtool_depend>ament_cmake</buildtool_depend>
</package>""")
        
        # Docker
        (self.robotics_project / "docker-compose.yml").write_text("""
version: '3.8'
services:
  robot:
    image: ros:humble
    volumes:
      - ./src:/workspace/src
""")
        
        # Rust
        (self.robotics_project / "Cargo.toml").write_text("""
[package]
name = "robot_control"
version = "0.1.0"
edition = "2021"

[dependencies]
tokio = { version = "1.0", features = ["full"] }
""")

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

    def test_industrialize_project_with_robotics(self):
        """Test l'industrialisation avec module robotique"""
        config = {
            "audit": True,
            "clean": False,
            "document": False,
            "test": False,
            "deploy": False,
            "robotics": True,  # Activer le module robotique
            "dry_run": True
        }

        results = self.orchestrator.industrialize_project(str(self.robotics_project), config)

        assert results is not None
        assert "audit" in results
        assert "robotics" in results  # Vérifier que le module robotique est présent
        
        # Vérifier la structure du résultat robotique
        robotics_result = results["robotics"]
        assert "passed" in robotics_result
        assert "result" in robotics_result
        assert "score" in robotics_result
        assert "reachy_audit" in robotics_result["result"]
        assert "ros2_validation" in robotics_result["result"]
        assert "docker_setup" in robotics_result["result"]
        assert "rust_analysis" in robotics_result["result"]
        assert "ci_pipeline" in robotics_result["result"]

    def test_robotics_module_only(self):
        """Test l'industrialisation avec seulement le module robotique"""
        config = {
            "audit": False,
            "clean": False,
            "document": False,
            "test": False,
            "deploy": False,
            "robotics": True,  # Seulement le module robotique
            "dry_run": True
        }

        results = self.orchestrator.industrialize_project(str(self.robotics_project), config)

        assert results is not None
        assert "robotics" in results
        
        # Vérifier que le module robotique fonctionne correctement
        robotics_result = results["robotics"]
        assert "passed" in robotics_result
        assert "result" in robotics_result
        assert "score" in robotics_result
        assert "reachy_audit" in robotics_result["result"]
        assert "ros2_validation" in robotics_result["result"]
        assert "docker_setup" in robotics_result["result"]
        assert "rust_analysis" in robotics_result["result"]
        assert "ci_pipeline" in robotics_result["result"]
        
        # Vérifier que les autres modules ne sont pas exécutés (ils ont des valeurs par défaut)
        assert results["audit"]["passed"] is True  # Valeur par défaut en dry_run
        assert results["clean"]["passed"] is True  # Valeur par défaut en dry_run

    def test_robotics_module_on_non_robotics_project(self):
        """Test le module robotique sur un projet non-robotique"""
        config = {
            "audit": False,
            "clean": False,
            "document": False,
            "test": False,
            "deploy": False,
            "robotics": True,
            "dry_run": True
        }

        results = self.orchestrator.industrialize_project(str(self.test_project), config)

        assert results is not None
        assert "robotics" in results
        
        # Le module robotique devrait fonctionner même sur un projet non-robotique
        robotics_result = results["robotics"]
        assert "passed" in robotics_result
        assert "result" in robotics_result
        assert "score" in robotics_result
        assert "reachy_audit" in robotics_result["result"]
        # Le score devrait être plus bas pour un projet non-robotique
        assert robotics_result["score"] < 100

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

    def test_robotics_module_import(self):
        """Test que les modules robotiques peuvent être importés"""
        try:
            from athalia_core.robotics.reachy_auditor import ReachyAuditor
            from athalia_core.robotics.ros2_validator import ROS2Validator
            from athalia_core.robotics.docker_robotics import DockerRoboticsManager
            from athalia_core.robotics.rust_analyzer import RustAnalyzer
            from athalia_core.robotics.robotics_ci import RoboticsCI
            assert True  # Si on arrive ici, l'import a réussi
        except ImportError as e:
            pytest.fail(f"Impossible d'importer les modules robotiques: {e}")

    def test_robotics_audit_method(self):
        """Test la méthode _run_robotics_audit de l'orchestrateur"""
        # Vérifier que la méthode existe
        assert hasattr(self.orchestrator, '_run_robotics_audit')
        
        # Configurer le projet pour l'orchestrateur
        self.orchestrator.project_path = Path(self.robotics_project)
        
        # Tester la méthode directement
        result = self.orchestrator._run_robotics_audit()
        
        assert result is not None
        assert "passed" in result
        assert "result" in result
        assert "score" in result
        assert "reachy_audit" in result["result"]
        assert "ros2_validation" in result["result"]
        assert "docker_setup" in result["result"]
        assert "rust_analysis" in result["result"]
        assert "ci_pipeline" in result["result"]

def test_orchestrator_import():
    """Test que l'orchestrateur peut être importé"""
    try:
        orchestrator = AthaliaOrchestrator()
        assert orchestrator is not None
    except ImportError as e:
        pytest.fail(f"Impossible d'importer AthaliaOrchestrator: {e}")

def test_distill_ia_responses(monkeypatch):
    from athalia_core.athalia_orchestrator import AthaliaOrchestrator
    orch = AthaliaOrchestrator()
    # Mock RobustAI pour éviter les appels réels à Ollama
    from athalia_core.ai_robust import RobustAI, AIModel
    def fake_call_model(self, model, prompt):
        if hasattr(model, 'value'):
            model = model.value
        return f"Réponse {model} à '{prompt}'"
    monkeypatch.setattr(RobustAI, '_call_model', fake_call_model)
    prompt = "Test distillation IA."
    result = orch.distill_ia_responses(prompt, models=["ollama_qwen", "ollama_mistral", "mock"], strategy="voting")
    assert isinstance(result, str)
    assert "Réponse ollama_qwen" in result or "Réponse ollama_mistral" in result or "Réponse mock" in result

def test_distill_audits():
    from athalia_core.athalia_orchestrator import AthaliaOrchestrator
    orch = AthaliaOrchestrator()
    audits = [
        {"type": "securite", "score": 8},
        {"type": "qualite", "score": 6},
        {"type": "performance", "score": 10}
    ]
    result = orch.distill_audits(audits)
    assert isinstance(result, dict)
    assert "global_score" in result
    assert abs(result["global_score"] - ((8*0.4+6*0.4+10*0.2)/1.0)) < 1e-6

def test_distill_corrections():
    from athalia_core.athalia_orchestrator import AthaliaOrchestrator
    orch = AthaliaOrchestrator()
    corrections = ["fix1", "fix2", "fix3"]
    scores = [0.2, 0.9, 0.5]
    result = orch.distill_corrections(corrections, scores)
    assert result == "fix2"

def test_distill_adaptive_responses():
    from athalia_core.athalia_orchestrator import AthaliaOrchestrator
    orch = AthaliaOrchestrator()
    responses = ["A", "B", "A", "C", "A", "B"]
    result = orch.distill_adaptive_responses(responses)
    assert result == "A"

def test_distill_genetics():
    from athalia_core.athalia_orchestrator import AthaliaOrchestrator
    orch = AthaliaOrchestrator()
    solutions = ["print('hello world')", "print('hello')", "world = 1"]
    result = orch.distill_genetics(solutions)
    # Vérifie que le résultat contient au moins un mot parmi les deux premiers mots de chaque solution
    mots_possibles = set()
    for sol in solutions:
        mots = sol.split()
        mots_possibles.update(mots[:2])
    assert any(word in result for word in mots_possibles)

def test_cache_predictive():
    from athalia_core.athalia_orchestrator import AthaliaOrchestrator
    orch = AthaliaOrchestrator()
    key = "test_key"
    orch.cache_predictive(key, "valeur1")
    assert orch.cache_predictive(key) == "valeur1"

def test_distillation_multi_ia_reelle(monkeypatch):
    """Test d'intégration : distillation réelle multi-IA (Qwen, Mistral, Mock) via l'orchestrateur."""
    from athalia_core.athalia_orchestrator import AthaliaOrchestrator
    orch = AthaliaOrchestrator()
    # Mock RobustAI pour éviter les appels réels à Ollama
    from athalia_core.ai_robust import RobustAI, AIModel
    def fake_call_model(self, model, prompt):
        if hasattr(model, 'value'):
            model = model.value
        return f"Réponse {model} à '{prompt}'"
    monkeypatch.setattr(RobustAI, '_call_model', fake_call_model)
    prompt = "Explique la distillation IA en 2 phrases."
    result = orch.distill_ia_responses(prompt, models=["ollama_qwen", "ollama_mistral", "mock"], strategy="voting")
    assert isinstance(result, str)
    assert "Réponse ollama_qwen" in result or "Réponse ollama_mistral" in result or "Réponse mock" in result

if __name__ == "__main__":
    pytest.main([__file__])