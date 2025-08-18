"""
Module d'autocomplétion pour Athalia
Moteur et serveur d'autocomplétion intelligente
"""

from typing import Any

try:
    from .autocomplete_engine import AutocompleteEngine
except ImportError:
    AutocompleteEngine: type[Any] = type("AutocompleteEngineFallback", (), {})

try:
    from .autocomplete_server import app as AutocompleteServer
except ImportError:
    AutocompleteServer: type[Any] = type("AutocompleteServerFallback", (), {})

__all__ = [
    "AutocompleteEngine",
    "AutocompleteServer",
]
