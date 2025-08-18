"""Module quality pour Athalia"""

try:
    from .code_linter import CodeLinter
except ImportError:
    CodeLinter = None

try:
    from .correction_optimizer import CorrectionOptimizer
except ImportError:
    CorrectionOptimizer = None

__all__ = [
    "CodeLinter",
    "CorrectionOptimizer",
]
