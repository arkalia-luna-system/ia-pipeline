# Utilisation rapide

## Prompts centralisés

Tous les prompts Markdown utilisés pour l’audit, la génération ou l’amélioration (tests, design, sécurité, UX/fun) sont désormais centralisés dans le dossier `prompts_central/`.

- Pour ajouter ou modifier un prompt, édite simplement le fichier correspondant dans ce dossier.
- Chaque prompt contient une date/version et un exemple d’utilisation.
- Les agents et scripts du pipeline utilisent ces prompts pour guider l’IA ou automatiser les audits.

---

## Lancer le menu CLI
```bash
python3 -m athalia_core.main
```

## Automatiser (Task)
```bash
task build   # Générer un projet IA
task test    # Lancer tous les tests
task clean   # Nettoyer tous les artefacts
task audit   # Audit sécurité sur tous les projets
```

## Tests
```bash
pytest tests/
```

## Export
```bash
task export
``` 