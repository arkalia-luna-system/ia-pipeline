#!/usr/bin/env python3
"""
Athalia Dev Setup - Système d'industrialisation et d'intelligence pour projets IA
Version 2.0.0
"""

from typing import Any

# Version
__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Système d'industrialisation et d'intelligence pour projets IA"

# Import du module core
try:
    from . import core
except ImportError:
    core: Any = None

# Imports conditionnels - seulement les modules qui existent
try:
    from .analytics.advanced_analytics import AdvancedAnalytics
except ImportError:
    AdvancedAnalytics: Any = None

try:
    from .automation.auto_cicd import AutoCICD
except ImportError:
    AutoCICD: Any = None

try:
    from .automation.auto_cleaner import AutoCleaner
except ImportError:
    AutoCleaner: Any = None

try:
    from .automation.auto_documenter import AutoDocumenter
except ImportError:
    AutoDocumenter: Any = None

try:
    from .automation.auto_tester import AutoTester
except ImportError:
    AutoTester: Any = None

try:
    from .quality.code_linter import CodeLinter
except ImportError:
    CodeLinter: Any = None

try:
    from .quality.correction_optimizer import CorrectionOptimizer
except ImportError:
    CorrectionOptimizer: Any = None

try:
    from .core.config_manager import ConfigManager
except ImportError:
    ConfigManager: Any = None

try:
    from .core.cache_manager import CacheManager
except ImportError:
    CacheManager: Any = None

try:
    from .core.error_codes import ErrorCode, ErrorSeverity
except ImportError:
    ErrorCode: Any = None
    ErrorSeverity: Any = None

try:
    from .core.error_handling import (
        AthaliaError,
        ErrorHandler,
        handle_error,
        raise_athalia_error,
    )
except ImportError:
    AthaliaError: Any = None
    ErrorHandler: Any = None
    handle_error: Any = None
    raise_athalia_error: Any = None

try:
    from .core.generation import generate_blueprint_mock, generate_project
except ImportError:
    generate_blueprint_mock: Any = None
    generate_project: Any = None

try:
    from .core.main import (
        log_main,
        main,
        menu,
        running,
        security_audit_project,
        signal_handler,
    )
except ImportError:
    main: Any = None
    menu: Any = None
    running: Any = None
    security_audit_project: Any = None
    signal_handler: Any = None
    log_main: Any = None

try:
    from .core import performance_analyzer
    from .core.performance_analyzer import PerformanceAnalyzer
except ImportError:
    PerformanceAnalyzer: Any = None
    performance_analyzer: Any = None

try:
    from .core.unified_orchestrator import UnifiedOrchestrator
except ImportError:
    UnifiedOrchestrator: Any = None

try:
    from .i18n import en, fr
except ImportError:
    en: Any = None
    fr: Any = None

try:
    from .templates import artistic_templates, base_templates
except ImportError:
    artistic_templates: Any = None
    base_templates: Any = None

try:
    from .classification import project_classifier, project_types
except ImportError:
    project_classifier: Any = None
    project_types: Any = None

try:
    from .ai import ai_robust, ai_robust_enhanced
except ImportError:
    ai_robust: Any = None
    ai_robust_enhanced: Any = None

try:
    from .advanced_modules import (
        auto_correction_advanced,
        dashboard_unified,
        user_profiles_advanced,
    )
except ImportError:
    auto_correction_advanced: Any = None
    dashboard_unified: Any = None
    user_profiles_advanced: Any = None

try:
    from .agents import ath_context_prompt, audit_agent, context_prompt, unified_agent
except ImportError:
    ath_context_prompt: Any = None
    audit_agent: Any = None
    context_prompt: Any = None
    unified_agent: Any = None

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
except ImportError:
    adaptive_distillation: Any = None
    audit_distiller: Any = None
    code_genetics: Any = None
    correction_distiller: Any = None
    multimodal_distiller: Any = None
    predictive_cache: Any = None
    quality_scorer: Any = None
    response_distiller: Any = None

try:
    from .robotics.ros2_validator import ROS2Validator
except ImportError:
    ROS2Validator: Any = None

try:
    from .plugins import (
        ExportDockerPlugin,
        HelloPlugin,
        PluginsManager,
        PluginsValidator,
    )
except ImportError:
    ExportDockerPlugin: Any = None
    HelloPlugin: Any = None
    PluginsManager: Any = None
    PluginsValidator: Any = None

try:
    # Renommer pour éviter le conflit avec PluginsValidator
    from .validation import PluginsValidator as ValidationPluginsValidator
    from .validation import SecurityManager, SecurityValidator
except ImportError:
    ValidationPluginsValidator: Any = None
    SecurityValidator: Any = None
    SecurityManager: Any = None

try:
    from .autocomplete import AutocompleteEngine, AutocompleteServer
except ImportError:
    AutocompleteEngine: Any = None
    AutocompleteServer: Any = None

try:
    from .analysis import (
        ArchitectureAnalyzer,
        ASTAnalyzer,
        IntelligentAnalyzer,
        IntelligentMemory,
        PatternDetector,
    )
except ImportError:
    ArchitectureAnalyzer: Any = None
    ASTAnalyzer: Any = None
    IntelligentAnalyzer: Any = None
    IntelligentMemory: Any = None
    PatternDetector: Any = None

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

    # Importer CLI séparément pour éviter le conflit
    from .utilities.cli import CLI as CLIUtility
    from .utilities.cli import cli
except ImportError:
    CLIUtility: Any = None
    Dashboard: Any = None
    GenerationBackup: Any = None
    GenerationSimple: Any = None
    LoggerAdvanced: Any = None
    MultiFileEditor: Any = None
    Onboarding: Any = None
    ProjectImporter: Any = None
    ReadyCheck: Any = None
    cli: Any = None

try:
    from .analytics import advanced_analytics as advanced_analytics_module
    from .analytics import analytics as analytics_module
except ImportError:
    analytics_module: Any = None
    advanced_analytics_module: Any = None

# Exports principaux - seulement les modules qui existent
__all__ = [
    "__version__",
    "__author__",
    "__description__",
]

# Ajouter dynamiquement les modules qui existent
if core is not None:
    __all__.append("core")

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
if CLIUtility is not None:
    __all__.append("CLI")
if cli is not None:
    __all__.append("cli")
if CodeLinter is not None:
    __all__.append("CodeLinter")
if ConfigManager is not None:
    __all__.append("ConfigManager")
if CacheManager is not None:
    __all__.append("CacheManager")
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
if menu is not None:
    __all__.append("menu")
if running is not None:
    __all__.append("running")
if security_audit_project is not None:
    __all__.append("security_audit_project")
if signal_handler is not None:
    __all__.append("signal_handler")
if log_main is not None:
    __all__.append("log_main")
if PerformanceAnalyzer is not None:
    __all__.append("PerformanceAnalyzer")
if performance_analyzer is not None:
    __all__.append("performance_analyzer")
if UnifiedOrchestrator is not None:
    __all__.append("UnifiedOrchestrator")

if en is not None:
    __all__.append("en")
if fr is not None:
    __all__.append("fr")

if artistic_templates is not None:
    __all__.append("artistic_templates")
if base_templates is not None:
    __all__.append("base_templates")

if project_classifier is not None:
    __all__.append("project_classifier")
if project_types is not None:
    __all__.append("project_types")

if ai_robust is not None:
    __all__.append("ai_robust")
if ai_robust_enhanced is not None:
    __all__.append("ai_robust_enhanced")

if analytics_module is not None:
    __all__.append("analytics")
if advanced_analytics_module is not None:
    __all__.append("advanced_analytics")

if auto_correction_advanced is not None:
    __all__.append("auto_correction_advanced")
if dashboard_unified is not None:
    __all__.append("dashboard_unified")
if user_profiles_advanced is not None:
    __all__.append("user_profiles_advanced")

if PluginsValidator is not None:
    __all__.append("PluginsValidator")

if ValidationPluginsValidator is not None:
    __all__.append("ValidationPluginsValidator")
if SecurityValidator is not None:
    __all__.append("SecurityValidator")
if SecurityManager is not None:
    __all__.append("SecurityManager")

if AutocompleteEngine is not None:
    __all__.append("AutocompleteEngine")
if AutocompleteServer is not None:
    __all__.append("AutocompleteServer")

if ArchitectureAnalyzer is not None:
    __all__.append("ArchitectureAnalyzer")
if ASTAnalyzer is not None:
    __all__.append("ASTAnalyzer")
if IntelligentAnalyzer is not None:
    __all__.append("IntelligentAnalyzer")
if IntelligentMemory is not None:
    __all__.append("IntelligentMemory")
if PatternDetector is not None:
    __all__.append("PatternDetector")

if Dashboard is not None:
    __all__.append("Dashboard")
if GenerationBackup is not None:
    __all__.append("GenerationBackup")
if GenerationSimple is not None:
    __all__.append("GenerationSimple")
if LoggerAdvanced is not None:
    __all__.append("LoggerAdvanced")
if MultiFileEditor is not None:
    __all__.append("MultiFileEditor")
if Onboarding is not None:
    __all__.append("Onboarding")
if ProjectImporter is not None:
    __all__.append("ProjectImporter")
if ReadyCheck is not None:
    __all__.append("ReadyCheck")

if ath_context_prompt is not None:
    __all__.append("ath_context_prompt")
if audit_agent is not None:
    __all__.append("audit_agent")
if context_prompt is not None:
    __all__.append("context_prompt")
if unified_agent is not None:
    __all__.append("unified_agent")

if adaptive_distillation is not None:
    __all__.append("adaptive_distillation")
if audit_distiller is not None:
    __all__.append("audit_distiller")
if code_genetics is not None:
    __all__.append("code_genetics")
if correction_distiller is not None:
    __all__.append("correction_distiller")
if multimodal_distiller is not None:
    __all__.append("multimodal_distiller")
if predictive_cache is not None:
    __all__.append("predictive_cache")
if quality_scorer is not None:
    __all__.append("quality_scorer")
if response_distiller is not None:
    __all__.append("response_distiller")

if ROS2Validator is not None:
    __all__.append("ROS2Validator")

if ExportDockerPlugin is not None:
    __all__.append("ExportDockerPlugin")
if HelloPlugin is not None:
    __all__.append("HelloPlugin")
if PluginsManager is not None:
    __all__.append("PluginsManager")
if PluginsValidator is not None:
    __all__.append("PluginsValidator")
