# 🎨 Système de Formatage Automatique Athalia

## Vue d'ensemble

Le système de formatage automatique Athalia résout le problème des hooks pre-commit qui modifient les fichiers sans les ajouter automatiquement au staging, créant ainsi un cycle infini de corrections.

## 🛠️ Outils disponibles

### 1. `./bin/ath-auto-format`
Script principal de formatage automatique.

**Options :**
- `--verbose, -v` : Affichage détaillé
- `--no-auto-add, -n` : Ne pas ajouter automatiquement les fichiers
- `--dry-run, -d` : Mode simulation
- `--help, -h` : Aide

**Exemples :**
```bash
# Formatage automatique complet
./bin/ath-auto-format

# Formatage avec affichage détaillé
./bin/ath-auto-format --verbose

# Formatage sans ajout automatique
./bin/ath-auto-format --no-auto-add
```

### 2. `./bin/ath-smart-commit`
Script de commit intelligent qui combine formatage + commit + push.

**Options :**
- `-m, --message TEXT` : Message de commit (obligatoire)
- `--push, -p` : Push automatique après commit
- `--verbose, -v` : Affichage détaillé
- `--dry-run, -d` : Mode simulation

**Exemples :**
```bash
# Commit simple
./bin/ath-smart-commit -m "feat: nouvelle fonctionnalité"

# Commit avec push automatique
./bin/ath-smart-commit -m "fix: correction bug" --push

# Simulation
./bin/ath-smart-commit -m "test" --dry-run
```

### 3. `./bin/ath-prepare-commit`
Script de préparation au commit avec options avancées.

**Options :**
- `--auto-fix, -a` : Correction automatique des problèmes
- `--skip-tests, -s` : Ignore les tests
- `--verbose, -v` : Affichage détaillé
- `--dry-run, -d` : Mode simulation

## 🔧 Configuration

### Hook pre-commit amélioré
Le hook pre-commit a été modifié pour :
1. Exécuter le formatage automatique avant les hooks standard
2. Ajouter automatiquement les fichiers modifiés
3. Continuer avec les hooks pre-commit standard
4. Ajouter automatiquement les fichiers modifiés par les hooks

### Configuration pre-commit
Le fichier `config/pre-commit-config.yaml` a été mis à jour avec :
- `require_serial: true` pour les hooks de formatage
- Ordre optimisé des hooks

## 📋 Workflow recommandé

### Workflow simple
```bash
# 1. Faire vos modifications
# 2. Formatage automatique
./bin/ath-auto-format

# 3. Commit intelligent
./bin/ath-smart-commit -m "votre message" --push
```

### Workflow avancé
```bash
# 1. Préparation complète
./bin/ath-prepare-commit --auto-fix

# 2. Tests
./bin/ath-test.py

# 3. Commit avec vérifications
./bin/ath-smart-commit -m "feat: fonctionnalité complète" --push
```

## 🚀 Avantages

### ✅ Résolution des problèmes
- **Plus de cycle infini** : Les fichiers modifiés sont automatiquement ajoutés
- **Formatage cohérent** : Black, isort, ruff appliqués dans le bon ordre
- **Hooks optimisés** : Configuration `require_serial: true` pour éviter les conflits

### ✅ Automatisation
- **Formatage automatique** : Plus besoin de corriger manuellement
- **Ajout automatique** : Les fichiers modifiés sont ajoutés au staging
- **Commit intelligent** : Une seule commande pour tout faire

### ✅ Flexibilité
- **Mode simulation** : Vérifier avant d'appliquer
- **Options multiples** : Différents niveaux de verbosité
- **Intégration Git** : Hooks pre-commit améliorés

## 🔍 Dépannage

### Problème : "Fichiers modifiés par le formatage"
**Solution :** Les fichiers sont automatiquement ajoutés au staging. Si le message persiste, utilisez :
```bash
git add .
```

### Problème : "Erreur lors du formatage automatique"
**Solution :** Vérifiez que les outils sont installés :
```bash
source .venv/bin/activate
pip install black isort ruff
```

### Problème : "Hook pre-commit échoue"
**Solution :** Le hook ajoute automatiquement les fichiers modifiés. Si le problème persiste :
```bash
git commit --no-verify -m "votre message"
```

## 📚 Commandes utiles

```bash
# Formatage manuel
black .
isort .
ruff format .
ruff check --fix

# Vérification du formatage
black . --check --diff
isort . --check-only --diff

# Nettoyage
./bin/ath-clean

# Tests
./bin/ath-test.py
```

## 🎯 Bonnes pratiques

1. **Utilisez le commit intelligent** : `./bin/ath-smart-commit` pour la plupart des cas
2. **Vérifiez avant de committer** : Utilisez `--dry-run` pour les modifications importantes
3. **Messages de commit clairs** : Utilisez des préfixes (feat:, fix:, docs:, etc.)
4. **Tests réguliers** : Exécutez `./bin/ath-test.py` après les modifications importantes

## 🔄 Migration depuis l'ancien système

Si vous utilisiez l'ancien workflow :

**Avant :**
```bash
git add .
git commit -m "message"  # Échouait souvent à cause du formatage
# Correction manuelle répétée...
```

**Maintenant :**
```bash
./bin/ath-smart-commit -m "message" --push
# Tout est automatique !
```

## 📞 Support

Pour toute question ou problème :
1. Vérifiez ce guide
2. Utilisez `--help` sur les scripts
3. Consultez les logs dans `logs/`
4. Exécutez `./bin/ath-clean` pour nettoyer
