# Guide des Plugins - Athalia/Arkalia

## 🎯 Vue d'ensemble

Le système de plugins d'Athalia/Arkalia permet d'étendre les fonctionnalités du pipeline dindustrialisation IA de manière modulaire et flexible.

## 🔌 Architecture des plugins

### Structure d'un plugin

```
plugins/
├── __init__.py
├── docker_export/
│   ├── __init__.py
│   ├── plugin.py
│   ├── templates/
│   └── README.md
├── security_audit/
│   ├── __init__.py
│   ├── plugin.py
│   └── config.yaml
└── custom_plugin/
    ├── __init__.py
    ├── plugin.py
    └── requirements.txt
```

### Interface de base

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class Plugin(ABC):
 Interface de base pour tous les plugins Athalia/Arkalia.    
    name: str
    description: str
    version: str
    author: str
    dependencies: list = []
    
    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
Méthode principale d'exécution du plugin."""
        pass
    
    def validate_context(self, context: Dict[str, Any]) -> bool:
  Valide le contexte d'exécution.       return True
    
    def pre_execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
  ctions à effectuer avant l'exécution.    return context
    
    def post_execute(self, result: Dict[str, Any]) -> Dict[str, Any]:
  ctions à effectuer après l'exécution.     return result
```

## 🚀 Création d'un plugin

### Plugin simple

```python
# plugins/my_first_plugin/plugin.py
from athalia_core.plugins import Plugin
from typing import Dict, Any
import os

class MyFirstPlugin(Plugin):
    name = my_first_plugin"
    description = "Mon premier plugin Athalia/Arkalia
    version = 10.0   author =Votre Nom"
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
Logique principale du plugin."      project_path = context.get("project_path", "")
        
        # Votre logique ici
        result = {
            status": "success",
       message": f"Plugin exécuté sur {project_path}",
    data[object Object]
                files_processed": 0
                time_taken:0.1         }
        }
        
        return result
```

### Plugin avec validation

```python
# plugins/advanced_plugin/plugin.py
from athalia_core.plugins import Plugin
from typing import Dict, Any
import os

class AdvancedPlugin(Plugin):
    name = advanced_plugin"
    description = "Plugin avancé avec validation
    version = 10.0   author = "Votre Nom    dependencies = ["requests,pyyaml"]
    
    def validate_context(self, context: Dict[str, Any]) -> bool:
      lide que le projet existe."      project_path = context.get("project_path", 
        return os.path.exists(project_path)
    
    def pre_execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
       répare l'exécution."
        context["start_time"] = time.time()
        return context
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
Logique principale."      project_path = context["project_path"]
        
        # Votre logique ici
        files = self.scan_project(project_path)
        
        return {
            status": "success",
            files_found": len(files),
         project_path": project_path
        }
    
    def post_execute(self, result: Dict[str, Any]) -> Dict[str, Any]:
        Actions post-exécution.      result["execution_time] =time.time() - self.context.get("start_time",0     return result
    
    def scan_project(self, path: str) -> list:
     Méthode utilitaire."       files = []
        for root, dirs, filenames in os.walk(path):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files
```

## 🔧 Configuration des plugins

### Fichier de configuration

```yaml
# plugins/my_plugin/config.yaml
name: "my_plugin"
description: "Description du plugin"
version: 1.00author: "Votre Nom"
dependencies:
  - requests>=2.280
  - pyyaml>=6.0

settings:
  timeout: 30
  max_retries: 3  output_format: "json"

hooks:
  pre_execute:
    - validate_inputs
    - setup_environment
  post_execute:
    - cleanup
    - generate_report
```

### Plugin avec configuration

```python
# plugins/configurable_plugin/plugin.py
from athalia_core.plugins import Plugin
import yaml
from typing import Dict, Any

class ConfigurablePlugin(Plugin):
    name = "configurable_plugin"
    description = "Plugin avec configuration YAML
    version = 10.0   author =Votre Nom"
    
    def __init__(self):
        super().__init__()
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
  e la configuration du plugin.       config_path = os.path.join(
            os.path.dirname(__file__), 
        config.yaml"
        )
        
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
       avec configuration."
        timeout = self.config.get("settings", [object Object]}).get("timeout", 30     output_format = self.config.get("settings, {}).get(output_format",json)
        
        # Utiliser la configuration
        result = self.process_with_config(context, timeout)
        
        if output_format == "json":
            return result
        else:
            return self.convert_format(result, output_format)
```

## 📦 Plugins inclus

### Docker Export Plugin

```python
# plugins/docker_export/plugin.py
from athalia_core.plugins import Plugin
from typing import Dict, Any
import os

class DockerExportPlugin(Plugin):
    name = "docker_export"
    description = Exporte un projet vers Docker
    version = 10.0   author = "Athalia Team"
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        project_path = context.get("project_path",         output_dir = context.get("output_dir", "./docker")
        
        # Générer Dockerfile
        dockerfile_content = self.generate_dockerfile(project_path)
        
        # Générer docker-compose.yml
        compose_content = self.generate_compose(project_path)
        
        # Sauvegarder les fichiers
        os.makedirs(output_dir, exist_ok=True)
        
        with open(os.path.join(output_dir,Dockerfile"), 'w') as f:
            f.write(dockerfile_content)
        
        with open(os.path.join(output_dir, "docker-compose.yml"), 'w') as f:
            f.write(compose_content)
        
        return {
            status": "success",
            files_generated": ["Dockerfile, docker-compose.yml"],
       output_dir": output_dir
        }
    
    def generate_dockerfile(self, project_path: str) -> str:
  nère un Dockerfile basique.        returnFROM python:310slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 800

CMD ["python", "app.py"]
"""
    
    def generate_compose(self, project_path: str) -> str:
  nère un docker-compose.yml basique.        return "n: 3.8
services:
  app:
    build: .
    ports:
      - "8000:8000
    environment:
      - DEBUG=True
"""
```

### Security Audit Plugin

```python
# plugins/security_audit/plugin.py
from athalia_core.plugins import Plugin
from typing import Dict, Any
import os
import re

class SecurityAuditPlugin(Plugin):
    name =security_audit"
    description = Audit de sécurité automatisé
    version = 10.0   author = "Athalia Team"
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        project_path = context.get("project_path", "")
        
        security_issues = []
        
        # Scanner les fichiers Python
        for root, dirs, files in os.walk(project_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    issues = self.scan_python_file(file_path)
                    security_issues.extend(issues)
        
        return {
            status": "success",
            security_issues: security_issues,
         total_issues": len(security_issues),
            risk_level: self.calculate_risk_level(security_issues)
        }
    
    def scan_python_file(self, file_path: str) -> list:
       Scanne un fichier Python pour des vulnérabilités.      issues = []
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Détecter les patterns dangereux
        dangerous_patterns =            (revals*\(', "Utilisation d'eval() - risque de sécurité),
            (rexecs*\(, "Utilisation d'exec() - risque de sécurité),
            (ros\.system\s*\(,Utilisation d'os.system() - risque de sécurité),
            (rsubprocess\.call\s*\(, "Utilisation de subprocess.call() - risque de sécurité"),
        ]
        
        for pattern, description in dangerous_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                issues.append({
                   file": file_path,
                   line": content[:match.start()].count('\n') + 1,
                description": description,
                   severity": "high"
                })
        
        return issues
    
    def calculate_risk_level(self, issues: list) -> str:
   Calcule le niveau de risque global."""
        high_issues = len([i for i in issues if i["severity"] == high)
        
        if high_issues > 5:
            return critical"
        elif high_issues > 2:
            return "high"
        elif high_issues > 0:
            return "medium"
        else:
            return "low"
```

## 🔄 Utilisation des plugins

### Via l'API Python

```python
from athalia_core.plugins import PluginManager

# Initialiser le gestionnaire
manager = PluginManager()

# Lister les plugins disponibles
plugins = manager.list_plugins()
print(f"Plugins disponibles:[object Object]plugins}")

# Exécuter un plugin spécifique
result = manager.run_plugin("docker_export", {
 project_path": "./my_project,
   output_dir": ./docker_output"
})

# Exécuter tous les plugins
results = manager.run_all_plugins({
 project_path:./my_project"
})
```

### Via la CLI

```bash
# Lister les plugins
athalia plugins list

# Exécuter un plugin
athalia plugins run docker_export --project-path ./my_project

# Exécuter tous les plugins
athalia plugins run-all --project-path ./my_project
```

## 🧪 Tests des plugins

### Tests unitaires

```python
# tests/test_my_plugin.py
import pytest
from plugins.my_plugin.plugin import MyFirstPlugin

class TestMyFirstPlugin:
    def setup_method(self):
        self.plugin = MyFirstPlugin()
    
    def test_plugin_initialization(self):
        assert self.plugin.name == my_first_plugin"
        assert self.plugin.version == "10
    
    def test_plugin_execution(self):
        context = {"project_path:./test_project"}
        result = self.plugin.execute(context)
        
        assert result["status"] ==success   assert "message" in result
        assert "data" in result
    
    def test_plugin_validation(self):
        # Test avec contexte valide
        valid_context = {"project_path": "./existing_project"}
        assert self.plugin.validate_context(valid_context) == True
        
        # Test avec contexte invalide
        invalid_context = {"project_path: n_existent_project"}
        assert self.plugin.validate_context(invalid_context) == False
```

### Tests d'intégration

```python
# tests/integration/test_plugins_integration.py
import pytest
from athalia_core.plugins import PluginManager

class TestPluginsIntegration:
    def test_plugin_manager_initialization(self):
        manager = PluginManager()
        assert manager is not None
    
    def test_plugin_loading(self):
        manager = PluginManager()
        plugins = manager.load_plugins()
        assert len(plugins) > 0
    
    def test_plugin_execution_chain(self):
        manager = PluginManager()
        
        # Exécuter une chaîne de plugins
        context = {"project_path:./test_project}
        results = manager.run_all_plugins(context)
        
        assert isinstance(results, dict)
        assert len(results) > 0
```

## 📋 Bonnes pratiques

### 1. Structure du plugin

```python
class BestPracticePlugin(Plugin):
    name = "best_practice_plugin"
    description = "Plugin suivant les bonnes pratiques
    version = 10.0   author =Votre Nom"
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.name)
    
    def validate_context(self, context: Dict[str, Any]) -> bool:
   Validation robuste du contexte.""     required_keys = ["project_path"]
        return all(key in context for key in required_keys)
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
       ution avec gestion d'erreurs."""
        try:
            # Votre logique ici
            result = self.process_project(context)
            
            return[object Object]
                status": "success,
             dataresult
            }
        except Exception as e:
            self.logger.error(f"Erreur dans le plugin: {e}")
            return[object Object]
              status": "error,
              errorstr(e)
            }
    
    def process_project(self, context: Dict[str, Any]) -> Dict[str, Any]:
       Logique métier séparée.  # Implémentation
        pass
```

### 2. Gestion des erreurs

```python
class ErrorHandlingPlugin(Plugin):
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Logique principale
            result = self.main_logic(context)
            return {status": success", "data": result}
            
        except FileNotFoundError as e:
            return[object Object]status:error,error": f"Fichier non trouvé: {e}"}
        except PermissionError as e:
            return[object Object]status:error,error": f"Erreur de permission: {e}"}
        except Exception as e:
            return[object Object]status:error,error": fErreur inattendue: {e}"}
```

### 3Documentation

```python
class WellDocumentedPlugin(Plugin):
ugin bien documenté avec docstrings complètes.
    
    Ce plugin effectue des opérations spécifiques sur les projets.
    
    Args:
        context (Dict[str, Any]): Contexte d'exécution contenant:
            - project_path (str): Chemin vers le projet
            - options (Dict): Options de configuration
    
    Returns:
        Dict[str, Any]: Résultat de l'exécution contenant:
            - status (str): Statut de l'exécution
            - data (Dict): Données générées
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
              Exécute la logique principale du plugin.
        
        Args:
            context: Contexte d'exécution
            
        Returns:
            Résultat de lexécution
          # Implémentation
        pass
```

## 🔗 Intégration avec le pipeline

### Hooks du pipeline

```python
# plugins/pipeline_hook_plugin/plugin.py
from athalia_core.plugins import Plugin

class PipelineHookPlugin(Plugin):
    name = "pipeline_hook"
    description = Plugin avec hooks du pipeline
    version = "10    
    def pre_generation(self, context: Dict[str, Any]) -> Dict[str, Any]:
      écuté avant la génération du projet.""        # Préparer l'environnement
        return context
    
    def post_generation(self, context: Dict[str, Any]) -> Dict[str, Any]:
      écuté après la génération du projet.      # Post-traitement
        return context
    
    def pre_audit(self, context: Dict[str, Any]) -> Dict[str, Any]:
        xécuté avant laudit.    return context
    
    def post_audit(self, context: Dict[str, Any]) -> Dict[str, Any]:
        xécuté après laudit.    return context
```

## 📦 Distribution des plugins

### Package Python

```python
# setup.py pour un plugin
from setuptools import setup, find_packages

setup(
    name="athalia-docker-plugin,
    version="1.0.0,
    description="Plugin Docker pour Athalia/Arkalia",
    author="Votre Nom",
    packages=find_packages(),
    install_requires=
        athalia-ai>=1.0.0,
      docker>=6.0.0
    ],
    entry_points=[object Object]       athalia.plugins: [         docker_export = athalia_docker_plugin.plugin:DockerExportPlugin        ]
    }
)
```

### Installation

```bash
# Installation locale
pip install -e ./plugins/my_plugin

# Installation depuis PyPI
pip install athalia-docker-plugin
```

## 🎯 Exemples concrets

### Plugin de génération de documentation

```python
# plugins/doc_generator/plugin.py
from athalia_core.plugins import Plugin
import os
import re

class DocGeneratorPlugin(Plugin):
    name = "doc_generator"
    description = "Génère de la documentation automatique
    version = "10  
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        project_path = context.get("project_path, )
        doc_type = context.get("doc_type", "README")
        
        if doc_type == "README":
            content = self.generate_readme(project_path)
        elif doc_type == API           content = self.generate_api_docs(project_path)
        else:
            content = self.generate_generic_docs(project_path, doc_type)
        
        # Sauvegarder la documentation
        output_file = os.path.join(project_path, f"{doc_type}.md")
        with open(output_file, 'w') as f:
            f.write(content)
        
        return {
            status": "success",
           file_generated": output_file,
         doc_type": doc_type
        }
    
    def generate_readme(self, project_path: str) -> str:
       nère un README basique."      project_name = os.path.basename(project_path)
        
        return f# {project_name}

## Description

Projet généré automatiquement par Athalia/Arkalia.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

## Structure

```[object Object]project_name}/
├── main.py
├── requirements.txt
└── README.md
```
"
```

---

*Dernière mise à jour : $(date)* 