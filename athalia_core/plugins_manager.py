#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import importlib.util
import logging

logger = logging.getLogger(__name__)

"""
Gestionnaire de plugins dynamiques.
"""

PLUGINS_DIR = os.path.join(os.path.dirname(__file__), '..', 'plugins')

def list_plugins():
    """Liste tous les plugins disponibles."""
    plugins = []
    for fname in os.listdir(PLUGINS_DIR):
        if fname.endswith('.py') and fname != '__init__.py':
            plugins.append(fname[:-3])
    return plugins

def load_plugin(name):
    """Charge dynamiquement un plugin par nom."""
    path = os.path.join(PLUGINS_DIR, f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Impossible de charger le plugin {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_all_plugins():
    """Exécute la fonction run() de tous les plugins et retourne les résultats."""
    results = {}
    for name in list_plugins():
        try:
            mod = load_plugin(name)
            if hasattr(mod, 'run'):
                results[name] = mod.run()
            else:
                results[name] = 'Pas de fonction run()'
        except Exception as e:
            results[name] = f"Erreur: {e}"
    return results