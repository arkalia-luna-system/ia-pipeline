# Guide d'utilisation - athalia-dev-setup

## Vue d'ensemble

Ce guide explique comment utiliser athalia-dev-setup.

## Configuration

```yaml
name: athalia-dev-setup
version: 1.0.0
description: # athalia-dev-setup
```

### Lancement rapide

```bash
# Mode développement
python athalia_unified.py . --action complete

# Mode audit
python athalia_unified.py . --action audit

# Mode production avec options
python athalia_unified.py . --action complete --no-dry-run
```

### Configuration

Le projet utilise un fichier de configuration YAML :

```yaml
# config/athalia_config.yaml
app:
  name: athalia-dev-setup
  debug: true
  port: 8000

database:
  url: sqlite:///app.db
  echo: false
```

## Fonctionnalités principales

### Classes principales

#### UnifiedOrchestrator

**Exemple d'utilisation :**

```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

# Créer une instance
instance = UnifiedOrchestrator("./mon-projet")
# Utiliser une méthode
result = instance.orchestrate_project_complete("./mon-projet")
```

#### IntelligentAuditor

Auditeur intelligent de projets générés.

**Exemple d'utilisation :**

```python
from athalia_core.intelligent_auditor import IntelligentAuditor

# Créer une instance
instance = IntelligentAuditor("./mon-projet")
# Utiliser une méthode
result = instance.audit_project()
```

#### AutoTester

Système de génération automatique de tests

**Exemple d'utilisation :**

```python
from athalia_core.auto_tester import AutoTester

# Créer une instance
instance = AutoTester("./mon-projet")
# Utiliser une méthode
result = instance.generate_tests()
```

### Fonctions utilitaires

#### main

Fonction principale du CLI unifié

**Exemple d'utilisation :**

```python
# Utilisation directe du script
python athalia_unified.py --help

# Ou import du module
from athalia_unified import main

result = main()
```

#### orchestrate_project_complete

**Exemple d'utilisation :**

```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

orchestrator = UnifiedOrchestrator("./mon-projet")
result = orchestrator.orchestrate_project_complete("./mon-projet")
```

#### audit_project_intelligent

**Exemple d'utilisation :**

```python
from athalia_core.audit import audit_project_intelligent

result = audit_project_intelligent(project_path)
```

#### scan_projects

**Exemple d'utilisation :**

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
