# Guide d'utilisation - athalia_core

## Vue d'ensemble

Ce guide explique comment utiliser athalia_core.

## Configuration

```yaml
name: athalia_core
version: 1.0.f(f
description: Projet athalia_core
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
  name: athalia_core
  debug: true
  port: 8000

database:
  url: sqlite:///app.db
  echo: false
```

## Fonctionnalités principales

### Classes principales

#### ProjectAuditor

Auditeur intelligent de projets générés.

**Exemple d'utilisation :**

```python
from athalia_core import ProjectAuditor

# Créer une instance
instance = ProjectAuditor()
# Utiliser une méthode
result = instance.__init__()
```

#### AIModel

Modèles IA disponibles.

**Exemple d'utilisation :**

```python
from athalia_core import AIModel

# Créer une instance
instance = AIModel()
```

#### PromptContext

Contextes de prompts.

**Exemple d'utilisation :**

```python
from athalia_core import PromptContext

# Créer une instance
instance = PromptContext()
```

### Fonctions utilitaires

#### generate_github_ci_yaml

**Exemple d'utilisation :**

```python
from athalia_core import generate_github_ci_yaml

result = generate_github_ci_yaml(outdir)
```

#### add_coverage_badge

**Exemple d'utilisation :**

```python
from athalia_core import add_coverage_badge

result = add_coverage_badge(outdir)
```

#### clean_old_tests_and_caches

Supprime les anciens fichiers de test non-suffixés et les caches Python dans le projet cible.
Log chaque suppression pour audit. Retourne la liste des fichiers supprimés.

**Exemple d'utilisation :**

```python
from athalia_core import clean_old_tests_and_caches

result = clean_old_tests_and_caches(outdir)
```

#### clean_macos_files

Supprime automatiquement les fichiers macOS parasites (.DS_Store, ._*) dans tout le projet. Retourne la liste des fichiers supprimés.

**Exemple d'utilisation :**

```python
from athalia_core import clean_macos_files

result = clean_macos_files(directory)
```

#### generate_blueprint_mock

**Exemple d'utilisation :**

```python
from athalia_core import generate_blueprint_mock

result = generate_blueprint_mock(idea)
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
*Généré automatiquement par Athalia* - 2025-07-19
