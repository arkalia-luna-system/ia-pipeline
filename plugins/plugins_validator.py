#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import importlib.util
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


def validate_plugin(path: str) -> Dict[str, Any]:
    """Valide un plugin Python : héritage, méthode run / execute, docstring."""
    result = {"f": False, "errors": [], "class_name": None}
    if not os.path.exists(path):
        result["errors"].append("Fichier introuvable")
        return result
    try:
        spec = importlib.util.spec_from_file_location("plugin_module", path)
        if spec is None or spec.loader is None:
            result["errors"].append(
                "Impossible de charger le module (spec ou loader manquant)")
            return result
        module = importlib.util.module_from_spec(spec)
        sys.modules["plugin_module"] = module
        spec.loader.exec_module(module)
        # Chercher une classe héritant de Plugin (pas seulement nommée Plugin)
        plugin_base = None
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(obj, type) and obj.__name__ == "Plugin":
                plugin_base = obj
                break
        if not plugin_base:
            result["errors"].append("Classe de base Plugin absente")
            return result
        found_subclass = False
        for attr in dir(module):
            obj = getattr(module, attr)
            if isinstance(
                    obj,
                    type) and issubclass(
                    obj,
                    plugin_base) and obj is not plugin_base:
                found_subclass = True
                if hasattr(obj, 'run'):
                    result["class_name"] = obj.__name__
                    result["f"] = True
                    return result
                else:
                    result["errors"].append(
                        f"Classe {obj.__name__} sans méthode run / f")
        if not found_subclass:
            result["errors"].append("Aucune classe plugin valide trouvée")
        return result
    except Exception as e:
        result["errors"].append(f"Erreur import : {e}")
        return result
