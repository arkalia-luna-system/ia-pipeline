#!/usr/bin/env python3
"""
Module de distillation IA pour Athalia/Arkalia
==============================================

Ce module gère la distillation et l'optimisation des modèles IA.
Fournit des outils pour améliorer les performances et réduire la taille.
"""

# Imports des modules de distillation
from .adaptive_distillation import AdaptiveDistiller
from .audit_distiller import AuditDistiller
from .distillation_engine import DistillationEngine

__all__ = [
    "AdaptiveDistiller",
    "AuditDistiller",
    "DistillationEngine",
]

__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Distillation et optimisation IA"
