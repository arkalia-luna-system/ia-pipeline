"""
Athalia/Arkalia AI Pipeline
Pipeline d'industrialisation IA pour génération automatique de projets
"""

__version__ = "1.0.0"
__author__ = "Arkalia Luna System"
__email__ = "contact@arkalia-luna.com"
__description__ = "Pipeline d'industrialisation IA pour génération automatique de projets"
__url__ = "https://github.com/arkalia-luna-system/ia-pipeline"

# Fichier d'initialisation du package principal athalia_core
# Imports principaux
from .ai_robust import RobustAI

__all__ = [
    "RobustAI",
]
