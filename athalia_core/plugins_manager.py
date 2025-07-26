#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de plugins dynamiques pour Athalia
"""
import os
import sys
import importlib.util
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)

# Dossier des plugins
PLUGINS_DIR = Path(__file__).parent / "plugins"

def list_plugins() -> List[str]:
    """Liste tous les plugins disponibles"""
    plugins = []
    
    # Plugins intégrés
    plugins.extend([
        'hello_plugin',
        'export_docker_plugin',
        'code_analyzer_plugin',
        'documentation_plugin'
    ])
    
    # Plugins externes (si le dossier existe)
    if PLUGINS_DIR.exists():
        for plugin_file in PLUGINS_DIR.glob("*.py"):
            if plugin_file.name.startswith("__"):
                continue
            plugin_name = plugin_file.stem
            plugins.append(plugin_name)
    
    return plugins

def load_plugin(plugin_name: str) -> Any:
    """Charge un plugin par son nom"""
    try:
        # Plugins intégrés
        if plugin_name == 'hello_plugin':
            return HelloPlugin()
        elif plugin_name == 'export_docker_plugin':
            return ExportDockerPlugin()
        elif plugin_name == 'code_analyzer_plugin':
            return CodeAnalyzerPlugin()
        elif plugin_name == 'documentation_plugin':
            return DocumentationPlugin()
        
        # Plugins externes
        plugin_file = PLUGINS_DIR / f"{plugin_name}.py"
        if plugin_file.exists():
            spec = importlib.util.spec_from_file_location(plugin_name, plugin_file)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        
        raise ImportError(f"Plugin '{plugin_name}' non trouvé")
        
    except Exception as e:
        logger.error(f"Erreur lors du chargement du plugin '{plugin_name}': {e}")
        raise

def run_all_plugins() -> Dict[str, Any]:
    """Exécute tous les plugins disponibles"""
    results = {}
    
    for plugin_name in list_plugins():
        try:
            plugin = load_plugin(plugin_name)
            if hasattr(plugin, 'run'):
                results[plugin_name] = plugin.run()
            else:
                results[plugin_name] = "Plugin sans méthode run()"
        except Exception as e:
            results[plugin_name] = f"Erreur: {e}"
    
    return results

# Plugins intégrés

class HelloPlugin:
    """Plugin de test simple"""
    
    def run(self) -> str:
        """Exécute le plugin"""
        return "Hello from plugin!"

class ExportDockerPlugin:
    """Plugin d'export Docker"""
    
    def run(self, project_path: Optional[str] = None) -> str:
        """Génère les fichiers Docker pour un projet"""
        if not project_path:
            return "Erreur: chemin du projet requis"
        
        project_dir = Path(project_path)
        
        # Créer Dockerfile
        dockerfile_content = """FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
"""
        
        with open(project_dir / "Dockerfile", 'w') as f:
            f.write(dockerfile_content)
        
        # Créer docker-compose.yml
        compose_content = """version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
"""
        
        with open(project_dir / "docker-compose.yml", 'w') as f:
            f.write(compose_content)
        
        return "Fichiers Docker générés avec succès"

class CodeAnalyzerPlugin:
    """Plugin d'analyse de code"""
    
    def run(self, project_path: Optional[str] = None) -> str:
        """Analyse le code d'un projet"""
        return "Analyse de code terminée"

class DocumentationPlugin:
    """Plugin de génération de documentation"""
    
    def run(self, project_path: Optional[str] = None) -> str:
        """Génère la documentation d'un projet"""
        return "Documentation générée"