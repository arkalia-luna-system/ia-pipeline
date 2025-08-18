"""
Module d'analyse de code et d'architecture pour Athalia
Analyse AST, patterns, architecture et intelligence
"""

from typing import Any

try:
    from .architecture_analyzer import ArchitectureAnalyzer
except ImportError:
    ArchitectureAnalyzer: type[Any] = type("ArchitectureAnalyzerFallback", (), {})

try:
    from .ast_analyzer import ASTAnalyzer
except ImportError:
    ASTAnalyzer: type[Any] = type("ASTAnalyzerFallback", (), {})

try:
    from .intelligent_analyzer import ComprehensiveAnalysis, IntelligentAnalyzer
except ImportError:
    IntelligentAnalyzer: type[Any] = type("IntelligentAnalyzerFallback", (), {})
    ComprehensiveAnalysis: type[Any] = type("ComprehensiveAnalysisFallback", (), {})

try:
    from .intelligent_memory import (
        CorrectionSuggestion,
        IntelligentMemory,
        LearningEvent,
        Prediction,
    )
except ImportError:
    IntelligentMemory: type[Any] = type("IntelligentMemoryFallback", (), {})
    CorrectionSuggestion: type[Any] = type("CorrectionSuggestionFallback", (), {})
    LearningEvent: type[Any] = type("LearningEventFallback", (), {})
    Prediction: type[Any] = type("PredictionFallback", (), {})

try:
    from .pattern_detector import PatternDetector
except ImportError:
    PatternDetector: type[Any] = type("PatternDetectorFallback", (), {})

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
