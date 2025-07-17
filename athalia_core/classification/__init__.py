# Fichier d'initialisation du sous-package classification d'athalia_core

"""
Module de classification intelligente des projets.
Analyse le contexte et détermine le type de projet approprié.
"""

from .project_classifier import classify_project
from .project_types import ProjectType, get_project_config

__all__ = ['classify_project', 'ProjectType', 'get_project_config'] 