"""Module quality pour Athalia"""

from typing import Any

try:
    from .code_linter import CodeLinter
except ImportError:
    CodeLinter: Any = None

try:
    from .correction_optimizer import CorrectionOptimizer
except ImportError:
    CorrectionOptimizer: Any = None

__all__ = [
    "CodeLinter",
    "CorrectionOptimizer",
]
