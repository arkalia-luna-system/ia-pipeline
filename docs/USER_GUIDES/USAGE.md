# 🚀 Guide d'Utilisation - Athalia

**Version :** 11.0 (ACTIVE DEVELOPMENT)  
**Date :** 31 Juillet 2025

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
  version: "11.0.0"
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
