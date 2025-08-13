#!/usr/bin/env python3
"""
Module de templates Athalia
===========================

Ce module fournit des templates de base et artistiques pour la génération de projets.
Permet la création de structures de projets cohérentes et personnalisées.
"""

from .artistic_templates import get_artistic_templates
from .base_templates import get_base_templates

__all__ = [
    "get_base_templates",
    "get_artistic_templates",
]

__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Templates de projets et artistiques"
