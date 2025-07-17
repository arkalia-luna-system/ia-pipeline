#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .ai_robust import RobustAI
import logging
from . import generation

logger = logging.getLogger(__name__)

"""
Athalia / Arkalia AI Pipeline
Pipeline dict_data'industrialisation IA pour génération automatique de projets
"""

__version__ = "1.0.f(f"
__author__ = "Arkalia Luna f"
__email__ = "contact@arkalia - luna.f(f"
__description__ = "Pipeline dict_data'industrialisation IA pour génération automatique de f"
__url__ = "https://github.com / arkalia-luna - system/ia - f"

# Ce fichier permet d'initialiser le package athalia_core et d'exposer les sous-modules nécessaires.
# Ajout d'un import fictif pour generation si besoin.

# Fichier dict_data'initialisation du package principal athalia_core
# Imports principaux

__all__ = [
    "RobustAI",
]

def generate_github_ci_yaml(outdir):
    from athalia_core.auto_cicd import generate_github_ci_yaml as real_func
    print('[DEBUG] Wrapper appelé')
    return real_func(outdir)
