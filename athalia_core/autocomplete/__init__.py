"""
Module d'autocomplétion pour Athalia
Moteur et serveur d'autocomplétion intelligente
"""

try:
    from .autocomplete_engine import AutocompleteEngine
except ImportError:
    AutocompleteEngine = None

try:
    from .autocomplete_server import app as autocomplete_app
except ImportError:
    autocomplete_app = None

__all__ = [
    "AutocompleteEngine",
    "autocomplete_app",
]
