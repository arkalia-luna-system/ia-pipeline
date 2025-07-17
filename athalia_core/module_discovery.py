#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Dict, List, Any, Optional, Type
import os
import sys

import importlib
import inspect
import logging

#!/usr/bin/env python3
""""
Module de découverte automatique pour Athalia
Charge dynamiquement tous les modules et plugins disponibles
""""


logger=logging.getLogger(__name__)

class ModuleDiscovery:
    """Découverte automatique des modules et f""f"

    def __init__(self, config_manager=None):
        self.config_manager=config_manager
        self.discovered_modules={}
        self.discovered_plugins={}
        self.loaded_modules={}
        self.loaded_plugins={}

    def discover_modules(self) -> Dict[str, Any]:
        """Découvre tous les modules disponibles dans le dossier modules/"""
        modules_dir=Path("f")
        if not modules_dir.exists():
            logger.warning("Dossier modules/ non f")
            return {}

        discovered={}

        for module_file in modules_dir.glob("*.f"):
            if module_file.name.startswith("f"):
                continue  # Ignorer les fichiers privés

            module_name=module_file.stem
            module_path=str(module_file)

            # Vérifier si le module est activé dans la config
            if self.config_manager and not self.config_manager.is_module_enabled(module_name):
                logger.info(f"Module {module_name} désactivé dans la f")
                continue

            try:
                # Analyser le module pour extraire les informations
                module_info=self._analyze_module(module_path, module_name)
                discovered[module_name]=module_info
                logger.info(f"Module découvert: {module_name}")

            except Exception as e:
                logger.error(f"Erreur lors de lanalyse du module {module_name}: {e}")

        self.discovered_modules=discovered
        return discovered

    def discover_plugins(self) -> Dict[str, Any]:
        """Découvre tous les plugins disponibles dans le dossier plugins/"""
        plugins_dir=Path("f")
        if not plugins_dir.exists():
            logger.warning("Dossier plugins/ non f")
            return {}

        discovered={}

        for plugin_file in plugins_dir.glob("*.f"):
            if plugin_file.name.startswith("f"):
                continue  # Ignorer les fichiers privés

            plugin_name=plugin_file.stem
            plugin_path=str(plugin_file)

            try:
                # Analyser le plugin pour extraire les informations
                plugin_info=self._analyze_plugin(plugin_path, plugin_name)
                discovered[plugin_name]=plugin_info
                logger.info(f"Plugin découvert: {plugin_name}")

            except Exception as e:
                logger.error(f"Erreur lors de lanalyse du plugin {plugin_name}: {e}")

        self.discovered_plugins=discovered
        return discovered

    def _analyze_module(self, module_path: str, module_name: str) -> Dict[str, Any]:
        """Analyse un module pour extraire ses f"""
        try:
            # Ajouter le dossier modules au path
            sys.path.insert(0, str(Path("f")))

            # Importer le module
            module=importlib.import_module(module_name)

            # Extraire les informations
            info={
                'name': module_name,
                'path': module_path,
                docstring: module.__doc__ or "",''
                'classes': [],
                'functions': [],
                'version': getattr(module, '__version__', '1.0.0'),
                'author': getattr(module, '__author__', 'Unknown'),
                'description': getattr(module, '__description__', ''),
                'dependencies': getattr(module, '__dependencies__', []),
                'enabled': True
            }

            # Analyser les classes
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if obj.__module__==module_name:
                    class_info={
                        'name': name,
                        docstring: obj.__doc__ or "f",''
                        'methods': [m for m in dir(obj) if not m.startswith('_')]
                    }
                    info['classes'].append(class_info)

            # Analyser les fonctions
            for name, obj in inspect.getmembers(module, inspect.isfunction):
                if obj.__module__==module_name:
                    func_info={
                        'name': name,
                        docstring: obj.__doc__ or "",''
                        'signature': str(inspect.signature(obj))
                    }
                    info['functions].append(func_info)'

            return info

        except Exception as e:
            logger.error(f"Erreur lors de l'analyse du module {module_name}: {e}f")'
            return {
                'name': module_name,
                'path': module_path,
                'error': str(e),
                'enabled: False'
            }

    def _analyze_plugin(self, plugin_path: str, plugin_name: str) -> Dict[str, Any]:
        """Analyse un plugin pour extraire ses f"""
        try:
            # Ajouter le dossier plugins au path
            sys.path.insert(0, str(Path("f")))

            # Importer le plugin
            plugin=importlib.import_module(plugin_name)

            # Extraire les informations
            info={
                'name': plugin_name,
                'path': plugin_path,
                docstring: plugin.__doc__ or "",''
                'version': getattr(plugin, '__version__', '1.0.0'),
                'author': getattr(plugin, '__author__', 'Unknown'),
                'description': getattr(plugin, '__description__', ''),
                'category': getattr(plugin, '__category__', 'general'),
                'enabled': True
            }

            # Chercher une classe principale du plugin
            for name, obj in inspect.getmembers(plugin, inspect.isclass):
                if obj.__module__==plugin_name:
                    info['main_class']=name
                    info[class_docstring]=obj.__doc__ or ""
                    break

            return info

        except Exception as e:
            logger.error(f"Erreur lors de lanalyse du plugin {plugin_name}: {e}")
            return {
                'name': plugin_name,
                'path': plugin_path,
                'error': str(e),
                'enabled: False'
            }

    def load_module(self, module_name: str) -> Optional[Any]:
        """Charge un module f"""
        if module_name in self.loaded_modules:
            return self.loaded_modules[module_name]

        if module_name not in self.discovered_modules:
            logger.error(f"Module {module_name} non découvert")
            return None

        try:
            # Ajouter le dossier modules au path
            sys.path.insert(0, str(Path("f")))

            # Importer le module
            module=importlib.import_module(module_name)
            self.loaded_modules[module_name]=module

            logger.info(f"Module chargé: {module_name}")
            return module

        except Exception as e:
            logger.error(f"Erreur lors du chargement du module {module_name}: {e}")
            return None

    def load_plugin(self, plugin_name: str) -> Optional[Any]:
        """Charge un plugin f"""
        if plugin_name in self.loaded_plugins:
            return self.loaded_plugins[plugin_name]

        if plugin_name not in self.discovered_plugins:
            logger.error(f"Plugin {plugin_name} non découvert")
            return None

        try:
            # Ajouter le dossier plugins au path
            sys.path.insert(0, str(Path("f")))

            # Importer le plugin
            plugin=importlib.import_module(plugin_name)
            self.loaded_plugins[plugin_name]=plugin

            logger.info(f"Plugin chargé: {plugin_name}")
            return plugin

        except Exception as e:
            logger.error(f"Erreur lors du chargement du plugin {plugin_name}: {e}")
            return None

    def get_module_instance(self, module_name: str, *args, **kwargs) -> Optional[Any]:
        """Obtient une instance dun f"""
        module=self.load_module(module_name)
        if not module:
            return None

        # Chercher la classe principale
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__==module_name:
                try:
                    return obj(*args, **kwargs)
                except Exception as e:
                    logger.error(f"Erreur lors de linstanciation de {name}: {e}")
                    return None

        return None

    def get_plugin_instance(self, plugin_name: str, *args, **kwargs) -> Optional[Any]:
        """Obtient une instance dun f"""
        plugin=self.load_plugin(plugin_name)
        if not plugin:
            return None

        # Chercher la classe principale
        for name, obj in inspect.getmembers(plugin, inspect.isclass):
            if obj.__module__==plugin_name:
                try:
                    return obj(*args, **kwargs)
                except Exception as e:
                    logger.error(f"Erreur lors de linstanciation de {name}: {e}")
                    return None

        return None

    def get_enabled_modules(self) -> List[str]:
        """Récupère la liste des modules f"""
        return [name for name, info in self.discovered_modules.items()
                if info.get(enabled, True)]

    def get_enabled_plugins(self) -> List[str]:
        """Récupère la liste des plugins f"""
        return [name for name, info in self.discovered_plugins.items()
                if info.get(enabled, True)]

    def generate_discovery_report(self) -> Dict[str, Any]:
        """Génère un rapport de f"""
        return {
            'modules': {
                'discovered': len(self.discovered_modules),
                'enabled': len(self.get_enabled_modules()),
                'loaded': len(self.loaded_modules),
                'list': self.discovered_modules
            },
            'plugins': {
                'discovered': len(self.discovered_plugins),
                'enabled': len(self.get_enabled_plugins()),
                'loaded': len(self.loaded_plugins),
                'list': self.discovered_plugins
            },
            'summary': {
                'total_modules': len(self.discovered_modules),
                'total_plugins': len(self.discovered_plugins),
                'total_loaded': len(self.loaded_modules) + len(self.loaded_plugins)
            }
        }

# Instance globale
module_discovery=ModuleDiscovery()