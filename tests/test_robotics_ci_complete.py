#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests complets pour le module robotics_ci.
Tests professionnels pour la CI/CD.
"""

import subprocess
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from athalia_core.robotics_ci import RoboticsCI, run_robotics_ci


class TestRoboticsCI:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.ci = RoboticsCI(project_path=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_project_path(self):
        """Test de l'initialisation avec project_path"""
        assert self.ci.project_path == Path(self.temp_dir)
        assert hasattr(self.ci, "ci_results")
        assert "build_status" in self.ci.ci_results
        assert "test_status" in self.ci.ci_results
        assert "lint_status" in self.ci.ci_results
        assert "security_status" in self.ci.ci_results
        assert "deployment_status" in self.ci.ci_results

    def test_check_project_structure_ros2(self):
        """Test de vérification de structure ROS2"""
        # Créer un projet ROS2
        package_xml = Path(self.temp_dir) / "package.xml"
        with open(package_xml, "w") as f:
            f.write("<package><name>test_package</name></package>")

        setup_py = Path(self.temp_dir) / "setup.py"
        with open(setup_py, "w") as f:
            f.write("from setuptools import setup\nsetup()")

        cmake_lists = Path(self.temp_dir) / "CMakeLists.txt"
        with open(cmake_lists, "w") as f:
            f.write("cmake_minimum_required(VERSION 3.8)\nproject(test_package)")

        self.ci._check_project_structure()
        assert self.ci.ci_results["build_status"] == "unknown"

    def test_check_project_structure_rust(self):
        """Test de vérification de structure Rust"""
        # Créer un projet Rust
        cargo_toml = Path(self.temp_dir) / "Cargo.toml"
        with open(cargo_toml, "w") as f:
            f.write('[package]\nname = "test_project"')

        src_dir = Path(self.temp_dir) / "src"
        src_dir.mkdir()

        self.ci._check_project_structure()
        assert self.ci.ci_results["build_status"] == "unknown"

    def test_check_project_structure_missing_files(self):
        """Test de vérification avec fichiers manquants"""
        self.ci._check_project_structure()
        assert len(self.ci.ci_results["errors"]) > 0

    @patch("subprocess.run")
    def test_run_build_rust_success(self, mock_run):
        """Test de build Rust réussi"""
        # Créer Cargo.toml
        cargo_toml = Path(self.temp_dir) / "Cargo.toml"
        with open(cargo_toml, "w") as f:
            f.write('[package]\nname = "test_project"')

        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        self.ci._run_build()
        assert self.ci.ci_results["build_status"] == "success"

    @patch("subprocess.run")
    def test_run_build_rust_failure(self, mock_run):
        """Test de build Rust échoué"""
        cargo_toml = Path(self.temp_dir) / "Cargo.toml"
        with open(cargo_toml, "w") as f:
            f.write('[package]\nname = "test_project"')

        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = "Build failed"

        self.ci._run_build()
        assert self.ci.ci_results["build_status"] == "failed"
        assert len(self.ci.ci_results["errors"]) > 0

    @patch("subprocess.run")
    def test_run_build_ros2_success(self, mock_run):
        """Test de build ROS2 réussi"""
        package_xml = Path(self.temp_dir) / "package.xml"
        with open(package_xml, "w") as f:
            f.write("<package><name>test_package</name></package>")

        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        self.ci._run_build()
        assert self.ci.ci_results["build_status"] == "success"

    @patch("subprocess.run")
    def test_run_build_python_success(self, mock_run):
        """Test de build Python réussi"""
        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        self.ci._run_build()
        assert self.ci.ci_results["build_status"] == "success"

    @patch("subprocess.run")
    def test_run_tests_rust_success(self, mock_run):
        """Test de tests Rust réussi"""
        cargo_toml = Path(self.temp_dir) / "Cargo.toml"
        with open(cargo_toml, "w") as f:
            f.write('[package]\nname = "test_project"')

        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        self.ci._run_tests()
        assert self.ci.ci_results["test_status"] == "success"

    @patch("subprocess.run")
    def test_run_tests_ros2_success(self, mock_run):
        """Test de tests ROS2 réussi"""
        package_xml = Path(self.temp_dir) / "package.xml"
        with open(package_xml, "w") as f:
            f.write("<package><name>test_package</name></package>")

        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        self.ci._run_tests()
        assert self.ci.ci_results["test_status"] == "success"

    @patch("subprocess.run")
    def test_run_linting_rust_success(self, mock_run):
        """Test de linting Rust réussi"""
        cargo_toml = Path(self.temp_dir) / "Cargo.toml"
        with open(cargo_toml, "w") as f:
            f.write('[package]\nname = "test_project"')

        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        self.ci._run_linting()
        assert self.ci.ci_results["lint_status"] == "success"

    @patch("subprocess.run")
    def test_run_linting_python_success(self, mock_run):
        """Test de linting Python réussi"""
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = ""

        self.ci._run_linting()
        assert self.ci.ci_results["lint_status"] == "success"

    @patch("subprocess.run")
    def test_run_security_scan_rust_success(self, mock_run):
        """Test de scan sécurité Rust réussi"""
        cargo_toml = Path(self.temp_dir) / "Cargo.toml"
        with open(cargo_toml, "w") as f:
            f.write('[package]\nname = "test_project"')

        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""

        self.ci._run_security_scan()
        assert self.ci.ci_results["security_status"] == "success"

    @patch("subprocess.run")
    def test_run_security_scan_python_success(self, mock_run):
        """Test de scan sécurité Python réussi"""
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = ""

        self.ci._run_security_scan()
        assert self.ci.ci_results["security_status"] == "success"

    def test_run_deployment_check_with_configs(self):
        """Test de vérification déploiement avec fichiers de config"""
        dockerfile = Path(self.temp_dir) / "Dockerfile"
        with open(dockerfile, "w") as f:
            f.write("FROM python:3.9")

        self.ci._run_deployment_check()
        assert self.ci.ci_results["deployment_status"] == "ready"
        assert "config_files" in self.ci.ci_results["metrics"]

    def test_run_deployment_check_without_configs(self):
        """Test de vérification déploiement sans fichiers de config"""
        self.ci._run_deployment_check()
        assert self.ci.ci_results["deployment_status"] == "not_ready"
        assert len(self.ci.ci_results["warnings"]) > 0

    def test_calculate_ci_score_perfect(self):
        """Test de calcul de score CI parfait"""
        self.ci.ci_results["build_status"] = "success"
        self.ci.ci_results["test_status"] = "success"
        self.ci.ci_results["lint_status"] = "success"
        self.ci.ci_results["security_status"] = "success"

        self.ci._calculate_ci_score()
        assert self.ci.ci_results["metrics"]["ci_score"] == 100

    def test_calculate_ci_score_with_failures(self):
        """Test de calcul de score CI avec échecs"""
        self.ci.ci_results["build_status"] = "failed"
        self.ci.ci_results["test_status"] = "failed"
        self.ci.ci_results["lint_status"] = "success"
        self.ci.ci_results["security_status"] = "success"
        self.ci.ci_results["errors"] = ["Error 1", "Error 2"]

        self.ci._calculate_ci_score()
        score = self.ci.ci_results["metrics"]["ci_score"]
        assert score < 100
        assert score >= 0

    def test_generate_ci_report(self):
        """Test de génération du rapport CI"""
        self.ci.ci_results["build_status"] = "success"
        self.ci.ci_results["test_status"] = "success"
        self.ci.ci_results["metrics"]["ci_score"] = 95

        report = self.ci.generate_ci_report()
        assert isinstance(report, str)
        assert "Rapport CI/CD Robotics" in report
        assert "success" in report
        assert "95" in report

    @patch("subprocess.run")
    def test_run_full_pipeline(self, mock_run):
        """Test du pipeline complet"""
        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""
        mock_run.return_value.stdout = ""

        result = self.ci.run_full_pipeline()
        assert isinstance(result, dict)
        assert "build_status" in result
        assert "test_status" in result
        assert "lint_status" in result
        assert "security_status" in result
        assert "deployment_status" in result

    def test_error_handling_timeout(self):
        """Test de gestion des timeouts"""
        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired("cmd", 60)):
            self.ci._run_build()
            assert self.ci.ci_results["build_status"] == "failed"
            assert len(self.ci.ci_results["errors"]) > 0

    def test_error_handling_exception(self):
        """Test de gestion des exceptions"""
        with patch("subprocess.run", side_effect=Exception("Test error")):
            self.ci._run_build()
            assert self.ci.ci_results["build_status"] == "failed"
            assert len(self.ci.ci_results["errors"]) > 0


class TestRoboticsCIIntegration:
    """Tests d'intégration pour RoboticsCI"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    @patch("subprocess.run")
    def test_full_ci_workflow(self, mock_run):
        """Test du workflow CI complet"""
        # Créer un projet Rust simple
        cargo_toml = Path(self.temp_dir) / "Cargo.toml"
        with open(cargo_toml, "w") as f:
            f.write('[package]\nname = "test_project"')

        src_dir = Path(self.temp_dir) / "src"
        src_dir.mkdir()

        main_rs = src_dir / "main.rs"
        with open(main_rs, "w") as f:
            f.write('fn main() { println!("Hello, world!"); }')

        # Mock tous les appels subprocess
        mock_run.return_value.returncode = 0
        mock_run.return_value.stderr = ""
        mock_run.return_value.stdout = ""

        ci = RoboticsCI(project_path=self.temp_dir)
        result = ci.run_full_pipeline()

        assert "build_status" in result
        assert "test_status" in result
        assert "lint_status" in result
        assert "security_status" in result
        assert "deployment_status" in result


# Tests pour les fonctions utilitaires
def test_run_robotics_ci_function():
    """Test de la fonction utilitaire run_robotics_ci"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch("athalia_core.robotics_ci.RoboticsCI") as mock_ci_class:
            mock_ci = Mock()
            mock_ci.run_full_pipeline.return_value = {"status": "success"}
            mock_ci_class.return_value = mock_ci

            result = run_robotics_ci(temp_dir)
            assert result["status"] == "success"
            mock_ci.run_full_pipeline.assert_called_once()
