# 🚀 Guide d'Utilisation - Athalia

**Version :** v12.0.0  
**Date :** 7 février 2026

---

## 🎯 **Vue d'Ensemble**

Ce guide explique comment utiliser Athalia, le plateforme d'automatisation DevOps avancé pour l'automatisation et l'optimisation de projets de développement.

---

## 🚀 **Utilisation Rapide**

### **Commandes Principales**

```bash
# Audit complet d'un projet
python bin/core/athalia_unified.py /chemin/vers/projet --action audit

# Industrialisation complète
python bin/core/athalia_unified.py /chemin/vers/projet --action complete

# Dashboard interactif
python bin/core/athalia_unified.py /chemin/vers/projet --action dashboard

# Mode simulation (dry-run)
python bin/core/athalia_unified.py /chemin/vers/projet --action audit --dry-run
```

### **Options Avancées**

```bash
# Audit avec détails
python bin/core/athalia_unified.py /chemin/vers/projet --action audit --verbose

# Industrialisation sans audit préalable
# python bin/core/athalia_unified.py /chemin/vers/projet --action complete --no-audit  # Options non disponibles

# Dashboard avec profil utilisateur
# python bin/core/athalia_unified.py /chemin/vers/projet --action dashboard --utilisateur dev  # Options non disponibles
```

---

## ⚙️ **Configuration**

### **Fichier de Configuration Principal**
```yaml
# config/athalia_config.yaml
general:
  lang: fr
  verbose: true
  auto_fix: true
  dry_run: false
  log_level: INFO
  log_file: logs/athalia.log

modules:
  audit: true
  clean: true
  document: false
  test: true
  cicd: false
  correction: true
  profiles: true
  dashboard: false
  security: true
  analytics: false
  linting: false

ai:
  models:
    - ollama_mistral
    - ollama_llama
    - mock
  timeout: 15
  max_retries: 2
  fallback_enabled: true

testing:
  auto_run: false
  coverage: false
  parallel: false
  timeout: 60

cicd:
  github_actions: false
  docker: false
  deployment: false
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
- Contact : arkalia.luna.system@gmail.com

---
*Généré automatiquement par Athalia* - 2025-08-20
