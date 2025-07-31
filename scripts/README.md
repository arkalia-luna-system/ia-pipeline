# Scripts Utilitaires Athalia

Ce dossier contient tous les scripts utilitaires organisés par catégorie.

## 📁 **Structure**

### Scripts Principaux
- `monitor_processes.py` - Monitoring des processus
- `quick_performance_test.py` - Tests de performance rapides
- `test_athalia_performance.py` - Tests de performance complets
- `validation_continue.py` - Validation continue
- `validation_dashboard_simple.py` - Dashboard de validation
- `validation_express.sh` - Validation express
- `validation_objective.py` - Validation objective

## 🚀 **Utilisation**

### Scripts de Performance
```bash
# Test de performance rapide
python3 scripts/quick_performance_test.py

# Test de performance complet
python3 scripts/test_athalia_performance.py
```

### Scripts de Validation
```bash
# Validation continue
python3 scripts/validation_continue.py

# Validation objective
python3 scripts/validation_objective.py
```

## 📋 **Conventions**

- **Nommage** : `[domaine]_[fonction].py`
- **Documentation** : Chaque script doit avoir un docstring
- **Tests** : Scripts testés avant intégration
- **Logs** : Utilisation du système de logging centralisé

## 🔧 **Ajout de Nouveaux Scripts**

1. Créer le dossier approprié si nécessaire
2. Suivre les conventions de nommage
3. Ajouter la documentation
4. Tester le script
5. Mettre à jour ce README 