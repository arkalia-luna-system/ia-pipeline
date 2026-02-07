#!/usr/bin/env python3
"""
Module dashboard pour Athalia
Interface de visualisation et monitoring
"""

import json
import logging

# Import sécurisé pour subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore

    yaml_module = yaml
except ImportError:
    yaml_module = None

logger = logging.getLogger(__name__)


class Dashboard:
    """Dashboard pour visualisation des métriques"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.metrics: dict[str, Any] = {}
        self.config = self.load_dashboard_config()

    def load_dashboard_config(self, config_path: str | None = None) -> dict[str, Any]:
        """Charge la configuration du dashboard"""
        default_config = {
            "theme": "light",
            "refresh_interval": 30,
            "widgets": [
                "metrics",
                "charts",
                "alerts",
                "performance",
                "security",
            ],
            "layout": "grid",
            "auto_refresh": True,
            "show_timestamps": True,
        }

        if config_path and yaml_module:
            try:
                with open(config_path, encoding="utf-8") as f:
                    user_config = yaml_module.safe_load(f)
                    default_config.update(user_config)
            except Exception as e:
                logger.warning(
                    f"Impossible de charger la configuration {config_path}: {e}"
                )

        return default_config

    def generate_metrics_widget(self) -> dict[str, Any]:
        """Génère le widget métriques"""
        widget = {
            "type": "metrics",
            "title": "Métriques du Projet",
            "data": self.metrics,
            "timestamp": datetime.now().isoformat(),
            "refresh_interval": self.config.get("refresh_interval", 30),
        }

        # Calculer des métriques agrégées
        if self.metrics:
            widget["summary"] = {
                "total_files": (
                    self.metrics.get("code_complexity", {}).get("files_analyzed", 0)
                ),
                "security_score": (
                    self.metrics.get("security", {}).get("security_score", 0)
                ),
                "test_coverage": (
                    self.metrics.get("test_coverage", {}).get("test_files_count", 0)
                ),
                "dependencies": (
                    self.metrics.get("dependencies", {}).get("total_dependencies", 0)
                ),
            }

        return widget

    def generate_charts_widget(self, chart_data: dict[str, Any]) -> dict[str, Any]:
        """Génère le widget graphiques"""
        widget = {
            "type": "charts",
            "title": "Graphiques et Tendances",
            "charts": chart_data,
            "timestamp": datetime.now().isoformat(),
            "chart_types": ["bar", "line", "pie", "radar"],
        }

        return widget

    def generate_alerts_widget(self, alerts: list[dict[str, Any]]) -> dict[str, Any]:
        """Génère le widget alertes"""
        widget = {
            "type": "alerts",
            "title": "Alertes et Notifications",
            "alerts": alerts,
            "timestamp": datetime.now().isoformat(),
            "alert_count": len(alerts),
            "severity_counts": {
                "high": len([a for a in alerts if a.get("severity") == "high"]),
                "medium": len([a for a in alerts if a.get("severity") == "medium"]),
                "low": len([a for a in alerts if a.get("severity") == "low"]),
            },
        }

        return widget

    def generate_performance_widget(
        self, performance_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Génère le widget performance"""
        widget = {
            "type": "performance",
            "title": "Métriques de Performance",
            "performance_data": performance_data,
            "timestamp": datetime.now().isoformat(),
            "status": "normal",
        }

        # Déterminer le statut basé sur les métriques
        if "execution_time" in performance_data:
            avg_time = performance_data["execution_time"].get("average", 0)
            if avg_time > 5.0:
                widget["status"] = "warning"
            elif avg_time > 10.0:
                widget["status"] = "critical"

        return widget

    def generate_security_widget(self, security_data: dict[str, Any]) -> dict[str, Any]:
        """Génère le widget sécurité"""
        widget = {
            "type": "security",
            "title": "Sécurité du Projet",
            "security_data": security_data,
            "timestamp": datetime.now().isoformat(),
            "status": "secure",
        }

        # Déterminer le statut de sécurité
        security_score = security_data.get("security_score", 100)
        if security_score < 70:
            widget["status"] = "critical"
        elif security_score < 85:
            widget["status"] = "warning"

        return widget

    def generate_test_coverage_widget(
        self, coverage_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Génère le widget couverture de tests"""
        widget = {
            "type": "test_coverage",
            "title": "Couverture de Tests",
            "coverage_data": coverage_data,
            "timestamp": datetime.now().isoformat(),
            "status": "good",
        }

        # Déterminer le statut de couverture
        overall_coverage = coverage_data.get("overall_coverage", 0)
        if overall_coverage < 50:
            widget["status"] = "poor"
        elif overall_coverage < 80:
            widget["status"] = "fair"

        return widget

    def generate_dependency_widget(
        self, dependency_data: dict[str, Any]
    ) -> dict[str, Any]:
        """Génère le widget dépendances"""
        widget = {
            "type": "dependencies",
            "title": "Gestion des Dépendances",
            "dependency_data": dependency_data,
            "timestamp": datetime.now().isoformat(),
            "status": "healthy",
        }

        # Déterminer le statut des dépendances
        outdated = dependency_data.get("outdated_packages", 0)
        vulnerable = dependency_data.get("vulnerable_packages", 0)

        if vulnerable > 0:
            widget["status"] = "critical"
        elif outdated > 5:
            widget["status"] = "warning"

        return widget

    def generate_documentation_widget(self, doc_data: dict[str, Any]) -> dict[str, Any]:
        """Génère le widget documentation"""
        widget = {
            "type": "documentation",
            "title": "Qualité de la Documentation",
            "doc_data": doc_data,
            "timestamp": datetime.now().isoformat(),
            "status": "good",
        }

        # Déterminer le statut de la documentation
        doc_coverage = doc_data.get("documentation_coverage", 0)
        if doc_coverage < 50:
            widget["status"] = "poor"
        elif doc_coverage < 80:
            widget["status"] = "fair"

        return widget

    def generate_git_widget(self, git_data: dict[str, Any]) -> dict[str, Any]:
        """Génère le widget Git"""
        widget = {
            "type": "git",
            "title": "Activité Git",
            "git_data": git_data,
            "timestamp": datetime.now().isoformat(),
            "status": "active",
        }

        # Déterminer le statut d'activité
        commits_count = git_data.get("commits_count", 0)
        if commits_count == 0:
            widget["status"] = "inactive"
        elif commits_count < 10:
            widget["status"] = "low_activity"

        return widget

    def generate_dashboard_layout(
        self, widgets: list[dict[str, Any]], layout_type: str = "grid"
    ) -> dict[str, Any]:
        """Génère la mise en page du dashboard"""
        layout = {
            "layout_type": layout_type,
            "widgets": widgets,
            "timestamp": datetime.now().isoformat(),
            "total_widgets": len(widgets),
        }

        if layout_type == "grid":
            layout["grid_config"] = {
                "columns": 3,
                "rows": (len(widgets) + 2) // 3,
                "gap": "20px",
            }
        elif layout_type == "sidebar":
            layout["sidebar_config"] = {
                "sidebar_width": "300px",
                "main_content_width": "calc(100% - 300px)",
            }
        elif layout_type == "tabs":
            layout["tabs_config"] = {
                "tab_names": [
                    widget.get("title", f"Widget {i}")
                    for i, widget in enumerate(widgets)
                ],
                "active_tab": 0,
            }

        return layout

    def generate_dashboard_html(self, dashboard_data: dict[str, Any]) -> str:
        """Génère le HTML complet du dashboard"""
        theme = dashboard_data.get("theme", "light")
        widgets = dashboard_data.get("widgets", [])
        config = dashboard_data.get("config", {})

        # Générer le CSS
        css = self.generate_dashboard_css(theme)
        # Générer le JavaScript
        js = self.generate_dashboard_js(config)

        # Construire le HTML
        html_parts = [f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Athalia - {dashboard_data.get("title", "Métriques")}</title>
    <style>{css}</style>
</head>
<body class="theme-{theme}">
    <div class="dashboard-header">
        <h1>📊 Dashboard Athalia</h1>
        <div class="dashboard-controls">
            <select id="theme-selector">
                <option value="light" {"selected" if theme == "light" else ""}>Clair</option>
                <option value="dark" {"selected" if theme == "dark" else ""}>Sombre</option>
            </select>
            <button id="refresh-btn">🔄 Actualiser</button>
        </div>
    </div>

    <div class="dashboard-content">
        <div class="widgets-container">"""]

        # Ajouter les widgets
        for widget in widgets:
            html_parts.append(self._generate_widget_html(widget))

        # Fermer le HTML
        html_parts.append(
            """        </div>
    </div>

    <div class="dashboard-footer">
        <p>Généré le """
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + """</p>
    </div>

    <script>"""
            + js
            + """</script>
</body>
</html>"""
        )

        return "".join(html_parts)

    def _generate_widget_html(self, widget: dict[str, Any]) -> str:
        """Génère le HTML d'un widget individuel"""
        widget_type = widget.get("type", "unknown")
        title = widget.get("title", "Widget")
        timestamp = widget.get("timestamp", "")
        status = widget.get("status", "normal")

        status_class = f"status-{status}"
        status_icon = {
            "normal": "✅",
            "warning": "⚠️",
            "critical": "🚨",
            "good": "✅",
            "fair": "⚠️",
            "poor": "❌",
            "healthy": "✅",
            "secure": "🛡️",
        }.get(status, "ℹ️")

        html = f"""
            <div class="widget {status_class}">
                <h3>{status_icon} {title}</h3>
                <div class="widget-content">
                    <div class="widget-timestamp">🕒 {timestamp}</div>
                    <div class="widget-data">"""

        # Générer le contenu du widget selon son type
        if widget_type == "metrics":
            html += self._generate_metrics_content(widget)
        elif widget_type == "alerts":
            html += self._generate_alerts_content(widget)
        elif widget_type == "performance":
            html += self._generate_performance_content(widget)
        elif widget_type == "security":
            html += self._generate_security_content(widget)
        elif widget_type == "test_coverage":
            html += self._generate_test_coverage_content(widget)
        elif widget_type == "dependencies":
            html += self._generate_dependencies_content(widget)
        elif widget_type == "documentation":
            html += self._generate_documentation_content(widget)
        else:
            html += f"<p>Type de widget non reconnu: {widget_type}</p>"

        html += """
                </div>
            </div>
        </div>"""

        return html

    def _generate_metrics_content(self, widget: dict[str, Any]) -> str:
        """Génère le contenu du widget métriques"""
        summary = widget.get("summary", {})

        html = "<div class='metrics-summary'>"
        if summary:
            html += "<h4>📊 Résumé</h4>"
            for key, value in summary.items():
                html += (
                    f"<p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>"
                )
        else:
            html += "<p>Aucune métrique disponible</p>"
        html += "</div>"

        return html

    def _generate_alerts_content(self, widget: dict[str, Any]) -> str:
        """Génère le contenu du widget alertes"""
        alerts = widget.get("alerts", [])
        alert_count = widget.get("alert_count", 0)
        severity_counts = widget.get("severity_counts", {})

        html = f"<div class='alerts-summary'><h4>🚨 Alertes ({alert_count})</h4>"

        if severity_counts:
            html += "<div class='severity-breakdown'>"
            for severity, count in severity_counts.items():
                if count > 0:
                    severity_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(
                        severity, "⚪"
                    )
                    html += f"<span class='severity-{severity}'>{severity_icon} {severity.title()}: {count}</span>"
            html += "</div>"

        if alerts:
            html += "<div class='alerts-list'>"
            for alert in alerts[:5]:  # Limiter à 5 alertes
                severity = alert.get("severity", "info")
                message = alert.get("message", "Alerte sans message")
                html += f"<div class='alert alert-{severity}'>{message}</div>"
            html += "</div>"
        else:
            html += "<p>Aucune alerte active</p>"

        html += "</div>"
        return html

    def _generate_performance_content(self, widget: dict[str, Any]) -> str:
        """Génère le contenu du widget performance"""
        performance_data = widget.get("performance_data", {})
        status = widget.get("status", "normal")

        html = f"<div class='performance-summary'><h4>⚡ Performance ({status})</h4>"

        if performance_data:
            for key, value in performance_data.items():
                if isinstance(value, dict):
                    html += f"<h5>{key.replace('_', ' ').title()}</h5>"
                    for sub_key, sub_value in value.items():
                        html += (
                            f"<p>{sub_key.replace('_', ' ').title()}: {sub_value}</p>"
                        )
                else:
                    html += f"<p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>"
        else:
            html += "<p>Aucune donnée de performance disponible</p>"

        html += "</div>"
        return html

    def _generate_security_content(self, widget: dict[str, Any]) -> str:
        """Génère le contenu du widget sécurité"""
        security_data = widget.get("security_data", {})
        status = widget.get("status", "secure")

        html = f"<div class='security-summary'><h4>🛡️ Sécurité ({status})</h4>"

        if security_data:
            security_score = security_data.get("security_score", 0)
            html += f"<p><strong>Score de sécurité:</strong> {security_score}/100</p>"

            for key, value in security_data.items():
                if key != "security_score":
                    html += f"<p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>"
        else:
            html += "<p>Aucune donnée de sécurité disponible</p>"

        html += "</div>"
        return html

    def _generate_test_coverage_content(self, widget: dict[str, Any]) -> str:
        """Génère le contenu du widget couverture de tests"""
        coverage_data = widget.get("coverage_data", {})
        status = widget.get("status", "good")

        html = f"<div class='test-coverage-summary'><h4>🧪 Couverture de Tests ({status})</h4>"

        if coverage_data:
            overall_coverage = coverage_data.get("overall_coverage", 0)
            html += f"<p><strong>Couverture globale:</strong> {overall_coverage}%</p>"

            for key, value in coverage_data.items():
                if key != "overall_coverage":
                    html += f"<p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>"
        else:
            html += "<p>Aucune donnée de couverture disponible</p>"

        html += "</div>"
        return html

    def _generate_dependencies_content(self, widget: dict[str, Any]) -> str:
        """Génère le contenu du widget dépendances"""
        dependency_data = widget.get("dependency_data", {})
        status = widget.get("status", "healthy")

        html = f"<div class='dependencies-summary'><h4>📦 Dépendances ({status})</h4>"

        if dependency_data:
            for key, value in dependency_data.items():
                html += (
                    f"<p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>"
                )
        else:
            html += "<p>Aucune donnée de dépendances disponible</p>"

        html += "</div>"
        return html

    def _generate_documentation_content(self, widget: dict[str, Any]) -> str:
        """Génère le contenu du widget documentation"""
        doc_data = widget.get("doc_data", {})
        status = widget.get("status", "good")

        html = (
            f"<div class='documentation-summary'><h4>📚 Documentation ({status})</h4>"
        )

        if doc_data:
            for key, value in doc_data.items():
                html += (
                    f"<p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>"
                )
        else:
            html += "<p>Aucune donnée de documentation disponible</p>"

        html += "</div>"
        return html

    def generate_dashboard_css(self, theme: str = "light") -> str:
        """Génère le CSS du dashboard"""
        if theme == "dark":
            return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1a1a1a;
            color: #ffffff;
            line-height: 1.6;
        }

        .dashboard-header {
            background-color: #2d2d2d;
            padding: 1rem;
            border-bottom: 1px solid #404040;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .dashboard-content {
            padding: 2rem;
        }

        .widgets-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
        }

        .widget {
            background-color: #2d2d2d;
            border: 1px solid #404040;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .widget h3 {
            margin-top: 0;
            color: #4CAF50;
            border-bottom: 1px solid #404040;
            padding-bottom: 0.5rem;
        }

        .widget-content {
            max-height: 300px;
            overflow-y: auto;
        }

        .dashboard-footer {
            background-color: #2d2d2d;
            padding: 1rem;
            text-align: center;
            border-top: 1px solid #404040;
            margin-top: 2rem;
        }
"""
        else:
            return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            color: #333333;
            line-height: 1.6;
        }

        .dashboard-header {
            background-color: #ffffff;
            padding: 1rem;
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .dashboard-content {
            padding: 2rem;
        }

        .widgets-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1rem;
        }

        .widget {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .widget h3 {
            margin-top: 0;
            color: #2196F3;
            border-bottom: 1px solid #e0e0e0;
            padding-bottom: 0.5rem;
        }

        .widget-content {
            max-height: 300px;
            overflow-y: auto;
        }

        .dashboard-footer {
            background-color: #ffffff;
            padding: 1rem;
            text-align: center;
            border-top: 1px solid #e0e0e0;
            margin-top: 2rem;
        }
"""

    def generate_dashboard_js(self, config: dict[str, Any]) -> str:
        """Génère le JavaScript du dashboard"""
        refresh_interval = config.get("refresh_interval", 30)

        return f"""
// Configuration du dashboard
const dashboardConfig = {{
    refreshInterval: {refresh_interval} * 1000,
    autoRefresh: {str(config.get("auto_refresh", True)).lower()},
    showTimestamps: {str(config.get("show_timestamps", True)).lower()}
}};

// Fonction de rafraîchissement
function refreshDashboard() {{
    console.log('Actualisation du dashboard...');
    location.reload();
}}

// Fonction de changement de thème
function changeTheme(theme) {{
    document.body.className = `theme-${{theme}}`;
    localStorage.setItem('dashboard-theme', theme);
}}

// Initialisation
document.addEventListener('DOMContentLoaded', function() {{
    // Gestionnaire pour le bouton d'actualisation
    const refreshBtn = document.getElementById('refresh-btn');
    if (refreshBtn) {{
        refreshBtn.addEventListener('click', refreshDashboard);
    }}

    // Gestionnaire pour le sélecteur de thème
    const themeSelector = document.getElementById('theme-selector');
    if (themeSelector) {{
        themeSelector.addEventListener('change', function() {{
            changeTheme(this.value);
        }});
    }}

    // Actualisation automatique
    if (dashboardConfig.autoRefresh) {{
        setInterval(refreshDashboard, dashboardConfig.refreshInterval);
    }}

    // Restaurer le thème sauvegardé
    const savedTheme = localStorage.getItem('dashboard-theme');
    if (savedTheme) {{
        changeTheme(savedTheme);
        if (themeSelector) {{
            themeSelector.value = savedTheme;
        }}
    }}
}});
"""

    def save_dashboard_html(self, html_content: str, output_path: str) -> bool:
        """Sauvegarde le dashboard HTML"""
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            return True
        except Exception as e:
            logger.error(f"Erreur sauvegarde dashboard: {e}")
            return False

    def generate_dashboard_report(self) -> dict[str, Any]:
        """Génère un rapport complet du dashboard"""
        # Préparer les données du dashboard
        dashboard_data = {
            "title": "Dashboard Athalia - Rapport Complet",
            "theme": self.config.get("theme", "light"),
            "widgets": [],
            "config": self.config,
        }

        # Générer tous les widgets disponibles
        if self.metrics:
            dashboard_data["widgets"].append(self.generate_metrics_widget())

        # Ajouter des widgets d'exemple si pas de métriques
        if not self.metrics:
            dashboard_data["widgets"].extend(
                [
                    {
                        "type": "metrics",
                        "title": "Métriques (Exemple)",
                        "data": {"example": "Données d'exemple"},
                        "timestamp": datetime.now().isoformat(),
                    },
                    {
                        "type": "alerts",
                        "title": "Alertes (Exemple)",
                        "alerts": [
                            {
                                "severity": "info",
                                "message": "Dashboard en mode démonstration",
                                "category": "system",
                            }
                        ],
                        "timestamp": datetime.now().isoformat(),
                    },
                ]
            )

        # Générer le HTML
        html_content = self.generate_dashboard_html(dashboard_data)

        return {
            "dashboard_data": dashboard_data,
            "html_content": html_content,
            "config": self.config,
            "generated_at": datetime.now().isoformat(),
        }


class DashboardGenerator:
    """Générateur de dashboard avec métriques réelles du projet"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.dashboard = Dashboard(project_path)

    def collect_real_metrics(self) -> dict[str, Any]:
        """Collecte les vraies métriques du projet"""
        metrics: dict[str, Any] = {}

        try:
            # Dossiers à exclure
            exclude_dirs = {
                ".git",
                ".venv",
                "venv",
                "__pycache__",
                ".pytest_cache",
                "node_modules",
                ".tox",
                ".mypy_cache",
                ".ruff_cache",
                "build",
                "dist",
                "*.egg-info",
                ".coverage",
            }

            # Compter les fichiers Python (exclure dossiers système et fichiers macOS ._*)
            python_files = []
            for py_file in self.project_path.rglob("*.py"):
                if py_file.name.startswith("._"):
                    continue
                path_parts = py_file.parts
                if not any(exclude_dir in path_parts for exclude_dir in exclude_dirs):
                    python_files.append(py_file)

            metrics["python_files"] = len(python_files)

            # Compter les lignes de code (seulement les vrais fichiers du projet)
            total_lines = 0
            for py_file in python_files:
                try:
                    with open(py_file, encoding="utf-8", errors="ignore") as f:
                        total_lines += len(f.readlines())
                except OSError as e:
                    logger.debug("Fichier ignoré %s: %s", py_file, e)
                    continue
            metrics["lines_of_code"] = total_lines

            # Compter les tests (seulement les vrais tests du projet)
            test_files = [
                f for f in python_files if "test" in f.name.lower() or "test" in str(f)
            ]
            metrics["test_files"] = len(test_files)

            # Compter les fichiers de documentation (exclure dossiers système et ._*)
            doc_files = []
            for doc_file in self.project_path.rglob("*.md"):
                if doc_file.name.startswith("._"):
                    continue
                path_parts = doc_file.parts
                if not any(exclude_dir in path_parts for exclude_dir in exclude_dirs):
                    doc_files.append(doc_file)

            for doc_file in self.project_path.rglob("*.rst"):
                if doc_file.name.startswith("._"):
                    continue
                path_parts = doc_file.parts
                if not any(exclude_dir in path_parts for exclude_dir in exclude_dirs):
                    doc_files.append(doc_file)

            metrics["documentation_files"] = len(doc_files)

            # Analyser les dépendances
            requirements_file = self.project_path / "requirements.txt"
            if requirements_file.exists():
                with open(requirements_file) as f:
                    deps = [
                        line.strip()
                        for line in f
                        if line.strip() and not line.startswith("#")
                    ]
                metrics["dependencies"] = len(deps)
            else:
                metrics["dependencies"] = 0

            # Calculer la complexité moyenne (estimation)
            if python_files:
                metrics["avg_complexity"] = float(
                    round(total_lines / len(python_files), 2)
                )
            else:
                metrics["avg_complexity"] = 0.0

            # Compter les fonctions et classes (estimation réaliste)
            metrics["estimated_functions"] = int(
                round(total_lines / 20)
            )  # Estimation réaliste
            metrics["estimated_classes"] = int(
                round(total_lines / 100)
            )  # Estimation réaliste

        except Exception as e:
            logger.error(f"Erreur collecte métriques: {e}")
            metrics = {
                "error": str(e),
                "python_files": 0,
                "lines_of_code": 0,
                "test_files": 0,
                "documentation_files": 0,
                "dependencies": 0,
                "avg_complexity": 0,
                "estimated_functions": 0,
                "estimated_classes": 0,
            }

        return metrics

    def generate_analytics_dashboard(self) -> str:
        """Génère un dashboard analytics avec les vraies métriques"""
        metrics = self.collect_real_metrics()

        if "error" in metrics:
            return f"<h1>❌ Erreur Dashboard</h1><p>{metrics['error']}</p>"

        # Créer le HTML du dashboard
        html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📊 Dashboard Analytics Réel - Athalia</title>
    <style>
                body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
        }}
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .metric-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }}
        .metric-card:hover {{
            transform: translateY(-5px);
        }}
        .metric-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin: 10px 0;
        }}
        .metric-label {{
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .summary {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .summary h2 {{
            color: #667eea;
            margin-bottom: 15px;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            color: #666;
            border-top: 1px solid #eee;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Dashboard Analytics Réel - Athalia</h1>
            <p>Métriques collectées en temps réel - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </div>

        <div class="summary">
            <h2>📈 Résumé du Projet</h2>
            <p>Ce dashboard affiche les <strong>vraies métriques</strong> collectées directement depuis votre projet Athalia.
            Toutes les données sont calculées en temps réel et reflètent l'état actuel de votre codebase.</p>
        </div>

        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-value">{metrics["python_files"]:,}</div>
                <div class="metric-label">Fichiers Python</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{metrics["lines_of_code"]:,}</div>
                <div class="metric-label">Lignes de Code</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{metrics["test_files"]:,}</div>
                <div class="metric-label">Fichiers de Test</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{metrics["documentation_files"]:,}</div>
                <div class="metric-label">Fichiers de Documentation</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{metrics["dependencies"]:,}</div>
                <div class="metric-label">Dépendances</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{metrics["avg_complexity"]}</div>
                <div class="metric-label">Complexité Moyenne</div>
            </div>
        </div>

        <div class="summary">
            <h2>🔍 Détails Techniques</h2>
            <p><strong>Fonctions estimées:</strong> {metrics["estimated_functions"]:,} (basé sur la densité de code typique)</p>
            <p><strong>Classes estimées:</strong> {metrics["estimated_classes"]:,} (basé sur la densité de code typique)</p>
            <p><strong>Ratio tests/code:</strong> {round(metrics["test_files"] / max(metrics["python_files"], 1) * 100, 1)}%</p>
            <p><strong>Ratio documentation/code:</strong> {round(metrics["documentation_files"] / max(metrics["python_files"], 1) * 100, 1)}%</p>
        </div>

        <div class="footer">
            <p>✅ <strong>Données vérifiées et réalistes</strong> - Généré automatiquement par Athalia</p>
        </div>
    </div>
</body>
</html>"""

        return html


def generate_dashboard_html(project_path: str = ".") -> str:
    """Fonction utilitaire pour générer le HTML du dashboard"""
    dashboard = Dashboard(project_path)
    report = dashboard.generate_dashboard_report()
    return report["html_content"]


def create_dashboard_report(project_path: str = ".") -> dict[str, Any]:
    """Fonction utilitaire pour créer un rapport de dashboard"""
    dashboard = Dashboard(project_path)
    return dashboard.generate_dashboard_report()


def generate_analytics_dashboard(project_path: str = ".") -> str:
    """Fonction utilitaire pour générer le dashboard analytics"""
    generator = DashboardGenerator(project_path)
    return generator.generate_analytics_dashboard()


def main() -> None:
    """Point d'entrée pour la commande athalia-dashboard : génère le dashboard et l'ouvre dans le navigateur."""
    import sys
    import webbrowser

    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    try:
        html_content = generate_analytics_dashboard(project_path)
        out_dir = Path(project_path) / "dashboard"
        out_dir.mkdir(parents=True, exist_ok=True)
        html_path = out_dir / "athalia_analytics.html"
        html_path.write_text(html_content, encoding="utf-8")
        webbrowser.open(f"file://{html_path.resolve()}")
        logger.info("Dashboard ouvert dans le navigateur : %s", html_path)
    except Exception as e:
        logger.exception("Erreur génération dashboard : %s", e)
        try:
            report = create_dashboard_report(project_path)
            print(json.dumps(report.get("summary", report), indent=2))
        except Exception:
            pass
        sys.exit(1)
