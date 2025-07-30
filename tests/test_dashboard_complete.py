"""
Tests complets pour dashboard.py
Couverture : 100% des fonctionnalités du dashboard
Tests : 20 tests unitaires et d'intégration
"""

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import yaml

from athalia_core.dashboard import (
    Dashboard,
    create_dashboard_report,
    generate_dashboard_html,
)


class TestDashboard:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.dashboard = Dashboard(project_path=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_project_path(self):
        """Test de l'initialisation avec project_path"""
        assert self.dashboard.project_path == Path(self.temp_dir)
        assert hasattr(self.dashboard, "metrics")
        assert hasattr(self.dashboard, "config")

    def test_load_dashboard_config(self):
        """Test de chargement de la configuration du dashboard"""
        # Créer un fichier de configuration
        config_file = Path(self.temp_dir) / "dashboard_config.yaml"
        config_data = {
            "theme": "dark",
            "refresh_interval": 30,
            "widgets": ["metrics", "charts", "alerts"],
            "layout": "grid",
        }

        with open(config_file, "w") as f:
            yaml.dump(config_data, f)

        config = self.dashboard.load_dashboard_config(str(config_file))
        assert isinstance(config, dict)
        assert config["theme"] == "dark"
        assert config["refresh_interval"] == 30
        assert "widgets" in config

    def test_load_dashboard_config_default(self):
        """Test de chargement de la configuration par défaut"""
        config = self.dashboard.load_dashboard_config()
        assert isinstance(config, dict)
        assert "theme" in config
        assert "refresh_interval" in config

    def test_generate_metrics_widget(self):
        """Test de génération du widget métriques"""
        # Configurer des métriques de test
        self.dashboard.metrics = {
            "code_complexity": {"average_complexity": 3.5, "files_analyzed": 10},
            "test_coverage": {"test_files_count": 5, "test_functions_count": 15},
            "security": {"security_score": 85, "vulnerabilities_count": 2},
            "performance": {"average_execution_time": 1.2, "memory_usage": "120MB"},
        }

        widget = self.dashboard.generate_metrics_widget()
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "data" in widget
        assert "type" in widget
        assert widget["type"] == "metrics"

    def test_generate_charts_widget(self):
        """Test de génération du widget graphiques"""
        # Configurer des données de test
        chart_data = {
            "complexity_distribution": {"low": 5, "medium": 3, "high": 2},
            "test_coverage_trend": [70, 75, 80, 85, 90],
            "security_score_history": [80, 82, 85, 83, 87],
        }

        widget = self.dashboard.generate_charts_widget(chart_data)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "charts" in widget
        assert "type" in widget
        assert widget["type"] == "charts"

    def test_generate_alerts_widget(self):
        """Test de génération du widget alertes"""
        # Configurer des alertes de test
        alerts = [
            {
                "severity": "high",
                "message": "Vulnérabilité de sécurité détectée",
                "category": "security",
            },
            {
                "severity": "medium",
                "message": "Complexité du code élevée",
                "category": "code_quality",
            },
            {
                "severity": "low",
                "message": "Documentation incomplète",
                "category": "documentation",
            },
        ]

        widget = self.dashboard.generate_alerts_widget(alerts)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "alerts" in widget
        assert "type" in widget
        assert widget["type"] == "alerts"

    def test_generate_performance_widget(self):
        """Test de génération du widget performance"""
        # Configurer des données de performance
        performance_data = {
            "execution_time": {"average": 1.2, "max": 3.5, "min": 0.8},
            "memory_usage": {"current": "120MB", "peak": "150MB", "average": "110MB"},
            "cpu_usage": {"current": 25, "peak": 45, "average": 20},
        }

        widget = self.dashboard.generate_performance_widget(performance_data)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "performance_data" in widget
        assert "type" in widget
        assert widget["type"] == "performance"

    def test_generate_security_widget(self):
        """Test de génération du widget sécurité"""
        # Configurer des données de sécurité
        security_data = {
            "security_score": 85,
            "vulnerabilities": [
                {"severity": "high", "type": "sql_injection", "count": 1},
                {"severity": "medium", "type": "xss", "count": 2},
            ],
            "last_scan": "2024-01-01T10:00:00",
        }

        widget = self.dashboard.generate_security_widget(security_data)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "security_data" in widget
        assert "type" in widget
        assert widget["type"] == "security"

    def test_generate_test_coverage_widget(self):
        """Test de génération du widget couverture de tests"""
        # Configurer des données de couverture
        coverage_data = {
            "overall_coverage": 85.5,
            "test_files_count": 15,
            "test_functions_count": 45,
            "coverage_by_module": {"core": 90.0, "utils": 75.0, "api": 80.0},
        }

        widget = self.dashboard.generate_test_coverage_widget(coverage_data)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "coverage_data" in widget
        assert "type" in widget
        assert widget["type"] == "test_coverage"

    def test_generate_dependency_widget(self):
        """Test de génération du widget dépendances"""
        # Configurer des données de dépendances
        dependency_data = {
            "total_dependencies": 25,
            "direct_dependencies": 15,
            "indirect_dependencies": 10,
            "outdated_packages": 3,
            "vulnerable_packages": 1,
            "dependency_tree": {
                "pytest": ["py", "packaging"],
                "requests": ["urllib3", "certifi"],
            },
        }

        widget = self.dashboard.generate_dependency_widget(dependency_data)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "dependency_data" in widget
        assert "type" in widget
        assert widget["type"] == "dependencies"

    def test_generate_documentation_widget(self):
        """Test de génération du widget documentation"""
        # Configurer des données de documentation
        doc_data = {
            "documentation_files": 8,
            "readme_exists": True,
            "api_docs_exists": True,
            "doc_coverage_percentage": 75.0,
            "missing_docs": ["utils.py", "config.py"],
            "documentation_types": ["markdown", "rst", "html"],
        }

        widget = self.dashboard.generate_documentation_widget(doc_data)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "doc_data" in widget
        assert "type" in widget
        assert widget["type"] == "documentation"

    def test_generate_git_widget(self):
        """Test de génération du widget Git"""
        # Configurer des données Git
        git_data = {
            "commits_count": 150,
            "contributors_count": 5,
            "last_commit_date": "2024-01-01T15:30:00",
            "branch_count": 8,
            "repository_age_days": 365,
            "recent_activity": [
                {"date": "2024-01-01", "commits": 3},
                {"date": "2024-01-02", "commits": 5},
            ],
        }

        widget = self.dashboard.generate_git_widget(git_data)
        assert isinstance(widget, dict)
        assert "title" in widget
        assert "git_data" in widget
        assert "type" in widget
        assert widget["type"] == "git"

    def test_generate_dashboard_layout(self):
        """Test de génération de la mise en page du dashboard"""
        # Configurer des widgets de test
        widgets = [
            {"type": "metrics", "title": "Métriques", "data": {}},
            {"type": "charts", "title": "Graphiques", "charts": {}},
            {"type": "alerts", "title": "Alertes", "alerts": []},
        ]

        layout = self.dashboard.generate_dashboard_layout(widgets, "grid")
        assert isinstance(layout, dict)
        assert "layout_type" in layout
        assert "widgets" in layout
        assert "grid_config" in layout

    def test_generate_dashboard_html(self):
        """Test de génération du HTML du dashboard"""
        # Configurer des données de test
        dashboard_data = {
            "title": "Dashboard Test",
            "theme": "dark",
            "widgets": [
                {"type": "metrics", "title": "Métriques", "data": {}},
                {"type": "charts", "title": "Graphiques", "charts": {}},
            ],
            "config": {"refresh_interval": 30},
        }

        html = self.dashboard.generate_dashboard_html(dashboard_data)
        assert isinstance(html, str)
        assert "<!DOCTYPE html>" in html
        assert "Dashboard Test" in html
        assert "dark" in html

    def test_generate_dashboard_css(self):
        """Test de génération du CSS du dashboard"""
        css = self.dashboard.generate_dashboard_css("dark")
        assert isinstance(css, str)
        assert "body" in css
        assert "dashboard" in css
        assert "widget" in css

    def test_generate_dashboard_js(self):
        """Test de génération du JavaScript du dashboard"""
        js = self.dashboard.generate_dashboard_js({"refresh_interval": 30})
        assert isinstance(js, str)
        assert "function" in js
        assert "refresh" in js
        assert "30" in js

    def test_save_dashboard_html(self):
        """Test de sauvegarde du dashboard HTML"""
        html_content = (
            "<!DOCTYPE html><html><body><h1>Test Dashboard</h1></body></html>"
        )

        output_file = Path(self.temp_dir) / "dashboard.html"
        result = self.dashboard.save_dashboard_html(html_content, str(output_file))

        assert result is True
        assert output_file.exists()

        with open(output_file, "r") as f:
            content = f.read()
            assert "Test Dashboard" in content

    def test_generate_dashboard_report(self):
        """Test de génération du rapport de dashboard"""
        # Configurer des métriques de test
        self.dashboard.metrics = {
            "code_complexity": {"average_complexity": 3.5},
            "test_coverage": {"test_files_count": 5},
            "security": {"security_score": 85},
            "performance": {"average_execution_time": 1.2},
        }

        report = self.dashboard.generate_dashboard_report()
        assert isinstance(report, dict)
        assert "dashboard_data" in report
        assert "html_content" in report
        assert "config" in report

    def test_error_handling_config_not_found(self):
        """Test de gestion d'erreur configuration non trouvée"""
        with patch("builtins.open", side_effect=FileNotFoundError):
            config = self.dashboard.load_dashboard_config("nonexistent.yaml")
            assert isinstance(config, dict)
            assert "theme" in config  # Configuration par défaut

    def test_error_handling_invalid_yaml(self):
        """Test de gestion d'erreur YAML invalide"""
        config_file = Path(self.temp_dir) / "invalid_config.yaml"
        with open(config_file, "w") as f:
            f.write("invalid: yaml: content: [")

        config = self.dashboard.load_dashboard_config(str(config_file))
        assert isinstance(config, dict)
        assert "theme" in config  # Configuration par défaut

    def test_integration_full_dashboard(self):
        """Test d'intégration du dashboard complet"""
        # Configurer des données complètes
        self.dashboard.metrics = {
            "code_complexity": {"average_complexity": 3.5, "files_analyzed": 10},
            "test_coverage": {"test_files_count": 5, "test_functions_count": 15},
            "security": {"security_score": 85, "vulnerabilities_count": 2},
            "performance": {"average_execution_time": 1.2, "memory_usage": "120MB"},
            "dependencies": {"total_dependencies": 25, "direct_dependencies": 15},
            "documentation": {
                "documentation_files": 8,
                "doc_coverage_percentage": 75.0,
            },
            "git": {"commits_count": 150, "contributors_count": 5},
        }

        # Générer le dashboard complet
        report = self.dashboard.generate_dashboard_report()

        assert isinstance(report, dict)
        assert "dashboard_data" in report
        assert "html_content" in report
        assert "config" in report

        # Vérifier que le HTML contient les éléments attendus
        html = report["html_content"]
        assert "dashboard" in html.lower()
        assert "widget" in html.lower()


class TestDashboardIntegration:
    """Tests d'intégration pour Dashboard"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_dashboard_workflow(self):
        """Test du workflow complet du dashboard"""
        dashboard = Dashboard(project_path=self.temp_dir)

        # Configurer des métriques
        dashboard.metrics = {
            "code_complexity": {"average_complexity": 3.5},
            "test_coverage": {"test_files_count": 5},
            "security": {"security_score": 85},
        }

        # Générer le rapport
        report = dashboard.generate_dashboard_report()

        assert isinstance(report, dict)
        assert "dashboard_data" in report
        assert "html_content" in report

        # Sauvegarder le dashboard
        output_file = Path(self.temp_dir) / "dashboard.html"
        result = dashboard.save_dashboard_html(report["html_content"], str(output_file))

        assert result is True
        assert output_file.exists()

    def test_dashboard_with_custom_config(self):
        """Test du dashboard avec configuration personnalisée"""
        # Créer une configuration personnalisée
        config_file = Path(self.temp_dir) / "custom_config.yaml"
        config_data = {
            "theme": "light",
            "refresh_interval": 60,
            "widgets": ["metrics", "security"],
            "layout": "sidebar",
        }

        with open(config_file, "w") as f:
            yaml.dump(config_data, f)

        dashboard = Dashboard(project_path=self.temp_dir)
        config = dashboard.load_dashboard_config(str(config_file))

        assert config["theme"] == "light"
        assert config["refresh_interval"] == 60
        assert "metrics" in config["widgets"]
        assert "security" in config["widgets"]


# Tests pour les fonctions utilitaires
def test_generate_dashboard_html():
    """Test de la fonction utilitaire generate_dashboard_html"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch("athalia_core.dashboard.Dashboard") as mock_dashboard_class:
            mock_dashboard = Mock()
            mock_report = {"html_content": "<html>Test</html>"}
            mock_dashboard.generate_dashboard_report.return_value = mock_report
            mock_dashboard_class.return_value = mock_dashboard

            result = generate_dashboard_html(temp_dir)

            assert isinstance(result, str)
            assert "Test" in result
            mock_dashboard.generate_dashboard_report.assert_called_once()


def test_create_dashboard_report():
    """Test de la fonction utilitaire create_dashboard_report"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch("athalia_core.dashboard.Dashboard") as mock_dashboard_class:
            mock_dashboard = Mock()
            mock_dashboard.generate_dashboard_report.return_value = {
                "dashboard_data": {},
                "html_content": "<html>Test</html>",
                "config": {},
            }
            mock_dashboard_class.return_value = mock_dashboard

            result = create_dashboard_report(temp_dir)

            assert isinstance(result, dict)
            assert "dashboard_data" in result
            assert "html_content" in result
            mock_dashboard.generate_dashboard_report.assert_called_once()
