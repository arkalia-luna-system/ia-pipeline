#!/usr/bin/env python3
"""
Module de classification intelligente des projets Athalia
========================================================

Ce module analyse le contexte et détermine le type de projet approprié.
Fournit une classification automatique et intelligente des projets.
"""

from .project_classifier import classify_project
from .project_types import ProjectType, get_project_config

__all__ = ["classify_project", "ProjectType", "get_project_config"]

__version__ = "2.0.0"
__author__ = "Athalia Team"
__description__ = "Classification intelligente des projets"
