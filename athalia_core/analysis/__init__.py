"""
Module d'analyse de code et d'architecture pour Athalia
Analyse AST, patterns, architecture et intelligence
"""

from typing import Any

try:
    from .architecture_analyzer import ArchitectureAnalyzer
except ImportError:
    ArchitectureAnalyzer: Any = None

try:
    from .ast_analyzer import ASTAnalyzer
except ImportError:
    ASTAnalyzer: Any = None

try:
    from .intelligent_analyzer import ComprehensiveAnalysis, IntelligentAnalyzer
except ImportError:
    IntelligentAnalyzer: Any = None
    ComprehensiveAnalysis: Any = None

try:
    from .intelligent_memory import (
        CorrectionSuggestion,
        IntelligentMemory,
        LearningEvent,
        Prediction,
    )
except ImportError:
    IntelligentMemory: Any = None
    CorrectionSuggestion: Any = None
    LearningEvent: Any = None
    Prediction: Any = None

try:
    from .pattern_detector import PatternDetector
except ImportError:
    PatternDetector: Any = None

__all__ = [
    "ArchitectureAnalyzer",
    "ASTAnalyzer",
    "IntelligentAnalyzer",
    "ComprehensiveAnalysis",
    "IntelligentMemory",
    "CorrectionSuggestion",
    "LearningEvent",
    "Prediction",
    "PatternDetector",
]
