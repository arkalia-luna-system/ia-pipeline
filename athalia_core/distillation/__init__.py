#!/usr/bin/env python3
"""
Module de distillation IA pour Athalia/Arkalia
==============================================

Ce module gère la distillation et l'optimisation des modèles IA.
Fournit des outils pour améliorer les performances et réduire la taille.
"""

# Imports des modules de distillation disponibles
from .adaptive_distillation import AdaptiveDistiller
from .audit_distiller import AuditDistiller
from .code_genetics import CodeGenetics
from .correction_distiller import CorrectionDistiller
from .multimodal_distiller import MultimodalDistiller
from .predictive_cache import PredictiveCache
from .quality_scorer import QualityScorer
from .response_distiller import ResponseDistiller

__all__ = [
    "AdaptiveDistiller",
    "AuditDistiller",
    "CodeGenetics",
    "CorrectionDistiller",
    "MultimodalDistiller",
    "PredictiveCache",
    "QualityScorer",
    "ResponseDistiller",
]

__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Distillation et optimisation IA"
