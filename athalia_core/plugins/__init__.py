"""
Module de gestion des plugins pour Athalia
Gestion, validation et chargement des plugins
"""

from typing import Any

# Import des fonctions des plugins
try:
    from .export_docker_plugin import get_info as docker_info
    from .export_docker_plugin import run as docker_run

    ExportDockerPlugin: type[Any] = type(
        "ExportDockerPlugin",
        (),
        {"run": staticmethod(docker_run), "get_info": staticmethod(docker_info)},
    )
except ImportError:
    ExportDockerPlugin: type[Any] = type("ExportDockerPlugin", (), {})

try:
    from .hello_plugin import get_info as hello_info
    from .hello_plugin import run as hello_run

    HelloPlugin: type[Any] = type(
        "HelloPlugin",
        (),
        {"run": staticmethod(hello_run), "get_info": staticmethod(hello_info)},
    )
except ImportError:
    HelloPlugin: type[Any] = type("HelloPlugin", (), {})

try:
    from .plugins_manager import list_plugins, load_plugin, run_all_plugins

    PluginsManager: type[Any] = type(
        "PluginsManager",
        (),
        {
            "list_plugins": staticmethod(list_plugins),
            "load_plugin": staticmethod(load_plugin),
            "run_all_plugins": staticmethod(run_all_plugins),
        },
    )
except ImportError:
    PluginsManager: type[Any] = type("PluginsManager", (), {})

try:
    from .plugins_validator import validate_plugin

    PluginsValidator: type[Any] = type(
        "PluginsValidator", (), {"validate_plugin": staticmethod(validate_plugin)}
    )
except ImportError:
    PluginsValidator: type[Any] = type("PluginsValidator", (), {})

__all__ = [
    "ExportDockerPlugin",
    "HelloPlugin",
    "PluginsManager",
    "PluginsValidator",
]
