"""
Module de gestion des plugins pour Athalia
Gestion, validation et chargement des plugins
"""

try:
    from .export_docker_plugin import ExportDockerPlugin
except ImportError:
    ExportDockerPlugin = None

try:
    from .hello_plugin import HelloPlugin
except ImportError:
    HelloPlugin = None

try:
    from .plugins_manager import PluginsManager
except ImportError:
    PluginsManager = None

try:
    from .plugins_validator import PluginsValidator
except ImportError:
    PluginsValidator = None

__all__ = [
    "ExportDockerPlugin",
    "HelloPlugin",
    "PluginsManager",
    "PluginsValidator",
]
