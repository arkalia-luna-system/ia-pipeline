# 🚀 Guide des Plugins - Athalia/Arkalia

**Dernière mise à jour :** 20 Août 2025  
**Version :** v12.0.0  
**Statut :** ✅ ACTIF ET MAINTENU - SYSTÈME MODULAIRE

> **Note de mise à jour (20/08/2025) :**
>
> - Le système de plugins est déjà en place, testé, documenté, et utilisé en production.
> - Les exemples et guides sont à jour avec l'état réel du code.

## 🎯 Vue d'ensemble

Le système de plugins d'Athalia/Arkalia permet d'étendre les fonctionnalités du pipeline d'industrialisation IA de manière modulaire et flexible.

## 🔌 Architecture des plugins

### Structure d'un plugin

```
athalia_core/plugins/
├── __init__.py
├── plugins_manager.py
├── plugins_validator.py
├── marketplace_interface.py
├── hello_plugin.py
└── export_docker_plugin.py
```

### Interface de base

Les plugins utilisent une interface simple basée sur des fonctions :

```python
def run():
    """Fonction principale d'exécution du plugin"""
    return {"status": "success", "message": "Plugin exécuté"}

def get_info():
    """Informations sur le plugin"""
    return {
        "name": "Nom du Plugin",
        "version": "1.0.0",
        "description": "Description du plugin"
    }
```

## 🚀 Création d'un plugin

### Plugin simple

```python
# athalia_core/plugins/my_first_plugin.py
def run():
    """Fonction principale du plugin"""
    return {
        "status": "success",
        "message": "Mon premier plugin Athalia/Arkalia exécuté",
        "data": {
            "files_processed": 0,
            "time_taken": 0.1
        }
    }

def get_info():
    """Informations sur le plugin"""
    return {
        "name": "my_first_plugin",
        "description": "Mon premier plugin Athalia/Arkalia",
        "version": "1.0.0",
        "author": "Votre Nom"
    }
```

### Plugin avec paramètres

```python
# athalia_core/plugins/advanced_plugin.py
import os
import time

def run(project_path="", **kwargs):
    """Plugin avancé avec paramètres"""
    start_time = time.time()
    
    if not project_path or not os.path.exists(project_path):
        return {
            "status": "error",
            "message": "Chemin de projet invalide"
        }
    
    # Votre logique ici
    files = scan_project(project_path)
    
    execution_time = time.time() - start_time
    
    return {
        "status": "success",
        "files_found": len(files),
        "project_path": project_path,
        "execution_time": execution_time
    }

def get_info():
    """Informations sur le plugin"""
    return {
        "name": "advanced_plugin",
        "description": "Plugin avancé avec validation",
        "version": "1.0.0",
        "author": "Votre Nom"
    }

def scan_project(path: str) -> list:
    """Méthode utilitaire pour scanner un projet"""
    files = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files
```

## 🔧 Configuration des plugins

### Fichier de configuration

```yaml
# config/plugins/my_plugin.yaml
name: "my_plugin"
description: "Description du plugin"
version: "1.0.0"
author: "Votre Nom"
dependencies:
  - requests>=2.28.0
  - pyyaml>=6.0

settings:
  timeout: 30
  max_retries: 3
  output_format: "json"
```

### Plugin avec configuration

```python
# athalia_core/plugins/configurable_plugin.py
import yaml
import os
from typing import Dict, Any

def run(config_path="", **kwargs):
    """Plugin avec configuration YAML"""
    if not config_path:
        config_path = os.path.join(
            os.path.dirname(__file__),
            "config.yaml"
        )
    
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        return {
            "status": "error",
            "message": "Fichier de configuration non trouvé"
        }
    
    timeout = config.get("settings", {}).get("timeout", 30)
    output_format = config.get("settings", {}).get("output_format", "json")
    
    # Utiliser la configuration
    result = process_with_config(kwargs, timeout)
    
    if output_format == "json":
        return result
    else:
        return convert_format(result, output_format)

def get_info():
    """Informations sur le plugin"""
    return {
        "name": "configurable_plugin",
        "description": "Plugin avec configuration YAML",
        "version": "1.0.0",
        "author": "Votre Nom"
    }
```

## 📦 Plugins inclus

### Hello Plugin

```python
# athalia_core/plugins/hello_plugin.py
def run():
    """Fonction principale du plugin"""
    return {"message": "Hello from plugin!", "status": "success"}

def get_info():
    """Informations sur le plugin"""
    return {
        "name": "Hello Plugin",
        "version": "1.0.0",
        "description": "Plugin de démonstration",
    }
```

### Docker Export Plugin

```python
# athalia_core/plugins/export_docker_plugin.py
import os

def run(project_path="", output_dir="./docker", **kwargs):
    """Exporte un projet vers Docker"""
    if not project_path:
        project_path = "."
    
    # Générer Dockerfile
    dockerfile_content = generate_dockerfile(project_path)
    
    # Générer docker-compose.yml
    compose_content = generate_compose(project_path)
    
    # Sauvegarder les fichiers
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "Dockerfile"), 'w') as f:
        f.write(dockerfile_content)
    
    with open(os.path.join(output_dir, "docker-compose.yml"), 'w') as f:
        f.write(compose_content)
    
    return {
        "status": "success",
        "files_generated": ["Dockerfile", "docker-compose.yml"],
        "output_dir": output_dir
    }

def get_info():
    """Informations sur le plugin"""
    return {
        "name": "Docker Export Plugin",
        "version": "1.0.0",
        "description": "Exporte un projet vers Docker",
        "author": "Athalia Team"
    }

def generate_dockerfile(project_path: str) -> str:
    """Génère un Dockerfile basique"""
    return """FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "app.py"]
"""

def generate_compose(project_path: str) -> str:
    """Génère un docker-compose.yml basique"""
    return """version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=True
"""
```

## 🚀 Utilisation des plugins

### Chargement et exécution

```python
from athalia_core.plugins import load_plugin, run_all_plugins, list_plugins

# Lister tous les plugins disponibles
plugins = list_plugins()
print(f"Plugins disponibles: {plugins}")

# Charger un plugin spécifique
plugin = load_plugin("hello_plugin")
if plugin:
    result = plugin.run()
    print(f"Résultat: {result}")

# Exécuter tous les plugins
results = run_all_plugins()
for plugin_name, result in results.items():
    print(f"{plugin_name}: {result}")
```

### Validation des plugins

```python
from athalia_core.plugins import validate_plugin

# Valider un plugin
is_valid = validate_plugin("hello_plugin")
if is_valid:
    print("Plugin valide")
else:
    print("Plugin invalide")
```

## 🔧 Gestion des plugins

### Plugins Manager

Le `plugins_manager.py` fournit les fonctions suivantes :

- `list_plugins()` : Liste tous les plugins disponibles
- `load_plugin(name)` : Charge un plugin par son nom
- `run_all_plugins()` : Exécute tous les plugins

### Plugins Validator

Le `plugins_validator.py` valide la structure et la conformité des plugins.

### Marketplace Interface

Le `marketplace_interface.py` gère l'interface avec le marketplace des plugins.

## 📋 Bonnes pratiques

1. **Simplicité** : Gardez vos plugins simples et focalisés
2. **Documentation** : Documentez clairement le but et l'utilisation
3. **Gestion d'erreurs** : Gérez gracieusement les erreurs
4. **Tests** : Testez vos plugins avant de les déployer
5. **Versioning** : Utilisez un versioning sémantique

## 🚨 Dépannage

### Erreurs courantes

**Plugin non trouvé :**
```bash
# Vérifiez que le fichier existe
ls athalia_core/plugins/my_plugin.py

# Vérifiez l'import dans __init__.py
cat athalia_core/plugins/__init__.py
```

**Erreur d'exécution :**
```bash
# Testez le plugin directement
python -c "from athalia_core.plugins import my_plugin; print(my_plugin.run())"
```

**Problème de dépendances :**
```bash
# Installez les dépendances manquantes
pip install -r requirements.txt
```

## 📚 Ressources

- **Documentation des plugins** : `docs/DEVELOPER/GUIDES/PLUGINS_GUIDE.md`
- **Exemples de plugins** : `athalia_core/plugins/`
- **Tests des plugins** : `tests/unit/plugins/`
- **Configuration** : `config/plugins/`

## 🎯 Prochaines étapes

1. **Créer votre premier plugin** en suivant les exemples
2. **Tester votre plugin** avec les outils de validation
3. **Intégrer votre plugin** dans le workflow Athalia
4. **Partager votre plugin** avec la communauté

---

**💡 Conseil :** Commencez par des plugins simples et ajoutez progressivement de la complexité !