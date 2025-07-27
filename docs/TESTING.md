# Guide de Tests - Athalia

**Date :** 27 juillet 2025  
**Objectif :** Stratégie complète de tests pour Athalia

---

## 🎯 Stratégie de Tests

### **Philosophie**
- **Tests First** : Écrire les tests avant le code
- **Couverture >90%** : Maintenir une couverture élevée
- **Tests Automatisés** : Intégration continue
- **Tests Manuels** : Validation UX

---

## 🧪 Types de Tests

### **1. Tests Unitaires**
```bash
# Lancer tous les tests unitaires
python3 -m pytest tests/ --verbose

# Tests avec couverture
python3 -m pytest tests/ --cov=athalia_core --cov-report=html

# Tests spécifiques
python3 -m pytest tests/test_intelligent_auditor.py -v
python3 -m pytest tests/test_auto_cleaner.py -v
```

### **2. Tests d'Intégration**
```bash
# Tests d'intégration complets
python3 -m pytest tests/integration/ --verbose

# Tests end-to-end
python3 -m pytest tests/integration/test_end_to_end.py -v

# Tests de workflow
python3 -m pytest tests/integration/test_workflow.py -v
```

### **3. Tests de Performance**
```bash
# Benchmarks de performance
python3 athalia_core/performance_analyzer.py --benchmark

# Tests de charge
python3 -m pytest tests/performance/ --verbose

# Tests de mémoire
python3 athalia_core/performance_analyzer.py --memory-test
```

### **4. Tests de Sécurité**
```bash
# Audit de sécurité
python3 athalia_core/security_auditor.py --project /chemin/projet

# Tests de vulnérabilités
python3 -m pytest tests/security/ --verbose

# Tests de validation
python3 athalia_core/plugins_validator.py --test-all
```

---

## 📋 Structure des Tests

### **Organisation des Fichiers**
```
tests/
├── test_intelligent_auditor.py      # Tests de l'auditeur
├── test_auto_cleaner.py             # Tests de nettoyage
├── test_auto_documenter.py          # Tests de documentation
├── test_auto_tester.py              # Tests du générateur de tests
├── test_ai_robust.py                # Tests de l'IA
├── test_performance_analyzer.py     # Tests de performance
├── integration/                     # Tests d'intégration
│   ├── test_end_to_end.py
│   ├── test_workflow.py
│   └── test_cli_robustesse.py
├── performance/                     # Tests de performance
│   ├── test_benchmarks.py
│   └── test_memory.py
└── security/                        # Tests de sécurité
    ├── test_vulnerabilities.py
    └── test_validation.py
```

### **Conventions de Nommage**
- **Fichiers** : `test_<module>.py`
- **Classes** : `Test<Module>`
- **Méthodes** : `test_<fonctionnalité>`
- **Fixtures** : `fixture_<nom>`

---

## 🔧 Outils de Test

### **Pytest Configuration**
```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --verbose
    --tb=short
    --strict-markers
    --disable-warnings
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    performance: marks tests as performance tests
    security: marks tests as security tests
```

### **Couverture de Code**
```bash
# Générer rapport de couverture
python3 -m pytest tests/ --cov=athalia_core --cov-report=html

# Couverture en ligne de commande
python3 -m pytest tests/ --cov=athalia_core --cov-report=term-missing

# Couverture XML pour CI/CD
python3 -m pytest tests/ --cov=athalia_core --cov-report=xml
```

### **Tests Automatisés**
```bash
# Script de validation complète
./scripts/run_all_tests.sh

# Tests avant commit
./scripts/pre_commit_tests.sh

# Tests de régression
./scripts/regression_tests.sh
```

---

## 📊 Métriques de Qualité

### **Indicateurs Clés**
- **Couverture de code** : >90%
- **Tests unitaires** : >500 tests
- **Tests d'intégration** : >50 tests
- **Temps d'exécution** : <5 minutes
- **Fiabilité** : >99%

### **Rapports de Test**
```bash
# Générer rapport complet
python3 athalia_core/auto_tester.py --report --output reports/

# Rapport de couverture
python3 -m pytest tests/ --cov=athalia_core --cov-report=html --cov-report=term

# Rapport de performance
python3 athalia_core/performance_analyzer.py --report
```

---

## 🚀 Tests en CI/CD

### **GitHub Actions**
```yaml
# .github/workflows/tests.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.10
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python3 -m pytest tests/ --cov=athalia_core --cov-report=xml
    - name: Upload coverage
      uses: codecov/codecov-action@v1
```

### **Tests Automatisés**
```bash
# Pipeline de tests
python3 athalia_core/auto_tester.py --pipeline

# Tests de régression automatiques
python3 athalia_core/auto_tester.py --regression

# Tests de performance automatiques
python3 athalia_core/performance_analyzer.py --auto-benchmark
```

---

## 🐛 Debug et Troubleshooting

### **Debug des Tests**
```bash
# Mode debug
python3 -m pytest tests/ --pdb

# Tests avec plus de détails
python3 -m pytest tests/ -v -s

# Tests spécifiques avec debug
python3 -m pytest tests/test_specific.py -v -s --pdb
```

### **Problèmes Courants**
```bash
# Tests qui échouent
python3 -m pytest tests/ --lf  # Last failed

# Tests lents
python3 -m pytest tests/ --durations=10

# Tests avec timeouts
python3 -m pytest tests/ --timeout=30
```

---

## 📋 Checklist de Tests

### **Avant chaque Commit**
- [ ] Tests unitaires passent
- [ ] Tests d'intégration passent
- [ ] Couverture >90%
- [ ] Pas de régressions
- [ ] Performance validée

### **Avant chaque Release**
- [ ] Tous les tests passent
- [ ] Tests de performance validés
- [ ] Tests de sécurité passés
- [ ] Tests de régression complets
- [ ] Documentation des tests mise à jour

### **Maintenance Mensuelle**
- [ ] Audit des tests obsolètes
- [ ] Optimisation des tests lents
- [ ] Mise à jour des fixtures
- [ ] Validation de la couverture
- [ ] Revue des tests de sécurité

---

## 🎯 Bonnes Pratiques

### **Écriture de Tests**
- **Un test = une assertion** : Un seul concept par test
- **Nommage clair** : Noms descriptifs des tests
- **Fixtures réutilisables** : Éviter la duplication
- **Tests indépendants** : Pas de dépendances entre tests

### **Maintenance**
- **Tests à jour** : Mettre à jour avec le code
- **Suppression obsolètes** : Nettoyer les tests inutiles
- **Optimisation** : Tests rapides et efficaces
- **Documentation** : Commenter les tests complexes

---

**🧪 Tests - Garant de la Qualité Athalia !** 