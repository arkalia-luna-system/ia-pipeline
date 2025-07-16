<<<<<<< HEAD
# ia-pipeline
Générateur IA souverain, modulaire, testé, automatisé, documenté
=======
# Athalia Pipeline IA – Générateur Souverain

## Architecture
- **athalia_core/** : modules (génération, nettoyage, CI, dashboard, onboarding, sécurité)
- **tests/** : tests unitaires et d’intégration pour chaque module
- **Taskfile.yaml** : automatisation (build, test, lint, clean, export, audit)
- **.gitignore** : repo toujours propre

## Utilisation rapide
1. **Lancer le menu CLI** :
   ```bash
   python3 -m athalia_core.main
   ```
2. **Automatiser** (nécessite Task) :
   ```bash
   task build   # Générer un projet IA
   task test    # Lancer tous les tests
   task clean   # Nettoyer tous les artefacts
   task audit   # Audit sécurité sur tous les projets
   ```

## Fonctionnalités principales
- Génération automatique de projets IA modulaires, prompts, scripts, tests, docs, CI, dashboard, tickets, guides, export
- Nettoyage automatique des tests/caches/artefacts
- Audit sécurité (scan de secrets, patterns à risque)
- Orchestration CLI interactive (génération, nettoyage, CI, dashboard, onboarding, audit…)
- Tests unitaires et d’intégration pour chaque brique
- Logs détaillés pour chaque action critique
- Export pipeline complet (tar.gz)

## Tests
- Tous les modules sont testés (pytest)
- Lancer :
  ```bash
  pytest tests/
  ```

## Sécurité
- Audit automatique des patterns à risque (clé API, mot de passe, shell, etc.)
- Résultats dans `security_audit.log` de chaque projet

## Nettoyage
- Tous les fichiers inutiles/caches sont ignorés ou supprimés automatiquement

## Export
- `task export` pour packager tout le pipeline

## Pour aller plus loin
- Ajouter vos propres prompts, modules, plugins dans `athalia_core/`
- Étendre le menu CLI selon vos besoins
- Contribuer, forker, industrialiser !
>>>>>>> 16d74de (Import complet du pipeline IA, code, tests, doc, automation)
