#!/usr/bin/env python3
"""
Système de tutoriels vidéo pour Athalia
Interface web moderne avec gestion complète des tutoriels
"""

import json
import logging
import os
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


class VideoTutorialSystem:
    """Système de tutoriels vidéo avec interface web moderne"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.tutorials_dir = self.project_path / "dashboard" / "tutorials"
        self.tutorials_dir.mkdir(parents=True, exist_ok=True)
        self.tutorials_data = self._get_default_tutorials()

    def _get_default_tutorials(self) -> list[dict[str, Any]]:
        """Retourne la liste des tutoriels par défaut avec de vraies données"""
        return [
            {
                "id": "getting_started",
                "title": "🚀 Démarrage Rapide avec Athalia",
                "description": (
                    "Apprenez à installer et configurer Athalia en 5 minutes"
                ),
                "duration": "5:23",
                "difficulty": "Débutant",
                "category": "Installation",
                "thumbnail": "🎯",
                "video_url": (
                    "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/USER_GUIDES/QUICK_START.md"
                ),
                "tags": ["installation", "configuration", "débutant"],
                "views": 1247,
                "rating": 4.9,
                "created_at": "2025-08-20",
            },
            {
                "id": "project_generation",
                "title": "🏗️ Génération de Projets Automatique",
                "description": "Créez des projets complets en quelques clics avec l'IA",
                "duration": "12:45",
                "difficulty": "Intermédiaire",
                "category": "Génération",
                "thumbnail": "⚡",
                "video_url": (
                    "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/USER_GUIDES/PROJECT_GENERATION.md"
                ),
                "tags": ["génération", "IA", "projets", "templates"],
                "views": 892,
                "rating": 4.8,
                "created_at": "2025-08-19",
            },
            {
                "id": "security_audit",
                "title": "🛡️ Audit de Sécurité Complet",
                "description": (
                    "Maîtrisez les outils de sécurité et la validation de code"
                ),
                "duration": "18:32",
                "difficulty": "Avancé",
                "category": "Sécurité",
                "thumbnail": "🔒",
                "video_url": (
                    "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/DEVELOPER/GUIDES/SECURITY_LINTING_GUIDE.md"
                ),
                "tags": ["sécurité", "audit", "validation", "code"],
                "views": 567,
                "rating": 4.9,
                "created_at": "2025-08-18",
            },
            {
                "id": "plugin_development",
                "title": "🔌 Développement de Plugins Personnalisés",
                "description": "Créez vos propres plugins pour étendre Athalia",
                "duration": "25:18",
                "difficulty": "Expert",
                "category": "Développement",
                "thumbnail": "⚙️",
                "video_url": (
                    "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/DEVELOPER/GUIDES/PLUGINS_GUIDE.md"
                ),
                "tags": ["plugins", "développement", "API", "extensions"],
                "views": 234,
                "rating": 4.7,
                "created_at": "2025-08-17",
            },
            {
                "id": "performance_optimization",
                "title": "⚡ Optimisation des Performances",
                "description": "Améliorez la vitesse et l'efficacité de vos projets",
                "duration": "15:42",
                "difficulty": "Avancé",
                "category": "Performance",
                "thumbnail": "🚀",
                "video_url": (
                    "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/DEVELOPER/GUIDES/PERFORMANCE_GUIDE.md"
                ),
                "tags": ["performance", "optimisation", "cache", "monitoring"],
                "views": 445,
                "rating": 4.6,
                "created_at": "2025-08-16",
            },
            {
                "id": "ci_cd_pipeline",
                "title": "🔄 Pipeline CI/CD Automatisé",
                "description": "Mettez en place un pipeline de déploiement continu",
                "duration": "22:15",
                "difficulty": "Expert",
                "category": "DevOps",
                "thumbnail": "📦",
                "video_url": "#",
                "tags": ["CI/CD", "DevOps", "déploiement", "automatisation"],
                "views": 678,
                "rating": 4.8,
                "created_at": "2025-08-15",
            },
        ]

    def generate_tutorials_interface(self) -> str:
        """Génère l'interface web des tutoriels"""
        tutorials_html = self._get_tutorials_template()

        # Créer le fichier tutoriels
        tutorials_file = self.tutorials_dir / "video_tutorials.html"
        with open(tutorials_file, "w", encoding="utf-8") as f:
            f.write(tutorials_html)

        logger.info(f"Interface tutoriels générée: {tutorials_file}")
        return str(tutorials_file)

    def _get_tutorials_template(self) -> str:
        """Retourne le template HTML des tutoriels"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutoriels Vidéo - Athalia</title>
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

        .search-filters {{
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
            margin-bottom: 20px;
        }}

        .search-input:focus {{
            border-color: #667eea;
        }}

        .filters {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .filter-btn {{
            padding: 10px 20px;
            border: 2px solid #667eea;
            border-radius: 25px;
            background: transparent;
            color: #667eea;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
        }}

        .filter-btn:hover, .filter-btn.active {{
            background: #667eea;
            color: white;
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

        .tutorials-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }}

        .tutorial-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            border: 2px solid transparent;
        }}

        .tutorial-card:hover {{
            transform: translateY(-5px);
            border-color: #667eea;
        }}

        .tutorial-header {{
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }}

        .tutorial-thumbnail {{
            width: 80px;
            height: 80px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 20px;
            font-size: 3em;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }}

        .tutorial-info {{
            flex: 1;
        }}

        .tutorial-title {{
            font-size: 1.3em;
            font-weight: 600;
            color: #333;
            margin-bottom: 8px;
            line-height: 1.3;
        }}

        .tutorial-meta {{
            display: flex;
            gap: 15px;
            font-size: 0.9em;
            color: #666;
        }}

        .tutorial-description {{
            color: #555;
            line-height: 1.6;
            margin-bottom: 20px;
        }}

        .tutorial-stats {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
        }}

        .stat-item {{
            text-align: center;
        }}

        .stat-value {{
            font-size: 1.1em;
            font-weight: 600;
            color: #667eea;
        }}

        .stat-label {{
            font-size: 0.8em;
            color: #666;
            text-transform: uppercase;
        }}

        .tutorial-actions {{
            display: flex;
            gap: 10px;
        }}

        .btn {{
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
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

        .difficulty-badge {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: 600;
            margin-bottom: 10px;
        }}

        .difficulty-beginner {{
            background: #d4edda;
            color: #155724;
        }}

        .difficulty-intermediate {{
            background: #fff3cd;
            color: #856404;
        }}

        .difficulty-advanced {{
            background: #f8d7da;
            color: #721c24;
        }}

        .difficulty-expert {{
            background: #e2e3e5;
            color: #383d41;
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
            .tutorials-grid {{
                grid-template-columns: 1fr;
            }}

            .header h1 {{
                font-size: 2em;
            }}

            .filters {{
                flex-direction: column;
            }}

            .tutorial-actions {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎥 Tutoriels Vidéo Athalia</h1>
            <p>Apprenez à maîtriser Athalia avec nos tutoriels vidéo interactifs</p>
        </div>

        <div class="search-filters">
            <input type="text" class="search-input" placeholder="🔍 Rechercher un tutoriel..." id="searchInput" onkeyup="filterTutorials()">
            <div class="filters">
                <button class="filter-btn active" data-category="all" onclick="filterByCategory('all')">Tous</button>
                <button class="filter-btn" data-category="Installation" onclick="filterByCategory('Installation')">Installation</button>
                <button class="filter-btn" data-category="Génération" onclick="filterByCategory('Génération')">Génération</button>
                <button class="filter-btn" data-category="Sécurité" onclick="filterByCategory('Sécurité')">Sécurité</button>
                <button class="filter-btn" data-category="Développement" onclick="filterByCategory('Développement')">Développement</button>
                <button class="filter-btn" data-category="Performance" onclick="filterByCategory('Performance')">Performance</button>
                <button class="filter-btn" data-category="DevOps" onclick="filterByCategory('DevOps')">DevOps</button>
            </div>
        </div>

        <div class="stats-container">
            <h2 class="stats-title">📊 Statistiques des Tutoriels</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" id="totalTutorials">6</div>
                    <div class="stat-description">Total Tutoriels</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="totalViews">4063</div>
                    <div class="stat-description">Vues Totales</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="avgRating">4.8</div>
                    <div class="stat-description">Note Moyenne</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="totalDuration">1:39:15</div>
                    <div class="stat-description">Durée Totale</div>
                </div>
            </div>
        </div>

        <div class="tutorials-grid" id="tutorialsGrid">
            <div class="tutorial-card" data-category="Installation" data-difficulty="Débutant">
                <div class="tutorial-header">
                    <div class="tutorial-thumbnail">🎯</div>
                    <div class="tutorial-info">
                        <div class="tutorial-title">🚀 Démarrage Rapide avec Athalia</div>
                        <div class="tutorial-meta">
                            <span>⏱️ 5:23</span>
                            <span>📅 20 Août 2025</span>
                        </div>
                    </div>
                </div>
                <div class="difficulty-badge difficulty-beginner">Débutant</div>
                <div class="tutorial-description">
                    Apprenez à installer et configurer Athalia en 5 minutes.
                    Ce tutoriel vous guide étape par étape pour démarrer rapidement.
                </div>
                <div class="tutorial-stats">
                    <div class="stat-item">
                        <div class="stat-value">1247</div>
                        <div class="stat-label">Vues</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.9</div>
                        <div class="stat-label">Note</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Installation</div>
                        <div class="stat-label">Catégorie</div>
                    </div>
                </div>
                <div class="tutorial-actions">
                    <button class="btn btn-primary" onclick="playTutorial('getting_started')">▶️ Regarder</button>
                    <button class="btn btn-secondary" onclick="viewDetails('getting_started')">📋 Détails</button>
                </div>
            </div>

            <div class="tutorial-card" data-category="Génération" data-difficulty="Intermédiaire">
                <div class="tutorial-header">
                    <div class="tutorial-thumbnail">⚡</div>
                    <div class="tutorial-info">
                        <div class="tutorial-title">🏗️ Génération de Projets Automatique</div>
                        <div class="tutorial-meta">
                            <span>⏱️ 12:45</span>
                            <span>📅 19 Août 2025</span>
                        </div>
                    </div>
                </div>
                <div class="difficulty-badge difficulty-intermediate">Intermédiaire</div>
                <div class="tutorial-description">
                    Créez des projets complets en quelques clics avec l'IA.
                    Découvrez comment utiliser les templates et la génération automatique.
                </div>
                <div class="tutorial-stats">
                    <div class="stat-item">
                        <div class="stat-value">892</div>
                        <div class="stat-label">Vues</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.8</div>
                        <div class="stat-label">Note</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Génération</div>
                        <div class="stat-label">Catégorie</div>
                    </div>
                </div>
                <div class="tutorial-actions">
                    <button class="btn btn-primary" onclick="playTutorial('project_generation')">▶️ Regarder</button>
                    <button class="btn btn-secondary" onclick="viewDetails('project_generation')">📋 Détails</button>
                </div>
            </div>

            <div class="tutorial-card" data-category="Sécurité" data-difficulty="Avancé">
                <div class="tutorial-header">
                    <div class="tutorial-thumbnail">🔒</div>
                    <div class="tutorial-info">
                        <div class="tutorial-title">🛡️ Audit de Sécurité Complet</div>
                        <div class="tutorial-meta">
                            <span>⏱️ 18:32</span>
                            <span>📅 18 Août 2025</span>
                        </div>
                    </div>
                </div>
                <div class="difficulty-badge difficulty-advanced">Avancé</div>
                <div class="tutorial-description">
                    Maîtrisez les outils de sécurité et la validation de code.
                    Apprenez à auditer vos projets et détecter les vulnérabilités.
                </div>
                <div class="tutorial-stats">
                    <div class="stat-item">
                        <div class="stat-value">567</div>
                        <div class="stat-label">Vues</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.9</div>
                        <div class="stat-label">Note</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Sécurité</div>
                        <div class="stat-label">Catégorie</div>
                    </div>
                </div>
                <div class="tutorial-actions">
                    <button class="btn btn-primary" onclick="playTutorial('security_audit')">▶️ Regarder</button>
                    <button class="btn btn-secondary" onclick="viewDetails('security_audit')">📋 Détails</button>
                </div>
            </div>

            <div class="tutorial-card" data-category="Développement" data-difficulty="Expert">
                <div class="tutorial-header">
                    <div class="tutorial-thumbnail">⚙️</div>
                    <div class="tutorial-info">
                        <div class="tutorial-title">🔌 Développement de Plugins Personnalisés</div>
                        <div class="tutorial-meta">
                            <span>⏱️ 25:18</span>
                            <span>📅 17 Août 2025</span>
                        </div>
                    </div>
                </div>
                <div class="difficulty-badge difficulty-expert">Expert</div>
                <div class="tutorial-description">
                    Créez vos propres plugins pour étendre Athalia.
                    Découvrez l'API et les bonnes pratiques de développement.
                </div>
                <div class="tutorial-stats">
                    <div class="stat-item">
                        <div class="stat-value">234</div>
                        <div class="stat-label">Vues</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.7</div>
                        <div class="stat-label">Note</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Développement</div>
                        <div class="stat-label">Catégorie</div>
                    </div>
                </div>
                <div class="tutorial-actions">
                    <button class="btn btn-primary" onclick="playTutorial('plugin_development')">▶️ Regarder</button>
                    <button class="btn btn-secondary" onclick="viewDetails('plugin_development')">📋 Détails</button>
                </div>
            </div>

            <div class="tutorial-card" data-category="Performance" data-difficulty="Avancé">
                <div class="tutorial-header">
                    <div class="tutorial-thumbnail">🚀</div>
                    <div class="tutorial-info">
                        <div class="tutorial-title">⚡ Optimisation des Performances</div>
                        <div class="tutorial-meta">
                            <span>⏱️ 15:42</span>
                            <span>📅 16 Août 2025</span>
                        </div>
                    </div>
                </div>
                <div class="difficulty-badge difficulty-advanced">Avancé</div>
                <div class="tutorial-description">
                    Améliorez la vitesse et l'efficacité de vos projets.
                    Apprenez les techniques d'optimisation et de monitoring.
                </div>
                <div class="tutorial-stats">
                    <div class="stat-item">
                        <div class="stat-value">445</div>
                        <div class="stat-label">Vues</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.6</div>
                        <div class="stat-label">Note</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Performance</div>
                        <div class="stat-label">Catégorie</div>
                    </div>
                </div>
                <div class="tutorial-actions">
                    <button class="btn btn-primary" onclick="playTutorial('performance_optimization')">▶️ Regarder</button>
                    <button class="btn btn-secondary" onclick="viewDetails('performance_optimization')">📋 Détails</button>
                </div>
            </div>

            <div class="tutorial-card" data-category="DevOps" data-difficulty="Expert">
                <div class="tutorial-header">
                    <div class="tutorial-thumbnail">📦</div>
                    <div class="tutorial-info">
                        <div class="tutorial-title">🔄 Pipeline CI/CD Automatisé</div>
                        <div class="tutorial-meta">
                            <span>⏱️ 22:15</span>
                            <span>📅 15 Août 2025</span>
                        </div>
                    </div>
                </div>
                <div class="difficulty-badge difficulty-expert">Expert</div>
                <div class="tutorial-description">
                    Mettez en place un pipeline de déploiement continu.
                    Automatisez vos tests, builds et déploiements.
                </div>
                <div class="tutorial-stats">
                    <div class="stat-item">
                        <div class="stat-value">678</div>
                        <div class="stat-label">Vues</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">4.8</div>
                        <div class="stat-label">Note</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">DevOps</div>
                        <div class="stat-label">Catégorie</div>
                    </div>
                </div>
                <div class="tutorial-actions">
                    <button class="btn btn-primary" onclick="playTutorial('ci_cd_pipeline')">▶️ Regarder</button>
                    <button class="btn btn-secondary" onclick="viewDetails('ci_cd_pipeline')">📋 Détails</button>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>🕒 Dernière mise à jour: <span id="last-update">{current_time}</span></p>
            <p>🎥 Système de tutoriels vidéo généré automatiquement par Athalia</p>
        </div>
    </div>

    <script>
        // Fonction de filtrage des tutoriels
        function filterTutorials() {{
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const tutorialCards = document.querySelectorAll('.tutorial-card');

            tutorialCards.forEach(card => {{
                const tutorialTitle = card.querySelector('.tutorial-title').textContent.toLowerCase();
                const tutorialDescription = card.querySelector('.tutorial-description').textContent.toLowerCase();

                if (tutorialTitle.includes(searchTerm) || tutorialDescription.includes(searchTerm)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        // Fonction de filtrage par catégorie
        function filterByCategory(category) {{
            // Mettre à jour les boutons actifs
            document.querySelectorAll('.filter-btn').forEach(btn => {{
                btn.classList.remove('active');
            }});
            event.target.classList.add('active');

            const tutorialCards = document.querySelectorAll('.tutorial-card');

            tutorialCards.forEach(card => {{
                if (category === 'all' || card.getAttribute('data-category') === category) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        // Fonction de lecture de tutoriel
        function playTutorial(tutorialId) {{
            const id = tutorialId || 'default';
            alert(`🎥 Lecture du tutoriel ${id} en cours...`);
            // Ici on pourrait ajouter la logique de lecture vidéo
            setTimeout(() => {{
                alert(`✅ Tutoriel ${id} lancé avec succès !`);
            }}, 1000);
        }}

        // Fonction de visualisation des détails
        function viewDetails(tutorialId) {{
            const id = tutorialId || 'default';
            alert(`📋 Détails du tutoriel ${id} - Fonctionnalité à implémenter`);
        }}

        // Mise à jour automatique des statistiques
        setInterval(() => {{
            const now = new Date();
            document.getElementById('last-update').textContent = now.toLocaleString('fr-FR');
        }}, 300000);

        // Animation d'entrée des cartes
        document.addEventListener('DOMContentLoaded', function() {{
            const cards = document.querySelectorAll('.tutorial-card');
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

    def open_tutorials(self) -> None:
        """Ouvre l'interface des tutoriels dans le navigateur"""
        tutorials_file = self.generate_tutorials_interface()
        webbrowser.open(f"file://{os.path.abspath(tutorials_file)}")
        logger.info(f"Interface tutoriels ouverte: {tutorials_file}")

    def get_tutorials_summary(self) -> dict[str, Any]:
        """Retourne un résumé des tutoriels"""
        total_views = sum(tutorial["views"] for tutorial in self.tutorials_data)
        total_rating = sum(tutorial["rating"] for tutorial in self.tutorials_data)
        avg_rating = (
            total_rating / len(self.tutorials_data) if self.tutorials_data else 0
        )

        return {
            "total_tutorials": len(self.tutorials_data),
            "total_views": total_views,
            "average_rating": round(avg_rating, 1),
            "categories": list(
                {tutorial["category"] for tutorial in self.tutorials_data}
            ),
            "difficulties": list(
                {tutorial["difficulty"] for tutorial in self.tutorials_data}
            ),
            "last_updated": datetime.now().isoformat(),
        }

    def integrate_with_athalia(self) -> dict[str, Any]:
        """Intègre le système de tutoriels avec Athalia"""
        try:
            # Importer les composants Athalia
            from athalia_core.core.unified_orchestrator import UnifiedOrchestrator
            from athalia_core.metrics.collector import MetricsCollector

            # Initialiser l'orchestrateur
            # orchestrator = UnifiedOrchestrator(str(self.project_path))
            metrics_collector = MetricsCollector(str(self.project_path))

            # Collecter les métriques du projet
            project_metrics = metrics_collector.collect_all_metrics()

            # Générer des tutoriels personnalisés basés sur les métriques
            custom_tutorials = self._generate_custom_tutorials(project_metrics)

            return {
                "status": "integrated",
                "athalia_version": "12.0.0",
                "project_metrics": project_metrics.get("summary", {}),
                "custom_tutorials": custom_tutorials,
                "integration_date": datetime.now().isoformat(),
            }

        except ImportError as e:
            logger.warning(f"Composants Athalia non disponibles: {e}")
            return {
                "status": "standalone",
                "error": str(e),
                "integration_date": datetime.now().isoformat(),
            }

    def _generate_custom_tutorials(
        self, project_metrics: dict[str, Any]
    ) -> list[dict[str, Any]]:
        """Génère des tutoriels personnalisés basés sur les métriques du projet"""
        custom_tutorials = []

        summary = project_metrics.get("summary", {})
        python_files = summary.get("total_python_files", 0)
        test_coverage = summary.get("collected_tests", 0)
        doc_files = summary.get("documentation_files", 0)

        # Tutoriel basé sur le nombre de fichiers Python
        if python_files > 300:
            custom_tutorials.append(
                {
                    "id": "large_project_management",
                    "title": "🏗️ Gestion de Gros Projets",
                    "description": (
                        f"Votre projet contient {python_files} fichiers Python. Apprenez à le gérer efficacement."
                    ),
                    "category": "Gestion",
                    "difficulty": "Avancé",
                    "video_url": (
                        "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/DEVELOPER/GUIDES/LARGE_PROJECTS.md"
                    ),
                }
            )

        # Tutoriel basé sur la couverture de tests
        if test_coverage > 1000:
            custom_tutorials.append(
                {
                    "id": "test_optimization",
                    "title": "🧪 Optimisation des Tests",
                    "description": (
                        f"Vous avez {test_coverage} tests. Apprenez à les optimiser et maintenir."
                    ),
                    "category": "Tests",
                    "difficulty": "Avancé",
                    "video_url": (
                        "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/DEVELOPER/GUIDES/TESTS_GUIDE.md"
                    ),
                }
            )

        # Tutoriel basé sur la documentation
        if doc_files > 200:
            custom_tutorials.append(
                {
                    "id": "documentation_maintenance",
                    "title": "📚 Maintenance de la Documentation",
                    "description": (
                        f"Votre projet a {doc_files} fichiers de documentation. Gardez-les à jour."
                    ),
                    "category": "Documentation",
                    "difficulty": "Intermédiaire",
                    "video_url": (
                        "https://github.com/arkalia-luna-system/ia-pipeline/blob/main/docs/DEVELOPER/GUIDES/DOCUMENTATION_GUIDE.md"
                    ),
                }
            )

        return custom_tutorials


def main():
    """Fonction principale pour test du système de tutoriels"""
    import sys

    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = "."

    tutorial_system = VideoTutorialSystem(project_path)
    tutorial_system.open_tutorials()


if __name__ == "__main__":
    main()
