"""
Module de gestion des plugins pour Athalia
Gestion, validation et chargement des plugins
"""

from typing import Any

# Import des fonctions des plugins
try:
    from .export_docker_plugin import get_info as docker_info
    from .export_docker_plugin import run as docker_run
except ImportError:
    docker_run_fallback: type[Any] = type("docker_run_fallback", (), {})
    docker_info_fallback: type[Any] = type("docker_info_fallback", (), {})
    docker_run = docker_run_fallback
    docker_info = docker_info_fallback

try:
    from .hello_plugin import get_info as hello_info
    from .hello_plugin import run as hello_run
except ImportError:
    hello_run_fallback: type[Any] = type("hello_run_fallback", (), {})
    hello_info_fallback: type[Any] = type("hello_info_fallback", (), {})
    hello_run = hello_run_fallback
    hello_info = hello_info_fallback

try:
    from .plugins_manager import list_plugins, load_plugin, run_all_plugins
except ImportError:
    list_plugins_fallback: type[Any] = type("list_plugins_fallback", (), {})
    load_plugin_fallback: type[Any] = type("load_plugin_fallback", (), {})
    run_all_plugins_fallback: type[Any] = type("run_all_plugins_fallback", (), {})
    list_plugins = list_plugins_fallback
    load_plugin = load_plugin_fallback
    run_all_plugins = run_all_plugins_fallback

try:
    from .plugins_validator import validate_plugin
except ImportError:
    validate_plugin_fallback: type[Any] = type("validate_plugin_fallback", (), {})
    validate_plugin = validate_plugin_fallback

__all__ = [
    "docker_run",
    "docker_info",
    "hello_run",
    "hello_info",
    "list_plugins",
    "load_plugin",
    "run_all_plugins",
    "validate_plugin",
]
