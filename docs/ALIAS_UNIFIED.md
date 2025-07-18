# 🚀 Alias Athalia/Arkalia Unifiés - Guide Complet

## 📋 Vue d'ensemble

Ce guide documente le nouveau système d'alias unifié d'Athalia/Arkalia qui combine tous les alias du projet en une interface professionnelle et facile à utiliser.

## 🔄 Migration depuis l'ancien système

### Ancien système (déprécié)
- `setup/alias.sh` - Ancien système d'alias
- `setup/git-aliases.sh` - Alias Git séparés
- Tests dispersés dans plusieurs fichiers

### Nouveau système (recommandé)
- `setup/alias-unified.sh` - **Système unifié**
- Tests complets dans `tests/test_aliases_unified.py`
- Documentation centralisée

## 🚀 Installation

### 1. Activation automatique
Ajoutez dans votre `~/.bashrc` ou `~/.zshrc` :
```bash
# Athalia/Arkalia - Alias unifiés
source /chemin/vers/athalia-dev-setup/setup/alias-unified.sh
```

### 2. Activation manuelle
```bash
source setup/alias-unified.sh
```

## 📚 Catégories d'Alias

### 🔧 Git Workflow Professionnel
Alias pour un développement Git sécurisé et professionnel :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `gstart` | Démarrage journée (develop + pull) | `gstart` |
| `gfeature` | Nouvelle feature branch | `gfeature ma-nouvelle-feature` |
| `gcom` | Retour sur main | `gcom` |
| `gcod` | Retour sur develop | `gcod` |
| `gs` | Status Git | `gs` |
| `gl` | Log oneline | `gl` |
| `gla` | Log avec graphique | `gla` |
| `ga` | Add tous les fichiers | `ga` |
| `gc` | Commit avec message | `gc "feat: nouvelle fonctionnalité"` |
| `gp` | Push | `gp` |
| `gpu` | Push avec upstream | `gpu ma-branche` |

### 🧪 Tests et Qualité
Alias pour les tests et la qualité du code :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `ath-test` | Tests complets avec couverture | `ath-test` |
| `ath-test-unit` | Tests unitaires uniquement | `ath-test-unit` |
| `ath-test-integration` | Tests d'intégration | `ath-test-integration` |
| `ath-test-performance` | Tests de performance | `ath-test-performance` |
| `ath-lint` | Lint du code | `ath-lint` |
| `ath-coverage` | Couverture de tests | `ath-coverage` |
| `ath-coverage-html` | Couverture HTML | `ath-coverage-html` |

### 🎯 Core Features
Fonctionnalités principales du pipeline IA :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `ath-cli` | CLI principale | `ath-cli` |
| `ath-dashboard` | Dashboard interactif | `ath-dashboard` |
| `ath-smart` | Prompt contextuel IA | `ath-smart` |
| `ath-audit` | Audit intelligent | `ath-audit` |
| `ath-audit-intelligent` | Audit intelligent avancé | `ath-audit-intelligent` |
| `ath-security` | Audit de sécurité | `ath-security` |

### 🔧 Développement
Outils de développement et debugging :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `ath-clean` | Nettoyage projet | `ath-clean` |
| `ath-clean-all` | Nettoyage complet | `ath-clean-all` |
| `ath-dev-boost` | Menu prompts IA | `ath-dev-boost` |
| `ath-jupyter` | Notebook Jupyter | `ath-jupyter` |
| `ath-perplex` | Perplexity.ai | `ath-perplex` |

### 📚 Documentation
Gestion de la documentation :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `ath-doc` | Générer documentation | `ath-doc` |
| `ath-doc-open` | Ouvrir documentation | `ath-doc-open` |
| `ath-doc-api` | Documentation API | `ath-doc-api` |
| `ath-doc-guide` | Guide utilisateur | `ath-doc-guide` |

### 🔌 Plugins
Système de plugins extensible :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `ath-plugin-docker` | Plugin Docker | `ath-plugin-docker` |
| `ath-plugin-hello` | Plugin Hello | `ath-plugin-hello` |
| `ath-plugins-list` | Lister plugins | `ath-plugins-list` |

### 🐳 Docker et Déploiement
Gestion des conteneurs :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `ath-docker` | Docker compose up | `ath-docker` |
| `ath-docker-build` | Docker compose build | `ath-docker-build` |
| `ath-docker-down` | Docker compose down | `ath-docker-down` |

### 📊 Benchmark et Performance
Tests de performance :

| Alias | Description | Exemple |
|-------|-------------|---------|
| `ath-benchmark` | Benchmark distillation | `ath-benchmark` |
| `ath-benchmark-full` | Benchmark complet | `ath-benchmark-full` |

## 🚀 Workflow Athalia Automatisé

### Démarrage de journée
```bash
ath-start
# Équivalent à : git checkout develop && git pull origin develop
```

### Nouvelle fonctionnalité
```bash
ath-feature ma-nouvelle-feature
# Équivalent à : git checkout -b feature/ma-nouvelle-feature
```

### Développement
```bash
# Développer...
ath-test-unit  # Tester
ath-lint       # Linter
ath-commit "feat: description"  # Commiter
ath-push ma-nouvelle-feature   # Pousser
```

### Retour sur develop
```bash
ath-merge
# Équivalent à : git checkout develop && git pull origin develop
```

## 🛠️ Fonctions d'Aide

### `ath-help`
Affiche l'aide complète avec toutes les commandes disponibles :
```bash
ath-help
```

### `ath-status`
Affiche l'état du projet :
```bash
ath-status
```
Affiche :
- Répertoire racine
- Branche actuelle
- Nombre de tests
- Nombre de plugins
- Nombre de fichiers de documentation

### `ath-user-context`
Affiche un message de bienvenue personnalisé selon l'utilisateur.

## 🔄 Auto-complétion

### ZSH
```bash
ath-<TAB>  # Auto-complétion pour tous les alias ath-
ath-plugin-<TAB>  # Auto-complétion pour les plugins
```

### Bash
```bash
ath-<TAB>  # Auto-complétion pour tous les alias ath-
```

## 🚧 Alias à Implémenter

Certains alias sont des placeholders pour les fonctionnalités futures :

| Alias | Statut | Description |
|-------|--------|-------------|
| `ath-generate` | 🚧 À implémenter | Génération de projet |
| `ath-correct` | 🚧 À implémenter | Auto-correction |
| `ath-profile` | 🚧 À implémenter | Gestion de profils |
| `ath-scan` | 🚧 À implémenter | Scan de sécurité |
| `ath-test-prompts` | 🚧 À implémenter | Tests de prompts |
| `ath-export` | 🚧 À implémenter | Export de pipeline |
| `ath-mkdocs` | 🚧 À implémenter | Documentation MkDocs |

## 🧪 Tests

### Exécution des tests d'alias
```bash
# Tests du système unifié
pytest tests/test_aliases_unified.py -v

# Tests des anciens alias (pour compatibilité)
pytest tests/test_aliases.py -v
pytest tests/test_aliases_execution.py -v
```

### Couverture des tests
```bash
pytest tests/test_aliases_unified.py --cov=setup.alias-unified --cov-report=html
```

## 🔧 Configuration

### Variables d'environnement
- `ATHALIA_ROOT` : Répertoire racine du projet (auto-détecté)

### Personnalisation
Vous pouvez personnaliser les alias en modifiant `setup/alias-unified.sh` ou en créant votre propre fichier d'alias qui source le fichier principal.

## 📋 Migration depuis l'ancien système

### 1. Sauvegarder l'ancien système
```bash
cp setup/alias.sh setup/alias.sh.backup
```

### 2. Mettre à jour votre configuration
Dans votre `~/.bashrc` ou `~/.zshrc`, remplacer :
```bash
# Ancien
source /chemin/vers/athalia-dev-setup/setup/alias.sh

# Nouveau
source /chemin/vers/athalia-dev-setup/setup/alias-unified.sh
```

### 3. Tester la migration
```bash
source ~/.bashrc  # ou ~/.zshrc
ath-help  # Vérifier que tout fonctionne
ath-status  # Vérifier l'état
```

## 🎯 Bonnes Pratiques

### ✅ À faire
- Utiliser `ath-start` au début de chaque journée
- Créer des branches feature avec `ath-feature`
- Tester avant de commiter avec `ath-test-unit`
- Utiliser des messages de commit conventionnels
- Consulter `ath-help` régulièrement

### ❌ À éviter
- Travailler directement sur `main`
- Ignorer les tests avant commit
- Utiliser des messages de commit vagues
- Ne pas utiliser l'auto-complétion

## 🔍 Dépannage

### Problème : Alias non reconnus
```bash
# Vérifier que le fichier est sourcé
source setup/alias-unified.sh

# Vérifier la syntaxe
bash -n setup/alias-unified.sh
```

### Problème : ATHALIA_ROOT non défini
```bash
# Vérifier que vous êtes dans le bon répertoire
pwd
git rev-parse --show-toplevel
```

### Problème : Auto-complétion ne fonctionne pas
```bash
# Redémarrer le shell
exec zsh  # ou exec bash
```

## 📚 Ressources

- [Guide Git Workflow](docs/GIT_WORKFLOW.md)
- [Guide des Tests](docs/TESTS_GUIDE.md)
- [Documentation API](docs/API_REFERENCE.md)
- [Guide Utilisateur](docs/USER_GUIDE.md)

## 🤝 Contribution

Pour ajouter de nouveaux alias :

1. Modifier `setup/alias-unified.sh`
2. Ajouter les tests dans `tests/test_aliases_unified.py`
3. Mettre à jour cette documentation
4. Vérifier que tous les tests passent

## 📝 Changelog

### v2.0.0 - Système Unifié
- ✅ Fusion de tous les alias en un seul fichier
- ✅ Workflow Git professionnel intégré
- ✅ Tests complets et couverture
- ✅ Auto-complétion améliorée
- ✅ Documentation centralisée
- ✅ Fonctions d'aide contextuelles 