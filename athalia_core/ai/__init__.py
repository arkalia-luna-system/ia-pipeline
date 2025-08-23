#!/usr/bin/env python3
"""
Module AI d'Athalia - Intelligence artificielle robuste
=======================================================

Ce module contient les composants d'intelligence artificielle :
- AI robuste de base
- AI robuste améliorée
- Gestion des erreurs IA
- Validation des modèles
"""

# Imports des modules AI
from .ai_robust import RobustAI, SecurityError, query_qwen, validateand_run
from .ai_robust_enhanced import RobustAI as RobustAIEnhanced

# Exports publics
__all__ = [
    "RobustAI",
    "RobustAIEnhanced",
    "SecurityError",
    "validate_and_run",
    "query_qwen",
]

__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Module AI - Intelligence artificielle robuste"
