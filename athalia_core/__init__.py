#!/usr/bin/env python3
"""
Athalia Dev Setup - Système d'industrialisation et d'intelligence pour projets IA
Version 2.0.0
"""

from typing import Any, Optional

# Version
__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Système d'industrialisation et d'intelligence pour projets IA"

# Exports principaux
__all__ = [
    "__version__",
    "__author__",
    "__description__",
]

# Imports directs des modules principaux
try:
    from . import core

    __all__.append("core")
except ImportError:
    pass

# Analytics
try:
    from .analytics.advanced_analytics import AdvancedAnalytics

    __all__.append("AdvancedAnalytics")
except ImportError:
    pass

# Automation
try:
    from .automation.auto_cicd import AutoCICD

    __all__.append("AutoCICD")
except ImportError:
    pass

try:
    from .automation.auto_cleaner import AutoCleaner

    __all__.append("AutoCleaner")
except ImportError:
    pass

try:
    from .automation.auto_documenter import AutoDocumenter

    __all__.append("AutoDocumenter")
except ImportError:
    pass

try:
    from .automation.auto_tester import AutoTester

    __all__.append("AutoTester")
except ImportError:
    pass

# Quality
try:
    from .quality.code_linter import CodeLinter

    __all__.append("CodeLinter")
except ImportError:
    pass

try:
    from .quality.correction_optimizer import CorrectionOptimizer

    __all__.append("CorrectionOptimizer")
except ImportError:
    pass

# Core
try:
    from .core.config_manager import ConfigManager

    __all__.append("ConfigManager")
except ImportError:
    pass

try:
    from .core.cache_manager import CacheManager

    __all__.append("CacheManager")
except ImportError:
    pass

try:
    from .core.error_codes import ErrorCode, ErrorSeverity

    __all__.extend(["ErrorCode", "ErrorSeverity"])
except ImportError:
    pass

try:
    from .core.error_handling import (
        AthaliaError,
        ErrorHandler,
        handle_error,
        raise_athalia_error,
    )

    __all__.extend(
        ["AthaliaError", "ErrorHandler", "handle_error", "raise_athalia_error"]
    )
except ImportError:
    pass

try:
    from .core.generation import generate_blueprint_mock, generate_project

    __all__.extend(["generate_blueprint_mock", "generate_project"])
except ImportError:
    pass

try:
    from .core.main import (
        log_main,
        main,
        menu,
        running,
        security_audit_project,
        signal_handler,
    )

    __all__.extend(
        [
            "main",
            "menu",
            "running",
            "security_audit_project",
            "signal_handler",
            "log_main",
        ]
    )
except ImportError:
    pass

try:
    from .core.performance_analyzer import PerformanceAnalyzer

    __all__.append("PerformanceAnalyzer")
except ImportError:
    pass

try:
    from .core.unified_orchestrator import UnifiedOrchestrator

    __all__.append("UnifiedOrchestrator")
except ImportError:
    pass

# I18n
try:
    from .i18n import en, fr

    __all__.extend(["en", "fr"])
except ImportError:
    pass

# Templates
try:
    from .templates import artistic_templates, base_templates

    __all__.extend(["artistic_templates", "base_templates"])
except ImportError:
    pass

# Classification
try:
    from .classification import project_classifier, project_types

    __all__.extend(["project_classifier", "project_types"])
except ImportError:
    pass

# AI
try:
    from .ai import ai_robust, ai_robust_enhanced

    __all__.extend(["ai_robust", "ai_robust_enhanced"])
except ImportError:
    pass

# Advanced modules
try:
    from .advanced_modules import (
        auto_correction_advanced,
        dashboard_unified,
        user_profiles_advanced,
    )

    __all__.extend(
        ["auto_correction_advanced", "dashboard_unified", "user_profiles_advanced"]
    )
except ImportError:
    pass

# Agents
try:
    from .agents import (
        ath_context_prompt,
        audit_agent,
        context_prompt,
        unified_agent,
    )

    __all__.extend(
        ["ath_context_prompt", "audit_agent", "context_prompt", "unified_agent"]
    )
except ImportError:
    pass

# Distillation
try:
    from .distillation import (
        adaptive_distillation,
        audit_distiller,
        code_genetics,
        correction_distiller,
        multimodal_distiller,
        predictive_cache,
        quality_scorer,
        response_distiller,
    )

    __all__.extend(
        [
            "adaptive_distillation",
            "audit_distiller",
            "code_genetics",
            "correction_distiller",
            "multimodal_distiller",
            "predictive_cache",
            "quality_scorer",
            "response_distiller",
        ]
    )
except ImportError:
    pass

# Robotics
try:
    from .robotics.ros2_validator import ROS2Validator

    __all__.append("ROS2Validator")
except ImportError:
    pass

# Plugins
try:
    from .plugins import (
        docker_info,
        docker_run,
        hello_info,
        hello_run,
        list_plugins,
        load_plugin,
        run_all_plugins,
        validate_plugin,
    )

    __all__.extend(
        [
            "docker_run",
            "docker_info",
            "hello_run",
            "hello_info",
            "list_plugins",
            "load_plugin",
            "run_all_plugins",
            "validate_plugin",
        ]
    )
except ImportError:
    pass

# Validation
try:
    from .validation import SecurityManager, SecurityValidator

    __all__.extend(["SecurityValidator", "SecurityManager"])
except ImportError:
    pass

# Autocomplete
try:
    from .autocomplete import AutocompleteEngine, autocomplete_app

    __all__.extend(["AutocompleteEngine", "autocomplete_app"])
except ImportError:
    pass

# Analysis
try:
    from .analysis import (
        ArchitectureAnalyzer,
        ASTAnalyzer,
        IntelligentAnalyzer,
        IntelligentMemory,
        PatternDetector,
    )

    __all__.extend(
        [
            "ArchitectureAnalyzer",
            "ASTAnalyzer",
            "IntelligentAnalyzer",
            "IntelligentMemory",
            "PatternDetector",
        ]
    )
except ImportError:
    pass

# Utilities
try:
    from .utilities import (
        Dashboard,
        GenerationBackup,
        GenerationSimple,
        LoggerAdvanced,
        MultiFileEditor,
        Onboarding,
        ProjectImporter,
        ReadyCheck,
    )

    __all__.extend(
        [
            "Dashboard",
            "GenerationBackup",
            "GenerationSimple",
            "LoggerAdvanced",
            "MultiFileEditor",
            "Onboarding",
            "ProjectImporter",
            "ReadyCheck",
        ]
    )
except ImportError:
    pass

try:
    from .utilities.cli import cli

    __all__.append("CLI")
except ImportError:
    pass

# Analytics
try:
    from .analytics import advanced_analytics, analytics

    __all__.extend(["analytics", "advanced_analytics"])
except ImportError:
    pass
