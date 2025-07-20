# Documentation API - Athalia/Arkalia

## 📚 Vue d'ensemble

Cette documentation décrit l'API complète d'Athalia/Arkalia, le pipeline dindustrialisation IA.

## 🚀 Installation et import

```python
# Installation
pip install athalia-ai

# Import principal
from athalia_core import *

# Imports spécifiques
from athalia_core.ai_robust import RobustAI
from athalia_core.generation import ProjectGenerator
from athalia_core.audit import AuditIntelligent
from athalia_core.analytics import Analytics
from athalia_core.plugins import PluginManager
```

## 🤖 RobustAI - IA Robuste

### Classe RobustAI

Gestionnaire d'IA robuste avec fallback intelligent et classification de complexité.

#### Constructeur

```python
RobustAI(
    models: Optional[List[Dict]] = None,
    fallback_chain: Optional[List[str]] = None,
    timeout: int = 30,
    max_retries: int = 3
    debug: bool = False
)
```

**Paramètres :**
- `models` : Liste des modèles IA disponibles
- `fallback_chain` : Chaîne de fallback des modèles
- `timeout` : Timeout en secondes pour les appels API
- `max_retries` : Nombre maximum de tentatives
- `debug` : Mode debug pour les logs détaillés

#### Méthodes principales

##### `detect_available_models() -> List[str]`

Détecte automatiquement les modèles IA disponibles.

```python
ai = RobustAI()
available_models = ai.detect_available_models()
# Retourne: [mistral, laude']
```

##### `build_fallback_chain() -> List[str]`

Construit la chaîne de fallback optimale.

```python
fallback_chain = ai.build_fallback_chain()
# Retourne: [mistral, laude']
```

##### `classify_project_complexity(description: str) -> str`

Classifie la complexité d'un projet.

```python
complexity = ai.classify_project_complexity(
  Application web moderne avec authentification et base de données"
)
# Retourne: 'medium'
```

**Types de complexité :**
- `simple` : Projet basique, 1-2 fichiers
- `medium` : Projet standard, plusieurs modules
- `complex` : Projet avancé, architecture distribuée

##### `get_dynamic_prompt(context: str, complexity: str = None) -> str`

Génère un prompt dynamique adapté au contexte et à la complexité.

```python
prompt = ai.get_dynamic_prompt("blueprint", complexity="medium")
```

##### `generate_blueprint(project_description: str, complexity: str = None) -> Dict`

Génère un blueprint de projet avec fallback automatique.

```python
result = ai.generate_blueprint(
    project_description="API REST avec FastAPI",
    complexity=medium"
)
```

**Retour :**
```python[object Object]status": "success,
 model_used": "mistral",
  fallback_used": False,
 blueprint": {
       structure": {...},
      files": {...},
     dependencies": [...],
      config": {...}
    }
}
```

##### `review_code(code: str, context: str = None) -> Dict`

Analyse et améliore du code existant.

```python
review = ai.review_code(
    code="def hello(): print('world)",
    context="Fonction de test"
)
```

##### `generate_documentation(project_path: str, doc_type: str =README") -> Dict`

Génère de la documentation pour un projet.

```python
docs = ai.generate_documentation(
    project_path="./my_project",
    doc_type=README"
)
```

## 🚀 ProjectGenerator - Génération de projets

### Classe ProjectGenerator

Générateur de projets IA avec gestion intelligente des fichiers existants.

#### Constructeur

```python
ProjectGenerator(
    ai_robust: Optional[RobustAI] = None,
    templates_dir: str = "templates",
    backup_enabled: bool = True
)
```

#### Méthodes principales

##### `generate_blueprint(description: str, output_dir: str, options: Dict = None) -> Dict`

Génère un projet complet à partir d'une description.

```python
generator = ProjectGenerator()

result = generator.generate_blueprint(
    description="Application web moderne avec React et Node.js",
    output_dir="./generated_project",
    options={
    framework": react,
        backend":nodejs",
       database": mongodb,
     auth": "jwt",
     tests: True,
    docs: True,
        docker": True
    }
)
```

**Options disponibles :**
- `framework` : Framework frontend (react, vue, angular)
- `backend` : Backend (nodejs, python, java, go)
- `database` : Base de données (mongodb, postgresql, mysql)
- `auth` : Authentification (jwt, oauth, basic)
- `tests` : Générer les tests (bool)
- `docs` : Générer la documentation (bool)
- `docker` : Générer Docker (bool)

##### `scan_existing_project(path: str) -> Dict`

Analyse un projet existant pour comprendre sa structure.

```python
project_info = generator.scan_existing_project("./existing_project")
```

##### `merge_or_suffix_file(content: str, filepath: str, strategy: str = merge") -> str`

Gère intelligemment les conflits de fichiers.

```python
final_content = generator.merge_or_suffix_file(
    content="Nouveau contenu",
    filepath="./existing_file.py",
    strategy="merge"  # ousuffix", "backup"
)
```

##### `backup_file(filepath: str) -> str`

Sauvegarde un fichier existant.

```python
backup_path = generator.backup_file("./important_file.py")
```

## 🔍 AuditIntelligent - Audit intelligent

### Classe AuditIntelligent

Auditeur intelligent de projets avec analyse multi-dimensionnelle.

#### Constructeur

```python
AuditIntelligent(
    ai_robust: Optional[RobustAI] = None,
    severity_levels: Dict = None
)
```

#### Méthodes principales

##### `audit_project(project_path: str) -> Dict`

Audit complet d'un projet.

```python
auditor = AuditIntelligent()

report = auditor.audit_project("./my_project)```

**Retour :**
```python[object Object]status": "success",
   overall_score": 85
  categories": {
       structure": {...},
     code_quality": {...},
      security": {...},
    performance": {...}
    },
    recommendations": [...],
    critical_issues": [...]
}
```

##### `audit_project_structure(project_path: str) -> Dict`

Audit de la structure du projet.

```python
structure_report = auditor.audit_project_structure("./my_project)
```

##### `audit_code_quality(project_path: str) -> Dict`

Audit de la qualité du code.

```python
quality_report = auditor.audit_code_quality("./my_project)
```

##### `audit_security(project_path: str) -> Dict`

Audit de sécurité.

```python
security_report = auditor.audit_security("./my_project)
```

##### `audit_performance(project_path: str) -> Dict`

Audit de performance.

```python
performance_report = auditor.audit_performance("./my_project")
```

##### `generate_audit_report(audit_results: Dict, output_file: str = None) -> str`

Génère un rapport d'audit formaté.

```python
report_path = auditor.generate_audit_report(
    audit_results,
    output_file=./audit_report.md"
)
```

## 📊 Analytics - Analytics et métriques

### Classe Analytics

Générateur d'analytics et métriques pour les projets.

#### Constructeur

```python
Analytics(
    output_dir: str = ./analytics,
    format: str = html
)```

#### Méthodes principales

##### `analyze_project(project_path: str) -> Dict`

Analyse complète d'un projet.

```python
analytics = Analytics()

data = analytics.analyze_project("./my_project")
```

##### `generate_heatmap_data(projects: List[str]) -> Dict`

Génère des données pour heatmap de complexité.

```python
heatmap_data = analytics.generate_heatmap_data([
   ./project1,   ./project2,
  ./project3`

##### `generate_technical_debt_analysis(project_path: str) -> Dict`

Analyse de la dette technique.

```python
debt_analysis = analytics.generate_technical_debt_analysis("./my_project")
```

##### `generate_html_report(data: Dict, output_file: str) -> str`

Génère un rapport HTML interactif.

```python
report_path = analytics.generate_html_report(
    data,
    output_file="./analytics_report.html"
)
```

##### `save_analytics(data: Dict, filename: str = None) -> str`

Sauvegarde les analytics au format JSON.

```python
file_path = analytics.save_analytics(data, project_analytics.json")
```

## 🔌 PluginManager - Système de plugins

### Classe PluginManager

Gestionnaire de plugins pour étendre les fonctionnalités.

#### Constructeur

```python
PluginManager(
    plugins_dir: str = "plugins",
    auto_load: bool = True
)
```

#### Méthodes principales

##### `load_plugins() -> List[Plugin]`

Charge tous les plugins disponibles.

```python
manager = PluginManager()
plugins = manager.load_plugins()
```

##### `run_plugin(plugin_name: str, context: Dict = None) -> Dict`

Exécute un plugin spécifique.

```python
result = manager.run_plugin("docker_export", {
 project_path": "./my_project,
   output_dir": "./docker"
})
```

##### `run_all_plugins(context: Dict = None) -> Dict`

Exécute tous les plugins disponibles.

```python
results = manager.run_all_plugins({
 project_path:./my_project"
})
```

##### `list_plugins() -> List[str]`

Liste tous les plugins disponibles.

```python
plugin_names = manager.list_plugins()
```

## 🛠️ Utilitaires

### Fonctions utilitaires

```python
from athalia_core.utils import *

# Validation de chemin
is_valid_path(./my_project)  # bool

# Nettoyage de cache
clean_cache(./cache")  # None

# Génération d'ID unique
unique_id = generate_unique_id()  # str

# Formatage de taille
formatted_size = format_size(1024  # "1 KB"
```

## 📝 Exemples d'utilisation

### Exemple complet : Génération d'un projet

```python
from athalia_core import RobustAI, ProjectGenerator, AuditIntelligent

#1. Initialiser l'IA robuste
ai = RobustAI()

# 2. Générer le projet
generator = ProjectGenerator(ai_robust=ai)
result = generator.generate_blueprint(
    description="API REST moderne avec authentification",
    output_dir="./api_project",
    options=[object Object]        backend":python",
        framework": fastapi",
       database": "postgresql,
     auth": "jwt",
     tests: True,
      docs: true
    }
)

# 3. Auditer le projet généré
auditor = AuditIntelligent(ai_robust=ai)
audit_report = auditor.audit_project(./api_project)print(f"Projet généré avec succès: {result[status']})
print(f"Score d'audit: {audit_report[overall_score]}/100")
```

### Exemple : Analytics de plusieurs projets

```python
from athalia_core import Analytics

analytics = Analytics()

# Analyser plusieurs projets
projects = ["./project1",./project2./project3]all_data = [object Object]roject in projects:
    data = analytics.analyze_project(project)
    all_dataproject] = data

# Générer un rapport comparatif
analytics.generate_html_report(all_data, "./comparison_report.html")
```

## 🔧 Configuration avancée

### Configuration personnalisée

```python
# Configuration de lIA
ai_config = {
    "models":        [object Object]name": "mistral", "provider": ollama",model": "mistral},
        {"name": "claude", "provider": "anthropic", model":claude-3sonnet-20240229}
    ],
   fallback_chain: [mistral", "claude],
    timeout": 60,
   max_retries": 5

ai = RobustAI(**ai_config)

# Configuration du générateur
generator_config = [object Object]  ai_robust": ai,
  templates_dir": "./custom_templates",
   backup_enabled": True
}

generator = ProjectGenerator(**generator_config)
```

## 🐛 Gestion d'erreurs

### Exceptions courantes

```python
from athalia_core.exceptions import *

try:
    result = ai.generate_blueprint("Description")
except AIModelError as e:
    print(f"Erreur de modèle IA: {e}")
except ProjectGenerationError as e:
    print(f"Erreur de génération: {e}")
except AuditError as e:
    print(fErreur d'audit: {e}")
```

### Codes d'erreur

- `AIModelError` : Erreur de modèle IA
- `ProjectGenerationError` : Erreur de génération de projet
- `AuditError` : Erreur d'audit
- `PluginError` : Erreur de plugin
- `ConfigurationError` : Erreur de configuration

---

*Dernière mise à jour : $(date)* 