# 🛠️ Commandes Athalia (bin/)

**Date :** 11 août 2025  
**Statut :** ✅ **43 COMMANDES TESTÉES UTILISATEUR (16/20)**

Ce dossier contient toutes les commandes exécutables et utilitaires système d'Athalia.

## 📊 **Statistiques Réelles**
- **Total commandes** : **43 fichiers** ✅ **COMPTÉ**
- **Commandes principales** : `athalia_unified.py`, `ath-*` ✅
- **Structure organisée** : Tests, nettoyage, workflow ✅

## 📂 Structure

### **cleanup/** - Scripts de nettoyage
- `ath-clean-appledouble` - Nettoyage des fichiers Apple Double
- `clean-null-bytes-robust.py` - Nettoyage robuste des octets null
- `ath-cleanup-*` - Scripts de nettoyage avancés

### **workflow/** - Scripts de workflow
- `ath-workflow` - Workflow principal Athalia
- `ath-workflow-complete` - Workflow complet
- `ath-test-workflow` - Workflow de tests

### **Commandes principales (racine)**
- `athalia_unified.py` - Point d'entrée principal
- `ath-*` - Commandes Athalia principales
- `ath-test.py` - Tests automatisés
- `ath-build.py` - Build du projet
- `ath-audit.py` - Audit de sécurité
- `ath-coverage.py` - Couverture de tests

## 🚀 Utilisation

### **Commandes principales**
```bash
# Point d'entrée principal
python bin/athalia_unified.py

# Tests automatisés
./bin/ath-test.py

# Audit de sécurité
./bin/ath-audit.py

# Build du projet
./bin/ath-build.py
```

### **Nettoyage**
```bash
# Nettoyage Apple Double
./bin/cleanup/ath-clean-appledouble

# Nettoyage octets null
python bin/cleanup/clean-null-bytes-robust.py
```

### **Workflow**
```bash
# Workflow principal
./bin/workflow/ath-workflow

# Workflow complet
./bin/workflow/ath-workflow-complete
```

## 📋 Commandes disponibles

### **Tests et Validation**
- `ath-test.py` - Tests automatisés
- `ath-test-clean.py` - Tests de nettoyage
- `ath-test-aliases.sh` - Alias de tests
- `ath-test-wrapper.sh` - Wrapper de tests

### **Nettoyage et Maintenance**
- `ath-clean` - Nettoyage complet
- `ath-clean-macos-temp` - Nettoyage macOS
- `ath-clean-shutdown` - Nettoyage à l'arrêt
- `ath-clean-tests` - Nettoyage des tests

### **Formatage et Linting**
- `ath-format-simple` - Formatage simple
- `ath-auto-format` - Formatage automatique
- `ath-lint.py` - Linting Python
- `ath-lint-secure` - Linting sécurisé
- `ath-verify-formatting` - Vérification du formatage

### **Workflow et CI/CD**
- `ath-workflow` - Workflow principal
- `ath-ci-pro-config` - Configuration CI pro
- `ath-ci-pro-pre-commit` - Pre-commit CI pro
- `ath-prepare-commit` - Préparation de commit
- `ath-smart-commit` - Commit intelligent
- `ath-push` - Push intelligent

### **Utilitaires**
- `ath-start` - Démarrage
- `ath-quick-start` - Démarrage rapide
- `ath-backup.py` - Sauvegarde
- `ath-protect-my-tests` - Protection des tests

## 📋 Maintenance

- ✅ **43 commandes disponibles** dans le dossier `bin/`
- ✅ **Toutes les commandes sont exécutables** (`chmod +x`)
- ✅ **Les commandes Python** ont un shebang `#!/usr/bin/env python3`
- ✅ **Les commandes shell** ont un shebang `#!/bin/bash`
- ✅ **Documentation complète** dans chaque script

*Documentation mise à jour avec 43 commandes réelles - 11 août 2025* 