# Guide de Fermeture Propre d'Athalia

**Dernière mise à jour :** 20 Août 2025  
**Version :** v12.0.0  
**Statut :** ✅ ACTIF ET MAINTENU

## Vue d'ensemble

Le script `ath-clean-shutdown` automatise le processus de fermeture propre d'Athalia en une seule commande. Il garantit que votre projet est dans un état propre avant de fermer votre session de développement.

## Fonctionnalités

### 🔄 **Gestion Git Automatique**
- ✅ Vérification de l'état du dépôt
- ✅ Commit automatique des changements
- ✅ Push vers la branche `develop`
- ✅ Messages de commit avec timestamp

### 🛑 **Arrêt des Processus**
- ✅ Arrêt des processus Python Athalia
- ✅ Arrêt des processus de test
- ✅ Arrêt des serveurs de développement
- ✅ Vérification qu'aucun processus ne reste actif

### 🧹 **Nettoyage Automatique**
- ✅ Suppression des fichiers temporaires macOS
- ✅ Nettoyage des caches Python (`__pycache__`, `.pyc`)
- ✅ Suppression des fichiers temporaires (`.tmp`, `.temp`)
- ✅ Nettoyage des logs orphelins

### 📋 **Vérification de Qualité**
- ✅ Vérification de la documentation
- ✅ Vérification de la présence des tests
- ✅ Vérification de la structure du projet
- ✅ Contrôle de l'espace disque

### 📊 **Rapport de Fermeture**
- ✅ Génération d'un rapport détaillé
- ✅ Statistiques de nettoyage
- ✅ État final du projet
- ✅ Horodatage de la fermeture

## Utilisation

### Installation des Alias

```bash
# Charger les alias
source setup/alias-clean-shutdown.sh
```

### Commandes Disponibles

```bash
# Fermeture propre complète
ath-shutdown

# Alias alternatifs
ath-close
ath-exit
ath-bye

# Ou directement
./bin/cleanup/ath-clean-shutdown
```

## Étapes du Script

### 1. **Vérification Git**
```bash
git status --porcelain
git add .
git commit -m "🧹 Nettoyage automatique - TIMESTAMP"
```

### 2. **Push vers GitHub**
```bash
git push origin develop
```

### 3. **Arrêt des Processus**
```bash
# Arrêt des processus Athalia
pgrep -f "athalia\|ath-" | xargs kill -TERM

# Arrêt des tests
pgrep -f "pytest.*athalia" | xargs kill -TERM

# Arrêt des serveurs
pgrep -f "python.*server\|uvicorn\|flask" | xargs kill -TERM
```

### 4. **Nettoyage macOS**
```bash
./bin/cleanup/ath-clean-macos-temp --execute
```

### 5. **Nettoyage Python**
```bash
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete
```

### 6. **Nettoyage Général**
```bash
find . -name "*.tmp" -delete
find . -name "*.temp" -delete
find . -name "*.log" -not -path "./logs/*" -delete
```

### 7. **Vérifications de Qualité**
- Présence de `README.md`
- Présence de `../INDEX.md`
- Présence de fichiers de test
- Structure du projet correcte

### 8. **Génération du Rapport**
Le rapport est sauvegardé dans `./logs/shutdown_report_YYYYMMDD_HHMMSS.txt`

## Exemple de Sortie

```
🚀 Démarrage de la fermeture propre d'Athalia
📂 Projet: ia-pipeline
🌿 Branche: develop

▶️  1. Vérification de l'état Git
✅ Commit créé avec succès

▶️  2. Push vers GitHub
✅ Code poussé vers origin/develop

▶️  3. Arrêt des processus Athalia
✅ 3 processus arrêtés

▶️  4. Nettoyage des fichiers temporaires macOS
✅ Fichiers temporaires macOS nettoyés

▶️  5. Nettoyage des caches Python
✅ Caches Python nettoyés

▶️  6. Nettoyage des fichiers temporaires
✅ Fichiers temporaires nettoyés

▶️  7. Vérification des règles de qualité
✅ Documentation principale présente
✅ Tests présents
✅ Structure du projet correcte

▶️  8. Vérification de l'état final
✅ Aucun processus Athalia en cours
✅ Espace disque suffisant (45%)

▶️  9. Génération du rapport de fermeture
✅ Rapport généré: ./logs/shutdown_report_20250730_181500.txt

🎉 FERMETURE TERMINÉE
===================
✅ Code poussé vers GitHub
✅ Processus arrêtés
✅ Fichiers temporaires nettoyés
✅ Règles de qualité vérifiées
✅ Rapport généré

📊 Statistiques:
   - Processus arrêtés: 3
   - Espace disque: 45%
   - Rapport: ./logs/shutdown_report_20250730_181500.txt

💡 Conseil: Vérifiez le rapport pour plus de détails
```

## Rapport de Fermeture

Le rapport contient :

```text
=== RAPPORT DE FERMETURE ATHALIA ===
Date: Wed Jul 30 18:15:00 CEST 2025
Projet: ia-pipeline
Branche: develop

=== ÉTAT GIT ===
0 fichiers modifiés
Dernier commit: abc1234 🧹 Nettoyage automatique

=== PROCESSUS ===
3 processus arrêtés
0 processus encore actifs

=== ESPACE DISQUE ===
Utilisation: 45%

=== FICHIERS TEMPORAIRES ===
12 fichiers cachés
0 fichiers temporaires

=== DOCUMENTATION ===
README.md: ✅
Documentation développeur: ✅

=== TESTS ===
Fichiers de test: 1774

=== RÉSUMÉ ===
Fermeture: ✅ Propre
```

## Configuration

### Variables Modifiables

Dans le script `bin/cleanup/ath-clean-shutdown` :

```bash
PROJECT_NAME="ia-pipeline"  # Nom du projet
BRANCH="develop"                  # Branche par défaut
REMOTE="origin"                   # Remote Git
```

### Personnalisation

Vous pouvez modifier le script pour :

- Ajouter des vérifications personnalisées
- Modifier les patterns de processus à arrêter
- Ajouter des nettoyages spécifiques
- Personnaliser le format du rapport

## Intégration avec le Workflow

### Avant de Fermer

1. **Sauvegardez votre travail** : Le script fait automatiquement un commit
2. **Vérifiez les changements** : Le script affiche l'état Git
3. **Arrêtez les processus** : Le script arrête tous les processus Athalia
4. **Nettoyez l'environnement** : Le script nettoie tous les fichiers temporaires

### Après la Fermeture

1. **Consultez le rapport** : Vérifiez `./logs/shutdown_report_*.txt`
2. **Vérifiez GitHub** : Confirmez que le push a réussi
3. **Redémarrez proprement** : Utilisez `ath-start` pour redémarrer

## Dépannage

### Erreurs Courantes

**Erreur de push :**
```bash
# Vérifiez votre connexion Git
git remote -v
git status
```

**Processus qui ne s'arrêtent pas :**
```bash
# Arrêt forcé
pkill -9 -f "athalia"
```

**Fichiers temporaires persistants :**
```bash
# Nettoyage manuel
./bin/cleanup/ath-clean-macos-temp --execute
```

### Logs

Les logs sont disponibles dans :
- `./logs/shutdown_report_*.txt` - Rapports de fermeture
- `./logs/athalia.log` - Logs généraux d'Athalia

## Bonnes Pratiques

1. **Utilisez toujours le script** avant de fermer votre session
2. **Vérifiez le rapport** après chaque fermeture
3. **Gardez votre branche à jour** avec `develop`
4. **Nettoyez régulièrement** même sans fermer
5. **Documentez les problèmes** dans les logs

## Support

Pour des problèmes ou suggestions :
1. Consultez les logs dans `./logs/`
2. Vérifiez la documentation dans `./docs/`
3. Utilisez `ath-help` pour l'aide générale
