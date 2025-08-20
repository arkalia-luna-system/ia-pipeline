# 🧹 Guide de Nettoyage du Projet Athalia

**Dernière mise à jour :** 14 Août 2025  
**Version :** v2.0  
**Statut :** ✅ ACTIF ET MAINTENU - SYSTÈME AUTOMATISÉ

## 🧹 Vue d'ensemble

Ce guide explique comment maintenir le projet Athalia propre et organisé en supprimant les fichiers indésirables qui s'accumulent au fil du temps.

## 📋 Scripts de Nettoyage Disponibles

### 1. `ath-cleanup-complete` - Nettoyage Complet
**Usage :** `./bin/cleanup/ath-cleanup-complete`

**Description :** Script de nettoyage complet qui supprime tous les types de fichiers indésirables en une seule exécution.

**Types de fichiers supprimés :**
- Fichiers temporaires macOS (.DS_Store, ._*)
- Fichiers Python compilés (*.pyc, __pycache__)
- Fichiers temporaires système (*.tmp, *.temp, *.swp, etc.)
- Fichiers de sauvegarde (*.bak, *.backup)
- Fichiers vides
- Fichiers désactivés (*.disabled)
- Logs anciens (>7 jours)
- Fichiers de cache
- Dossiers vides

### 2. `ath-cleanup-preventive` - Nettoyage Préventif
**Usage :** `./bin/cleanup/ath-cleanup-preventive`

**Description :** Script de maintenance préventive à exécuter régulièrement pour éviter l'accumulation de fichiers indésirables.

**Caractéristiques :**
- Exclut l'environnement virtuel (.venv) et Git (.git)
- Nettoyage plus conservateur des logs (>30 jours)
- Recommandations pour la maintenance continue

### 3. `ath-cleanup-analysis` - Analyse des Fichiers
**Usage :** `./bin/cleanup/ath-cleanup-analysis`

**Description :** Script d'analyse qui identifie les fichiers indésirables sans les supprimer.

**Fonctionnalités :**
- Statistiques détaillées des fichiers
- Identification des doublons potentiels
- Recommandations de nettoyage
- Analyse des permissions

## 🎯 Types de Fichiers Indésirables

### Fichiers Temporaires macOS
- **.DS_Store** : Métadonnées macOS
- **._*** : Fichiers AppleDouble (métadonnées étendues)

### Fichiers Python
- **__pycache__/** : Dossiers de cache Python
- ***.pyc** : Fichiers Python compilés
- ***.pyo** : Fichiers Python optimisés

### Fichiers Temporaires Système
- ***.tmp, *.temp** : Fichiers temporaires
- ***.swp, *.swo** : Fichiers de swap Vim
- ***~** : Fichiers de sauvegarde
- **.#*** : Fichiers de verrouillage
- ***.orig, *.rej** : Fichiers de conflit Git

### Fichiers de Sauvegarde
- ***.bak, *.backup** : Sauvegardes automatiques
- ***.old** : Anciennes versions

### Fichiers Vides
- Fichiers de taille 0 octets
- Dossiers vides

### Logs et Cache
- ***.log** : Fichiers de logs (selon l'âge)
- ***.cache** : Fichiers de cache
- **.mypy_cache/** : Cache de vérification de types

## 📅 Planification de la Maintenance

### Nettoyage Hebdomadaire
```bash
# Exécuter le nettoyage préventif
./bin/cleanup/ath-cleanup-preventive
```

### Nettoyage Mensuel
```bash
# Exécuter le nettoyage complet
./bin/cleanup/ath-cleanup-complete
```

### Nettoyage Avant Commit
```bash
# Vérifier l'état du projet
./bin/cleanup/ath-cleanup-analysis
```

## 🛡️ Bonnes Pratiques

### 1. Configuration Git
Le fichier `.gitignore` est configuré pour ignorer automatiquement :
- Fichiers temporaires macOS
- Fichiers Python compilés
- Environnements virtuels
- Fichiers de cache
- Logs et données temporaires

### 2. Configuration IDE
Configurez votre IDE pour ignorer :
- Dossiers `__pycache__`
- Fichiers `.DS_Store`
- Fichiers temporaires

### 3. Surveillance Continue
- Surveillez la taille du projet
- Vérifiez régulièrement les nouveaux types de fichiers
- Mettez à jour les scripts de nettoyage si nécessaire

## 🔧 Personnalisation

### Ajouter de Nouveaux Types de Fichiers
Pour ajouter de nouveaux patterns de fichiers à nettoyer :

1. Modifiez les scripts dans `bin/`
2. Ajoutez les patterns au `.gitignore`
3. Testez avec `ath-cleanup-analysis`

### Exemples de Patterns Personnalisés
```bash
# Fichiers de test temporaires
find . -name "test_*.tmp" -delete

# Fichiers de rapport temporaires
find . -name "*_report.tmp" -delete

# Fichiers de données temporaires
find . -name "temp_*.json" -delete
```

## 📊 Statistiques de Nettoyage

### Exemple de Sortie
```
🧹 Nettoyage complet du projet - Suppression des fichiers indésirables
================================================================

📋 1. Suppression des fichiers temporaires macOS
   Suppression de 5 fichiers .DS_Store...
   Suppression de 2389 fichiers AppleDouble (._*)...

📋 2. Suppression des fichiers Python compilés
   Suppression de 501 fichiers .pyc...
   Suppression de 56 dossiers __pycache__...

🎯 Total: 3288 éléments supprimés
```

## ⚠️ Précautions

### Fichiers à Ne Pas Supprimer
- Fichiers dans `.venv/` (environnement virtuel)
- Fichiers dans `.git/` (référentiel Git)
- Fichiers de configuration importants
- Fichiers de données nécessaires

### Sauvegarde
- Effectuez une sauvegarde avant un nettoyage complet
- Vérifiez les fichiers supprimés avec `ath-cleanup-analysis`
- Testez le projet après le nettoyage

## 🚀 Intégration CI/CD

### Script de Pré-commit
```bash
#!/bin/bash
# Script à exécuter avant chaque commit
./bin/cleanup/ath-cleanup-preventive
./bin/testing/ath-test.py
```

### Automatisation
- Configurez un cron job pour le nettoyage hebdomadaire
- Intégrez le nettoyage dans votre pipeline CI/CD
- Surveillez l'espace disque utilisé

## 📞 Support

En cas de problème avec les scripts de nettoyage :
1. Vérifiez les permissions d'exécution
2. Consultez les logs d'erreur
3. Testez avec `ath-cleanup-analysis` d'abord
4. Contactez l'équipe de développement

---

**Note :** Ce guide doit être mis à jour régulièrement pour refléter les nouvelles pratiques et outils de nettoyage.
