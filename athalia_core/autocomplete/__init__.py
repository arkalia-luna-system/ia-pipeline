"""
Module d'autocomplétion pour Athalia
Moteur d'autocomplétion intelligent et serveur
"""

try:
    from .autocomplete_engine import AutocompleteEngine
except ImportError:
    pass

try:
    from .autocomplete_server import app as AutocompleteServer
except ImportError:
    pass

__all__ = [
    "AutocompleteEngine",
    "AutocompleteServer",
]
