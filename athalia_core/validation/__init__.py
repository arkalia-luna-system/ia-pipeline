"""
Module de validation et sécurité pour Athalia
Validation des plugins, sécurité et audit
"""

from typing import Any

try:
    from .plugins_validator import PluginValidator
except ImportError:
    PluginValidator: type[Any] = type("PluginValidatorFallback", (), {})

try:
    from .security_validator import SecurityValidator
except ImportError:
    SecurityValidator: type[Any] = type("SecurityValidatorFallback", (), {})

try:
    from .security_validator import SecurityManager
except ImportError:
    SecurityManager: type[Any] = type("SecurityManagerFallback", (), {})

__all__ = [
    "PluginValidator",
    "SecurityValidator",
    "SecurityManager",
]
