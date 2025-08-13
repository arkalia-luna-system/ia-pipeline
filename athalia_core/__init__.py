#!/usr/bin/env python3
"""
Athalia Dev Setup - Système d'industrialisation et d'intelligence pour projets IA
Version 2.0.0
"""

# Version
__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Système d'industrialisation et d'intelligence pour projets IA"

# Imports conditionnels - seulement les modules qui existent
try:
    from .analytics.advanced_analytics import AdvancedAnalytics
except ImportError:
    AdvancedAnalytics = None

try:
    from .auto_cicd import AutoCICD
except ImportError:
    AutoCICD = None

try:
    from .auto_cleaner import AutoCleaner
except ImportError:
    AutoCleaner = None

try:
    from .auto_documenter import AutoDocumenter
except ImportError:
    AutoDocumenter = None

try:
    from .auto_tester import AutoTester
except ImportError:
    AutoTester = None

try:
    from .cli import cli
except ImportError:
    cli = None

try:
    from .code_linter import CodeLinter
except ImportError:
    CodeLinter = None

try:
    from .config_manager import ConfigManager
except ImportError:
    ConfigManager = None

try:
    from .correction_optimizer import CorrectionOptimizer
except ImportError:
    CorrectionOptimizer = None

try:
    from .error_codes import ErrorCode, ErrorSeverity
except ImportError:
    ErrorCode = None
    ErrorSeverity = None

try:
    from .error_handling import (
        AthaliaError,
        ErrorHandler,
        handle_error,
        raise_athalia_error,
    )
except ImportError:
    AthaliaError = None
    ErrorHandler = None
    handle_error = None
    raise_athalia_error = None

try:
    from .generation import generate_blueprint_mock, generate_project
except ImportError:
    generate_blueprint_mock = None
    generate_project = None

try:
    from .main import main
except ImportError:
    main = None

try:
    from .performance_analyzer import PerformanceAnalyzer
except ImportError:
    PerformanceAnalyzer = None

try:
    from .unified_orchestrator import UnifiedOrchestrator
except ImportError:
    UnifiedOrchestrator = None

# Exports principaux - seulement les modules qui existent
__all__ = [
    "__version__",
    "__author__",
    "__description__",
]

# Ajouter dynamiquement les modules qui existent
if AdvancedAnalytics is not None:
    __all__.append("AdvancedAnalytics")
if AutoCICD is not None:
    __all__.append("AutoCICD")
if AutoCleaner is not None:
    __all__.append("AutoCleaner")
if AutoDocumenter is not None:
    __all__.append("AutoDocumenter")
if AutoTester is not None:
    __all__.append("AutoTester")
if cli is not None:
    __all__.append("cli")
if CodeLinter is not None:
    __all__.append("CodeLinter")
if ConfigManager is not None:
    __all__.append("ConfigManager")
if CorrectionOptimizer is not None:
    __all__.append("CorrectionOptimizer")
if ErrorCode is not None:
    __all__.append("ErrorCode")
if ErrorSeverity is not None:
    __all__.append("ErrorSeverity")
if AthaliaError is not None:
    __all__.append("AthaliaError")
if ErrorHandler is not None:
    __all__.append("ErrorHandler")
if handle_error is not None:
    __all__.append("handle_error")
if raise_athalia_error is not None:
    __all__.append("raise_athalia_error")
if generate_project is not None:
    __all__.append("generate_project")
if generate_blueprint_mock is not None:
    __all__.append("generate_blueprint_mock")
if main is not None:
    __all__.append("main")
if PerformanceAnalyzer is not None:
    __all__.append("PerformanceAnalyzer")
if UnifiedOrchestrator is not None:
    __all__.append("UnifiedOrchestrator")
