# Guide Développeur - Athalia/Arkalia

## 🚀 Vue densemble

Athalia/Arkalia est un pipeline dindustrialisation IA pour la génération automatique de projets, tests, documentation, audit, CI/CD et intégration dIA robuste locale.

## 📁 Architecture du projet

```
athalia-dev-setup/
├── athalia_core/           # Cœur du système
│   ├── __init__.py        # Point dentrée principal
│   ├── ai_robust.py       # IA robuste avec fallback
│   ├── generation.py      # Génération de projets
│   ├── audit.py          # Audit intelligent
│   ├── analytics.py      # Analytics et métriques
│   └── plugins.py        # Système de plugins
├── agents/                # Agents IA spécialisés
├── prompts/              # Templates de prompts
├── templates/            # Templates de projets
├── tests/               # Tests unitaires et intégration
├── docs/                # Documentation
├── setup/               # Scripts de configuration
└── tasks/               # Tâches automatisées
```

## 🛠️ Installation pour développement

### Prérequis
- Python310+
- Git
- Ollama (pour l'IA locale)

### Installation
```bash
# Cloner le projet
git clone <repository>
cd athalia-dev-setup

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer en mode développement
pip install -e .

# Installer les dépendances de développement
pip install -r requirements.txt
```

## 🔧 Configuration

### Variables d'environnement
Créez un fichier `.env` :
```bash
# API Keys (optionnelles pour l'IA locale)
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Configuration Ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral

# Configuration du projet
ATHALIA_LOG_LEVEL=INFO
ATHALIA_CACHE_DIR=./cache
```

### Configuration Ollama
```bash
# Installer Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Télécharger le modèle Mistral
ollama pull mistral

# Vérifier l'installation
ollama list
```

## 🧪 Tests

### Exécuter tous les tests
```bash
python -m pytest tests/ -v
```

### Tests avec couverture
```bash
python -m pytest tests/ --cov=athalia_core --cov-report=html
```

### Tests spécifiques
```bash
# Tests d'intégration
python -m pytest tests/integration/ -v

# Tests de lIA robuste
python -m pytest tests/test_ai_robust.py -v

# Tests d'audit
python -m pytest tests/test_audit_intelligent.py -v
```

## 🔌 Système de plugins

### Structure d'un plugin
```python
# plugins/my_plugin.py
from athalia_core.plugins import Plugin

class MyPlugin(Plugin):
    name = "my_plugin"
    description = "Description de mon plugin
    version = "10  
    def execute(self, context):
Logique principale du plugin
        return {status": success,data:result"}
```

### Utilisation des plugins
```python
from athalia_core.plugins import PluginManager

# Charger tous les plugins
manager = PluginManager()
plugins = manager.load_plugins()

# Exécuter un plugin spécifique
result = manager.run_plugin("my_plugin", context={})
```

## 🤖 IA Robuste

### Configuration des modèles
```python
from athalia_core.ai_robust import RobustAI

# Configuration automatique
ai = RobustAI()

# Configuration manuelle
ai = RobustAI(
    models=       [object Object]name": "mistral", "provider": ollama",model": "mistral},
        {"name": "claude", "provider": "anthropic", model":claude-3sonnet-20240229}   ],
    fallback_chain=[mistral",claude]
)
```

### Utilisation
```python
# Génération avec fallback automatique
response = ai.generate_blueprint(
    project_description=Projet de test",
    complexity="simple"
)

# Classification de complexité
complexity = ai.classify_project_complexity("Description du projet)# Prompt dynamique
prompt = ai.get_dynamic_prompt("blueprint", complexity="medium")
```

## 📊 Analytics et métriques

### Génération d'analytics
```python
from athalia_core.analytics import Analytics

analytics = Analytics()

# Analyser un projet
data = analytics.analyze_project("path/to/project")

# Générer un rapport HTML
analytics.generate_html_report(data,report.html")

# Heatmap de complexité
heatmap_data = analytics.generate_heatmap_data(["project1", project2"])
```

## 🔍 Audit intelligent

### Audit complet d'un projet
```python
from athalia_core.audit import AuditIntelligent

auditor = AuditIntelligent()

# Audit complet
report = auditor.audit_project("path/to/project")

# Audit spécifique
security_report = auditor.audit_security("path/to/project")
quality_report = auditor.audit_code_quality("path/to/project")
```

## 🚀 Génération de projets

### Génération simple
```python
from athalia_core.generation import ProjectGenerator

generator = ProjectGenerator()

# Générer un projet
result = generator.generate_blueprint(
    description="Application web moderne",
    output_dir="./generated_project"
)
```

### Génération avec options avancées
```python
result = generator.generate_blueprint(
    description="API REST avec FastAPI",
    output_dir="./api_project",
    options={
        framework": fastapi",
       database": "postgresql,
     auth": "jwt",
     tests: True,
    docs: True,
        docker": True
    }
)
```

## 📝 Contribution

### Standards de code
- PEP 8 pour le style Python
- Docstrings pour toutes les fonctions
- Type hints pour les signatures
- Tests unitaires pour toutes les fonctionnalités

### Workflow Git
```bash
# Créer une branche pour une fonctionnalité
git checkout -b feature/nouvelle-fonctionnalite

# Développer et tester
# ...

# Commiter avec un message descriptif
git commit -m "feat: ajouter nouvelle fonctionnalité X"

# Pousser et créer une PR
git push origin feature/nouvelle-fonctionnalite
```

### Tests avant commit
```bash
# Lancer tous les tests
python -m pytest tests/ -v

# Vérifier la couverture
python -m pytest tests/ --cov=athalia_core --cov-report=term-missing

# Linter
flake8 athalia_core/
mypy athalia_core/
```

## 🐛 Debugging

### Logs détaillés
```python
import logging

# Activer les logs détaillés
logging.basicConfig(level=logging.DEBUG)

# Ou via variable d'environnement
export ATHALIA_LOG_LEVEL=DEBUG
```

### Mode debug de lIA```python
from athalia_core.ai_robust import RobustAI

ai = RobustAI(debug=True)
# Affiche les détails des appels API et fallbacks
```

## 📚 API Reference

### Classes principales

#### RobustAI
Gestionnaire d'IA robuste avec fallback intelligent.

**Méthodes principales :**
- `generate_blueprint(description, complexity=None)`
- `classify_project_complexity(description)`
- `get_dynamic_prompt(context, complexity)`

#### ProjectGenerator
Générateur de projets IA.

**Méthodes principales :**
- `generate_blueprint(description, output_dir, options=None)`
- `scan_existing_project(path)`
- `merge_or_suffix_file(content, filepath)`

#### AuditIntelligent
Auditeur intelligent de projets.

**Méthodes principales :**
- `audit_project(path)`
- `audit_security(path)`
- `audit_code_quality(path)`

#### Analytics
Générateur d'analytics et métriques.

**Méthodes principales :**
- `analyze_project(path)`
- `generate_html_report(data, output_file)`
- `generate_heatmap_data(projects)`

## 🔗 Liens utiles

- [Documentation utilisateur](USER_GUIDE.md)
- [Guide d'installation](INSTALL.md)
- [Dépannage](TROUBLESHOOTING.md)
- [Architecture](ARCHITECTURE.md)
- [FAQ](FAQ.md)

## 🤝 Support

Pour toute question ou problème :1 Consultez la [FAQ](FAQ.md)
2. Vérifiez le [guide de dépannage](TROUBLESHOOTING.md)
3. Ouvrez une issue sur GitHub
4Contactez l'équipe de développement

---

*Dernière mise à jour : $(date)* 