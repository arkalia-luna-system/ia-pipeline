#!/usr/bin/env python3
"""
Module dashboard pour Athalia
Interface de visualisation et monitoring
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

logger = logging.getLogger(__name__)


class Dashboard:
    """Dashboard pour visualisation des métriques"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.metrics = {}
        self.config = self.load_dashboard_config()

    def load_dashboard_config(
        self, config_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """Charge la configuration du dashboard"""
        default_config = {
            "theme": "light",
            "refresh_interval": 30,
            "widgets": ["metrics", "charts", "alerts", "performance", "security"],
            "layout": "grid",
            "auto_refresh": True,
            "show_timestamps": True,
        }

        if config_path:
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    user_config = yaml.safe_load(f)
                    default_config.update(user_config)
            except Exception as e:
                logger.warning(
                    f"Impossible de charger la configuration {config_path}: {e}"
                )

        return default_config

    def generate_metrics_widget(self) -> Dict[str, Any]:
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

    def generate_charts_widget(self, chart_data: Dict[str, Any]) -> Dict[str, Any]:
        """Génère le widget graphiques"""
        widget = {
            "type": "charts",
            "title": "Graphiques et Tendances",
            "charts": chart_data,
            "timestamp": datetime.now().isoformat(),
            "chart_types": ["bar", "line", "pie", "radar"],
        }

        return widget

    def generate_alerts_widget(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
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
        self, performance_data: Dict[str, Any]
    ) -> Dict[str, Any]:
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

    def generate_security_widget(self, security_data: Dict[str, Any]) -> Dict[str, Any]:
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
        self, coverage_data: Dict[str, Any]
    ) -> Dict[str, Any]:
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
        self, dependency_data: Dict[str, Any]
    ) -> Dict[str, Any]:
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

    def generate_documentation_widget(self, doc_data: Dict[str, Any]) -> Dict[str, Any]:
        """Génère le widget documentation"""
        widget = {
            "type": "documentation",
            "title": "Documentation du Projet",
            "doc_data": doc_data,
            "timestamp": datetime.now().isoformat(),
            "status": "complete",
        }

        # Déterminer le statut de la documentation
        doc_coverage = doc_data.get("doc_coverage_percentage", 0)
        if doc_coverage < 30:
            widget["status"] = "incomplete"
        elif doc_coverage < 70:
            widget["status"] = "partial"

        return widget

    def generate_git_widget(self, git_data: Dict[str, Any]) -> Dict[str, Any]:
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
        self, widgets: List[Dict[str, Any]], layout_type: str = "grid"
    ) -> Dict[str, Any]:
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

    def generate_dashboard_html(self, dashboard_data: Dict[str, Any]) -> str:
        """Génère le HTML du dashboard"""
        theme = dashboard_data.get("theme", "light")
        widgets = dashboard_data.get("widgets", [])
        config = dashboard_data.get("config", {})

        html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dashboard_data.get('title', 'Dashboard Athalia')}</title>
    <style>
        {self.generate_dashboard_css(theme)}
    </style>
</head>
<body class="theme-{theme}">
    <header class="dashboard-header">
        <h1>{dashboard_data.get('title', 'Dashboard Athalia')}</h1>
        <div class="dashboard-controls">
            <button id="refresh-btn">Actualiser</button>
            <select id="theme-selector">
                <option value="light" {'selected' if theme == 'light' else ''}>Clair</option>
                <option value="dark" {'selected' if theme == 'dark' else ''}>Sombre</option>
            </select>
        </div>
    </header>

    <main class="dashboard-content">
        <div class="widgets-container">
"""

        for widget in widgets:
            html_template += f"""
            <div class="widget widget-{widget.get('type', 'default')}">
                <h3>{widget.get('title', 'Widget')}</h3>
                <div class="widget-content">
                    <pre>{json.dumps(widget, indent=2, ensure_ascii=False)}</pre>
                </div>
            </div>
"""

        html_template += f"""
        </div>
    </main>

    <footer class="dashboard-footer">
        <p>Généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </footer>

    <script>
        {self.generate_dashboard_js(config)}
    </script>
</body>
</html>"""

        return html_template

    def generate_dashboard_css(self, theme: str = "light") -> str:
        """Génère le CSS du dashboard"""
        if theme == "dark":
            return """
body {
    background-color: #1a1a1a;
    color: #ffffff;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
}

.dashboard-header {
    background-color: #2d2d2d;
    padding: 1rem;
    border-bottom: 1px solid #444;
    display: flex;
    justify-content: space-between;
    align-items: center;
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
    border: 1px solid #444;
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.widget h3 {
    margin-top: 0;
    color: #4CAF50;
    border-bottom: 1px solid #444;
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
    border-top: 1px solid #444;
    margin-top: 2rem;
}
"""
        else:
            return """
body {
    background-color: #f5f5f5;
    color: #333333;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
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

    def generate_dashboard_js(self, config: Dict[str, Any]) -> str:
        """Génère le JavaScript du dashboard"""
        refresh_interval = config.get("refresh_interval", 30)

        return f"""
// Configuration du dashboard
const dashboardConfig = {{
    refreshInterval: {refresh_interval} * 1000,
    autoRefresh: {str(config.get('auto_refresh', True)).lower()},
    showTimestamps: {str(config.get('show_timestamps', True)).lower()}
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

    def generate_dashboard_report(self) -> Dict[str, Any]:
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


def generate_dashboard_html(project_path: str = ".") -> str:
    """Fonction utilitaire pour générer le HTML du dashboard"""
    dashboard = Dashboard(project_path)
    report = dashboard.generate_dashboard_report()
    return report["html_content"]


def create_dashboard_report(project_path: str = ".") -> Dict[str, Any]:
    """Fonction utilitaire pour créer un rapport de dashboard"""
    dashboard = Dashboard(project_path)
    return dashboard.generate_dashboard_report()
