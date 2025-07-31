# 🚀 Guide d'Utilisation - Athalia

**Version :** 10.0 (FINAL - 100% TERMINÉE ✅)
**Date :** 30 Juillet 2025

---

## 🎯 **Vue d'Ensemble**

Ce guide explique comment utiliser Athalia, le système d'intelligence artificielle avancé pour l'automatisation et l'optimisation de projets de développement.

---

## 🚀 **Utilisation Rapide**

### **Commandes Principales**

```bash
# Audit complet d'un projet
python athalia_unified.py /chemin/vers/projet --action audit

# Industrialisation complète
python athalia_unified.py /chemin/vers/projet --action complete

# Dashboard interactif
python athalia_unified.py /chemin/vers/projet --action dashboard

# Mode simulation (dry-run)
python athalia_unified.py /chemin/vers/projet --action audit --dry-run
```

### **Options Avancées**

```bash
# Audit avec détails
python athalia_unified.py /chemin/vers/projet --action audit --verbose

# Industrialisation sans audit préalable
python athalia_unified.py /chemin/vers/projet --action complete --no-audit

# Dashboard avec profil utilisateur
python athalia_unified.py /chemin/vers/projet --action dashboard --utilisateur dev
```

---

## ⚙️ **Configuration**

### **Fichier de Configuration Principal**
```yaml
# config/athalia_config.yaml
app:
  name: athalia-dev-setup
  version: "10.0.0"
  debug: false
  port: 8000

security:
  validate_commands: true
  allowed_paths:
    - "/usr/bin"
    - "/opt/homebrew"

logging:
  level: "INFO"
  file: "logs/athalia.log"
  max_size: "10MB"
```

---

## 🔧 **Fonctionnalités Principales**

### **🤖 Intelligence Artificielle**

#### **Audit Intelligent**
```python
from athalia_core.intelligent_auditor import IntelligentAuditor

# Créer un auditeur
auditor = IntelligentAuditor("/chemin/vers/projet")

# Audit complet
result = auditor.audit_project()
print(f"Score qualité: {result['quality_score']}/100")
print(f"Problèmes détectés: {len(result['issues'])}")
```

#### **Génération Automatique de Tests**
```python
from athalia_core.auto_tester import AutoTester

# Créer un générateur de tests
tester = AutoTester("/chemin/vers/projet")

# Générer des tests
result = tester.generate_tests()
print(f"Tests générés: {result['tests_created']}")
```

#### **Analyse de Performance**
```python
from athalia_core.performance_analyzer import PerformanceAnalyzer

# Analyser les performances
analyzer = PerformanceAnalyzer()
report = analyzer.analyze_project_performance("/chemin/vers/projet")
print(f"Score performance: {report.score}/100")
```

### **🛡️ Sécurité et Validation**

#### **Audit de Sécurité**
```python
from athalia_core.security_auditor import SecurityAuditor

# Audit de sécurité
security_auditor = SecurityAuditor("/chemin/vers/projet")
security_report = security_auditor.run()
print(f"Score sécurité: {security_report['security_score']}/100")
```

#### **Validation de Code**
```python
from athalia_core.code_linter import CodeLinter

# Linting et validation
linter = CodeLinter("/chemin/vers/projet")
lint_result = linter.lint_project()
print(f"Erreurs détectées: {len(lint_result['errors'])}")
```

### **🧹 Maintenance et Nettoyage**

#### **Nettoyage Automatique**
```python
from athalia_core.auto_cleaner import AutoCleaner

# Nettoyer le projet
cleaner = AutoCleaner("/chemin/vers/projet")
clean_result = cleaner.clean_project()
print(f"Fichiers nettoyés: {clean_result['files_cleaned']}")
```

---

## 📊 **Exemples d'Utilisation Avancée**

### **Workflow Complet d'Industrialisation**

```bash
# 1. Audit initial
python athalia_unified.py /mon-projet --action audit --verbose

# 2. Correction automatique
python athalia_unified.py /mon-projet --action fix --auto-fix

# 3. Industrialisation complète
python athalia_unified.py /mon-projet --action complete

# 4. Validation finale
python athalia_unified.py /mon-projet --action audit --verbose
```

### **Monitoring Continu**

```bash
# Dashboard en temps réel
python athalia_unified.py /mon-projet --action dashboard --utilisateur dev

# Monitoring des performances
python athalia_core/performance_analyzer.py --monitor --project /mon-projet
```

---

## 🎯 **Cas d'Usage Spécifiques**

### **Projet Python Standard**
```bash
# Audit d'un projet Python
python athalia_unified.py /chemin/projet-python --action audit

# Industrialisation avec tests
python athalia_unified.py /chemin/projet-python --action complete --with-tests
```

### **Projet Robotique (ROS2)**
```bash
# Audit robotique spécialisé
python athalia_unified.py /chemin/projet-ros2 --action audit --robotics

# Validation ROS2
python athalia_core/robotics/ros2_validator.py /chemin/projet-ros2
```

### **Projet Web**
```bash
# Audit d'application web
python athalia_unified.py /chemin/projet-web --action audit --web

# Optimisation frontend
python athalia_core/performance_analyzer.py --frontend --project /chemin/projet-web
```

---

## 🔧 **Dépannage**

### **Problèmes Courants**

#### **Erreur de Permissions**
```bash
# Corriger les permissions
chmod +x bin/*.py
chmod +x bin/*.sh
```

#### **Dépendances Manquantes**
```bash
# Réinstaller les dépendances
pip install --force-reinstall -r requirements.txt
```

#### **Problèmes de Configuration**
```bash
# Vérifier la configuration
python athalia_core/config_manager.py --validate

# Réinitialiser la configuration
python athalia_core/config_manager.py --reset
```

---

## 🎉 **Prochaines Étapes**

1. **Explorer les [Guides développeur](../DEVELOPER/)**
2. **Consulter la [Documentation API](../API/)**
3. **Tester avec vos propres projets**
4. **Contribuer au développement**

---

*Guide d'utilisation complet et détaillé - Prêt pour la production !* ✅

```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

orchestrator = UnifiedOrchestrator("./workspace")
result = orchestrator.scan_projects("./workspace")
```

#### audit_project_intelligent

Fonction principale pour l'audit intelligent.

**Exemple d'utilisation :**

```python
from athalia_core.audit import audit_project_intelligent

result = audit_project_intelligent(project_path)
```


## Cas d'usage avancés

### Intégration avec d'autres outils

```python
# Exemple d'intégration

# Configuration personnalisée
config = {
    'option1': 'value1',
    'option2': 'value2'
}

# Utilisation
app = main_class(config)
app.run()
```

### Gestion des erreurs

```python
try:
    result = some_function()
except Exception as e:
    logger.info(f"Erreur: {e}")
    # Gestion de l'erreur
```

## Bonnes pratiques

1. **Toujours utiliser un environnement virtuel**
2. **Vérifier la configuration avant le lancement**
3. **Utiliser les logs pour le débogage**
4. **Tester les nouvelles fonctionnalités**

## Support et assistance

- Documentation API complète
- Signaler un bug
- Proposer une amélioration
- Contact : support@example.com

---
*Généré automatiquement par Athalia* - 2025-07-29
