"""
Module d'analyse de code et d'architecture pour Athalia
Analyse AST, patterns, architecture et intelligence
"""

try:
    from .architecture_analyzer import ArchitectureAnalyzer
except ImportError:
    pass

try:
    from .ast_analyzer import ASTAnalyzer
except ImportError:
    pass

try:
    from .intelligent_analyzer import ComprehensiveAnalysis, IntelligentAnalyzer
except ImportError:
    pass

try:
    from .intelligent_memory import (
        CorrectionSuggestion,
        IntelligentMemory,
        LearningEvent,
        Prediction,
    )
except ImportError:
    pass

try:
    from .pattern_detector import PatternDetector
except ImportError:
    pass

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
