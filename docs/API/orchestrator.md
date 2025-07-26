# 🎼 Orchestrateur - Documentation API

**Date :** 26 juillet 2025  
**Module :** Orchestrateur  
**Statut :** Documentation complète

## 🎯 Vue d'ensemble

L'orchestrateur unifié d'Athalia coordonne tous les modules pour fournir un pipeline complet d'industrialisation des projets.

## 🏗️ Architecture

### **Unified Orchestrator** (`athalia_core.unified_orchestrator`)

L'orchestrateur principal qui coordonne tous les modules.

#### Classes Principales
```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

# Créer une instance
orchestrator = UnifiedOrchestrator("./mon-projet")

# Industrialiser un projet
results = orchestrator.orchestrate_project_complete("./mon-projet")
```

#### Configuration
```python
config = {
    "audit": True,        # Audit intelligent
    "lint": True,         # Linting et qualité de code
    "security": True,     # Audit de sécurité
    "analytics": True,    # Analytics et métriques
    "docs": True,         # Génération de documentation
    "cicd": True,         # Configuration CI/CD
    "robotics": False,    # Intégration robotics
    "intelligence": True, # Modules IA
    "predictions": True,  # Prédictions et optimisations
    "optimizations": True, # Optimisations automatiques
    "learning": True,     # Apprentissage automatique
    "plugins": True,      # Système de plugins
    "templates": True     # Système de templates
}
```

## 🔄 Pipeline d'Industrialisation

### **Étape 1 : Audit et Analyse**
```python
# Audit intelligent du projet
audit_results = orchestrator._run_audit(project_path)

# Analyse de la structure
structure_analysis = orchestrator._analyze_project_structure(project_path)
```

### **Étape 2 : Nettoyage et Optimisation**
```python
# Nettoyage automatique
cleanup_results = orchestrator._run_cleanup(project_path)

# Optimisation de la structure
optimization_results = orchestrator._optimize_project_structure(project_path)
```

### **Étape 3 : Documentation et Tests**
```python
# Génération de documentation
docs_results = orchestrator._generate_documentation(project_path)

# Génération de tests
tests_results = orchestrator._generate_tests(project_path)
```

### **Étape 4 : CI/CD et Déploiement**
```python
# Configuration CI/CD
cicd_results = orchestrator._setup_cicd(project_path)

# Configuration de déploiement
deployment_results = orchestrator._setup_deployment(project_path)
```

### **Étape 5 : Validation et Monitoring**
```python
# Validation complète
validation_results = orchestrator._validate_project(project_path)

# Configuration du monitoring
monitoring_results = orchestrator._setup_monitoring(project_path)
```

## 🎯 Fonctionnalités Principales

### **Gestion de Projets**
```python
# Scanner les projets
projects = orchestrator.scan_projects("./workspace")

# Industrialiser un projet spécifique
results = orchestrator.industrialize_project("./mon-projet", config)

# Valider un projet
validation = orchestrator.validate_project("./mon-projet")
```

### **Pipeline Complet**
```python
# Exécuter le pipeline complet
results = orchestrator.orchestrate_project_complete("./mon-projet", config)

# Exécuter des étapes spécifiques
results = orchestrator.run_industrialization_steps("./mon-projet", ["audit", "cleanup"])
```

### **Intégration Robotics**
```python
# Audit robotics
robotics_audit = orchestrator._run_robotics_audit(project_path)

# Configuration Reachy
reachy_config = orchestrator._configure_reachy(project_path)

# Intégration ROS2
ros2_integration = orchestrator._setup_ros2(project_path)
```

### **Phase 2 - Sauvegarde et Validation**
```python
# Sauvegarde automatique
backup_results = orchestrator.orchestrator_auto_backup()

# Validation des entrées
validation = orchestrator.validate_phase2_inputs(project_path)

# Statistiques de sauvegarde
stats = orchestrator.get_phase2_backup_stats()
```

## 📊 Métriques et Rapports

### **Rapport d'Industrialisation**
```python
# Générer un rapport complet
report = orchestrator.generate_industrialization_report(project_path)

# Métriques de qualité
metrics = orchestrator.get_project_metrics(project_path)

# Recommandations d'amélioration
recommendations = orchestrator.get_improvement_recommendations(project_path)
```

### **Dashboard et Monitoring**
```python
# Générer un dashboard
dashboard = orchestrator.generate_dashboard(project_path)

# Configuration du monitoring
monitoring = orchestrator.setup_project_monitoring(project_path)

# Alertes et notifications
alerts = orchestrator.configure_alerts(project_path)
```

## 🔧 Configuration Avancée

### **Configuration Personnalisée**
```python
# Configuration personnalisée
custom_config = {
    "audit": {
        "enabled": True,
        "depth": "comprehensive",
        "include_security": True
    },
    "cleanup": {
        "enabled": True,
        "aggressive": False,
        "backup_before": True
    },
    "documentation": {
        "enabled": True,
        "format": ["markdown", "html"],
        "include_api": True
    }
}

results = orchestrator.orchestrate_with_config("./mon-projet", custom_config)
```

### **Plugins et Extensions**
```python
# Charger des plugins personnalisés
orchestrator.load_custom_plugins(["./plugins/custom_audit.py"])

# Exécuter des plugins
plugin_results = orchestrator._run_plugins(project_path)

# Générer des templates
template_results = orchestrator._run_templates(project_path)
```

## 🔗 Navigation

- [Documentation API principale](README.md)
- [Core Modules](core_modules.md)
- [Plugins et Templates](plugins.md)
- [Robotics](robotics.md)

---

**Généré automatiquement** - 26/07/2025


