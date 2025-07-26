# 📚 Documentation API - Athalia

**Date :** 26 juillet 2025  
**Version :** 2.0.0  
**Statut :** Documentation réorganisée et optimisée

## 🎯 Vue d'ensemble

Cette documentation décrit l'API complète d'Athalia, le pipeline d'industrialisation IA. L'API est organisée en modules logiques pour faciliter la navigation et la maintenance.

## 📁 Modules Principaux

### 🔧 **Core Modules** (`athalia_core/`)
- [Analytics](core_modules.md#analytics) - Analyse et métriques de projets
- [Audit](core_modules.md#audit) - Audit intelligent de projets
- [Auto Cleaner](core_modules.md#auto-cleaner) - Nettoyage automatique
- [Auto Documenter](core_modules.md#auto-documenter) - Documentation automatique
- [Auto Tester](core_modules.md#auto-tester) - Tests automatiques
- [AI Robust](core_modules.md#ai-robust) - IA robuste avec fallback
- [Config Manager](core_modules.md#config-manager) - Gestionnaire de configuration

### 🎼 **Orchestrateur** (`orchestrator.md`)
- [Unified Orchestrator](orchestrator.md#unified-orchestrator) - Orchestrateur principal
- [Industrialization Pipeline](orchestrator.md#industrialization-pipeline) - Pipeline d'industrialisation
- [Project Management](orchestrator.md#project-management) - Gestion de projets

### 🔌 **Plugins et Templates** (`plugins.md`)
- [Plugin System](plugins.md#plugin-system) - Système de plugins
- [Template Engine](plugins.md#template-engine) - Moteur de templates
- [Custom Plugins](plugins.md#custom-plugins) - Plugins personnalisés

### 🤖 **Robotics** (`robotics.md`)
- [Reachy Integration](robotics.md#reachy-integration) - Intégration Reachy
- [ROS2 Support](robotics.md#ros2-support) - Support ROS2
- [Docker Robotics](robotics.md#docker-robotics) - Docker pour robotics

## 🚀 Démarrage Rapide

### Installation
```bash
pip install -r requirements.txt
```

### Utilisation Basique
```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

# Créer une instance
orchestrator = UnifiedOrchestrator("./mon-projet")

# Industrialiser un projet
results = orchestrator.orchestrate_project_complete("./mon-projet")
```

### Configuration
```python
config = {
    "audit": True,
    "lint": True,
    "security": True,
    "analytics": True,
    "docs": True,
    "cicd": True,
    "robotics": False
}
```

## 📊 Fonctionnalités Principales

### 🔍 **Audit Intelligent**
- Analyse complète des projets
- Détection de vulnérabilités
- Score de qualité
- Recommandations d'amélioration

### 🧹 **Nettoyage Automatique**
- Suppression des fichiers parasites
- Nettoyage des caches
- Optimisation de l'espace disque
- Détection de doublons

### 📚 **Documentation Automatique**
- Génération de documentation
- Support multi-langues
- Templates personnalisables
- Mise à jour automatique

### 🧪 **Tests Automatiques**
- Génération de tests unitaires
- Tests d'intégration
- Couverture de code
- Validation continue

### ⚙️ **CI/CD Automatique**
- Configuration GitHub Actions
- Déploiement automatique
- Intégration continue
- Pipeline automatisé

## 🔗 Navigation

- [Documentation principale](../README.md)
- [Guide d'utilisation](../USAGE.md)
- [Guide d'installation](../INSTALLATION.md)
- [Guide développeur](../GUIDES/developer.md)

## 📈 Métriques

- **Modules principaux :** 15+
- **Fonctionnalités :** 50+
- **Tests :** 200+
- **Documentation :** 100% couverte

---

**Généré automatiquement** - 26/07/2025 