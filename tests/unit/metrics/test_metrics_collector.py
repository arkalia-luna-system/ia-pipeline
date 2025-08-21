"""
Tests unitaires pour le module metrics_collector.
"""

import os
import shutil
import tempfile
from pathlib import Path
from unittest.mock import Mock, mock_open, patch

import pytest

from athalia_core.metrics.collector import MetricsCollector


class TestMetricsCollector:
    """Tests pour la classe MetricsCollector."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.collector = MetricsCollector(project_root=self.temp_dir)

        # Créer une structure de projet temporaire
        self.create_temp_project_structure()

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir)

    def create_temp_project_structure(self):
        """Crée une structure de projet temporaire pour les tests."""
        # Créer des fichiers Python
        python_files = [
            "main.py",
            "utils/helper.py",
            "core/processor.py",
            "tests/test_main.py",
            "tests/test_utils.py",
        ]

        for file_path in python_files:
            full_path = os.path.join(self.temp_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            # Créer un fichier avec du contenu
            with open(full_path, "w") as f:
                f.write("# Test file\n")
                f.write("def test_function():\n")
                f.write("    pass\n")
                f.write("\n")
                f.write("class TestClass:\n")
                f.write("    def test_method(self):\n")
                f.write("        pass\n")

        # Créer des fichiers de documentation
        doc_files = ["README.md", "docs/guide.md", "docs/api.md"]

        for file_path in doc_files:
            full_path = os.path.join(self.temp_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            with open(full_path, "w") as f:
                f.write("# Documentation\n")
                f.write("This is a test documentation file.\n")

    def test_init(self):
        """Test de l'initialisation du collecteur."""
        assert str(self.collector.project_root.resolve()) == str(
            Path(self.temp_dir).resolve()
        )
        assert isinstance(self.collector.metrics_data, dict)
        assert "exclude_patterns" in self.collector.__dict__

    def test_collect_python_files(self):
        """Test de la collecte des fichiers Python."""
        python_data = self.collector.collect_python_metrics()

        # Devrait trouver des fichiers Python
        assert python_data["count"] > 0
        assert "count" in python_data
        assert "total_lines" in python_data

    def test_count_lines_of_code(self):
        """Test du comptage des lignes de code."""
        python_data = self.collector.collect_python_metrics()

        # Vérifier que les lignes de code sont comptées
        assert python_data["total_lines"] > 0
        assert "total_lines" in python_data

    def test_collect_tests(self):
        """Test de la collecte des tests."""
        test_data = self.collector.collect_test_metrics()

        # Devrait trouver des fichiers de test
        assert test_data["test_files_count"] > 0
        assert "test_files_count" in test_data
        assert "collected_tests_count" in test_data

    def test_collect_documentation(self):
        """Test de la collecte de la documentation."""
        doc_data = self.collector.collect_documentation_metrics()

        # Devrait trouver des fichiers de documentation
        assert doc_data["total_files"] > 0
        assert "total_files" in doc_data
        assert "by_format" in doc_data

    def test_collect_all_metrics(self):
        """Test de la collecte complète des métriques."""
        result = self.collector.collect_all_metrics()

        # Vérifier que la collecte a réussi
        assert result is not None
        assert "summary" in result
        assert "python_files" in result
        assert "tests" in result
        assert "documentation" in result

    def test_get_metrics_summary(self):
        """Test de l'obtention du résumé des métriques."""
        self.collector.collect_all_metrics()
        summary = self.collector.metrics_data["summary"]

        assert "total_python_files" in summary
        assert "lines_of_code" in summary
        assert "collected_tests" in summary
        assert "documentation_files" in summary

    def test_empty_project(self):
        """Test avec un projet vide."""
        empty_dir = tempfile.mkdtemp()
        empty_collector = MetricsCollector(project_root=empty_dir)

        empty_collector.collect_all_metrics()
        summary = empty_collector.metrics_data["summary"]

        assert summary["total_python_files"] == 0
        assert summary["lines_of_code"] == 0
        assert summary["collected_tests"] == 0
        assert summary["documentation_files"] == 0

        shutil.rmtree(empty_dir)

    def test_invalid_project_root(self):
        """Test avec un chemin de projet invalide."""
        invalid_collector = MetricsCollector(project_root="/invalid/path")

        # Ne devrait pas lever d'exception, mais retourner des métriques vides
        invalid_collector.collect_all_metrics()
        summary = invalid_collector.metrics_data["summary"]

        assert summary["total_python_files"] == 0
        assert summary["lines_of_code"] == 0
        assert summary["collected_tests"] == 0
        assert summary["documentation_files"] == 0


if __name__ == "__main__":
    pytest.main([__file__])
