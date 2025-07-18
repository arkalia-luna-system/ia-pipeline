# Alias Athalia/Arkalia

Ce fichier documente tous les alias fournis dans `setup/alias.sh` pour accélérer le développement et l’utilisation du pipeline IA.

## Activation
Ajoutez dans votre `~/.bashrc` ou `~/.zshrc` :
```bash
source /chemin/vers/athalia-dev-setup/setup/alias.sh
```

## Alias disponibles

| Alias         | Action                                                                                   |
|---------------|-----------------------------------------------------------------------------------------|
| `ath-chat`    | Lance un shell IA (commande `continue`)                                                 |
| `ath-clean`   | Nettoie tous les caches Python, .DS_Store et logs dans le projet                        |
| `ath-dev-boost` | Menu interactif pour afficher des prompts IA utiles (debug, UX, audit, test, refactor) |
| `ath-perplex` | Ouvre Perplexity.ai dans le navigateur                                                  |
| `ath-test`    | Lance les tests via Taskfile (`task test`)                                              |
| `ath-lint`    | Lint le code via Taskfile (`task lint`)                                                 |
| `ath-build`   | Build le projet via Taskfile (`task build`)                                             |
| `ath-smart`   | Lance le prompt contextuel IA (agents/ath_context_prompt.py)                            |

> **Note** : L’alias `ath-new` est désactivé car le script `setup/ath-new.sh` est manquant. Pour ajouter un générateur de projet, créez ce script ou retirez l’alias.

## Exemples d’utilisation

- Nettoyer le projet :
  ```bash
  ath-clean
  ```
- Lancer le menu de prompts IA :
  ```bash
  ath-dev-boost
  ```
- Lancer les tests :
  ```bash
  ath-test
  ```
- Lancer le prompt contextuel IA :
  ```bash
  ath-smart
  ``` 