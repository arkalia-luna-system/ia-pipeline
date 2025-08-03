#!/usr/bin/env python3
from enum import Enum
from typing import Any

"""
Types de projets et leurs configurations spécialisées.
"""


class ProjectType(Enum):
    """Types de projets supportés."""

    ARTISTIC = "artistic"  # Projets artistiques (fleur qui danse, etc.)
    API = "api"  # APIs et services
    GAME = "game"  # Jeux et applications interactives
    DATA = "data"  # Projets data / ML
    WEB = "web"  # Applications web
    MOBILE = "mobile"  # Applications mobiles
    IOT = "iot"  # Internet des objets
    ROBOTICS = "robotics"  # Projets robotiques et contrôle
    GENERIC = "generic"  # Projet générique (fallback)


def get_project_config(project_type: ProjectType) -> dict[str, Any]:
    """Retourne la configuration spécialisée pour un type de projet."""

    configs = {
        ProjectType.ARTISTIC: {
            "modules": ["core", "animation", "visual", "audio"],
            "dependencies": ["numpy", "opencv-python", "matplotlib", "pygame"],
            "structure": [
                "src/",
                "assets/",
                "animations/",
                "audio/",
                "tests/",
            ],
            "prompts": [
                "artistic_animation.yaml",
                "visual_effects.yaml",
                "audio_sync.yaml",
            ],
            "booster_ia": ["artistic"],
            "description": "Projet artistique avec animations",
        },
        ProjectType.API: {
            "modules": ["core", "api", "auth", "database"],
            "dependencies": [
                "fastapi",
                "sqlalchemy",
                "pydantic",
                "python-jose",
            ],
            "structure": [
                "src/",
                "api/",
                "models/",
                "database/",
                "tests/",
                "docs/",
            ],
            "prompts": [
                "api_design.yaml",
                "security_audit.yaml",
                "performance.yaml",
            ],
            "booster_ia": ["api"],
            "description": "API REST avec authentification et sécurité",
        },
        ProjectType.GAME: {
            "modules": ["core", "game", "ui", "physics"],
            "dependencies": ["pygame", "numpy", "pymunk", "pygame-gui"],
            "structure": ["src/", "game/", "assets/", "levels/", "tests/"],
            "prompts": [
                "game_mechanics.yaml",
                "level_design.yaml",
                "ux_fun_boost.yaml",
            ],
            "booster_ia": ["game"],
            "description": "Jeu interactif avec physique",
        },
        ProjectType.DATA: {
            "modules": ["core", "data", "ml", "viz"],
            "dependencies": [
                "pandas",
                "scikit-learn",
                "matplotlib",
                "seaborn",
            ],
            "structure": ["src/", "data/", "models/", "notebooks/", "tests/"],
            "prompts": [
                "ml_pipeline.yaml",
                "data_analysis.yaml",
                "model_evaluation.yaml",
            ],
            "booster_ia": ["data"],
            "description": "Projet de data science et ML",
        },
        ProjectType.WEB: {
            "modules": ["core", "web", "ui", "database"],
            "dependencies": ["flask", "jinja2", "sqlalchemy", "flask-cors"],
            "structure": [
                "src/",
                "templates/",
                "static/",
                "database/",
                "tests/",
            ],
            "prompts": [
                "web_design.yaml",
                "responsive_ui.yaml",
                "seo_optimization.yaml",
            ],
            "booster_ia": ["web"],
            "description": "Application web responsive",
        },
        ProjectType.MOBILE: {
            "modules": ["core", "ui", "api", "storage"],
            "dependencies": ["kivy", "requests", "sqlite3", "plyer"],
            "structure": ["src/", "ui/", "api/", "storage/", "tests/"],
            "prompts": [
                "mobile_ui.yaml",
                "offline_sync.yaml",
                "performance.yaml",
            ],
            "booster_ia": ["mobile"],
            "description": "Application mobile cross-platform",
        },
        ProjectType.IOT: {
            "modules": ["core", "sensors", "communication", "data"],
            "dependencies": ["pyserial", "paho-mqtt", "numpy", "matplotlib"],
            "structure": [
                "src/",
                "sensors/",
                "communication/",
                "data/",
                "tests/",
            ],
            "prompts": [
                "iot_architecture.yaml",
                "sensor_integration.yaml",
                "data_analysis.yaml",
            ],
            "booster_ia": ["iot"],
            "description": "Projet IoT avec capteurs",
        },
        ProjectType.ROBOTICS: {
            "modules": ["core", "control", "sensors", "interface"],
            "dependencies": ["rclpy", "opencv-python", "numpy", "pyserial"],
            "structure": [
                "src/",
                "control/",
                "sensors/",
                "interface/",
                "tests/",
            ],
            "prompts": [
                "robotics_control.yaml",
                "sensor_integration.yaml",
                "interface_design.yaml",
            ],
            "booster_ia": ["robotics"],
            "description": "Projet robotique avec contrôle et capteurs",
        },
        ProjectType.GENERIC: {
            "modules": ["core", "utils", "tests"],
            "dependencies": ["requests", "pytest", "logging"],
            "structure": ["src/", "tests/", "api/", "prompts/"],
            "prompts": ["${ENV:-production}_debug.yaml", "ux_fun_boost.yaml"],
            "booster_ia": ["generic"],
            "description": "Projet générique",
        },
    }

    return configs.get(project_type, configs[ProjectType.GENERIC])
