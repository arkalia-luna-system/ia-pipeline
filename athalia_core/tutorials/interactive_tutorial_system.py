#!/usr/bin/env python3
"""
Système de Tutoriels Interactifs Avancé pour Athalia
Interface web moderne avec tutoriels étape par étape et suivi de progression
"""

import json
import logging
import os
import webbrowser
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


@dataclass
class TutorialStep:
    """Représente une étape d'un tutoriel interactif"""

    id: str
    title: str
    description: str
    instructions: str
    expected_output: str
    hints: list[str]
    difficulty: str  # "easy", "medium", "hard"
    estimated_time: int  # en minutes
    prerequisites: list[str]  # IDs des étapes préalables


@dataclass
class InteractiveTutorial:
    """Représente un tutoriel interactif complet"""

    id: str
    title: str
    description: str
    category: str
    difficulty: str
    steps: list[TutorialStep]
    estimated_total_time: int
    tags: list[str]
    created_at: str
    updated_at: str
    completion_rate: float
    average_rating: float
    total_attempts: int


@dataclass
class UserProgress:
    """Suivi de la progression d'un utilisateur"""

    user_id: str
    tutorial_id: str
    current_step: int
    completed_steps: list[str]
    started_at: str
    last_activity: str
    total_time_spent: int  # en minutes
    score: float  # 0-100


class InteractiveTutorialSystem:
    """Système de tutoriels interactifs avancé pour Athalia"""

    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.tutorials_dir = self.project_path / "dashboard" / "tutorials"
        self.tutorials_dir.mkdir(parents=True, exist_ok=True)
        self.progress_dir = self.tutorials_dir / "progress"
        self.progress_dir.mkdir(exist_ok=True)

        # Initialiser les tutoriels interactifs
        self.tutorials = self._create_interactive_tutorials()
        self.user_progress: dict[
            str, Any
        ] = {}  # user_id -> {tutorial_id -> UserProgress}
        self._load_user_progress()

    def _create_interactive_tutorials(self) -> list[InteractiveTutorial]:
        """Crée une collection de tutoriels interactifs avancés"""
        return [
            InteractiveTutorial(
                id="athalia_mastery",
                title="🚀 Maîtrise Complète d'Athalia",
                description="Devenez un expert d'Athalia en suivant ce parcours interactif complet",
                category="Formation",
                difficulty="Avancé",
                estimated_total_time=120,
                tags=["formation", "expert", "complet", "interactif"],
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                completion_rate=0.0,
                average_rating=0.0,
                total_attempts=0,
                steps=[
                    TutorialStep(
                        id="setup_environment",
                        title="🔧 Configuration de l'Environnement",
                        description="Configurez votre environnement de développement Athalia",
                        instructions="""
1. Vérifiez que Python 3.10+ est installé
2. Clonez le repository Athalia
3. Créez un environnement virtuel
4. Installez les dépendances
                        """.strip(),
                        expected_output="Environnement configuré et tests passants",
                        hints=[
                            "Utilisez 'python -m venv venv' pour créer l'environnement",
                            "Activez l'environnement avec 'source venv/bin/activate'",
                            "Installez les dépendances avec 'pip install -r requirements.txt'",
                        ],
                        difficulty="easy",
                        estimated_time=15,
                        prerequisites=[],
                    ),
                    TutorialStep(
                        id="first_project",
                        title="🏗️ Création de Votre Premier Projet",
                        description="Générez votre premier projet avec Athalia",
                        instructions="""
1. Lancez l'orchestrateur Athalia
2. Choisissez le type de projet
3. Configurez les paramètres
4. Générez la structure
                        """.strip(),
                        expected_output="Projet généré avec succès et structure créée",
                        hints=[
                            "Utilisez 'python -m athalia_core.demo.quickcheck' pour tester",
                            "Vérifiez que tous les composants sont disponibles",
                            "Testez la génération d'un projet simple d'abord",
                        ],
                        difficulty="medium",
                        estimated_time=25,
                        prerequisites=["setup_environment"],
                    ),
                    TutorialStep(
                        id="security_audit",
                        title="🛡️ Audit de Sécurité Complet",
                        description="Maîtrisez les outils de sécurité d'Athalia",
                        instructions="""
1. Lancez le dashboard de sécurité
2. Exécutez tous les scans de sécurité
3. Analysez les résultats
4. Corrigez les vulnérabilités détectées
                        """.strip(),
                        expected_output="Score de sécurité > 80/100 et vulnérabilités corrigées",
                        hints=[
                            "Utilisez le dashboard de sécurité intégré",
                            "Lancez les scans Bandit, Safety, et pip-audit",
                            "Corrigez d'abord les vulnérabilités critiques",
                        ],
                        difficulty="hard",
                        estimated_time=35,
                        prerequisites=["first_project"],
                    ),
                    TutorialStep(
                        id="performance_optimization",
                        title="⚡ Optimisation des Performances",
                        description="Optimisez votre projet avec les outils de benchmark",
                        instructions="""
1. Lancez le système de benchmark
2. Identifiez les goulots d'étranglement
3. Appliquez les optimisations recommandées
4. Mesurez l'amélioration des performances
                        """.strip(),
                        expected_output="Amélioration des performances > 20%",
                        hints=[
                            "Utilisez le système de benchmark intégré",
                            "Concentrez-vous sur les fonctions les plus lentes",
                            "Testez les optimisations avant/après",
                        ],
                        difficulty="hard",
                        estimated_time=45,
                        prerequisites=["security_audit"],
                    ),
                ],
            ),
            InteractiveTutorial(
                id="devops_expert",
                title="🔧 Expert DevOps avec Athalia",
                description="Maîtrisez les workflows DevOps et CI/CD avec Athalia",
                category="DevOps",
                difficulty="Expert",
                estimated_total_time=90,
                tags=["devops", "ci-cd", "workflows", "expert"],
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                completion_rate=0.0,
                average_rating=0.0,
                total_attempts=0,
                steps=[
                    TutorialStep(
                        id="ci_cd_setup",
                        title="🔄 Configuration CI/CD",
                        description="Configurez un pipeline CI/CD complet",
                        instructions="""
1. Configurez GitHub Actions
2. Définissez les étapes de build
3. Configurez les tests automatisés
4. Mettez en place le déploiement
                        """.strip(),
                        expected_output="Pipeline CI/CD fonctionnel et tests automatisés",
                        hints=[
                            "Utilisez les workflows GitHub Actions d'Athalia",
                            "Configurez les tests avec pytest",
                            "Intégrez le linting avec black et ruff",
                        ],
                        difficulty="hard",
                        estimated_time=30,
                        prerequisites=[],
                    ),
                    TutorialStep(
                        id="monitoring_setup",
                        title="📊 Monitoring et Observabilité",
                        description="Mettez en place le monitoring de votre projet",
                        instructions="""
1. Configurez les métriques de base
2. Mettez en place les alertes
3. Configurez les dashboards
4. Testez le monitoring
                        """.strip(),
                        expected_output="Système de monitoring fonctionnel avec alertes",
                        hints=[
                            "Utilisez le collecteur de métriques intégré",
                            "Configurez les seuils d'alerte appropriés",
                            "Testez avec des scénarios réels",
                        ],
                        difficulty="medium",
                        estimated_time=25,
                        prerequisites=["ci_cd_setup"],
                    ),
                ],
            ),
            InteractiveTutorial(
                id="plugin_development",
                title="🔌 Développement de Plugins Avancés",
                description="Créez vos propres plugins pour étendre Athalia",
                category="Développement",
                difficulty="Expert",
                estimated_total_time=75,
                tags=["plugins", "développement", "extensions", "expert"],
                created_at=datetime.now().isoformat(),
                updated_at=datetime.now().isoformat(),
                completion_rate=0.0,
                average_rating=0.0,
                total_attempts=0,
                steps=[
                    TutorialStep(
                        id="plugin_architecture",
                        title="🏗️ Architecture des Plugins",
                        description="Comprenez l'architecture des plugins Athalia",
                        instructions="""
1. Étudiez la structure des plugins existants
2. Comprenez le système de hooks
3. Identifiez les points d'extension
4. Planifiez votre plugin
                        """.strip(),
                        expected_output="Architecture du plugin planifiée et documentée",
                        hints=[
                            "Examinez les plugins dans athalia_core/plugins/",
                            "Identifiez les interfaces et classes de base",
                            "Documentez votre architecture",
                        ],
                        difficulty="medium",
                        estimated_time=20,
                        prerequisites=[],
                    ),
                    TutorialStep(
                        id="plugin_implementation",
                        title="⚙️ Implémentation du Plugin",
                        description="Implémentez votre plugin étape par étape",
                        instructions="""
1. Créez la structure du plugin
2. Implémentez les fonctionnalités de base
3. Ajoutez la gestion d'erreurs
4. Testez le plugin
                        """.strip(),
                        expected_output="Plugin fonctionnel et testé",
                        hints=[
                            "Suivez les conventions de nommage",
                            "Ajoutez des tests unitaires",
                            "Gérez les erreurs gracieusement",
                        ],
                        difficulty="hard",
                        estimated_time=35,
                        prerequisites=["plugin_architecture"],
                    ),
                ],
            ),
        ]

    def _load_user_progress(self) -> None:
        """Charge la progression des utilisateurs depuis les fichiers"""
        try:
            for progress_file in self.progress_dir.glob("*.json"):
                with open(progress_file, encoding="utf-8") as f:
                    progress_data = json.load(f)
                    user_id = progress_data["user_id"]
                    tutorial_id = progress_data["tutorial_id"]

                    if user_id not in self.user_progress:
                        self.user_progress[user_id] = {}

                    self.user_progress[user_id][tutorial_id] = UserProgress(
                        **progress_data
                    )
        except Exception as e:
            logger.warning(f"Impossible de charger la progression: {e}")

    def _save_user_progress(self, user_id: str, tutorial_id: str) -> None:
        """Sauvegarde la progression d'un utilisateur"""
        try:
            if (
                user_id in self.user_progress
                and tutorial_id in self.user_progress[user_id]
            ):
                progress = self.user_progress[user_id][tutorial_id]
                progress_file = self.progress_dir / f"{user_id}_{tutorial_id}.json"

                with open(progress_file, "w", encoding="utf-8") as f:
                    json.dump(asdict(progress), f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde de la progression: {e}")

    def start_tutorial(self, user_id: str, tutorial_id: str) -> dict[str, Any]:
        """Démarre un tutoriel pour un utilisateur"""
        tutorial = next((t for t in self.tutorials if t.id == tutorial_id), None)
        if not tutorial:
            return {"error": "Tutoriel non trouvé"}

        # Créer ou récupérer la progression
        if user_id not in self.user_progress:
            self.user_progress[user_id] = {}

        if tutorial_id not in self.user_progress[user_id]:
            self.user_progress[user_id][tutorial_id] = UserProgress(
                user_id=user_id,
                tutorial_id=tutorial_id,
                current_step=0,
                completed_steps=[],
                started_at=datetime.now().isoformat(),
                last_activity=datetime.now().isoformat(),
                total_time_spent=0,
                score=0.0,
            )
        else:
            # Mettre à jour l'activité
            self.user_progress[user_id][
                tutorial_id
            ].last_activity = datetime.now().isoformat()

        # Mettre à jour les statistiques
        tutorial.total_attempts += 1

        self._save_user_progress(user_id, tutorial_id)

        return {
            "tutorial": asdict(tutorial),
            "progress": asdict(self.user_progress[user_id][tutorial_id]),
            "current_step": tutorial.steps[0] if tutorial.steps else None,
        }

    def get_current_step(self, user_id: str, tutorial_id: str) -> TutorialStep | None:
        """Récupère l'étape actuelle d'un utilisateur"""
        if user_id in self.user_progress and tutorial_id in self.user_progress[user_id]:
            progress = self.user_progress[user_id][tutorial_id]
            tutorial = next((t for t in self.tutorials if t.id == tutorial_id), None)

            if tutorial and progress.current_step < len(tutorial.steps):
                return tutorial.steps[progress.current_step]

        return None

    def complete_step(
        self, user_id: str, tutorial_id: str, step_output: str
    ) -> dict[str, Any]:
        """Marque une étape comme terminée et calcule le score"""
        if (
            user_id not in self.user_progress
            or tutorial_id not in self.user_progress[user_id]
        ):
            return {"error": "Progression non trouvée"}

        progress = self.user_progress[user_id][tutorial_id]
        tutorial = next((t for t in self.tutorials if t.id == tutorial_id), None)

        if not tutorial or progress.current_step >= len(tutorial.steps):
            return {"error": "Étape invalide"}

        current_step = tutorial.steps[progress.current_step]

        # Calculer le score de l'étape (simulation basée sur la complexité)
        step_score = self._calculate_step_score(current_step, step_output)

        # Marquer l'étape comme terminée
        if current_step.id not in progress.completed_steps:
            progress.completed_steps.append(current_step.id)

        # Passer à l'étape suivante
        progress.current_step += 1

        # Calculer le score total
        total_steps = len(tutorial.steps)
        completed_steps = len(progress.completed_steps)
        progress.score = (completed_steps / total_steps) * 100

        # Mettre à jour le temps passé
        progress.total_time_spent += current_step.estimated_time
        progress.last_activity = datetime.now().isoformat()

        # Mettre à jour les statistiques du tutoriel
        tutorial.completion_rate = (completed_steps / total_steps) * 100

        self._save_user_progress(user_id, tutorial_id)

        return {
            "step_completed": True,
            "step_score": step_score,
            "total_score": progress.score,
            "next_step": self.get_current_step(user_id, tutorial_id),
            "tutorial_completed": progress.current_step >= len(tutorial.steps),
        }

    def _calculate_step_score(self, step: TutorialStep, output: str) -> float:
        """Calcule le score d'une étape basé sur la complexité et la sortie"""
        base_score = 100.0

        # Réduire le score si l'étape est difficile
        if step.difficulty == "hard":
            base_score *= 0.9
        elif step.difficulty == "medium":
            base_score *= 0.95

        # Bonus pour la qualité de la sortie (simulation)
        if len(output) > 50:  # Sortie détaillée
            base_score *= 1.1

        return min(100.0, base_score)

    def get_user_progress(self, user_id: str) -> dict[str, Any]:
        """Récupère la progression complète d'un utilisateur"""
        if user_id not in self.user_progress:
            return {"user_id": user_id, "tutorials": [], "overall_progress": 0.0}

        user_tutorials = []
        total_progress = 0.0

        for tutorial_id, progress in self.user_progress[user_id].items():
            tutorial = next((t for t in self.tutorials if t.id == tutorial_id), None)
            if tutorial:
                user_tutorials.append(
                    {"tutorial": asdict(tutorial), "progress": asdict(progress)}
                )
                total_progress += progress.score

        overall_progress = (
            total_progress / len(user_tutorials) if user_tutorials else 0.0
        )

        return {
            "user_id": user_id,
            "tutorials": user_tutorials,
            "overall_progress": overall_progress,
        }

    def get_tutorials_summary(self) -> dict[str, Any]:
        """Retourne un résumé des tutoriels avec statistiques réelles"""
        total_tutorials = len(self.tutorials)
        total_steps = sum(len(t.steps) for t in self.tutorials)
        total_attempts = sum(t.total_attempts for t in self.tutorials)

        # Calculer les statistiques réelles
        completion_rates = [t.completion_rate for t in self.tutorials]
        avg_completion = (
            sum(completion_rates) / len(completion_rates) if completion_rates else 0
        )

        return {
            "total_tutorials": total_tutorials,
            "total_steps": total_steps,
            "total_attempts": total_attempts,
            "average_completion_rate": round(avg_completion, 1),
            "categories": list({t.category for t in self.tutorials}),
            "difficulties": list({t.difficulty for t in self.tutorials}),
            "last_updated": datetime.now().isoformat(),
        }

    def generate_tutorials_interface(self) -> str:
        """Génère l'interface web des tutoriels interactifs"""
        try:
            tutorials_file = self.tutorials_dir / "interactive_tutorials.html"
            html_content = self._get_tutorials_template()

            with open(tutorials_file, "w", encoding="utf-8") as f:
                f.write(html_content)

            logger.info(f"Interface des tutoriels générée: {tutorials_file}")
            return str(tutorials_file)

        except Exception as e:
            logger.error(f"Erreur lors de la génération de l'interface: {e}")
            return ""

    def _get_tutorials_template(self) -> str:
        """Retourne le template HTML de l'interface des tutoriels"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutoriels Interactifs - Athalia</title>
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

        .stats-container {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}

        .stats-title {{
            font-size: 2em;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}

        .stat-item {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            border-left: 4px solid #667eea;
        }}

        .stat-value {{
            font-size: 2.5em;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 5px;
        }}

        .stat-label {{
            font-size: 1em;
            color: #666;
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
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}

        .tutorial-card:hover {{
            transform: translateY(-5px);
        }}

        .tutorial-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }}

        .tutorial-title {{
            font-size: 1.5em;
            font-weight: 600;
            color: #667eea;
        }}

        .tutorial-difficulty {{
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 600;
            text-transform: uppercase;
        }}

        .difficulty-beginner {{
            background: #28a745;
            color: white;
        }}

        .difficulty-intermediate {{
            background: #ffc107;
            color: #333;
        }}

        .difficulty-advanced {{
            background: #fd7e14;
            color: white;
        }}

        .difficulty-expert {{
            background: #dc3545;
            color: white;
        }}

        .tutorial-description {{
            color: #666;
            line-height: 1.6;
            margin-bottom: 20px;
        }}

        .tutorial-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            font-size: 0.9em;
            color: #999;
        }}

        .tutorial-stats {{
            display: flex;
            gap: 20px;
        }}

        .stat {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .btn {{
            display: inline-block;
            padding: 12px 24px;
            border: none;
            border-radius: 10px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            text-align: center;
        }}

        .btn-primary {{
            background: #667eea;
            color: white;
        }}

        .btn-primary:hover {{
            background: #5a6fd8;
            transform: translateY(-2px);
        }}

        .btn-success {{
            background: #28a745;
            color: white;
        }}

        .btn-success:hover {{
            background: #218838;
            transform: translateY(-2px);
        }}

        .progress-bar {{
            width: 100%;
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 15px;
        }}

        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #28a745, #20c997);
            transition: width 0.3s ease;
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
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎓 Tutoriels Interactifs Athalia</h1>
            <p>Apprenez Athalia étape par étape avec des tutoriels interactifs personnalisés</p>
        </div>

        <div class="stats-container">
            <h2 class="stats-title">📊 Statistiques des Tutoriels</h2>
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-value">{len(self.tutorials)}</div>
                    <div class="stat-label">Tutoriels Disponibles</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{sum(len(t.steps) for t in self.tutorials)}</div>
                    <div class="stat-label">Étapes Totales</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{sum(t.total_attempts for t in self.tutorials)}</div>
                    <div class="stat-label">Tentatives Totales</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">{round(sum(t.completion_rate for t in self.tutorials) / len(self.tutorials), 1)}%</div>
                    <div class="stat-label">Taux de Réussite Moyen</div>
                </div>
            </div>
        </div>

        <div class="tutorials-grid">
            {self._generate_tutorials_html()}
        </div>

        <div class="footer">
            <p>🕒 Dernière mise à jour: {current_time}</p>
            <p>🎓 Système de tutoriels interactifs généré automatiquement par Athalia</p>
        </div>
    </div>

    <script>
        // Système de gestion des tutoriels interactifs
        let currentUser = 'user_' + Date.now();
        let userProgress = {{}};

        function startTutorial(tutorialId) {{
            // Simuler le démarrage d'un tutoriel
            alert(`🚀 Démarrage du tutoriel ${{tutorialId}} en cours...`);

            // Ici, on pourrait appeler l'API pour démarrer le tutoriel
            if (!userProgress[tutorialId]) {{
                userProgress[tutorialId] = {{
                    currentStep: 0,
                    completedSteps: [],
                    score: 0,
                    startedAt: new Date().toISOString()
                }};
            }}

            // Mettre à jour l'interface
            updateTutorialProgress(tutorialId);
        }}

        function updateTutorialProgress(tutorialId) {{
            const progress = userProgress[tutorialId];
            if (progress) {{
                const progressBar = document.querySelector(`#progress-${{tutorialId}} .progress-fill`);
                if (progressBar) {{
                    const percentage = (progress.completedSteps.length / 6) * 100; // 6 étapes par défaut
                    progressBar.style.width = percentage + '%';
                }}
            }}
        }}

        function completeStep(tutorialId, stepId) {{
            const progress = userProgress[tutorialId];
            if (progress && !progress.completedSteps.includes(stepId)) {{
                progress.completedSteps.push(stepId);
                progress.score = (progress.completedSteps.length / 6) * 100;
                updateTutorialProgress(tutorialId);

                alert(`✅ Étape ${{stepId}} terminée ! Score: ${{progress.score.toFixed(1)}}%`);
            }}
        }}

        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {{
            console.log('🎓 Système de tutoriels interactifs chargé !');
        }});
    </script>
</body>
</html>"""

    def _generate_tutorials_html(self) -> str:
        """Génère le HTML pour les tutoriels"""
        html = ""
        for tutorial in self.tutorials:
            difficulty_class = f"difficulty-{tutorial.difficulty.lower()}"
            progress_percentage = tutorial.completion_rate

            html += f"""
            <div class="tutorial-card" id="tutorial-{tutorial.id}">
                <div class="tutorial-header">
                    <div class="tutorial-title">{tutorial.title}</div>
                    <div class="tutorial-difficulty {difficulty_class}">{tutorial.difficulty}</div>
                </div>

                <div class="tutorial-description">{tutorial.description}</div>

                <div class="tutorial-meta">
                    <div class="tutorial-stats">
                        <div class="stat">⏱️ {tutorial.estimated_total_time} min</div>
                        <div class="stat">📚 {len(tutorial.steps)} étapes</div>
                        <div class="stat">🎯 {tutorial.total_attempts} tentatives</div>
                    </div>
                    <div class="stat">⭐ {tutorial.average_rating:.1f}/5.0</div>
                </div>

                <div class="progress-bar" id="progress-{tutorial.id}">
                    <div class="progress-fill" style="width: {progress_percentage}%"></div>
                </div>

                <div style="display: flex; gap: 10px;">
                    <button class="btn btn-primary" onclick="startTutorial('{tutorial.id}')">
                        🚀 Commencer
                    </button>
                    <button class="btn btn-success" onclick="completeStep('{tutorial.id}', 'step_1')">
                        ✅ Étape 1
                    </button>
                </div>
            </div>
            """
        return html

    def open_tutorials(self) -> None:
        """Ouvre l'interface des tutoriels dans le navigateur"""
        try:
            tutorials_file = self.generate_tutorials_interface()
            if tutorials_file and Path(tutorials_file).exists():
                webbrowser.open(f"file://{Path(tutorials_file).absolute()}")
                logger.info("🌐 Interface des tutoriels ouverte dans le navigateur")
            else:
                logger.error("❌ Impossible de générer l'interface des tutoriels")
        except Exception as e:
            logger.error(f"Erreur lors de l'ouverture des tutoriels: {e}")

    def integrate_with_athalia(self) -> dict[str, Any]:
        """Intègre le système de tutoriels avec Athalia"""
        try:
            # Importer les composants Athalia
            from athalia_core.metrics.collector import MetricsCollector

            # Initialiser le collecteur de métriques
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
                    "estimated_time": 45,
                    "steps": 4,
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
                    "estimated_time": 35,
                    "steps": 3,
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
                    "estimated_time": 25,
                    "steps": 3,
                }
            )

        return custom_tutorials


def main():
    """Fonction principale pour test du système de tutoriels interactifs"""
    import sys

    if len(sys.argv) > 1:
        project_path = sys.argv[1]
    else:
        project_path = "."

    tutorial_system = InteractiveTutorialSystem(project_path)

    if len(sys.argv) > 2 and sys.argv[2] == "test":
        print("🧪 Tests du système de tutoriels interactifs...")

        # Tester la création d'un utilisateur
        user_id = "test_user_001"
        tutorial_id = "athalia_mastery"

        # Démarrer un tutoriel
        result = tutorial_system.start_tutorial(user_id, tutorial_id)
        print(f"✅ Tutoriel démarré: {result}")

        # Récupérer la progression
        progress = tutorial_system.get_user_progress(user_id)
        print(f"📊 Progression utilisateur: {progress}")

        print("✅ Tests terminés")
    else:
        # Ouvrir l'interface
        tutorial_system.open_tutorials()


if __name__ == "__main__":
    main()
