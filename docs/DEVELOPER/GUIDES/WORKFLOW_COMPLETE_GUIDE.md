# Guide du Workflow Complet Athalia

## Vue d'ensemble

Le système de workflow complet d'Athalia automatise tout le cycle de développement, de la fermeture propre à la reprise de travail. Il garantit un environnement de développement cohérent et propre.

## 🎯 Objectifs

### ✅ **Fermeture Propre**
- Commit automatique des changements
- Push vers GitHub
- Arrêt de tous les processus
- Nettoyage des fichiers temporaires
- Vérification des règles de qualité
- Génération de rapports

### ✅ **Démarrage Rapide**
- Vérification de l'environnement
- Chargement des alias
- Activation de l'environnement virtuel
- Vérification des dépendances
- Affichage des commandes disponibles

### ✅ **Workflow Automatisé**
- Cycle complet start → work → shutdown
- Vérifications automatiques
- Interactions guidées
- Rapports détaillés

## 🛠️ Scripts Disponibles

### Scripts Principaux

| Script | Fonction | Usage |
|--------|----------|-------|
| `ath-clean-shutdown` | Fermeture propre | `./bin/cleanup/ath-clean-shutdown` |
| `ath-quick-start` | Démarrage rapide | `./bin/core/ath-quick-start` |
| `ath-workflow-complete` | Workflow complet | `./bin/workflow/ath-workflow-complete [command]` |

### Alias Disponibles

| Alias | Commande | Description |
|-------|----------|-------------|
| `ath-shutdown` | Fermeture propre | Fermeture complète avec nettoyage |
| `ath-start` | Démarrage rapide | Démarrage de l'environnement |
| `ath-workflow` | Workflow complet | Gestion du cycle complet |
| `ath-close` | Alias fermeture | Alternative à ath-shutdown |
| `ath-quick` | Alias démarrage | Alternative à ath-start |
| `ath-flow` | Alias workflow | Alternative à ath-workflow |

## 📋 Workflow Recommandé

### Option 1: Workflow Simple

```bash
# 1. Démarrage
ath-start

# 2. Travail sur le projet
# ... votre travail ...

# 3. Fermeture
ath-shutdown
```

### Option 2: Workflow Complet

```bash
# Cycle complet automatisé
ath-workflow full
```

### Option 3: Workflow Modulaire

```bash
# 1. Démarrage
ath-workflow start

# 2. Préparation au travail
ath-workflow work

# 3. Travail sur le projet
# ... votre travail ...

# 4. Fermeture
ath-workflow shutdown
```

## 🔧 Installation et Configuration

### 1. Charger les Alias

```bash
# Charger tous les alias
source setup/alias-clean-shutdown.sh
```

### 2. Vérifier l'Installation

```bash
# Tester les commandes
ath-workflow help
```

### 3. Configuration Automatique

Les alias sont automatiquement chargés par :
- `ath-start`
- `ath-workflow start`
- `ath-workflow full`

## 📊 Fonctionnalités Détaillées

### Fermeture Propre (`ath-shutdown`)

#### Étapes Automatiques :
1. **Vérification Git**
   - Détection des changements
   - Commit automatique avec timestamp
   - Message de commit structuré

2. **Push vers GitHub**
   - Push vers la branche `develop`
   - Vérification du succès

3. **Arrêt des Processus**
   - Processus Python Athalia
   - Processus de test
   - Serveurs de développement

4. **Nettoyage**
   - Fichiers temporaires macOS
   - Caches Python
   - Fichiers temporaires généraux

5. **Vérifications de Qualité**
   - Documentation
   - Tests
   - Structure du projet

6. **Génération de Rapport**
   - Rapport détaillé avec timestamp
   - Statistiques de nettoyage
   - État final du projet

### Démarrage Rapide (`ath-start`)

#### Étapes Automatiques :
1. **Vérification de l'Environnement**
   - Python 3.x
   - Git
   - Outils système

2. **Vérification du Projet**
   - Branche Git
   - Changements non commités
   - État du dépôt

3. **Chargement des Alias**
   - Alias de workflow
   - Alias de fermeture
   - Commandes personnalisées

4. **Environnement Virtuel**
   - Détection de `.venv`
   - Activation automatique
   - Vérification des dépendances

5. **Vérifications Finales**
   - Tests disponibles
   - Documentation présente
   - Espace disque

### Workflow Complet (`ath-workflow`)

#### Commandes Disponibles :

| Commande | Description |
|----------|-------------|
| `start` | Démarrage rapide de l'environnement |
| `work` | Préparation au travail avec vérifications |
| `shutdown` | Fermeture propre complète |
| `full` | Cycle complet automatisé |
| `help` | Aide détaillée |

#### Mode Interactif (`work`) :
- Vérification de l'état Git
- Proposition de commit
- Exécution optionnelle des tests
- Vérification optionnelle du linting

## 📈 Rapports et Monitoring

### Rapports de Fermeture

Les rapports sont générés dans `./logs/shutdown_report_YYYYMMDD_HHMMSS.txt` :

```text
=== RAPPORT DE FERMETURE ATHALIA ===
Date: Wed Jul 30 18:20:06 CEST 2025
Projet: ia-pipeline
Branche: develop

=== ÉTAT GIT ===
0 fichiers modifiés
Dernier commit: efd0df7b 🧹 Nettoyage automatique

=== PROCESSUS ===
0 processus arrêtés
0 processus encore actifs

=== ESPACE DISQUE ===
Utilisation: 3%

=== FICHIERS TEMPORAIRES ===
2001 fichiers cachés
0 fichiers temporaires

=== DOCUMENTATION ===
README.md: ✅
Documentation développeur: ✅

=== TESTS ===
Fichiers de test: 281

=== RÉSUMÉ ===
Fermeture: ✅ Propre
```

### Statistiques en Temps Réel

- **Processus actifs** : Nombre de processus Athalia en cours
- **Espace disque** : Utilisation du disque en pourcentage
- **Tests disponibles** : Nombre de fichiers de test
- **Documentation** : État des fichiers de documentation

## 🔍 Dépannage

### Problèmes Courants

#### Erreur de Push
```bash
# Vérifier la connexion Git
git remote -v
git status

# Vérifier les permissions
ls -la .git/
```

#### Processus qui ne s'arrêtent pas
```bash
# Arrêt forcé
pkill -9 -f "athalia"

# Vérifier les processus
ps aux | grep athalia
```

#### Fichiers temporaires persistants
```bash
# Nettoyage manuel
./bin/cleanup/ath-clean-macos-temp --execute

# Vérification
find . -name ".*" -type f | wc -l
```

### Logs et Debugging

#### Fichiers de Log
- `./logs/shutdown_report_*.txt` - Rapports de fermeture
- `./logs/athalia.log` - Logs généraux d'Athalia
- `./logs/errors.log` - Logs d'erreurs

#### Mode Debug
```bash
# Activer le mode verbose
set -x
./bin/cleanup/ath-clean-shutdown
set +x
```

## 🚀 Intégration Avancée

### Personnalisation

#### Modifier les Variables
```bash
# Dans bin/cleanup/ath-clean-shutdown
PROJECT_NAME="votre-projet"
BRANCH="main"
REMOTE="origin"
```

#### Ajouter des Vérifications
```bash
# Ajouter dans la section "Vérifications de Qualité"
if [ -f "./votre-fichier-special" ]; then
    show_success "Fichier spécial présent"
else
    show_warning "Fichier spécial manquant"
fi
```

#### Personnaliser les Messages
```bash
# Modifier les messages de commit
COMMIT_MSG="🔄 Mise à jour automatique - $TIMESTAMP"
```

### Intégration CI/CD

#### Hook Pre-commit
```bash
#!/bin/bash
# .git/hooks/pre-commit
./bin/cleanup/ath-clean-shutdown --pre-commit
```

#### Hook Post-merge
```bash
#!/bin/bash
# .git/hooks/post-merge
./bin/core/ath-quick-start
```

## 📚 Bonnes Pratiques

### Avant de Commencer
1. **Utilisez toujours `ath-start`** au début de votre session
2. **Vérifiez l'état Git** avec `git status`
3. **Chargez les alias** avec `source setup/alias-clean-shutdown.sh`

### Pendant le Développement
1. **Commitez régulièrement** vos changements
2. **Testez fréquemment** avec `ath-test`
3. **Vérifiez la qualité** avec `ath-lint`
4. **Nettoyez périodiquement** avec `ath-clean-macos`

### Avant de Fermer
1. **Utilisez `ath-shutdown`** pour une fermeture propre
2. **Vérifiez le rapport** généré
3. **Confirmez le push** sur GitHub
4. **Sauvegardez les logs** importants

### Workflow Recommandé
```bash
# Session de développement typique
ath-workflow full

# Ou étape par étape
ath-start
# ... travail ...
ath-workflow work
# ... plus de travail ...
ath-shutdown
```

## 🎯 Avantages du Système

### ✅ **Cohérence**
- Environnement toujours propre
- Processus standardisés
- Rapports uniformes

### ✅ **Productivité**
- Automatisation des tâches répétitives
- Workflow optimisé
- Moins d'erreurs manuelles

### ✅ **Qualité**
- Vérifications automatiques
- Tests intégrés
- Documentation à jour

### ✅ **Traçabilité**
- Rapports détaillés
- Historique des actions
- Logs complets

## 🔮 Évolutions Futures

### Fonctionnalités Prévues
- **Mode batch** pour plusieurs projets
- **Intégration Docker** pour l'isolation
- **Synchronisation cloud** des rapports
- **Interface web** pour les rapports
- **Notifications** Slack/Email

### Améliorations Techniques
- **Parallélisation** des tâches
- **Cache intelligent** des vérifications
- **Récupération automatique** d'erreurs
- **Profils utilisateur** personnalisés

## 📞 Support

### Documentation
- `CLEAN_SHUTDOWN_GUIDE.md` - Guide de fermeture
- `../MAINTENANCE/MACOS_TEMP_CLEANUP.md` - Nettoyage macOS
- `../INDEX.md` - Index complet

### Commandes d'Aide
```bash
ath-workflow help      # Aide du workflow
ath-help              # Aide générale
./bin/cleanup/ath-clean-shutdown --help  # Aide fermeture
```

### Logs et Debugging
```bash
# Voir les derniers rapports
ls -la ./logs/shutdown_report_*.txt | tail -5

# Analyser les erreurs
tail -f ./logs/errors.log
```

---

**💡 Conseil Final : Utilisez `ath-workflow full` pour un workflow complètement automatisé !**
