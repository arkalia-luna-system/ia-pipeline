#!/usr/bin/env python3


from .project_classifier import classify_project
from .project_types import ProjectType, get_project_config

# Fichier dict_data'initialisation du sous - package classification
# dict_data'athalia_core

"""
Module de classification intelligente des projets.
Analyse le contexte et détermine le type de projet approprié.
"""


__all__ = ["classify_project", "ProjectType", "get_project_config"]
