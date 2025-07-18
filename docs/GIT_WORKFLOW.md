# 🚀 Workflow Git Professionnel - Athalia

## 📋 Vue d'ensemble

Ce guide décrit le workflow Git professionnel pour le projet Athalia, basé sur le modèle **Git Flow** adapté pour un projet IA/ML.

## 🌿 Structure des Branches

### Branches Principales
- **`main`** : Code stable, prêt pour la production
- **`develop`** : Branche de développement, intégration des features
- **`gh-pages`** : Documentation et dashboard (GitHub Pages)

### Branches de Travail
- **`feature/nom-feature`** : Nouvelles fonctionnalités
- **`hotfix/nom-fix`** : Corrections urgentes
- **`release/v1.x.x`** : Préparation des releases

## 🔄 Workflow Quotidien

### 1. Démarrage de la journée
```bash
# Basculer sur develop
git checkout develop

# Récupérer les dernières modifications
git pull origin develop

# Vérifier l'état
git status
```

### 2. Créer une branche pour une nouvelle fonctionnalité
```bash
# Créer et basculer sur une branche feature
git checkout -b feature/nouvelle-fonctionnalite

# Ou pour un hotfix
git checkout -b hotfix/correction-urgente
```

### 3. Développement
```bash
# Faire tes modifications
# ... code ...

# Vérifier les changements
git status
git diff

# Ajouter les fichiers
git add .

# Commiter avec un message descriptif
git commit -m "feat: ajout de la nouvelle fonctionnalité X

- Description détaillée
- Tests ajoutés
- Documentation mise à jour"
```

### 4. Pousser la branche
```bash
# Pousser la branche vers GitHub
git push -u origin feature/nouvelle-fonctionnalite
```

### 5. Créer une Pull Request
- Aller sur GitHub
- Créer une Pull Request de `feature/nouvelle-fonctionnalite` vers `develop`
- Ajouter une description détaillée
- Assigner des reviewers si nécessaire

### 6. Merge et nettoyage
```bash
# Une fois la PR approuvée et mergée
git checkout develop
git pull origin develop

# Supprimer la branche locale
git branch -d feature/nouvelle-fonctionnalite

# Supprimer la branche distante
git push origin --delete feature/nouvelle-fonctionnalite
```

## 🏷️ Convention de Nommage

### Branches
- `feature/nom-descriptive` : Nouvelles fonctionnalités
- `hotfix/nom-descriptive` : Corrections urgentes
- `release/v1.2.3` : Préparation de release
- `docs/nom-descriptive` : Documentation

### Commits
Format : `type(scope): description`

Types :
- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage, point-virgules manquants, etc.
- `refactor` : Refactoring de code
- `test` : Ajout ou modification de tests
- `chore` : Tâches de maintenance

Exemples :
```bash
git commit -m "feat(analytics): ajout de nouveaux métriques de performance"
git commit -m "fix(ci): correction des tests unitaires"
git commit -m "docs(api): mise à jour de la documentation"
```

## 🚀 Processus de Release

### 1. Préparation de Release
```bash
# Créer une branche release
git checkout -b release/v1.2.0 develop

# Faire les ajustements finaux
# - Mettre à jour les versions
# - Corriger les derniers bugs
# - Mettre à jour la documentation

# Commiter les changements
git commit -m "chore(release): préparation v1.2.0"
```

### 2. Merge vers main et develop
```bash
# Merge vers main
git checkout main
git merge release/v1.2.0

# Tagger la release
git tag -a v1.2.0 -m "Release v1.2.0"

# Merge vers develop
git checkout develop
git merge release/v1.2.0

# Pousser tout
git push origin main develop
git push origin v1.2.0

# Supprimer la branche release
git branch -d release/v1.2.0
git push origin --delete release/v1.2.0
```

## 🔧 Commandes Utiles

### Gestion des branches
```bash
# Lister toutes les branches
git branch -a

# Voir les branches mergées
git branch --merged

# Voir les branches non mergées
git branch --no-merged

# Supprimer une branche locale
git branch -d nom-branche

# Supprimer une branche distante
git push origin --delete nom-branche
```

### Gestion des commits
```bash
# Voir l'historique avec graphique
git log --oneline --graph --all

# Voir les derniers commits
git log --oneline -10

# Annuler le dernier commit (garder les changements)
git reset --soft HEAD~1

# Annuler le dernier commit (perdre les changements)
git reset --hard HEAD~1
```

### Gestion des conflits
```bash
# Voir les fichiers en conflit
git status

# Résoudre les conflits manuellement
# Puis ajouter les fichiers résolus
git add .

# Continuer le merge
git commit
```

## 🛡️ Bonnes Pratiques

### ✅ À faire
- Toujours travailler sur une branche feature
- Faire des commits fréquents et descriptifs
- Tester avant de pousser
- Créer des Pull Requests pour review
- Maintenir `main` stable
- Documenter les changements majeurs

### ❌ À éviter
- Travailler directement sur `main`
- Commits trop gros
- Messages de commit vagues
- Pousser du code non testé
- Ignorer les conflits

## 🎯 Workflow Recommandé pour Athalia

### Développement quotidien
1. **Début de journée** : `git checkout develop && git pull`
2. **Nouvelle feature** : `git checkout -b feature/nom-feature`
3. **Développement** : commits fréquents et descriptifs
4. **Tests** : `pytest tests/` avant push
5. **Push** : `git push -u origin feature/nom-feature`
6. **PR** : Créer Pull Request sur GitHub
7. **Review** : Attendre approbation
8. **Merge** : Merge vers `develop`
9. **Nettoyage** : Supprimer la branche

### Release mensuelle
1. **Créer release branch** : `git checkout -b release/v1.x.x develop`
2. **Finaliser** : Tests, docs, version
3. **Merge main** : `git checkout main && git merge release/v1.x.x`
4. **Tag** : `git tag -a v1.x.x -m "Release v1.x.x"`
5. **Merge develop** : `git checkout develop && git merge release/v1.x.x`
6. **Push** : Pousser tout vers GitHub

## 📚 Ressources

- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) 