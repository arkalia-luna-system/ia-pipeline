#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

from .project_types import ProjectType

"""
Classifieur intelligent de projets.
Analyse le contexte et détermine le type de projet approprié.
"""


def classify_project(idea: str) -> ProjectType:
    """
    Analyse l'idée du projet et retourne le type approprié.

    Args:
        idea: Description du projet en une phrase

    Returns:
        ProjectType: Type de projet détecté
    """
    idea_lower = idea.lower()

    # Ajout détection explicite pour todo-list
    if any(
        kw in idea_lower
        for kw in [
            "todo",
            "tâche",
            "taches",
            "task",
            "liste de tâches",
            "liste de taches",
            "todo-list",
            "todo list",
        ]
    ):
        return ProjectType.API

    # Mots-clés pour chaque type de projet
    artistic_keywords = [
        "fleure",
        "fleur",
        "danse",
        "dance",
        "art",
        "artistique",
        "visuel",
        "animation",
        "musique",
        "couleur",
        "peinture",
        "dessin",
        "sculpture",
        "créatif",
        "creative",
        "esthétique",
        "beauté",
        "harmonie",
    ]

    api_keywords = [
        "api",
        "service",
        "backend",
        "rest",
        "graphql",
        "microservice",
        "endpoint",
        "webservice",
        "serveur",
        "server",
        "interface",
    ]

    game_keywords = [
        "jeu",
        "game",
        "jouer",
        "play",
        "score",
        "niveau",
        "level",
        "gagner",
        "win",
        "perdre",
        "lose",
        "règles",
        "rules",
        "plateforme",
    ]

    data_keywords = [
        "data",
        "données",
        "analyse",
        "analysis",
        "ml",
        "machine learning",
        "ai",
        "intelligence artificielle",
        "statistiques",
        "stats",
        "prédiction",
        "prediction",
        "modèle",
        "model",
    ]

    web_keywords = [
        "web",
        "site",
        "application web",
        "frontend",
        "backend",
        "html",
        "css",
        "javascript",
        "react",
        "vue",
        "angular",
    ]

    mobile_keywords = [
        "mobile",
        "app",
        "application mobile",
        "smartphone",
        "tablet",
        "ios",
        "android",
        "touch",
        "geste",
        "swipe",
    ]

    iot_keywords = [
        "iot",
        "capteur",
        "sensor",
        "arduino",
        "raspberry",
        "pi",
        "électronique",
        "electronic",
        "hardware",
        "matériel",
    ]

    # Calcul des scores pour chaque type
    scores = {
        ProjectType.ARTISTIC: sum(1 for kw in artistic_keywords if kw in idea_lower),
        ProjectType.API: sum(1 for kw in api_keywords if kw in idea_lower),
        ProjectType.GAME: sum(1 for kw in game_keywords if kw in idea_lower),
        ProjectType.DATA: sum(1 for kw in data_keywords if kw in idea_lower),
        ProjectType.WEB: sum(1 for kw in web_keywords if kw in idea_lower),
        ProjectType.MOBILE: sum(1 for kw in mobile_keywords if kw in idea_lower),
        ProjectType.IOT: sum(1 for kw in iot_keywords if kw in idea_lower),
    }

    # Règles spéciales
    if "fleure qui danse" in idea_lower or "fleur qui danse" in idea_lower:
        return ProjectType.ARTISTIC

    if "api" in idea_lower and any(kw in idea_lower for kw in ["service", "backend"]):
        return ProjectType.API

    if any(word in idea_lower for word in ["jeu", "game", "play"]):
        return ProjectType.GAME

    # Retourner le type avec le score le plus élevé
    max_score = max(scores.values())
    if max_score > 0:
        for project_type, score in scores.items():
            if score == max_score:
                return project_type

    # Fallback vers générique
    return ProjectType.GENERIC


def get_project_name(idea: str, project_type: ProjectType) -> str:
    """
    Génère un nom de projet approprié basé sur l'idée et le type.

    Args:
        idea: Description du projet
        project_type: Type de projet détecté

    Returns:
        str: Nom de projet généré
    """
    # Extraire des mots-clés de l'idée
    words = re.findall(r"\b\w+\b", idea.lower())

    if project_type == ProjectType.ARTISTIC:
        if "fleure" in idea.lower() or "fleur" in idea.lower():
            return "artistic_flower_dance"
        return "artistic_project"

    elif project_type == ProjectType.API:
        return "api_service"

    elif project_type == ProjectType.GAME:
        return "interactive_game"

    elif project_type == ProjectType.DATA:
        return "data_analysis_project"

    elif project_type == ProjectType.WEB:
        return "web_application"

    elif project_type == ProjectType.MOBILE:
        return "mobile_app"

    elif project_type == ProjectType.IOT:
        return "iot_project"

    else:
        # Générique : utiliser les premiers mots de l'idée
        if len(words) >= 2:
            return f"{words[0]}_{words[1]}_project"
        return "ia_project"
