"""Module quality pour Athalia"""

from typing import Any

try:
    from .code_linter import CodeLinter
except ImportError:
    CodeLinter: type[Any] = type("CodeLinterFallback", (), {})

try:
    from .correction_optimizer import CorrectionOptimizer
except ImportError:
    CorrectionOptimizer: type[Any] = type("CorrectionOptimizerFallback", (), {})

__all__ = [
    "CodeLinter",
    "CorrectionOptimizer",
]
