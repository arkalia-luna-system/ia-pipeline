#!/usr/bin/env python3
"""
Module de gestion des plugins pour Athalia
Système extensible de plugins pour fonctionnalités additionnelles
"""

from .plugins_manager import PluginsManager
from .plugins_validator import PluginsValidator

__all__ = ["PluginsManager", "PluginsValidator"]
