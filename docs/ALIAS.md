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
| `ath-lint`    | Lint le code du projet via script Python dédié (bin/ath-lint.py) |
| `ath-build`   | Build le projet via script Python dédié (bin/ath-build.py) |
| `ath-smart`   | Lance le prompt contextuel IA (agents/ath_context_prompt.py)                            |
| `ath-dashboard` | Ouvre le dashboard interactif dans le navigateur |
| `ath-cli`       | Lance la CLI principale Athalia/Arkalia         |
| `ath-cleanup`   | Nettoyage avancé (script cleanup_workspace.py)  |
| `ath-doc`       | Génère la documentation (Taskfile)              |
| `ath-code`      | Ouvre le projet dans VS Code                    |
| `ath-pip`       | Met à jour les dépendances Python               |
| `ath-docker`    | Lance le serveur Docker (docker compose up)     |
| `ath-coverage`  | Vérifie la couverture de tests                  |
| `ath-jupyter`   | Lance un notebook Jupyter                      |
| `ath-dashboard-py` | Lance le dashboard web en Python |
| `ath-cli-main` | Lance la CLI principale Athalia/Arkalia |
| `ath-unified` | Lance la CLI unifiée (athalia_unified.py) |
| `ath-audit`           | Audit intelligent via script Python dédié (bin/ath-audit.py) |
| `ath-generate` | Génère un nouveau projet IA (script à implémenter) |
| `ath-correct` | Auto-correction avancée d’un projet (script à implémenter) |
| `ath-profile` | Gestion des profils utilisateur (script à implémenter) |
| `ath-scan` | Scan de sécurité ou de projets (script à implémenter) |
| `ath-test-prompts` | Lance les tests prompts (script à implémenter) |
| `ath-benchmark` | Lance le benchmark de distillation (script à implémenter) |
| `ath-export` | Exporte le pipeline complet (script à implémenter) |
| `ath-mkdocs` | Lance le serveur de documentation locale (script à implémenter) |

> **Note** : L’alias `ath-new` est désactivé car le script `setup/ath-new.sh` est manquant. Pour ajouter un générateur de projet, créez ce script ou retirez l’alias.

## Alias avancés / modules / plugins / outils

| Alias                 | Action                                                                 |
|-----------------------|------------------------------------------------------------------------|
| `ath-auto-correct`    | Lance le module d’auto-correction avancée                              |
| `ath-dashboard-unified` | Lance le dashboard unifié avancé                                      |
| `ath-profile-advanced` | Lance le module de profils utilisateur avancés                        |
| `ath-plugin-docker`   | Lance le plugin d’export Docker                                        |
| `ath-plugin-hello`    | Lance le plugin hello                                                  |
| `ath-test-ci`         | Lance le test CI manuel                                                |
| `ath-test-final`      | Lance le test final complet                                            |
| `ath-test-dashboard`  | Lance le test du dashboard unifié                                      |
| `ath-benchmark-full`  | Lance le benchmark de distillation complet                             |
| `ath-doc-open`        | Ouvre la documentation principale locale                               |
| `ath-prompts`         | Ouvre le dossier des prompts                                           |
| `ath-config`          | Ouvre le fichier de configuration principal                            |
| `ath-plugins-list`    | Liste tous les plugins disponibles                                     |
| `ath-notebook`        | Lance un notebook Jupyter                                              |
| `ath-profile`         | Lance un profiling Python (cProfile)                                   |
| `ath-coverage-html`   | Ouvre le rapport de couverture HTML                                    |
| `ath-final-report`    | Ouvre le rapport final du projet                                       |
| `ath-dashboard-full`  | Ouvre le dashboard analytics complet                                   |

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
- Ouvrir le dashboard interactif :
  ```bash
  ath-dashboard
  ```
- Lancer la CLI principale :
  ```bash
  ath-cli
  ```
- Nettoyage avancé :
  ```bash
  ath-cleanup
  ```
- Générer la documentation :
  ```bash
  ath-doc
  ```
- Ouvrir dans VS Code :
  ```bash
  ath-code
  ```
- Mettre à jour les dépendances :
  ```bash
  ath-pip
  ```
- Lancer Docker :
  ```bash
  ath-docker
  ```
- Vérifier la couverture de tests :
  ```bash
  ath-coverage
  ```
- Lancer Jupyter :
  ```bash
  ath-jupyter
  ``` 
- Lancer le dashboard Python :
  ```bash
  ath-dashboard-py
  ```
- Lancer la CLI principale :
  ```bash
  ath-cli-main
  ```
- Lancer la CLI unifiée :
  ```bash
  ath-unified
  ```
- Audit intelligent :
  ```bash
  ath-audit
  ```
- Générer un projet IA :
  ```bash
  ath-generate
  ```
- Correction avancée :
  ```bash
  ath-correct
  ```
- Gestion des profils :
  ```bash
  ath-profile
  ```
- Scan de sécurité/projets :
  ```bash
  ath-scan
  ```
- Tests prompts :
  ```bash
  ath-test-prompts
  ```
- Benchmark :
  ```bash
  ath-benchmark
  ```
- Export pipeline :
  ```bash
  ath-export
  ```
- Documentation locale :
  ```bash
  ath-mkdocs
  ``` 

## Exemples d’utilisation avancée

- Lancer le module d’auto-correction avancée :
  ```bash
  ath-auto-correct
  ```
- Lancer le dashboard unifié :
  ```bash
  ath-dashboard-unified
  ```
- Lancer le module de profils utilisateur avancés :
  ```bash
  ath-profile-advanced
  ```
- Lancer le plugin Docker :
  ```bash
  ath-plugin-docker
  ```
- Lancer le test CI manuel :
  ```bash
  ath-test-ci
  ```
- Ouvrir la documentation locale :
  ```bash
  ath-doc-open
  ```
- Ouvrir le dossier des prompts :
  ```bash
  ath-prompts
  ```
- Ouvrir la config principale :
  ```bash
  ath-config
  ```
- Lister les plugins :
  ```bash
  ath-plugins-list
  ```
- Lancer un notebook Jupyter :
  ```bash
  ath-notebook
  ```
- Profiling Python :
  ```bash
  ath-profile
  ```
- Ouvrir le rapport de couverture :
  ```bash
  ath-coverage-html
  ```
- Ouvrir le rapport final :
  ```bash
  ath-final-report
  ```
- Ouvrir le dashboard analytics complet :
  ```bash
  ath-dashboard-full
  ``` 

## Fonctionnalités avancées

### Auto-complétion intelligente
- Tapez `ath-` puis Tab pour voir tous les alias disponibles (zsh et bash).
- L’auto-complétion est activée automatiquement si vous sourcez `setup/alias.sh` dans votre shell.

### Alias magique : aide dynamique
- Utilisez la commande `ath-help` pour afficher dynamiquement la liste de tous les alias disponibles, avec leur description extraite de cette documentation.
- Exemple :
  ```bash
  ath-help
  ```

### Alias contextuels (préparation)
- Il est possible d’ajouter des alias qui s’adaptent au contexte du dossier courant (ex : projet principal, module, plugin, etc.).
- Voir la fonction `ath-context` dans `setup/alias.sh` pour un exemple de base à personnaliser.

### Auto-complétion intelligente pour les plugins
- Tapez `ath-plugin-` puis Tab pour voir tous les plugins disponibles (auto-détection des fichiers *_plugin.py dans plugins/).
- L’auto-complétion fonctionne sous zsh et bash si vous sourcez `setup/alias.sh`.

### Alias dynamique selon l’utilisateur courant
- Utilisez la commande `ath-user-context` pour afficher un message ou activer des alias spécifiques selon votre nom d’utilisateur (admin, dev, etc.).
- Exemple :
  ```bash
  ath-user-context
  ```
- Personnalisez la fonction dans `setup/alias.sh` pour adapter les alias à votre workflow ou à votre rôle.

## Couverture de test des alias

- Tous les alias sont testés automatiquement pour leur présence et leur exécution (exit code 0) via `tests/test_aliases.py` et `tests/test_aliases_execution.py`.
- Les alias interactifs ou ouvrant des fichiers/GUI sont ignorés dans le test d’exécution.
- Les alias à implémenter sont listés explicitement et signalés dans la doc.
- Cela garantit la robustesse, la maintenabilité et la fiabilité de l’outillage shell Athalia/Arkalia.

--- 