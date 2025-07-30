# 📚 Documentation API - Athalia Dev Setup

**Section :** Documentation API  
**Date :** 29 juillet 2025  
**Version :** 2.0.0

---

## 🎯 **Vue d'Ensemble**

Cette section contient toute la documentation API d'Athalia Dev Setup, organisée par modules et fonctionnalités.

---

## 📋 **Modules Principaux**

### **🧠 Cœur du Système**
- [Orchestrateur Principal](CORE_MODULES.md) - `athalia_orchestrator.py`
- [Gestion d'Erreurs](ERROR_HANDLING.md) - `error_handling.py` et `error_codes.py`
- [Configuration](CONFIG_MANAGER.md) - `config_manager.py`

### **🤖 Intelligence Artificielle**
- [IA Robuste](AI_ROBUST.md) - `ai_robust.py`
- [Distillation](DISTILLATION.md) - Modules de distillation
- [Agents](AGENTS.md) - Système d'agents

### **🏭 Industrialisation**
- [Génération](GENERATION.md) - `generation.py`
- [Tests Automatiques](AUTO_TESTER.md) - `auto_tester.py`
- [Documentation Auto](AUTO_DOCUMENTER.md) - `auto_documenter.py`
- [CI/CD Auto](AUTO_CICD.md) - `auto_cicd.py`

### **🔧 Outils et Utilitaires**
- [CLI](CLI.md) - Interface en ligne de commande
- [Dashboard](DASHBOARD.md) - Interface web
- [Plugins](PLUGINS.md) - Système de plugins

---

## 🚀 **Utilisation Rapide**

### **Import des Modules**
```python
# Orchestrateur principal
from athalia_core.athalia_orchestrator import AthaliaOrchestrator

# Gestion d'erreurs
from athalia_core.error_handling import AthaliaError, ErrorHandler

# IA robuste
from athalia_core.ai_robust import RobustAI

# Génération
from athalia_core.generation import generate_project
```

### **Exemple d'Utilisation**
```python
# Créer l'orchestrateur
orch = AthaliaOrchestrator()

# Générer un projet
project_path = orch.generate_project(
    blueprint={"project_name": "mon_projet"},
    output_dir="./generated"
)

# Analyser le projet
analysis = orch.analyze_project(project_path)
```

---

## 📊 **Statistiques API**

- **Modules principaux :** 15+
- **Fonctions exportées :** 200+
- **Classes principales :** 25+
- **Tests de couverture :** >90%

---

## 🔗 **Navigation**

- [← Retour à l'index principal](../README.md)
- [→ Guides développeur](../DEVELOPER/)
- [→ Exemples d'utilisation](../GUIDES/)

---

*Documentation générée automatiquement par Athalia - 2025-07-29*
