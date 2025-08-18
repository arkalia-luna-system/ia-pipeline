#!/usr/bin/env python3
"""
Athalia Dev Setup - Système d'industrialisation et d'intelligence pour projets IA
Version 2.0.0
"""

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
    AdvancedAnalytics = None

# Automation
try:
    from .automation.auto_cicd import AutoCICD

    __all__.append("AutoCICD")
except ImportError:
    AutoCICD = None

try:
    from .automation.auto_cleaner import AutoCleaner

    __all__.append("AutoCleaner")
except ImportError:
    AutoCleaner = None

try:
    from .automation.auto_documenter import AutoDocumenter

    __all__.append("AutoDocumenter")
except ImportError:
    AutoDocumenter = None

try:
    from .automation.auto_tester import AutoTester

    __all__.append("AutoTester")
except ImportError:
    AutoTester = None

# Quality
try:
    from .quality.code_linter import CodeLinter

    __all__.append("CodeLinter")
except ImportError:
    CodeLinter = None

try:
    from .quality.correction_optimizer import CorrectionOptimizer

    __all__.append("CorrectionOptimizer")
except ImportError:
    CorrectionOptimizer = None

# Core
try:
    from .core.config_manager import ConfigManager

    __all__.append("ConfigManager")
except ImportError:
    ConfigManager = None

try:
    from .core.cache_manager import CacheManager

    __all__.append("CacheManager")
except ImportError:
    CacheManager = None

try:
    from .core.error_codes import ErrorCode, ErrorSeverity

    __all__.extend(["ErrorCode", "ErrorSeverity"])
except ImportError:
    ErrorCode = None
    ErrorSeverity = None

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
    AthaliaError = None
    ErrorHandler = None
    handle_error = None
    raise_athalia_error = None

try:
    from .core.generation import generate_blueprint_mock, generate_project

    __all__.extend(["generate_blueprint_mock", "generate_project"])
except ImportError:
    generate_blueprint_mock = None
    generate_project = None

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
            "log_main",
            "main",
            "menu",
            "running",
            "security_audit_project",
            "signal_handler",
        ]
    )
except ImportError:
    log_main = None
    main = None
    menu = None
    running = None
    security_audit_project = None
    signal_handler = None

try:
    from .core.performance_analyzer import PerformanceAnalyzer

    __all__.append("PerformanceAnalyzer")
except ImportError:
    PerformanceAnalyzer = None

try:
    from .core.unified_orchestrator import UnifiedOrchestrator

    __all__.append("UnifiedOrchestrator")
except ImportError:
    UnifiedOrchestrator = None

# I18n
try:
    from .i18n import en, fr

    __all__.extend(["en", "fr"])
except ImportError:
    en = None
    fr = None

# Templates
try:
    from .templates import artistic_templates, base_templates

    __all__.extend(["artistic_templates", "base_templates"])
except ImportError:
    artistic_templates = None
    base_templates = None

# Classification
try:
    from .classification import project_classifier, project_types

    __all__.extend(["project_classifier", "project_types"])
except ImportError:
    project_classifier = None
    project_types = None

# AI
try:
    from .ai import ai_robust, ai_robust_enhanced

    __all__.extend(["ai_robust", "ai_robust_enhanced"])
except ImportError:
    ai_robust = None
    ai_robust_enhanced = None

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
    auto_correction_advanced = None
    dashboard_unified = None
    user_profiles_advanced = None

# Agents
try:
    from .agents import ath_context_prompt, audit_agent, context_prompt, unified_agent

    __all__.extend(
        ["ath_context_prompt", "audit_agent", "context_prompt", "unified_agent"]
    )
except ImportError:
    ath_context_prompt = None
    audit_agent = None
    context_prompt = None
    unified_agent = None

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
    adaptive_distillation = None
    audit_distiller = None
    code_genetics = None
    correction_distiller = None
    multimodal_distiller = None
    predictive_cache = None
    quality_scorer = None
    response_distiller = None

# Robotics
try:
    from .robotics.ros2_validator import ROS2Validator

    __all__.append("ROS2Validator")
except ImportError:
    ROS2Validator = None

# Plugins
try:
    from .plugins import (
        ExportDockerPlugin,
        HelloPlugin,
        PluginsManager,
        PluginsValidator,
    )

    __all__.extend(
        ["ExportDockerPlugin", "HelloPlugin", "PluginsManager", "PluginsValidator"]
    )
except ImportError:
    ExportDockerPlugin = None
    HelloPlugin = None
    PluginsManager = None
    PluginsValidator = None

# Validation
try:
    from .validation import SecurityValidator

    __all__.append("SecurityValidator")
except ImportError:
    SecurityValidator = None

try:
    from .validation.security_validator import SecurityManager

    __all__.append("SecurityManager")
except ImportError:
    SecurityManager = None

# Autocomplete
try:
    from .autocomplete import AutocompleteEngine, AutocompleteServer

    __all__.extend(["AutocompleteEngine", "AutocompleteServer"])
except ImportError:
    AutocompleteEngine = None
    AutocompleteServer = None

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
    ArchitectureAnalyzer = None
    ASTAnalyzer = None
    IntelligentAnalyzer = None
    IntelligentMemory = None
    PatternDetector = None

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
    Dashboard = None
    GenerationBackup = None
    GenerationSimple = None
    LoggerAdvanced = None
    MultiFileEditor = None
    Onboarding = None
    ProjectImporter = None
    ReadyCheck = None

try:
    from .utilities.cli import CLI

    __all__.append("CLI")
except ImportError:
    CLI = None

# Analytics
try:
    from .analytics import advanced_analytics, analytics

    __all__.extend(["analytics", "advanced_analytics"])
except ImportError:
    advanced_analytics = None
    analytics = None
