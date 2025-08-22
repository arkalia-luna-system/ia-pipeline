#!/usr/bin/env python3
"""
Dashboard de sécurité web pour Athalia
Interface moderne pour visualiser les rapports de sécurité en temps réel
"""

import json
import logging
import os
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any

# Import des composants Athalia réels
try:
    from athalia_core.core.cache_manager import CacheManager
    from athalia_core.metrics.collector import MetricsCollector
    from athalia_core.quality.code_linter import CodeLinter
    from athalia_core.validation.security_validator import CommandSecurityValidator

    ATHALIA_AVAILABLE = True
except ImportError as e:
    logging.warning(f"Composants Athalia non disponibles: {e}")
    ATHALIA_AVAILABLE = False

logger = logging.getLogger(__name__)


class SecurityDashboard:
    """Dashboard de sécurité web moderne avec vraie intégration Athalia"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.dashboard_dir = self.project_path / "dashboard" / "security"
        self.dashboard_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir = self.project_path / ".github" / "workflows" / "artifacts"

        # Initialisation des composants Athalia
        self.athalia_components = self._initialize_athalia_components()

    def _initialize_athalia_components(self) -> dict[str, Any]:
        """Initialise les composants Athalia pour le dashboard de sécurité"""
        if not ATHALIA_AVAILABLE:
            return {}

        try:
            components: dict[str, Any] = {}

            # Initialisation sécurisée de chaque composant
            try:
                components["security_validator"] = CommandSecurityValidator()
            except Exception as e:
                logger.warning(
                    f"Impossible d'initialiser CommandSecurityValidator: {e}"
                )

            try:
                components["code_linter"] = CodeLinter(str(self.project_path))
            except Exception as e:
                logger.warning(f"Impossible d'initialiser CodeLinter: {e}")

            try:
                components["cache_manager"] = CacheManager(".athalia_cache")
            except Exception as e:
                logger.warning(f"Impossible d'initialiser CacheManager: {e}")

            try:
                components["metrics_collector"] = MetricsCollector(
                    str(self.project_path)
                )
            except Exception as e:
                logger.warning(f"Impossible d'initialiser MetricsCollector: {e}")

            return components
        except Exception as e:
            logger.error(
                f"Erreur critique d'initialisation des composants Athalia: {e}"
            )
            return {}

    def collect_security_data(self) -> dict[str, Any]:
        """Collecte les vraies données de sécurité depuis les composants Athalia"""
        security_data: dict[str, Any] = {
            "timestamp": datetime.now().isoformat(),
            "project_path": str(self.project_path),
            "athalia_available": ATHALIA_AVAILABLE,
            "security_score": 0,
            "vulnerabilities": {"high": 0, "medium": 0, "low": 0},
            "security_checks": {},
            "linting_results": {},
            "cache_security": {},
            "recommendations": [],
        }

        if not self.athalia_components:
            security_data["recommendations"].append(
                "Composants Athalia non disponibles"
            )
            return security_data

        try:
            # Collecte des données de sécurité
            if "security_validator" in self.athalia_components:
                security_validator = self.athalia_components["security_validator"]

                # Scan de sécurité complet avec la vraie méthode
                if hasattr(security_validator, "run_comprehensive_scan"):
                    scan_results = security_validator.run_comprehensive_scan(
                        str(self.project_path)
                    )
                    security_data["security_checks"][
                        "comprehensive_scan"
                    ] = scan_results

                    # Calcul du score de sécurité intelligent et contextuel
                    total_vulns = scan_results.get("vulnerabilities_found", 0)
                    if total_vulns > 0:
                        vulnerabilities = scan_results.get("vulnerabilities", [])

                        # Classification intelligente des vulnérabilités
                        high_count = sum(
                            1
                            for v in vulnerabilities
                            if v.get("type") in ["xss", "sql_injection"]
                        )
                        medium_count = sum(
                            1
                            for v in vulnerabilities
                            if v.get("type") == "dangerous_function"
                        )
                        low_count = total_vulns - high_count - medium_count

                        # Score intelligent : pénalise plus les vraies vulnérabilités critiques
                        critical_penalty = high_count * 3  # XSS/SQL = très grave
                        medium_penalty = (
                            medium_count * 1
                        )  # open()/__import__ = moins grave en dev
                        total_penalty = critical_penalty + medium_penalty

                        # Score de base 85 pour un projet de développement (normal)
                        base_score = 85
                        security_data["security_score"] = max(
                            20, base_score - total_penalty
                        )

                        security_data["vulnerabilities"]["high"] = high_count
                        security_data["vulnerabilities"]["medium"] = medium_count
                        security_data["vulnerabilities"]["low"] = low_count
                    else:
                        security_data["security_score"] = 100
                        security_data["vulnerabilities"] = {
                            "high": 0,
                            "medium": 0,
                            "low": 0,
                        }

            # Collecte des résultats de linting
            if "code_linter" in self.athalia_components:
                code_linter = self.athalia_components["code_linter"]

                if hasattr(code_linter, "run_security_checks"):
                    linting_results = code_linter.run_security_checks()
                    security_data["linting_results"] = linting_results

                    # Ajout des vulnérabilités de linting
                    if linting_results and isinstance(linting_results, dict):
                        lint_vulns = linting_results.get("security_issues", {})
                        if isinstance(lint_vulns, dict):
                            for level, count in lint_vulns.items():
                                if (
                                    isinstance(level, str)
                                    and isinstance(count, int | float)
                                    and level in security_data["vulnerabilities"]
                                ):
                                    security_data["vulnerabilities"][level] += int(
                                        count
                                    )

            # Collecte des métriques de cache
            if "cache_manager" in self.athalia_components:
                cache_manager = self.athalia_components["cache_manager"]

                if hasattr(cache_manager, "get_security_stats"):
                    cache_stats = cache_manager.get_security_stats()
                    security_data["cache_security"] = cache_stats

            # Génération des recommandations
            security_data["recommendations"] = self._generate_security_recommendations(
                security_data
            )

        except Exception as e:
            logger.error(f"Erreur lors de la collecte des données de sécurité: {e}")
            security_data["error"] = str(e)

        return security_data

    def _generate_security_recommendations(
        self, security_data: dict[str, Any]
    ) -> list[str]:
        """Génère des recommandations de sécurité basées sur les vraies données"""
        recommendations = []

        # Recommandations basées sur le score de sécurité
        security_score = security_data.get("security_score", 0)
        if security_score < 50:
            recommendations.append(
                "🚨 CRITIQUE: Score de sécurité très faible - Audit immédiat requis"
            )
        elif security_score < 70:
            recommendations.append(
                "⚠️ ATTENTION: Score de sécurité faible - Actions correctives nécessaires"
            )
        elif security_score < 85:
            recommendations.append(
                "🔶 AMÉLIORATION: Score de sécurité acceptable mais peut être amélioré"
            )
        else:
            recommendations.append(
                "✅ EXCELLENT: Score de sécurité élevé - Maintenir les bonnes pratiques"
            )

        # Recommandations basées sur les vulnérabilités
        vulnerabilities = security_data.get("vulnerabilities", {})
        if vulnerabilities.get("high", 0) > 0:
            recommendations.append(
                "🚨 CRITIQUE: Vulnérabilités critiques détectées - Correction immédiate requise"
            )
        if vulnerabilities.get("medium", 0) > 5:
            recommendations.append(
                "⚠️ ATTENTION: Nombre élevé de vulnérabilités moyennes - Plan de correction nécessaire"
            )
        if vulnerabilities.get("low", 0) > 10:
            recommendations.append(
                "🔶 AMÉLIORATION: Nombre élevé de vulnérabilités mineures - Nettoyage recommandé"
            )

        # Recommandations basées sur les composants
        if not security_data.get("athalia_available", False):
            recommendations.append(
                "🔧 TECHNIQUE: Installer/mettre à jour les composants Athalia pour une sécurité optimale"
            )

        # Recommandations générales
        if not recommendations:
            recommendations.append("✅ SÉCURISÉ: Aucune action immédiate requise")

        recommendations.append(
            "📚 DOCUMENTATION: Consulter le guide de sécurité Athalia pour plus d'informations"
        )

        return recommendations

    def generate_security_dashboard(self) -> str:
        """Génère le dashboard de sécurité HTML avec vraies données"""
        # Collecter les vraies données de sécurité
        security_data = self.collect_security_data()

        # Générer le HTML avec les vraies données
        dashboard_html = self._generate_dashboard_html(security_data)

        # Créer le fichier dashboard
        dashboard_file = self.dashboard_dir / "security_dashboard.html"
        with open(dashboard_file, "w", encoding="utf-8") as f:
            f.write(dashboard_html)

        logger.info(
            f"Dashboard de sécurité généré avec vraies données: {dashboard_file}"
        )
        return str(dashboard_file)

    def _generate_dashboard_html(self, security_data: dict[str, Any]) -> str:
        """Génère le HTML du dashboard avec les vraies données de sécurité"""

        # Extraction des données pour le template
        security_score = security_data.get("security_score", 0)
        vulnerabilities = security_data.get(
            "vulnerabilities", {"high": 0, "medium": 0, "low": 0}
        )
        recommendations = security_data.get("recommendations", [])
        timestamp = security_data.get("timestamp", "")
        project_path = security_data.get("project_path", "")

        # Calcul des métriques
        total_vulnerabilities = sum(vulnerabilities.values())
        high_vulns = vulnerabilities.get("high", 0)
        medium_vulns = vulnerabilities.get("medium", 0)
        low_vulns = vulnerabilities.get("low", 0)

        # Couleurs et statuts
        score_color = (
            "#28a745"
            if security_score >= 85
            else "#ffc107" if security_score >= 70 else "#dc3545"
        )
        score_status = (
            "Sécurisé"
            if security_score >= 85
            else "Attention" if security_score >= 70 else "Critique"
        )

        html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Sécurité - Athalia</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}

        .header {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            font-size: 3em;
            color: #667eea;
            margin-bottom: 10px;
            font-weight: 300;
        }}

        .header p {{
            font-size: 1.2em;
            color: #666;
        }}

        .security-overview {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .security-score {{
            font-size: 4em;
            font-weight: 700;
            color: {score_color};
            margin: 20px 0;
        }}

        .security-status {{
            font-size: 1.5em;
            color: {score_color};
            margin-bottom: 20px;
        }}

        .vulnerabilities-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}

        .vuln-card {{
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            border-left: 4px solid;
        }}

        .vuln-high {{
            border-left-color: #dc3545;
            background: #f8d7da;
        }}

        .vuln-medium {{
            border-left-color: #ffc107;
            background: #fff3cd;
        }}

        .vuln-low {{
            border-left-color: #28a745;
            background: #d4edda;
        }}

        .vuln-number {{
            font-size: 2.5em;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .vuln-high .vuln-number {{
            color: #dc3545;
        }}

        .vuln-medium .vuln-number {{
            color: #ffc107;
        }}

        .vuln-low .vuln-number {{
            color: #28a745;
        }}

        .security-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }}

        .security-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .security-card h3 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.5em;
        }}

        .recommendations {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .recommendation-item {{
            background: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #667eea;
        }}

        .chart-container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .footer {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            color: #666;
        }}

        .refresh-btn {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-size: 1.1em;
            cursor: pointer;
            margin: 20px 0;
            transition: all 0.3s ease;
        }}

        .refresh-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }}

        .metric-row {{
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 5px;
        }}

        .metric-label {{
            font-weight: bold;
        }}

        .metric-value {{
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ Dashboard Sécurité Athalia</h1>
            <p>Surveillance en temps réel de la sécurité du projet</p>
        </div>

        <div class="security-overview">
            <h2>Vue d'ensemble de la sécurité</h2>
            <div class="security-score">{security_score}/100</div>
            <div class="security-status">{score_status}</div>
            <p>Projet: {project_path}</p>
            <p>Dernière mise à jour: {timestamp}</p>
            <button class="refresh-btn" onclick="location.reload()">🔄 Actualiser</button>
        </div>

        <div class="vulnerabilities-grid">
            <div class="vuln-card vuln-high">
                <div class="vuln-number">{high_vulns}</div>
                <div>Vulnérabilités Critiques</div>
            </div>
            <div class="vuln-card vuln-medium">
                <div class="vuln-number">{medium_vulns}</div>
                <div>Vulnérabilités Moyennes</div>
            </div>
            <div class="vuln-card vuln-low">
                <div class="vuln-number">{low_vulns}</div>
                <div>Vulnérabilités Mineures</div>
            </div>
            <div class="vuln-card">
                <div class="vuln-number">{total_vulnerabilities}</div>
                <div>Total Vulnérabilités</div>
            </div>
        </div>

        <div class="security-grid">
            <div class="security-card">
                <h3>🔍 Validation des Commandes</h3>
                <div id="commandValidationDetails">
                    {self._generate_command_validation_html(security_data)}
                </div>
            </div>

            <div class="security-card">
                <h3>📝 Analyse de Code</h3>
                <div id="codeAnalysisDetails">
                    {self._generate_code_analysis_html(security_data)}
                </div>
            </div>

            <div class="security-card">
                <h3>💾 Cache et Performance</h3>
                <div id="cacheSecurityDetails">
                    {self._generate_cache_security_html(security_data)}
                </div>
            </div>

            <div class="security-card">
                <h3>📊 Métriques de Sécurité</h3>
                <div id="securityMetricsDetails">
                    {self._generate_security_metrics_html(security_data)}
                </div>
            </div>
        </div>

        <div class="chart-container">
            <h3>📈 Graphiques de Sécurité</h3>
            <canvas id="securityChart" width="400" height="200"></canvas>
        </div>

        <div class="recommendations">
            <h3>💡 Recommandations de Sécurité</h3>
            {self._generate_recommendations_html(recommendations)}
        </div>

        <div class="footer">
            <p>🕒 Dernière mise à jour: {timestamp}</p>
            <p>🛡️ Dashboard de sécurité généré automatiquement par Athalia v12.0.0</p>
        </div>
    </div>

    <script>
        // Graphique des vulnérabilités
        const ctx = document.getElementById('securityChart').getContext('2d');
        new Chart(ctx, {{
            type: 'doughnut',
            data: {{
                labels: ['Critiques', 'Moyennes', 'Mineures', 'Sécurisé'],
                datasets: [{{
                    data: [{high_vulns}, {medium_vulns}, {low_vulns}, {max(0, 100 - total_vulnerabilities)}],
                    backgroundColor: [
                        '#dc3545',
                        '#ffc107',
                        '#28a745',
                        '#6c757d'
                    ],
                    borderWidth: 2,
                    borderColor: '#fff'
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    title: {{
                        display: true,
                        text: 'Répartition des Vulnérabilités'
                    }},
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});

        // Actualisation automatique toutes les 5 minutes
        setInterval(() => {{
            location.reload();
        }}, 300000);
    </script>
</body>
</html>"""

        return html_template

    def _generate_command_validation_html(self, security_data: dict[str, Any]) -> str:
        """Génère le HTML pour la validation des commandes"""
        command_validation = security_data.get("security_checks", {}).get(
            "command_validation", {}
        )

        if not command_validation:
            return "<p>Aucune donnée de validation disponible</p>"

        html = ""
        for key, value in command_validation.items():
            if isinstance(value, int | float):
                html += f"""
                <div class="metric-row">
                    <span class="metric-label">{key.replace('_', ' ').title()}</span>
                    <span class="metric-value">{value}</span>
                </div>
                """

        return html if html else "<p>Données de validation en cours de collecte...</p>"

    def _generate_code_analysis_html(self, security_data: dict[str, Any]) -> str:
        """Génère le HTML pour l'analyse de code"""
        linting_results = security_data.get("linting_results", {})

        if not linting_results:
            return "<p>Aucune analyse de code disponible</p>"

        html = ""
        for key, value in linting_results.items():
            if isinstance(value, int | float):
                html += f"""
                <div class="metric-row">
                    <span class="metric-label">{key.replace('_', ' ').title()}</span>
                    <span class="metric-value">{value}</span>
                </div>
                """

        return html if html else "<p>Analyse de code en cours...</p>"

    def _generate_cache_security_html(self, security_data: dict[str, Any]) -> str:
        """Génère le HTML pour la sécurité du cache"""
        cache_security = security_data.get("cache_security", {})

        if not cache_security:
            return "<p>Aucune donnée de cache disponible</p>"

        html = ""
        for key, value in cache_security.items():
            if isinstance(value, int | float):
                html += f"""
                <div class="metric-row">
                    <span class="metric-label">{key.replace('_', ' ').title()}</span>
                    <span class="metric-value">{value}</span>
                </div>
                """

        return html if html else "<p>Métriques de cache en cours de collecte...</p>"

    def _generate_security_metrics_html(self, security_data: dict[str, Any]) -> str:
        """Génère le HTML pour les métriques de sécurité"""
        html = f"""
        <div class="metric-row">
            <span class="metric-label">Score Global</span>
            <span class="metric-value">{security_data.get('security_score', 0)}/100</span>
        </div>
        <div class="metric-row">
            <span class="metric-label">Vulnérabilités Total</span>
            <span class="metric-value">{sum(security_data.get('vulnerabilities', {}).values())}</span>
        </div>
        <div class="metric-row">
            <span class="metric-label">Composants Athalia</span>
            <span class="metric-value">{'✅ Disponibles' if security_data.get('athalia_available') else '❌ Non disponibles'}</span>
        </div>
        """

        return html

    def _generate_recommendations_html(self, recommendations: list[str]) -> str:
        """Génère le HTML pour les recommandations"""
        if not recommendations:
            return "<p>Aucune recommandation disponible</p>"

        html = ""
        for recommendation in recommendations:
            html += f'<div class="recommendation-item">{recommendation}</div>'

        return html

    def open_dashboard(self):
        """Ouvre le dashboard de sécurité dans le navigateur"""
        try:
            dashboard_file = self.generate_security_dashboard()
            if dashboard_file and Path(dashboard_file).exists():
                webbrowser.open(f"file://{Path(dashboard_file).absolute()}")
                logger.info("🌐 Dashboard de sécurité ouvert dans le navigateur")
            else:
                logger.error("❌ Impossible de générer le dashboard de sécurité")
        except Exception as e:
            logger.error(f"Erreur lors de l'ouverture du dashboard: {e}")


# Fonction principale pour exécution directe
def main():
    """Fonction principale pour exécution directe du dashboard de sécurité"""
    import argparse

    parser = argparse.ArgumentParser(description="Dashboard de sécurité Athalia")
    parser.add_argument(
        "--project-path", default=".", help="Chemin du projet à analyser"
    )
    parser.add_argument(
        "--open", action="store_true", help="Ouvrir le dashboard dans le navigateur"
    )
    parser.add_argument(
        "--generate-only",
        action="store_true",
        help="Générer le dashboard sans l'ouvrir",
    )

    args = parser.parse_args()

    # Initialisation du dashboard
    security_dashboard = SecurityDashboard(args.project_path)

    if args.generate_only:
        dashboard_file = security_dashboard.generate_security_dashboard()
        print(f"📊 Dashboard de sécurité généré: {dashboard_file}")
    elif args.open:
        security_dashboard.open_dashboard()
    else:
        # Par défaut, générer et ouvrir
        print("🚀 Génération du dashboard de sécurité...")
        dashboard_file = security_dashboard.generate_security_dashboard()
        print(f"📊 Dashboard généré: {dashboard_file}")

        print("🌐 Ouverture dans le navigateur...")
        security_dashboard.open_dashboard()


if __name__ == "__main__":
    main()
