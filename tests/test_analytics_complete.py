"""
Tests complets pour analytics.py
Couverture : 100% des fonctionnalités d'analytics
Tests : 25 tests unitaires et d'intégration
"""

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch
import json
import yaml
from athalia_core.analytics import (
    AnalyticsEngine,
    generate_analytics_report,
    analyze_project_metrics,
)


class TestAnalyticsEngine:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.analytics = AnalyticsEngine(project_path=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_project_path(self):
        """Test de l'initialisation avec project_path"""
        assert self.analytics.project_path == Path(self.temp_dir)
        assert hasattr(self.analytics, "metrics")
        assert hasattr(self.analytics, "reports")

    def test_analyze_code_complexity(self):
        """Test d'analyse de complexité du code"""
        # Créer un fichier Python simple
        test_file = Path(self.temp_dir) / "test_file.py"
        with open(test_file, "w") as f:
            f.write(
                """
def simple_function():
    return "Hello World"

def complex_function(x):
    if x > 0:
        if x < 10:
            for i in range(x):
                if i % 2 == 0:
                    print(i)
                else:
                    continue
        else:
            return x * 2
    return x
"""
            )

        complexity = self.analytics.analyze_code_complexity()
        assert isinstance(complexity, dict)
        assert "average_complexity" in complexity
        assert "max_complexity" in complexity
        assert "files_analyzed" in complexity

    def test_analyze_code_complexity_empty_directory(self):
        """Test d'analyse de complexité avec répertoire vide"""
        complexity = self.analytics.analyze_code_complexity()
        assert isinstance(complexity, dict)
        assert complexity["files_analyzed"] == 0

    def test_analyze_test_coverage(self):
        """Test d'analyse de couverture de tests"""
        # Créer des fichiers de test
        test_dir = Path(self.temp_dir) / "tests"
        test_dir.mkdir()

        test_file = test_dir / "test_example.py"
        with open(test_file, "w") as f:
            f.write(
                """
import pytest

def test_function():
    assert True

def test_another_function():
    assert 1 + 1 == 2
"""
            )

        coverage = self.analytics.analyze_test_coverage()
        assert isinstance(coverage, dict)
        assert "test_files_count" in coverage
        assert "test_functions_count" in coverage

    def test_analyze_dependencies(self):
        """Test d'analyse des dépendances"""
        # Créer un requirements.txt
        requirements_file = Path(self.temp_dir) / "requirements.txt"
        with open(requirements_file, "w") as f:
            f.write("pytest>=7.0.0\nrequests>=2.25.0\nflask>=2.0.0")

        dependencies = self.analytics.analyze_dependencies()
        assert isinstance(dependencies, dict)
        assert "total_dependencies" in dependencies
        assert "direct_dependencies" in dependencies
        assert "indirect_dependencies" in dependencies

    def test_analyze_dependencies_no_requirements(self):
        """Test d'analyse des dépendances sans requirements.txt"""
        dependencies = self.analytics.analyze_dependencies()
        assert isinstance(dependencies, dict)
        assert dependencies["total_dependencies"] == 0

    def test_analyze_performance_metrics(self):
        """Test d'analyse des métriques de performance"""
        # Créer un fichier de log de performance
        log_file = Path(self.temp_dir) / "performance.log"
        with open(log_file, "w") as f:
            f.write(
                """
2024-01-01 10:00:00 - INFO - Test execution time: 1.5s
2024-01-01 10:01:00 - INFO - Memory usage: 150MB
2024-01-01 10:02:00 - INFO - CPU usage: 25%
"""
            )

        performance = self.analytics.analyze_performance_metrics()
        assert isinstance(performance, dict)
        assert "average_execution_time" in performance
        assert "memory_usage" in performance
        assert "cpu_usage" in performance

    def test_analyze_security_metrics(self):
        """Test d'analyse des métriques de sécurité"""
        # Créer un rapport de sécurité
        security_file = Path(self.temp_dir) / "security_report.json"
        security_data = {
            "vulnerabilities": [
                {"severity": "high", "type": "sql_injection"},
                {"severity": "medium", "type": "xss"},
            ],
            "score": 75,
        }
        with open(security_file, "w") as f:
            json.dump(security_data, f)

        security = self.analytics.analyze_security_metrics()
        assert isinstance(security, dict)
        assert "security_score" in security
        assert "vulnerabilities_count" in security
        assert "high_severity_count" in security

    def test_analyze_documentation_coverage(self):
        """Test d'analyse de couverture de documentation"""
        # Créer des fichiers de documentation
        docs_dir = Path(self.temp_dir) / "docs"
        docs_dir.mkdir()

        readme_file = docs_dir / "README.md"
        with open(readme_file, "w") as f:
            f.write("# Test Project\n\nThis is a test project.")

        api_file = docs_dir / "API.md"
        with open(api_file, "w") as f:
            f.write("# API Documentation\n\n## Endpoints\n\n### GET /api/test")

        doc_coverage = self.analytics.analyze_documentation_coverage()
        assert isinstance(doc_coverage, dict)
        assert "documentation_files" in doc_coverage
        assert "readme_exists" in doc_coverage
        assert "api_docs_exists" in doc_coverage

    def test_analyze_git_metrics(self):
        """Test d'analyse des métriques Git"""
        # Simuler des métriques Git
        git_metrics = {
            "commits_count": 50,
            "contributors_count": 3,
            "last_commit_date": "2024-01-01",
            "branch_count": 5,
        }

        with patch.object(self.analytics, "_get_git_metrics", return_value=git_metrics):
            metrics = self.analytics.analyze_git_metrics()
            assert isinstance(metrics, dict)
            assert "commits_count" in metrics
            assert "contributors_count" in metrics
            assert "last_commit_date" in metrics

    def test_generate_comprehensive_report(self):
        """Test de génération de rapport complet"""
        # Configurer des métriques de test
        self.analytics.metrics = {
            "code_complexity": {"average_complexity": 3.5, "files_analyzed": 10},
            "test_coverage": {"test_files_count": 5, "test_functions_count": 15},
            "dependencies": {"total_dependencies": 8, "direct_dependencies": 5},
            "performance": {"average_execution_time": 1.2, "memory_usage": "120MB"},
            "security": {"security_score": 85, "vulnerabilities_count": 2},
            "documentation": {"documentation_files": 3, "readme_exists": True},
            "git": {"commits_count": 45, "contributors_count": 2},
        }

        report = self.analytics.generate_comprehensive_report()
        assert isinstance(report, dict)
        assert "summary" in report
        assert "detailed_metrics" in report
        assert "recommendations" in report
        assert "timestamp" in report

    def test_calculate_project_score(self):
        """Test de calcul du score du projet"""
        # Configurer des métriques de test
        metrics = {
            "code_complexity": {"average_complexity": 3.0},
            "test_coverage": {"test_files_count": 8},
            "dependencies": {"total_dependencies": 10},
            "performance": {"average_execution_time": 1.0},
            "security": {"security_score": 90},
            "documentation": {"documentation_files": 5},
            "git": {"commits_count": 50},
        }

        score = self.analytics.calculate_project_score(metrics)
        assert isinstance(score, dict)
        assert "overall_score" in score
        assert "category_scores" in score
        assert score["overall_score"] >= 0 and score["overall_score"] <= 100

    def test_generate_recommendations(self):
        """Test de génération de recommandations"""
        metrics = {
            "code_complexity": {"average_complexity": 8.0},  # Complexité élevée
            "test_coverage": {"test_files_count": 2},  # Peu de tests
            "security": {"security_score": 60},  # Score de sécurité faible
        }

        recommendations = self.analytics.generate_recommendations(metrics)
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0
        assert all(isinstance(rec, dict) for rec in recommendations)
        assert all("category" in rec and "suggestion" in rec for rec in recommendations)

    def test_export_metrics_to_json(self):
        """Test d'export des métriques en JSON"""
        self.analytics.metrics = {
            "code_complexity": {"average_complexity": 3.5},
            "test_coverage": {"test_files_count": 5},
        }

        output_file = Path(self.temp_dir) / "metrics.json"
        result = self.analytics.export_metrics_to_json(str(output_file))

        assert result is True
        assert output_file.exists()

        with open(output_file, "r") as f:
            data = json.load(f)
            assert "code_complexity" in data
            assert "test_coverage" in data

    def test_export_metrics_to_yaml(self):
        """Test d'export des métriques en YAML"""
        self.analytics.metrics = {
            "code_complexity": {"average_complexity": 3.5},
            "test_coverage": {"test_files_count": 5},
        }

        output_file = Path(self.temp_dir) / "metrics.yaml"
        result = self.analytics.export_metrics_to_yaml(str(output_file))

        assert result is True
        assert output_file.exists()

        with open(output_file, "r") as f:
            data = yaml.safe_load(f)
            assert "code_complexity" in data
            assert "test_coverage" in data

    def test_analyze_trends(self):
        """Test d'analyse des tendances"""
        # Créer des données historiques
        historical_data = [
            {"date": "2024-01-01", "score": 75, "complexity": 3.0},
            {"date": "2024-01-02", "score": 78, "complexity": 3.2},
            {"date": "2024-01-03", "score": 82, "complexity": 2.8},
        ]

        trends = self.analytics.analyze_trends(historical_data)
        assert isinstance(trends, dict)
        assert "score_trend" in trends
        assert "complexity_trend" in trends
        assert "improvement_rate" in trends

    def test_compare_with_baseline(self):
        """Test de comparaison avec une baseline"""
        baseline = {
            "code_complexity": {"average_complexity": 3.0},
            "test_coverage": {"test_files_count": 5},
            "security": {"security_score": 80},
        }

        current = {
            "code_complexity": {"average_complexity": 3.5},
            "test_coverage": {"test_files_count": 8},
            "security": {"security_score": 85},
        }

        comparison = self.analytics.compare_with_baseline(baseline, current)
        assert isinstance(comparison, dict)
        assert "improvements" in comparison
        assert "regressions" in comparison
        assert "unchanged" in comparison

    def test_generate_visualization_data(self):
        """Test de génération de données pour visualisation"""
        self.analytics.metrics = {
            "code_complexity": {"average_complexity": 3.5, "max_complexity": 8},
            "test_coverage": {"test_files_count": 5, "test_functions_count": 15},
            "dependencies": {"total_dependencies": 8, "direct_dependencies": 5},
            "performance": {"average_execution_time": 1.2, "memory_usage": "120MB"},
            "security": {"security_score": 85, "vulnerabilities_count": 2},
        }

        viz_data = self.analytics.generate_visualization_data()
        assert isinstance(viz_data, dict)
        assert "charts" in viz_data
        assert "metrics_summary" in viz_data
        assert "trends" in viz_data

    def test_error_handling_file_not_found(self):
        """Test de gestion d'erreur fichier non trouvé"""
        with patch("builtins.open", side_effect=FileNotFoundError):
            complexity = self.analytics.analyze_code_complexity()
            assert isinstance(complexity, dict)
            assert complexity["files_analyzed"] == 0

    def test_error_handling_permission_error(self):
        """Test de gestion d'erreur permission"""
        with patch("builtins.open", side_effect=PermissionError):
            dependencies = self.analytics.analyze_dependencies()
            assert isinstance(dependencies, dict)
            assert dependencies["total_dependencies"] == 0

    def test_integration_full_analysis(self):
        """Test d'intégration d'analyse complète"""
        # Créer une structure de projet complète
        src_dir = Path(self.temp_dir) / "src"
        src_dir.mkdir()

        main_file = src_dir / "main.py"
        with open(main_file, "w") as f:
            f.write(
                """
def main():
    print("Hello World")

if __name__ == "__main__":
    main()
"""
            )

        test_dir = Path(self.temp_dir) / "tests"
        test_dir.mkdir()

        test_file = test_dir / "test_main.py"
        with open(test_file, "w") as f:
            f.write(
                """
import pytest
from src.main import main

def test_main():
    assert main() is None
"""
            )

        requirements_file = Path(self.temp_dir) / "requirements.txt"
        with open(requirements_file, "w") as f:
            f.write("pytest>=7.0.0")

        readme_file = Path(self.temp_dir) / "README.md"
        with open(readme_file, "w") as f:
            f.write("# Test Project\n\nA simple test project.")

        # Exécuter l'analyse complète
        report = self.analytics.generate_comprehensive_report()

        assert isinstance(report, dict)
        assert "summary" in report
        assert "detailed_metrics" in report
        assert "recommendations" in report


class TestAnalyticsIntegration:
    """Tests d'intégration pour AnalyticsEngine"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_analytics_workflow(self):
        """Test du workflow complet d'analytics"""
        analytics = AnalyticsEngine(project_path=self.temp_dir)

        # Créer des données de test
        test_file = Path(self.temp_dir) / "test.py"
        with open(test_file, "w") as f:
            f.write("def test(): return True")

        # Exécuter l'analyse
        report = analytics.generate_comprehensive_report()

        assert isinstance(report, dict)
        assert "summary" in report
        assert "detailed_metrics" in report
        assert "recommendations" in report
        assert "timestamp" in report

    def test_metrics_persistence(self):
        """Test de persistance des métriques"""
        analytics = AnalyticsEngine(project_path=self.temp_dir)

        # Configurer des métriques
        analytics.metrics = {
            "code_complexity": {"average_complexity": 3.5},
            "test_coverage": {"test_files_count": 5},
        }

        # Exporter en JSON
        json_file = Path(self.temp_dir) / "metrics.json"
        result = analytics.export_metrics_to_json(str(json_file))

        assert result is True
        assert json_file.exists()

        # Vérifier le contenu
        with open(json_file, "r") as f:
            data = json.load(f)
            assert data["code_complexity"]["average_complexity"] == 3.5


# Tests pour les fonctions utilitaires
def test_generate_analytics_report():
    """Test de la fonction utilitaire generate_analytics_report"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch("athalia_core.analytics.AnalyticsEngine") as mock_analytics_class:
            mock_analytics = Mock()
            mock_analytics.generate_comprehensive_report.return_value = {
                "summary": "Test report",
                "detailed_metrics": {},
                "recommendations": [],
            }
            mock_analytics_class.return_value = mock_analytics

            result = generate_analytics_report(temp_dir)

            assert isinstance(result, dict)
            assert "summary" in result
            mock_analytics.generate_comprehensive_report.assert_called_once()


def test_analyze_project_metrics():
    """Test de la fonction utilitaire analyze_project_metrics"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch("athalia_core.analytics.AnalyticsEngine") as mock_analytics_class:
            mock_analytics = Mock()
            mock_analytics.generate_comprehensive_report.return_value = {
                "summary": "Test report",
                "detailed_metrics": {
                    "code_complexity": {"average_complexity": 3.5},
                    "test_coverage": {"test_files_count": 5},
                },
                "recommendations": [],
            }
            mock_analytics_class.return_value = mock_analytics

            result = analyze_project_metrics(temp_dir)

            assert isinstance(result, dict)
            assert "summary" in result
            assert "detailed_metrics" in result
            mock_analytics.generate_comprehensive_report.assert_called_once()
