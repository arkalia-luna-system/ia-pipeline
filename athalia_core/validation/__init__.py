"""
Module de validation et sécurité pour Athalia
Validation des plugins, sécurité et audit
"""

from typing import Any

try:
    from .plugins_validator import PluginValidator
except ImportError:
    PluginValidator: type[Any] = type("PluginValidator", (), {})

try:
    from .security_validator import SecurityValidator
except ImportError:
    SecurityValidator: type[Any] = type("SecurityValidator", (), {})

try:
    from .security_validator import SecurityManager
except ImportError:
    SecurityManager: type[Any] = type("SecurityManager", (), {})

__all__ = [
    "PluginValidator",
    "SecurityValidator",
    "SecurityManager",
]
