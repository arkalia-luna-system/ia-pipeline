"""
Module d'autocomplétion pour Athalia
Moteur et serveur d'autocomplétion intelligente
"""

from typing import Any

try:
    from .autocomplete_engine import AutocompleteEngine
except ImportError:
    AutocompleteEngine: Any = None

try:
    from .autocomplete_server import AutocompleteServer
except ImportError:
    AutocompleteServer: Any = None

__all__ = [
    "AutocompleteEngine",
    "AutocompleteServer",
]
