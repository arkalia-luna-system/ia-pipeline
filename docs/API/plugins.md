# 🔌 Plugins et Templates - Documentation API

**Dernière mise à jour :** 20 Août 2025  
**Version :** v12.0.0  
**Statut :** ✅ ACTIF ET MAINTENU - SYSTÈME MODULAIRE  
**Module :** Plugins et Templates

## 🎯 Vue d'ensemble

Le système de plugins et templates d'Athalia permet d'étendre les fonctionnalités et de personnaliser la génération de contenu.

## 🔌 Système de Plugins

### **Architecture des Plugins**

Les plugins sont des modules Python qui étendent les fonctionnalités d'Athalia.

#### Structure d'un Plugin
```python
# plugins/hello_plugin.py
def hello_plugin():
    """Plugin de démonstration"""
    return {
        "name": "Hello Plugin",
        "version": "11.0.0",
        "description": "Plugin de démonstration",
        "result": "Hello World!"
    }
```

#### Chargement des Plugins
```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

# Créer une instance avec plugins activés
orchestrator = UnifiedOrchestrator("./mon-projet")
orchestrator.config["plugins"] = True

# Exécuter les plugins
plugin_results = orchestrator._run_plugins("./mon-projet")
```

### **Plugins Disponibles**

#### **Hello Plugin**
- **Fonction :** Démonstration basique
- **Résultat :** Message de bienvenue
- **Utilisation :** Test et validation

#### **Export Docker Plugin**
- **Fonction :** Génération de fichiers Docker
- **Résultat :** Dockerfile et docker-compose.yml
- **Utilisation :** Containerisation de projets

#### **Custom Plugins**
- **Fonction :** Plugins personnalisés
- **Résultat :** Fonctionnalités spécifiques
- **Utilisation :** Extensions métier

## 📋 Système de Templates

### **Architecture des Templates**

Les templates sont des modèles de fichiers qui peuvent être personnalisés et générés automatiquement.

#### Structure des Templates
```
templates/
├── api/
│   └── main.py.j2          # Template API Flask
├── memory/
│   └── memory.py.j2        # Template système mémoire
└── tts/
    └── tts.py.j2           # Template Text-to-Speech
```

#### Utilisation des Templates
```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

# Créer une instance avec templates activés
orchestrator = UnifiedOrchestrator("./mon-projet")
orchestrator.config["templates"] = True

# Générer les templates
template_results = orchestrator._run_templates("./mon-projet")
```

### **Templates Disponibles**

#### **API Template** (`api/main.py.j2`)
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```

#### **Memory Template** (`memory/memory.py.j2`)
```python
class Memory:
    def __init__(self):
        self.data = {}

    def store(self, key, value):
        self.data[key] = value

    def retrieve(self, key):
        return self.data.get(key)
```

#### **TTS Template** (`tts/tts.py.j2`)
```python
class TTS:
    def __init__(self):
        self.engine = None

    def speak(self, text):
        # Implémentation TTS
        pass
```

## 🔧 Configuration

### **Configuration des Plugins**
```python
config = {
    "plugins": {
        "enabled": True,
        "auto_load": True,
        "custom_path": "./plugins",
        "exclude": ["test_plugin.py"]
    }
}
```

### **Configuration des Templates**
```python
config = {
    "templates": {
        "enabled": True,
        "output_dir": "./generated_templates",
        "overwrite": False,
        "custom_vars": {
            "project_name": "MonProjet",
            "author": "Développeur"
        }
    }
}
```

## 🎯 Fonctionnalités Avancées

### **Plugins Dynamiques**
```python
# Chargement dynamique de plugins
def load_dynamic_plugin(plugin_path):
    """Charge un plugin dynamiquement"""
    import importlib.util
    spec = importlib.util.spec_from_file_location("plugin", plugin_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
```

### **Templates Conditionnels**
```python
# Template avec conditions
{% if project_type == "web" %}
from flask import Flask
{% elif project_type == "api" %}
from fastapi import FastAPI
{% endif %}
```

### **Variables d'Environnement**
```python
# Utilisation de variables d'environnement dans les templates
{{ env.PROJECT_NAME }}
{{ env.AUTHOR }}
{{ env.VERSION }}
```

## 📊 Métriques et Monitoring

### **Statistiques des Plugins**
```python
# Obtenir les statistiques des plugins
plugin_stats = orchestrator.get_plugin_statistics()

# Métriques disponibles
{
    "total_plugins": 5,
    "loaded_plugins": 3,
    "failed_plugins": 1,
    "execution_time": 2.5
}
```

### **Statistiques des Templates**
```python
# Obtenir les statistiques des templates
template_stats = orchestrator.get_template_statistics()

# Métriques disponibles
{
    "total_templates": 10,
    "generated_files": 8,
    "failed_generations": 1,
    "output_size": "2.3MB"
}
```

## 🔗 Navigation

- [Documentation API principale](INDEX.md)
- [Core Modules](core_modules.md)
- [Orchestrateur](orchestrator.md)
- [Robotics](robotics.md)

---

**Généré automatiquement** - 26/07/2025
