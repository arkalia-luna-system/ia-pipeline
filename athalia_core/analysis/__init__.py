"""
Module d'analyse de code et d'architecture pour Athalia
Analyse AST, patterns, architecture et intelligence
"""

try:
    from .architecture_analyzer import ArchitectureAnalyzer
except ImportError:
    ArchitectureAnalyzer = None

try:
    from .ast_analyzer import ASTAnalyzer
except ImportError:
    ASTAnalyzer = None

try:
    from .intelligent_analyzer import ComprehensiveAnalysis, IntelligentAnalyzer
except ImportError:
    IntelligentAnalyzer = None
    ComprehensiveAnalysis = None

try:
    from .intelligent_memory import IntelligentMemory
except ImportError:
    IntelligentMemory = None

try:
    from .pattern_detector import PatternDetector
except ImportError:
    PatternDetector = None

__all__ = [
    "ArchitectureAnalyzer",
    "ASTAnalyzer",
    "IntelligentAnalyzer",
    "ComprehensiveAnalysis",
    "IntelligentMemory",
    "PatternDetector",
]
