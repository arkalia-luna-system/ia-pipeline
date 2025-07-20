# Organisation du Projet Athalia

## Structure des Dossiers

### 📁 **Racine du Projet**
- `README.md` - Documentation principale
- `requirements.txt` - Dépendances Python
- `athalia_unified.py` - Point d'entrée unifié
- `CHANGELOG.md` - Historique des changements
- `DASHBOARD.md` - Guide du dashboard
- `LICENSE` - Licence du projet
- `progress_optimisation.md` - Suivi de l'optimisation
- `GUIDE_OPTIMISATION_MANUEL.md` - Guide de migration manuelle
- `PLAN_OPTIMISATION_COMPLET.md` - Plan d'optimisation détaillé

### 📁 **athalia_core/** - Cœur du système
- **Modules principaux** - Fonctionnalités de base
  - `main.py` - Point d'entrée principal
  - `cli.py` - Interface en ligne de commande
  - `dashboard.py` - Dashboard Streamlit
  - `analytics.py` - Analytics IA
  - `advanced_analytics.py` - Analytics avancée
  - `athalia_orchestrator.py` - Orchestrateur principal
  - `intelligent_auditor.py` - Auditeur intelligent
  - `auto_documenter.py` - Générateur de documentation
  - `auto_tester.py` - Générateur de tests
  - `auto_cleaner.py` - Nettoyeur automatique
  - `auto_cicd.py` - CI/CD automatique
  - `audit.py` - Audit de projet
  - `security_auditor.py` - Audit de sécurité
  - `config_manager.py` - Gestionnaire de configuration
  - `plugins_manager.py` - Gestionnaire de plugins
  - `plugins_validator.py` - Validateur de plugins
  - `project_importer.py` - Importateur de projets
  - `ready_check.py` - Vérificateur de préparation
  - `cleanup.py` - Nettoyage
  - `ci.py` - Intégration continue
  - `onboarding.py` - Intégration
  - `code_linter.py` - Linter de code
  - `generation.py` - Génération de code
  - `autocomplete_engine.py` - Moteur d'auto-complétion
  - `autocomplete_server.py` - Serveur d'auto-complétion
  - `multi_file_editor.py` - Éditeur multi-fichiers
  - `security.py` - Sécurité
  - `logger_advanced.py` - Logger avancé
  - `correction_optimizer.py` - Optimiseur de corrections
  - `ai_robust.py` - IA robuste

- **📁 advanced_modules/** - Modules avancés
  - `auto_correction_advanced.py` - Correction automatique avancée
  - `dashboard_unified.py` - Dashboard unifié simplifié
  - `user_profiles_advanced.py` - Gestion avancée des profils utilisateur

- **📁 agents/** - Agents IA spécialisés
  - `context_prompt.py` - Agent de prompts contextuels
  - `network_agent.py` - Agent de gestion réseau
  - `audit_agent.py` - Agent d'audit intelligent
  - `qwen_agent.py` - Agent Qwen spécialisé

- **📁 external_plugins/** - Plugins externes
  - `docker_export_plugin.py` - Plugin d'export Docker
  - `hello_world_plugin.py` - Plugin Hello World

- **📁 distillation/** - Distillation IA
  - Modules de distillation et optimisation

- **📁 classification/** - Classification de projets
  - `project_classifier.py` - Classifieur de projets
  - `project_types.py` - Types de projets

- **📁 i18n/** - Internationalisation
  - `en.py` - Anglais
  - `fr.py` - Français

- **📁 templates/** - Templates
  - `artistic_templates.py` - Templates artistiques
  - `base_templates.py` - Templates de base

- **📁 plugins/** - Plugins internes
  - Plugins développés en interne

- **📁 robotics/** - Modules robotiques
  - Modules pour l'intégration robotique

### 📁 **docs/** - Documentation
- `analyses/` - Analyses complètes du système
  - `ANALYSE_INTELLIGENCE_COMPLETE.md`
  - `ANALYSE_ARCHITECTURE_COMPLETE.md`
  - `SYSTEME_INTELLIGENT_ATHALIA.md`
  - `SUPER_CERVEAU_ATHALIA_FINAL.md`
  - `ANALYSE_PLAN_OPTIMISATION_AVANCE.md`
- `roadmaps/` - Plans de développement
  - `ROADMAP.md`
  - `ROADMAP_REALISTE.md`
- `benchmarks/` - Benchmarks et tests de performance
  - `BENCHMARK.md`
- `robotics/` - Documentation robotique
  - `ROBOTICS_QUICK_START.md`
  - `ROBOTICS_INTEGRATION_SUMMARY.md`
  - `reachy_audit_*.md`

### 📁 **tests/** - Tests
- Tests unitaires, d'intégration et de performance
- Tests pour tous les modules du système

### 📁 **scripts/** - Scripts utilitaires
- `robotics/` - Scripts robotiques
  - `athalia_robotics_integration.py`
  - `demo_robotics.py`
- `debug/` - Scripts de débogage
  - `debug_correction.py`

### 📁 **dashboard/** - Dashboards web
- `dashboard.html` - Dashboard principal
- `analytics_dashboard.html` - Dashboard analytics
- `index.html` - Page d'accueil

### 📁 **data/** - Données
- `athalia_analytics.db` - Base de données analytics
- `profils_utilisateur.db` - Base de données profils

### 📁 **config/** - Configuration
- `athalia_config.yaml` - Configuration principale
- `paths.yaml` - Chemins du système
- `pyproject.toml` - Configuration Python
- `pytest.ini` - Configuration tests
- `requirements.txt` - Dépendances
- `docker-compose.yml` - Configuration Docker
- `Dockerfile` - Image Docker
- `Taskfile.yaml` - Tâches automatisées
- `Cargo.toml` - Configuration Rust

### 📁 **bin/** - Scripts binaires
- `ath-clean` - Nettoyage
- `ath-test.py` - Tests
- `ath-lint.py` - Linting
- `ath-build.py` - Build
- `ath-audit.py` - Audit
- `ath-coverage.py` - Couverture de tests
- `ath-test-aliases.sh` - Tests des alias

### 📁 **setup/** - Configuration et alias
- `alias.sh` - Alias de développement
- `alias-unified.sh` - Alias unifiés
- Scripts de configuration et d'installation

### 📁 **prompts/** - Prompts IA
- Prompts pour les différents agents et modules

### 📁 **templates/** - Templates de génération
- `api/` - Templates API
- `memory/` - Templates mémoire
- `tts/` - Templates TTS

### 📁 **projects/** - Projets générés
- Projets créés par le système

### 📁 **blueprints_history/** - Historique des blueprints
- Blueprints de projets générés

### 📁 **archive/** - Archives
- Rapports et données archivées

### 📁 **logs/** - Logs
- Fichiers de logs du système

### 📁 **htmlcov/** - Couverture de code
- Rapports de couverture HTML

## 🎯 **Principes d'Organisation**

### **Centralisation**
- Tous les modules principaux dans `athalia_core/`
- Organisation logique par type de fonctionnalité
- Séparation claire entre modules de base et avancés

### **Cohérence**
- Noms de fichiers en anglais
- Conventions de nommage standardisées
- Structure de packages Python appropriée

### **Modularité**
- Modules indépendants et réutilisables
- Interfaces claires entre les composants
- Plugins extensibles

### **Maintenabilité**
- Documentation complète
- Tests pour chaque module
- Configuration centralisée

## 📊 **Métriques d'Organisation**

### **Avant Réorganisation**
- **Modules dispersés** : 9 modules dans 3 dossiers différents
- **Structure incohérente** : Noms de fichiers mixtes
- **Imports complexes** : Chemins relatifs multiples

### **Après Réorganisation**
- **Modules centralisés** : 9 modules dans `athalia_core/`
- **Structure cohérente** : Noms standardisés en anglais
- **Imports simplifiés** : Packages Python appropriés

## 🚀 **Utilisation**

### **Import des Modules**
```python
# Modules avancés
from athalia_core.advanced_modules import DashboardUnifieSimple
from athalia_core.advanced_modules.auto_correction_advanced import *

# Agents IA
from athalia_core.agents.context_prompt import *
from athalia_core.agents.network_agent import *

# Plugins externes
from athalia_core.external_plugins.docker_export_plugin import *
```

### **Alias de Développement**
```bash
# Charger les alias
source setup/alias.sh

# Utiliser les modules
ath-dashboard-unified
ath-auto-correct
ath-smart
```

## 📝 **Maintenance**

### **Ajout d'un Nouveau Module**
1. Créer le fichier dans le dossier approprié
2. Ajouter l'import dans le `__init__.py` correspondant
3. Créer les tests associés
4. Mettre à jour la documentation
5. Ajouter l'alias si nécessaire

### **Modification d'un Module**
1. Tester les changements
2. Mettre à jour la documentation
3. Vérifier la compatibilité
4. Commiter les changements

---

**Dernière mise à jour :** 19/07/2025 14:57
**Version :** 2.0 - Structure réorganisée 