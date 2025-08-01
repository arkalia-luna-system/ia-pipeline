# 📚 Documentation API - Athalia Dev Setup

**Section :** Documentation API
**Date :** 29 juillet 2025
**Version :** 11.0 (ACTIVE DEVELOPMENT)

---

## 🎯 **Vue d'Ensemble**

Cette section contient toute la documentation API d'Athalia Dev Setup, organisée par modules et fonctionnalités.

---

## 📋 **Modules Principaux**

### **🧠 Cœur du Système**
- [Modules Core](core_modules.md) - Modules principaux du système
- [Gestion d'Erreurs](ERROR_HANDLING.md) - Gestion des erreurs
- [Orchestrateur](orchestrator.md) - Orchestrateur unifié

### **🤖 Intelligence Artificielle**
- [Commandes](COMMANDES.md) - Commandes principales
- [Commandes Avancées](COMMANDES_AVANCEES.md) - Commandes avancées
- [Plugins](plugins.md) - Système de plugins

### **🏭 Industrialisation**
- [Robotique](robotics.md) - Modules robotiques
- [Référence](REFERENCE.md) - Référence complète de l'API

---

## 🚀 **Utilisation Rapide**

### **Import des Modules**
```python
# Modules principaux
from athalia_core import ai_robust, analytics, audit

# IA robuste
from athalia_core.ai_robust import RobustAI

# Analytics
from athalia_core.analytics import analyze_project

# Audit
from athalia_core.audit import audit_project
```

### **Exemple d'Utilisation**
```python
# Analyser un projet
from athalia_core.analytics import analyze_project

analysis = analyze_project("/chemin/vers/projet")
print(f"Score qualité: {analysis['quality_score']}")

# Audit de sécurité
from athalia_core.audit import audit_project

audit_result = audit_project("/chemin/vers/projet")
print(f"Score sécurité: {audit_result['security_score']}")
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
