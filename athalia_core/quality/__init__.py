"""Module quality pour Athalia"""

try:
    from .code_linter import CodeLinter
except ImportError:
    pass

try:
    from .correction_optimizer import CorrectionOptimizer
except ImportError:
    pass

__all__ = [
    "CodeLinter",
    "CorrectionOptimizer",
]
