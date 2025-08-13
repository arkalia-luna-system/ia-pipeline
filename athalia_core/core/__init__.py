#!/usr/bin/env python3
"""
Module Core d'Athalia - Fonctionnalités de base essentielles
============================================================

Ce module contient les composants fondamentaux d'Athalia :
- Gestion de configuration
- Gestion du cache
- Gestion des erreurs
- Génération de projets
- Orchestrateur unifié
- Analyseur de performance
- Interface principale
"""

from .cache_manager import CacheManager
from .config_manager import ConfigManager
from .error_codes import ErrorCode, ErrorSeverity
from .error_handling import (
    AthaliaError,
    ErrorHandler,
    handle_error,
    raise_athalia_error,
)
from .generation import generate_blueprint_mock, generate_project
from .main import (
    log_main,
    main,
    menu,
    running,
    security_audit_project,
    signal_handler,
)
from .performance_analyzer import PerformanceAnalyzer
from .unified_orchestrator import UnifiedOrchestrator

# Exports publics
__all__ = [
    # Configuration et cache
    "CacheManager",
    "ConfigManager",
    # Gestion des erreurs
    "AthaliaError",
    "ErrorCode",
    "ErrorHandler",
    "ErrorSeverity",
    "handle_error",
    "raise_athalia_error",
    # Génération
    "generate_blueprint_mock",
    "generate_project",
    # Interface principale
    "log_main",
    "main",
    "menu",
    "running",
    "security_audit_project",
    "signal_handler",
    # Analyse et orchestration
    "PerformanceAnalyzer",
    "UnifiedOrchestrator",
]

__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Module Core - Fonctionnalités de base essentielles"
