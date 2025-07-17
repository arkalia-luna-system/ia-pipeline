"""
Types de projets et leurs configurations spécialisées.
"""

from enum import Enum
from typing import Dict, List, Any

class ProjectType(Enum):
    """Types de projets supportés."""
    ARTISTIC = "artistic"      # Projets artistiques (fleure qui danse, etc.)
    API = "api"               # APIs et services
    GAME = "game"             # Jeux et applications interactives
    DATA = "data"             # Projets data/ML
    WEB = "web"               # Applications web
    MOBILE = "mobile"         # Applications mobiles
    IOT = "iot"               # Internet des objets
    GENERIC = "generic"       # Projet générique (fallback)

def get_project_config(project_type: ProjectType) -> Dict[str, Any]:
    """Retourne la configuration spécialisée pour un type de projet."""
    
    configs = {
        ProjectType.ARTISTIC: {
            "modules": ["animation", "audio", "visualization", "interaction"],
            "dependencies": ["pygame", "opencv-python", "numpy", "matplotlib"],
            "structure": ["src/", "assets/", "animations/", "audio/", "tests/"],
            "prompts": ["artistic_animation.md", "visual_effects.md", "audio_sync.md"],
            "code_templates": ["artistic"],
            "description": "Projet artistique interactif"
        },
        
        ProjectType.API: {
            "modules": ["api", "database", "auth", "docs"],
            "dependencies": ["fastapi", "sqlalchemy", "pydantic", "uvicorn"],
            "structure": ["src/", "api/", "models/", "database/", "tests/"],
            "prompts": ["api_design.md", "security_audit.md", "performance.md"],
            "code_templates": ["api"],
            "description": "API REST avec authentification"
        },
        
        ProjectType.GAME: {
            "modules": ["game_engine", "physics", "ui", "audio"],
            "dependencies": ["pygame", "pymunk", "tkinter", "pygame-mixer"],
            "structure": ["src/", "game/", "assets/", "levels/", "tests/"],
            "prompts": ["game_mechanics.md", "level_design.md", "ux_fun_boost.md"],
            "code_templates": ["game"],
            "description": "Jeu interactif avec physique"
        },
        
        ProjectType.DATA: {
            "modules": ["data_processing", "ml", "visualization", "api"],
            "dependencies": ["pandas", "scikit-learn", "matplotlib", "fastapi"],
            "structure": ["src/", "data/", "models/", "notebooks/", "tests/"],
            "prompts": ["ml_pipeline.md", "data_analysis.md", "model_evaluation.md"],
            "code_templates": ["data"],
            "description": "Projet de data science et ML"
        },
        
        ProjectType.WEB: {
            "modules": ["frontend", "backend", "database", "auth"],
            "dependencies": ["flask", "jinja2", "sqlalchemy", "flask-login"],
            "structure": ["src/", "templates/", "static/", "database/", "tests/"],
            "prompts": ["web_design.md", "responsive_ui.md", "seo_optimization.md"],
            "code_templates": ["web"],
            "description": "Application web complète"
        },
        
        ProjectType.MOBILE: {
            "modules": ["ui", "api", "storage", "notifications"],
            "dependencies": ["kivy", "requests", "sqlite3", "plyer"],
            "structure": ["src/", "ui/", "api/", "storage/", "tests/"],
            "prompts": ["mobile_ui.md", "offline_sync.md", "performance.md"],
            "code_templates": ["mobile"],
            "description": "Application mobile cross-platform"
        },
        
        ProjectType.IOT: {
            "modules": ["sensors", "communication", "data_logging", "api"],
            "dependencies": ["pyserial", "requests", "sqlite3", "fastapi"],
            "structure": ["src/", "sensors/", "communication/", "data/", "tests/"],
            "prompts": ["iot_architecture.md", "sensor_integration.md", "data_analysis.md"],
            "code_templates": ["iot"],
            "description": "Projet IoT avec capteurs"
        },
        
        ProjectType.GENERIC: {
            "modules": ["api", "tts", "memory"],
            "dependencies": ["flask", "tts", "memorylib"],
            "structure": ["src/", "tests/", "api/", "prompts/"],
            "prompts": ["dev_debug.yaml", "ux_fun_boost.md"],
            "code_templates": ["generic"],
            "description": "Projet générique"
        }
    }
    
    return configs.get(project_type, configs[ProjectType.GENERIC]) 