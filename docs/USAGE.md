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
python main.py

# Mode production
python main.py --production
```

### Configuration

Le projet utilise un fichier de configuration YAML :

```yaml
# config.yml
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

#### TestLoggingSystem

Tests pour le système de logging d'Athalia

**Exemple d'utilisation :**

```python
from athalia-dev-setup import TestLoggingSystem

# Créer une instance
instance = TestLoggingSystem()
# Utiliser une méthode
result = instance.setup_method()
```

### Fonctions utilitaires

#### main

Fonction principale du CLI unifié

**Exemple d'utilisation :**

```python
from athalia-dev-setup import main

result = main()
```

#### industrialize_project

**Exemple d'utilisation :**

```python
from athalia-dev-setup import industrialize_project

result = industrialize_project(project_path, config)
```

#### audit_project

**Exemple d'utilisation :**

```python
from athalia-dev-setup import audit_project

result = audit_project(project_path)
```

#### scan_projects

**Exemple d'utilisation :**

```python
from athalia-dev-setup import scan_projects

result = scan_projects(project_path)
```

#### audit_project_intelligent

Fonction principale pour l'audit intelligent.

**Exemple d'utilisation :**

```python
from athalia-dev-setup import audit_project_intelligent

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
