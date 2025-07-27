# 🔧 Core Modules - Documentation API

**Date :** 26 juillet 2025  
**Module :** Core Modules  
**Statut :** Documentation complète

## 🎯 Vue d'ensemble

Les modules principaux d'Athalia fournissent les fonctionnalités de base pour l'industrialisation des projets.

## 📁 Modules Disponibles

### 📊 **Analytics** (`athalia_core.analytics`)

Module d'analyse et de métriques de projets.

#### Fonctions Principales
```python
from athalia_core.analytics import analyze_project, generate_analytics_html

# Analyser un projet
analysis = analyze_project("./mon-projet")

# Générer un rapport HTML
html_report = generate_analytics_html("./mon-projet")
```

#### Métriques Disponibles
- **Structure du projet** : Organisation des fichiers et dossiers
- **Qualité du code** : Score de qualité basé sur plusieurs critères
- **Couverture de tests** : Pourcentage de code testé
- **Documentation** : Qualité et complétude de la documentation
- **Sécurité** : Vulnérabilités détectées

### 🔍 **Audit** (`athalia_core.audit`)

Module d'audit intelligent de projets.

#### Fonctions Principales
```python
from athalia_core.audit import audit_project_intelligent

# Auditer un projet
audit_result = audit_project_intelligent("./mon-projet")
```

#### Critères d'Audit
- **Architecture** : Structure et organisation du code
- **Standards** : Respect des bonnes pratiques
- **Performance** : Optimisations possibles
- **Maintenabilité** : Facilité de maintenance
- **Sécurité** : Vulnérabilités et risques

### 🧹 **Auto Cleaner** (`athalia_core.auto_cleaner`)

Module de nettoyage automatique des projets.

#### Classes Principales
```python
from athalia_core.auto_cleaner import AutoCleaner

# Créer un nettoyeur
cleaner = AutoCleaner("./mon-projet")

# Nettoyer le projet
results = cleaner.clean_project()
```

#### Types de Nettoyage
- **Fichiers temporaires** : `.tmp`, `.temp`, `.cache`
- **Fichiers système** : `.DS_Store`, `Thumbs.db`
- **Fichiers de build** : `__pycache__`, `.pyc`, `.pyo`
- **Fichiers de backup** : `.bak`, `.backup`, `~`
- **Dossiers vides** : Suppression automatique

### 📚 **Auto Documenter** (`athalia_core.auto_documenter`)

Module de génération automatique de documentation.

#### Fonctions Principales
```python
from athalia_core.auto_documenter import generate_documentation

# Générer la documentation
docs = generate_documentation("./mon-projet")
```

#### Types de Documentation
- **README.md** : Documentation principale du projet
- **API.md** : Documentation de l'API
- **CHANGELOG.md** : Historique des changements
- **CONTRIBUTING.md** : Guide de contribution
- **Documentation technique** : Docstrings et commentaires

### 🧪 **Auto Tester** (`athalia_core.auto_tester`)

Module de génération automatique de tests.

#### Fonctions Principales
```python
from athalia_core.auto_tester import generate_tests

# Générer les tests
tests = generate_tests("./mon-projet")
```

#### Types de Tests
- **Tests unitaires** : Tests des fonctions individuelles
- **Tests d'intégration** : Tests des interactions entre modules
- **Tests de régression** : Tests de non-régression
- **Tests de performance** : Tests de performance
- **Tests de sécurité** : Tests de vulnérabilités

### 🤖 **AI Robust** (`athalia_core.ai_robust`)

Module d'IA robuste avec système de fallback.

#### Classes Principales
```python
from athalia_core.ai_robust import RobustAI

# Créer une instance IA
ai = RobustAI()

# Générer un blueprint
blueprint = ai.generate_blueprint("projet web")
```

#### Fonctionnalités
- **Génération de blueprints** : Plans de projets intelligents
- **Revue de code** : Analyse automatique du code
- **Génération de documentation** : Documentation IA
- **Système de fallback** : Basculement automatique entre modèles
- **Prompts dynamiques** : Génération contextuelle

### ⚙️ **Config Manager** (`athalia_core.config_manager`)

Module de gestion de configuration.

#### Classes Principales
```python
from athalia_core.config_manager import ConfigManager

# Créer un gestionnaire de config
config = ConfigManager()

# Charger la configuration
settings = config.load_config()
```

#### Fonctionnalités
- **Chargement de configuration** : YAML, JSON, INI
- **Validation de configuration** : Vérification des paramètres
- **Configuration par défaut** : Valeurs par défaut
- **Configuration environnementale** : Variables d'environnement
- **Sauvegarde de configuration** : Persistance des paramètres

## 🔗 Navigation

- [Documentation API principale](README.md)
- [Orchestrateur](API/orchestrator.md)
- [Plugins et Templates](API/plugins.md)
- [Robotics](API/robotics.md)

---

**Généré automatiquement** - 26/07/2025 