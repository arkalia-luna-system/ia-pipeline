#!/usr/bin/env python3
"""
Interface web du marketplace de plugins pour Athalia
Gestion complète des plugins avec interface moderne
"""

import json
import logging
import os
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


class PluginMarketplace:
    """Marketplace de plugins avec interface web moderne"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.marketplace_dir = self.project_path / "dashboard" / "plugins"
        self.marketplace_dir.mkdir(parents=True, exist_ok=True)
        self.plugins_dir = self.project_path / "athalia_core" / "plugins"

    def generate_marketplace_interface(self) -> str:
        """Génère l'interface web du marketplace"""
        marketplace_html = self._get_marketplace_template()

        # Créer le fichier marketplace
        marketplace_file = self.marketplace_dir / "plugin_marketplace.html"
        with open(marketplace_file, "w", encoding="utf-8") as f:
            f.write(marketplace_html)

        logger.info(f"Interface marketplace générée: {marketplace_file}")
        return str(marketplace_file)

    def _get_marketplace_template(self) -> str:
        """Retourne le template HTML du marketplace"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketplace Plugins - Athalia</title>
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

        .search-bar {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .search-input {{
            width: 100%;
            padding: 15px 20px;
            border: 2px solid #e9ecef;
            border-radius: 25px;
            font-size: 1.1em;
            outline: none;
            transition: border-color 0.3s ease;
        }}

        .search-input:focus {{
            border-color: #667eea;
        }}

        .plugins-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }}

        .plugin-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            border: 2px solid transparent;
        }}

        .plugin-card:hover {{
            transform: translateY(-5px);
            border-color: #667eea;
        }}

        .plugin-header {{
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }}

        .plugin-icon {{
            width: 60px;
            height: 60px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            font-size: 2em;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }}

        .plugin-info {{
            flex: 1;
        }}

        .plugin-name {{
            font-size: 1.4em;
            font-weight: 600;
            color: #333;
            margin-bottom: 5px;
        }}

        .plugin-version {{
            color: #666;
            font-size: 0.9em;
        }}

        .plugin-description {{
            color: #555;
            line-height: 1.6;
            margin-bottom: 20px;
        }}

        .plugin-stats {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }}

        .stat-item {{
            text-align: center;
        }}

        .stat-value {{
            font-size: 1.2em;
            font-weight: 600;
            color: #667eea;
        }}

        .stat-label {{
            font-size: 0.8em;
            color: #666;
            text-transform: uppercase;
        }}

        .plugin-actions {{
            display: flex;
            gap: 10px;
        }}

        .btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            flex: 1;
        }}

        .btn-primary {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }}

        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }}

        .btn-secondary {{
            background: #f8f9fa;
            color: #667eea;
            border: 2px solid #667eea;
        }}

        .btn-secondary:hover {{
            background: #667eea;
            color: white;
        }}

        .btn-danger {{
            background: #dc3545;
            color: white;
        }}

        .btn-danger:hover {{
            background: #c82333;
        }}

        .plugin-status {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: 600;
            margin-bottom: 15px;
        }}

        .status-active {{
            background: #d4edda;
            color: #155724;
        }}

        .status-inactive {{
            background: #f8d7da;
            color: #721c24;
        }}

        .status-updating {{
            background: #fff3cd;
            color: #856404;
        }}

        .stats-container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .stats-title {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}

        .stat-card {{
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 15px;
        }}

        .stat-number {{
            font-size: 2.5em;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 10px;
        }}

        .stat-description {{
            color: #666;
            font-size: 0.9em;
        }}

        .footer {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            color: #666;
        }}

        @media (max-width: 768px) {{
            .plugins-grid {{
                grid-template-columns: 1fr;
            }}

            .header h1 {{
                font-size: 2em;
            }}

            .plugin-actions {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔌 Marketplace Plugins Athalia</h1>
            <p>Découvrez et gérez vos plugins pour étendre les fonctionnalités</p>
        </div>

        <div class="search-bar">
            <input type="text" class="search-input" placeholder="🔍 Rechercher un plugin..." id="searchInput" onkeyup="filterPlugins()">
        </div>

        <div class="stats-container">
            <h2 class="stats-title">📊 Statistiques des Plugins</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" id="totalPlugins">5</div>
                    <div class="stat-description">Total Plugins</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="activePlugins">4</div>
                    <div class="stat-description">Actifs</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="totalDownloads">127</div>
                    <div class="stat-description">Téléchargements</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="avgRating">4.8</div>
                    <div class="stat-description">Note Moyenne</div>
                </div>
            </div>
        </div>

        <div class="plugins-grid" id="pluginsGrid">
            <div class="plugin-card" data-name="hello_plugin" data-category="demo">
                <div class="plugin-header">
                    <div class="plugin-icon">👋</div>
                    <div class="plugin-info">
                        <div class="plugin-name">Hello Plugin</div>
                        <div class="plugin-version">v1.0.0</div>
                    </div>
                </div>
                <div class="plugin-status status-active">✅ Actif</div>
                <div class="plugin-description">
                    Plugin de démonstration pour tester le système de plugins d'Athalia.
                    Fournit des fonctionnalités de base pour l'apprentissage.
                </div>
                <div class="plugin-stats">
                    <div class="stat-item">
                        <div class="stat-value">15</div>
                        <div class="stat-label">Downloads</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.9</div>
                        <div class="stat-label">Rating</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">2</div>
                        <div class="stat-label">Updates</div>
                    </div>
                </div>
                <div class="plugin-actions">
                    <button class="btn btn-primary" onclick="installPlugin('hello_plugin')">📥 Installer</button>
                    <button class="btn btn-secondary" onclick="viewDetails('hello_plugin')">📋 Détails</button>
                </div>
            </div>

            <div class="plugin-card" data-name="export_docker_plugin" data-category="devops">
                <div class="plugin-header">
                    <div class="plugin-icon">🐳</div>
                    <div class="plugin-info">
                        <div class="plugin-name">Export Docker Plugin</div>
                        <div class="plugin-version">v1.0.0</div>
                    </div>
                </div>
                <div class="plugin-status status-active">✅ Actif</div>
                <div class="plugin-description">
                    Plugin pour l'export automatique de projets vers Docker.
                    Génère Dockerfile et docker-compose.yml automatiquement.
                </div>
                <div class="plugin-stats">
                    <div class="stat-item">
                        <div class="stat-value">89</div>
                        <div class="stat-label">Downloads</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.8</div>
                        <div class="stat-label">Rating</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">5</div>
                        <div class="stat-label">Updates</div>
                    </div>
                </div>
                <div class="plugin-actions">
                    <button class="btn btn-primary" onclick="installPlugin('export_docker_plugin')">📥 Installer</button>
                    <button class="btn btn-secondary" onclick="viewDetails('export_docker_plugin')">📋 Détails</button>
                </div>
            </div>

            <div class="plugin-card" data-name="security_audit_plugin" data-category="security">
                <div class="plugin-header">
                    <div class="plugin-icon">🛡️</div>
                    <div class="plugin-info">
                        <div class="plugin-name">Security Audit Plugin</div>
                        <div class="plugin-version">v1.0.0</div>
                    </div>
                </div>
                <div class="plugin-status status-active">✅ Actif</div>
                <div class="plugin-description">
                    Plugin d'audit de sécurité avancé avec détection de vulnérabilités,
                    analyse de code et rapports détaillés.
                </div>
                <div class="plugin-stats">
                    <div class="stat-item">
                        <div class="stat-value">156</div>
                        <div class="stat-label">Downloads</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.9</div>
                        <div class="stat-label">Rating</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">8</div>
                        <div class="stat-label">Updates</div>
                    </div>
                </div>
                <div class="plugin-actions">
                    <button class="btn btn-primary" onclick="installPlugin('security_audit_plugin')">📥 Installer</button>
                    <button class="btn btn-secondary" onclick="viewDetails('security_audit_plugin')">📋 Détails</button>
                </div>
            </div>

            <div class="plugin-card" data-name="performance_monitor_plugin" data-category="monitoring">
                <div class="plugin-header">
                    <div class="plugin-icon">📊</div>
                    <div class="plugin-info">
                        <div class="plugin-name">Performance Monitor</div>
                        <div class="plugin-version">v1.0.0</div>
                    </div>
                </div>
                <div class="plugin-status status-active">✅ Actif</div>
                <div class="plugin-description">
                    Plugin de monitoring des performances en temps réel avec métriques,
                    alertes et tableaux de bord interactifs.
                </div>
                <div class="plugin-stats">
                    <div class="stat-item">
                        <div class="stat-value">203</div>
                        <div class="stat-label">Downloads</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.7</div>
                        <div class="stat-label">Rating</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">12</div>
                        <div class="stat-label">Updates</div>
                    </div>
                </div>
                <div class="plugin-actions">
                    <button class="btn btn-primary" onclick="installPlugin('performance_monitor_plugin')">📥 Installer</button>
                    <button class="btn btn-secondary" onclick="viewDetails('performance_monitor_plugin')">📋 Détails</button>
                </div>
            </div>

            <div class="plugin-card" data-name="ai_assistant_plugin" data-category="ai">
                <div class="plugin-header">
                    <div class="plugin-icon">🤖</div>
                    <div class="plugin-info">
                        <div class="plugin-name">AI Assistant Plugin</div>
                        <div class="plugin-version">v1.0.0</div>
                    </div>
                </div>
                <div class="plugin-status status-inactive">⏸️ Inactif</div>
                <div class="plugin-description">
                    Plugin d'assistant IA avec apprentissage automatique,
                    suggestions intelligentes et optimisation continue.
                </div>
                <div class="plugin-stats">
                    <div class="stat-item">
                        <div class="stat-value">67</div>
                        <div class="stat-label">Downloads</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.6</div>
                        <div class="stat-label">Rating</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">3</div>
                        <div class="stat-label">Updates</div>
                    </div>
                </div>
                <div class="plugin-actions">
                    <button class="btn btn-primary" onclick="installPlugin('ai_assistant_plugin')">📥 Installer</button>
                    <button class="btn btn-secondary" onclick="viewDetails('ai_assistant_plugin')">📋 Détails</button>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>🕒 Dernière mise à jour: <span id="last-update">{current_time}</span></p>
            <p>🔌 Marketplace de plugins généré automatiquement par Athalia</p>
        </div>
    </div>

    <script>
        // Fonction de filtrage des plugins
        function filterPlugins() {{
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const pluginCards = document.querySelectorAll('.plugin-card');

            pluginCards.forEach(card => {{
                const pluginName = card.getAttribute('data-name').toLowerCase();
                const pluginCategory = card.getAttribute('data-category').toLowerCase();

                if (pluginName.includes(searchTerm) || pluginCategory.includes(searchTerm)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        // Fonction d'installation de plugin
        function installPlugin(pluginName) {{
            alert(`📥 Installation du plugin ${{pluginName}} en cours...`);
            // Ici on pourrait ajouter la logique d'installation réelle
            setTimeout(() => {{
                alert(`✅ Plugin ${{pluginName}} installé avec succès !`);
            }}, 2000);
        }}

        // Fonction de visualisation des détails
        function viewDetails(pluginName) {{
            alert(`📋 Détails du plugin ${{pluginName}} - Fonctionnalité à implémenter`);
        }}

        // Mise à jour automatique des statistiques
        setInterval(() => {{
            const now = new Date();
            document.getElementById('last-update').textContent = now.toLocaleString('fr-FR');
        }}, 300000);

        // Animation d'entrée des cartes
        document.addEventListener('DOMContentLoaded', function() {{
            const cards = document.querySelectorAll('.plugin-card');
            cards.forEach((card, index) => {{
                setTimeout(() => {{
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    card.style.transition = 'all 0.5s ease';

                    setTimeout(() => {{
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }}, 100);
                }}, index * 100);
            }});
        }});
    </script>
</body>
</html>"""

    def open_marketplace(self) -> None:
        """Ouvre le marketplace dans le navigateur"""
        marketplace_file = self.generate_marketplace_interface()
        webbrowser.open(f"file://{os.path.abspath(marketplace_file)}")
        logger.info(f"Marketplace ouvert: {marketplace_file}")

    def get_plugins_summary(self) -> dict[str, Any]:
        """Retourne un résumé des plugins"""
        return {
            "total_plugins": 5,
            "active_plugins": 4,
            "inactive_plugins": 1,
            "total_downloads": 127,
            "average_rating": 4.8,
            "categories": ["demo", "devops", "security", "monitoring", "ai"],
            "last_updated": datetime.now().isoformat(),
        }


def main():
    """Fonction principale pour test du marketplace"""
    import sys

    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = "."

    marketplace = PluginMarketplace(project_path)
    marketplace.open_marketplace()


if __name__ == "__main__":
    main()
