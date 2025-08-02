#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Athalia Dev Setup - Système d'industrialisation et d'intelligence pour projets IA
Version 2.0.0
"""

# Analytics et performance
from .advanced_analytics import AdvancedAnalytics

# IA et génération
# from .ai_robust import RobustAI  # Import conditionnel pour éviter les dépendances
from .auto_cicd import AutoCICD
from .auto_cleaner import AutoCleaner
from .auto_documenter import AutoDocumenter

# Modules automatiques
from .auto_tester import AutoTester
from .cli import cli
from .code_linter import CodeLinter

# Configuration et utilitaires
from .config_manager import ConfigManager
from .correction_optimizer import CorrectionOptimizer

# Gestion d'erreurs
from .error_codes import ErrorCode, ErrorSeverity
from .error_handling import (
    AthaliaError,
    ErrorHandler,
    handle_error,
    raise_athalia_error,
)
from .generation import generate_blueprint_mock, generate_project
from .main import main
from .performance_analyzer import PerformanceAnalyzer

# Sécurité et qualité
from .security_auditor import SecurityAuditor

# Imports principaux
from .unified_orchestrator import UnifiedOrchestrator

# Version
__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Système d'industrialisation et d'intelligence pour projets IA"

# Exports principaux
__all__ = [
    # Orchestrateur principal
    "UnifiedOrchestrator",
    "main",
    "cli",
    # Gestion d'erreurs
    "ErrorCode",
    "ErrorSeverity",
    "AthaliaError",
    "ErrorHandler",
    "handle_error",
    "raise_athalia_error",
    # IA et génération
    # "RobustAI",  # Import conditionnel
    "generate_project",
    "generate_blueprint_mock",
    # Modules automatiques
    "AutoTester",
    "AutoDocumenter",
    "AutoCleaner",
    "AutoCICD",
    # Analytics et performance
    "AdvancedAnalytics",
    "PerformanceAnalyzer",
    # Sécurité et qualité
    "SecurityAuditor",
    "CodeLinter",
    "CorrectionOptimizer",
    # Configuration et utilitaires
    "ConfigManager",
]
