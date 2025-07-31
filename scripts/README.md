# 📁 Scripts Athalia

Ce dossier contient tous les scripts d'analyse, validation et monitoring du projet Athalia.

## 📂 Structure

### **ci/** - Scripts CI/CD
- `ci_diagnostic.py` - Diagnostic complet de la configuration CI/CD
- `ci_pro_analyzer.py` - Analyse professionnelle des niveaux CI/CD
- `ci_progress_tracker.py` - Suivi des progrès CI/CD

### **validation/** - Scripts de validation
- `validation_continue.py` - Validation continue du projet
- `validation_dashboard_simple.py` - Dashboard de validation simple
- `validation_objective.py` - Validation objective des métriques
- `validation_express.sh` - Validation rapide en shell

### **monitoring/** - Scripts de monitoring
- `monitor_processes.py` - Monitoring des processus
- `test_athalia_performance.py` - Tests de performance Athalia
- `quick_performance_test.py` - Tests de performance rapides

### **Scripts utilitaires**
- `prevent_python_version_issues.py` - Prévention des problèmes de versions Python
- `sync_develop_to_ci_pro.sh` - Synchronisation develop vers CI pro
- `validate_ci_cd.sh` - Validation CI/CD en shell

## 🚀 Utilisation

```bash
# Diagnostic CI/CD
python scripts/ci/ci_diagnostic.py

# Validation continue
python scripts/validation/validation_continue.py

# Monitoring des performances
python scripts/monitoring/test_athalia_performance.py
```

## 📋 Maintenance

- Tous les scripts sont documentés et testés
- Les scripts de validation génèrent des rapports dans `data/reports/`
- Les scripts de monitoring peuvent être exécutés en continu
