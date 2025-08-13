#!/usr/bin/env python3
"""
Module Automation d'Athalia - Automatisation intelligente
========================================================

Ce module contient les composants d'automatisation :
- CI/CD automatique
- Nettoyage automatique
- Documentation automatique
- Tests automatiques
- CI robotique
"""

# Imports des modules d'automatisation
from .auto_cicd import AutoCICD
from .auto_cleaner import AutoCleaner
from .auto_documenter import AutoDocumenter
from .auto_tester import AutoTester
from .robotics_ci import RoboticsCI, run_robotics_ci

# Exports publics
__all__ = [
    "AutoCICD",
    "AutoCleaner",
    "AutoDocumenter",
    "AutoTester",
    "RoboticsCI",
    "run_robotics_ci",
]

__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Module Automation - Automatisation intelligente"
