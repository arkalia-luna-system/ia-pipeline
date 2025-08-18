"""
Module de gestion des plugins pour Athalia
Gestion, validation et chargement des plugins
"""

# Import des fonctions des plugins
try:
    from .export_docker_plugin import get_info as docker_info
    from .export_docker_plugin import run as docker_run
except ImportError:
    docker_info = None
    docker_run = None

try:
    from .hello_plugin import get_info as hello_info
    from .hello_plugin import run as hello_run
except ImportError:
    hello_info = None
    hello_run = None

try:
    from .plugins_manager import list_plugins, load_plugin, run_all_plugins
except ImportError:
    list_plugins = None
    load_plugin = None
    run_all_plugins = None

try:
    from .plugins_validator import validate_plugin
except ImportError:
    validate_plugin = None

__all__ = [
    "docker_info",
    "docker_run",
    "hello_info",
    "hello_run",
    "list_plugins",
    "load_plugin",
    "run_all_plugins",
    "validate_plugin",
]
