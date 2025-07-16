# Architecture

- **athalia_core/** : modules (génération, nettoyage, CI, dashboard, onboarding, sécurité)
- **tests/** : tests unitaires et d’intégration
- **Taskfile.yaml** : automatisation
- **.gitignore** : workspace propre
- **docs-tech/** : documentation technique (mkdocs)

Chaque module est indépendant, testé, loggé, et extensible. 