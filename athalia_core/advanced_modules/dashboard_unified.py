#!/usr/bin/env python3
import json
import logging
import os
import sqlite3
import sys
import webbrowser
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

# !/usr/bin/env python3
"""
Module de dashboard unifié simplifié pour Athalia
Rapports consolidés et métriques en temps réel (sans graphiques)
"""


logger = logging.getLogger(__name__)


class DashboardUnifieSimple:
    """Dashboard unifié simplifié avec rapports fonctionnels"""

    def __init__(self, db_path: str = "athalia_analytics.db"):
        self.db_path = db_path
        self._init_database()

    def _init_database(self):
        """Initialisation de la base de données"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Table des métriques
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS metriques (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,
                    valeur REAL,
                    projet TEXT,
                    timestamp TEXT,
                    details TEXT
                )
            """
            )

            # Table des événements
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS evenements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,
                    projet TEXT,
                    utilisateur TEXT,
                    timestamp TEXT,
                    duree INTEGER,
                    statut TEXT,
                    details TEXT
                )
            """
            )

            # Table des rapports
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS rapports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL,
                    projet TEXT,
                    contenu TEXT,
                    timestamp TEXT,
                    score_qualite INTEGER,
                    score_securite INTEGER
                )
            """
            )

            conn.commit()

    def enregistrer_metrique(
        self,
        type_metrique: str,
        valeur: float,
        projet: str | None = None,
        details: dict | None = None,
    ):
        """Enregistrement une métrique"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO metriques (type, valeur, projet, timestamp, details)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    type_metrique,
                    valeur,
                    projet,
                    datetime.now().isoformat(),
                    json.dumps(details) if details else None,
                ),
            )
            conn.commit()

    def enregistrer_evenement(
        self,
        type_evenement: str,
        projet: str | None = None,
        utilisateur: str | None = None,
        duree: int = 0,
        statut: str = "succes",
        details: dict | None = None,
    ):
        """Enregistrement un événement"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO evenements
                (type, projet, utilisateur, timestamp, duree, statut, details)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    type_evenement,
                    projet,
                    utilisateur,
                    datetime.now().isoformat(),
                    duree,
                    statut,
                    json.dumps(details) if details else None,
                ),
            )
            conn.commit()

    def enregistrer_rapport(
        self,
        type_rapport: str,
        projet: str,
        contenu: str,
        score_qualite: int = 0,
        score_securite: int = 0,
    ):
        """Enregistrement un rapport"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO rapports
                (type, projet, contenu, timestamp, score_qualite, score_securite)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    type_rapport,
                    projet,
                    contenu,
                    datetime.now().isoformat(),
                    score_qualite,
                    score_securite,
                ),
            )
            conn.commit()

    def obtenir_metriques_temps_reel(self) -> dict[str, Any]:
        """Obtention des métriques en temps réel"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Métriques des dernières 24h
            hier = (datetime.now() - timedelta(days=1)).isoformat()

            # Projets analysés
            cursor.execute(
                """
                SELECT COUNT(DISTINCT projet) as total_projets
                FROM evenements
                WHERE timestamp > ? AND type = 'audit_projet'
            """,
                (hier,),
            )
            projets_analyses = cursor.fetchone()[0]

            # Actions effectuées
            cursor.execute(
                """
                SELECT COUNT(*) as total_actions
                FROM evenements
                WHERE timestamp > ?
            """,
                (hier,),
            )
            actions_effectuees = cursor.fetchone()[0]

            # Score qualité moyen
            cursor.execute(
                """
                SELECT AVG(score_qualite) as score_moyen
                FROM rapports
                WHERE timestamp > ? AND score_qualite > 0
            """,
                (hier,),
            )
            score_qualite_moyen = cursor.fetchone()[0] or 0

            # Score sécurité moyen
            cursor.execute(
                """
                SELECT AVG(score_securite) as score_moyen
                FROM rapports
                WHERE timestamp > ? AND score_securite > 0
            """,
                (hier,),
            )
            score_securite_moyen = cursor.fetchone()[0] or 0

            return {
                "projets_analyses": projets_analyses,
                "actions_effectuees": actions_effectuees,
                "score_qualite_moyen": round(score_qualite_moyen, 1),
                "score_securite_moyen": round(score_securite_moyen, 1),
                "derniere_mise_a_jour": datetime.now().strftime("%H:%M:%S"),
            }

    def generer_rapport_consolide(self) -> str:
        """Génération d'un rapport consolidé"""
        metriques = self.obtenir_metriques_temps_reel()

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Top projets par score
            cursor.execute(
                """
                SELECT projet, AVG(score_qualite) as score_qualite,
                       AVG(score_securite) as score_securite
                FROM rapports
                WHERE score_qualite > 0 OR score_securite > 0
                GROUP BY projet
                ORDER BY (score_qualite + score_securite) / 2 DESC
                LIMIT 10
            """
            )

            top_projets = []
            for row in cursor.fetchall():
                top_projets.append(
                    {
                        "projet": row[0],
                        "score_qualite": round(row[1] or 0, 1),
                        "score_securite": round(row[2] or 0, 1),
                        "score_moyen": round(((row[1] or 0) + (row[2] or 0)) / 2, 1),
                    }
                )

            # Événements récents
            cursor.execute(
                """
                SELECT type, projet, utilisateur, timestamp, statut
                FROM evenements
                ORDER BY timestamp DESC
                LIMIT 20
            """
            )

            evenements_recents = []
            for row in cursor.fetchall():
                evenements_recents.append(
                    {
                        "type": row[0],
                        "projet": row[1],
                        "utilisateur": row[2],
                        "timestamp": (
                            datetime.fromisoformat(row[3]).strftime("%d/%m/%Y %H:%f")
                        ),
                        "statut": row[4],
                    }
                )

        rapport = []
        rapport.append("# 📊 Dashboard Unifié")
        rapport.append("")
        rapport.append(f"*Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}*")
        rapport.append("")

        # Métriques temps réel
        rapport.append("## 🚀 Métriques en Temps Réel")
        rapport.append("")
        rapport.append(f"- **Projets analysés (24h)**: {metriques['projets_analyses']}")
        rapport.append(
            f"- **Actions effectuées (24h)**: {metriques['actions_effectuees']}"
        )
        rapport.append(
            f"- **Score qualité moyen**: {metriques['score_qualite_moyen']}/100"
        )
        rapport.append(
            f"- **Score sécurité moyen**: {metriques['score_securite_moyen']}/100"
        )
        rapport.append("")

        # Top projets
        if top_projets:
            rapport.append("## �� Top 10 Projets par Score")
            rapport.append("")
            rapport.append("| Projet | Qualité | Sécurité | Moyenne |")
            rapport.append("|--------|---------|----------|---------|")
            for projet in top_projets:
                rapport.append(
                    f"| {projet['projet']} | {projet['score_qualite']} | "
                    f"{projet['score_securite']} | {projet['score_moyen']} |"
                )
            rapport.append("")

        # Événements récents
        if evenements_recents:
            rapport.append("## 📅 Événements Récents")
            rapport.append("")
            rapport.append("| Type | Projet | Utilisateur | Date | Statut |")
            rapport.append("|------|--------|-------------|------|--------|")
            for event in evenements_recents[:10]:
                statut_emoji = "✅" if event["statut"] == "succes" else "❌"
                rapport.append(
                    f"| {event['type']} | {event['projet'] or '-'} | "
                    f"{event['utilisateur'] or '-'} | {event['timestamp']} | "
                    f"{statut_emoji} |"
                )
            rapport.append("")

        return "\n".join(rapport)

    def ajouter_section_distillation(self, file_handle):
        """
        Ajoute une section Distillation IA au dashboard (exemple statique).
        """
        file_handle.write("<h2>Résultat de la distillation IA</h2>")
        file_handle.write(
            "<p><b>Réponse distillée:</b> Réponse de Ollama à "
            '"Explique la distillation IA en 2 phrases."</p>'
        )
        file_handle.write("<p><b>Score audit distillé:</b> 7.60</p>")
        file_handle.write("<p><b>Correction distillée:</b> fix2</p>")

    def generer_dashboard_html(self, output_file: str = "dashboard/index.html"):
        """Génération d'un dashboard HTML moderne et valide"""
        metriques = self.obtenir_metriques_temps_reel()

        html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Athalia</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
        }}
        .metric-card {{
            background: #f8f9fa;
            border-radius: 10px;
            padding: 25px;
            text-align: center;
            border-left: 4px solid #667eea;
        }}
        .metric-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin: 10px 0;
        }}
        .metric-label {{
            color: #6c757d;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .content-section {{
            padding: 30px;
            background: #f8f9fa;
        }}
        .footer {{
            background: #343a40;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        .update-time {{
            color: #adb5bd;
            font-size: 0.9em;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #667eea;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 Dashboard Athalia</h1>
            <p>Analytics et métriques en temps réel</p>
        </div>
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-label">Projets Analysés (24h)</div>
                <div class="metric-value">{metriques["projets_analyses"]}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Actions Effectuées (24h)</div>
                <div class="metric-value">{metriques["actions_effectuees"]}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Score Qualité Moyen</div>
                <div class="metric-value">{metriques["score_qualite_moyen"]}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Score Sécurité Moyen</div>
                <div class="metric-value">{metriques["score_securite_moyen"]}</div>
            </div>
        </div>
        <div class="content-section">
            <h2>📊 Statistiques Détaillées</h2>
        logger.info("Usage: python dashboard_unifie_simple.py <action> [options]")
        </div>
        <div class="footer">
            <div class="update-time">
                Dernière mise à jour: {metriques["derniere_mise_a_jour"]}
            </div>
        </div>
    </div>
</body>
</html>
"""
        # Création du dossier et sauvegarde
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(html_content)
            self.ajouter_section_distillation(file_handle)
        return str(output_path)

    def ouvrir_dashboard(self):
        """Ouverture du dashboard dans le navigateur"""
        html_file = self.generer_dashboard_html()
        webbrowser.open(f"file://{os.path.abspath(html_file)}")
        logger.info(f"Dashboard ouvert: {html_file}")


def main():
    """Fonction principale pour test du f"""

    if len(sys.argv) < 2:
        logger.info("Usage: python dashboard_unifie_simple.py <action> [options]")
        logger.info("Actions: metrics, report, html, f")
        sys.exit(1)

    action = sys.argv[1]
    dashboard = DashboardUnifieSimple()

    if action == "metrics":
        metriques = dashboard.obtenir_metriques_temps_reel()
        logger.info("📊 Métriques en temps réel:")
        for key, value in metriques.items():
            logger.info(f"  {key}: {value}")

    elif action == "report":
        rapport = dashboard.generer_rapport_consolide()
        logger.info(rapport)

    elif action == "html":
        html_file = dashboard.generer_dashboard_html()
        logger.info(f"✅ Dashboard HTML généré: {html_file}")

    elif action == "f":
        dashboard.ouvrir_dashboard()
        logger.info("🌐 Dashboard ouvert dans le f")

    else:
        logger.info("❌ Action non f")


if __name__ == "__main__":
    main()
