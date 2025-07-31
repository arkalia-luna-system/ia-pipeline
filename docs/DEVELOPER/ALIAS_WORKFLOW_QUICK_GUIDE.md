# 🚀 Guide Rapide - Alias de Workflow Athalia

## 📋 Installation

### Installation automatique
```bash
# Depuis la racine du projet
./setup/install-workflow-aliases.sh
```

### Installation manuelle
```bash
# Ajouter à votre .bashrc ou .zshrc
source "$(pwd)/setup/athalia-workflow-aliases.sh"
```

## ⚡ Utilisation Rapide

### Développement quotidien
```bash
# Workflow rapide (tout automatique)
ath-quick

# Ou étape par étape
ath-prepare-fix    # Préparation avec corrections
git add .
git commit -m "feat: nouvelle fonctionnalité"
ath-push-smart     # Push avec vérifications
```

### Nouvelle feature
```bash
# Créer une branche feature
git checkout -b feature/ma-nouvelle-feature

# Développement avec workflow complet
ath-feature-full

# Ou manuellement
ath-prepare-fix
git add .
git commit -m "feat: ma nouvelle feature"
ath-push-smart --branch feature/ma-nouvelle-feature
```

### Release
```bash
# Basculer sur main
git checkout main

# Workflow de release complet
ath-release-full

# Ou manuellement
ath-prepare-fix
git add .
git commit -m "release: v1.2.3"
ath-push-smart
```

## 🎯 Alias Disponibles

### Préparation au commit
| Alias | Description | Usage |
|-------|-------------|-------|
| `ath-prepare` | Préparation basique | `ath-prepare` |
| `ath-prepare-fix` | Préparation + corrections auto | `ath-prepare-fix` |
| `ath-prepare-dry` | Préparation en simulation | `ath-prepare-dry` |

### Push intelligent
| Alias | Description | Usage |
|-------|-------------|-------|
| `ath-push-smart` | Push avec vérifications | `ath-push-smart` |
| `ath-push-dry` | Push en simulation | `ath-push-dry` |
| `ath-push-force` | Push forcé | `ath-push-force` |

### Workflow complet
| Alias | Description | Usage |
|-------|-------------|-------|
| `ath-dev` | Workflow développement | `ath-dev` |
| `ath-feature` | Workflow feature | `ath-feature` |
| `ath-hotfix` | Workflow hotfix | `ath-hotfix` |
| `ath-release` | Workflow release | `ath-release` |

### Workflow rapide
| Alias | Description | Usage |
|-------|-------------|-------|
| `ath-quick` | Développement quotidien | `ath-quick` |
| `ath-dev-auto` | Dev + commit auto | `ath-dev-auto` |
| `ath-dev-push` | Dev + commit + push auto | `ath-dev-push` |
| `ath-feature-full` | Feature complète | `ath-feature-full` |
| `ath-release-full` | Release complète | `ath-release-full` |

## 🔧 Options Avancées

### Mode simulation
```bash
# Tous les outils supportent --dry-run
ath-prepare --dry-run
ath-push-smart --dry-run
ath-workflow --mode develop --dry-run
```

### Mode verbose
```bash
# Affichage détaillé
ath-prepare --verbose
ath-workflow --mode feature --verbose
```

### Mode force
```bash
# Ignorer les erreurs
ath-push-smart --force
ath-workflow --mode release --force
```

## 📊 Exemples Concrets

### Scénario 1 : Développement quotidien
```bash
# 1. Démarrer la journée
ath-start

# 2. Développer
# ... votre code ...

# 3. Préparer le commit
ath-prepare-fix

# 4. Commiter
git add .
git commit -m "feat: amélioration de la fonction X"

# 5. Pousser
ath-push-smart
```

### Scénario 2 : Nouvelle feature
```bash
# 1. Créer la branche
git checkout -b feature/nouvelle-fonction

# 2. Développer
# ... votre code ...

# 3. Workflow complet
ath-feature-full

# 4. Créer la Pull Request sur GitHub
```

### Scénario 3 : Hotfix urgent
```bash
# 1. Créer la branche hotfix
git checkout -b hotfix/correction-urgente

# 2. Corriger
# ... votre correction ...

# 3. Workflow rapide
ath-hotfix --auto-commit --auto-push

# 4. Merge sur main et develop
```

## 🚨 Gestion des Erreurs

### Erreurs courantes
```bash
# Fichiers polluants détectés
ath-prepare-fix  # Correction automatique

# Tests qui échouent
ath-prepare --skip-tests  # Ignorer les tests

# Problèmes de linting
ath-prepare-fix  # Correction automatique

# Push refusé
ath-push-force  # Forcer le push
```

### Mode debug
```bash
# Affichage détaillé
ath-prepare --verbose
ath-push-smart --verbose
ath-workflow --mode develop --verbose
```

## 💡 Conseils d'Utilisation

### Workflow recommandé
1. **Développement quotidien** : `ath-quick`
2. **Nouvelles features** : `ath-feature-full`
3. **Corrections urgentes** : `ath-hotfix --auto-commit --auto-push`
4. **Releases** : `ath-release-full`

### Bonnes pratiques
- Utilisez `ath-prepare-fix` avant chaque commit
- Utilisez `ath-push-smart` avant chaque push
- Utilisez les modes `--dry-run` pour tester
- Consultez `ath-workflow-help` pour l'aide

### Intégration avec Git
```bash
# Hook pré-commit automatique (déjà installé)
git commit -m "votre message"  # Vérifications automatiques

# Ignorer les vérifications si nécessaire
git commit --no-verify -m "message urgent"
```

## 🔗 Liens Utiles

- **Documentation complète** : `docs/DEVELOPER/WORKFLOW_AMELIORATIONS.md`
- **Aide en ligne** : `ath-workflow-help`
- **Configuration** : `setup/athalia-workflow-aliases.sh`

## 🆘 Support

### Problèmes courants
1. **Alias non reconnus** : Redémarrez le terminal ou `source ~/.bashrc`
2. **Scripts manquants** : Vérifiez que tous les scripts sont présents dans `bin/`
3. **Permissions** : `chmod +x bin/ath-*`

### Debug
```bash
# Vérifier l'installation
ls -la bin/ath-prepare-commit bin/ath-push bin/ath-workflow

# Tester les alias
type ath-prepare
type ath-push-smart
type ath-quick

# Vérifier la configuration
cat setup/athalia-workflow-aliases.sh
```

---

**💡 Astuce** : Tapez `ath-` puis `Tab` pour l'auto-complétion de tous les alias disponibles !
