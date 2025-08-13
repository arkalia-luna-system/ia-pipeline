"""
Module d'autocomplétion pour Athalia
Moteur et serveur d'autocomplétion intelligente
"""

try:
    from .autocomplete_engine import AutocompleteEngine
except ImportError:
    AutocompleteEngine = None

try:
    from .autocomplete_server import AutocompleteServer
except ImportError:
    AutocompleteServer = None

__all__ = [
    "AutocompleteEngine",
    "AutocompleteServer",
]
