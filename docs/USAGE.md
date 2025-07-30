# 🚀 Guide d'Utilisation - Athalia

**Version :** 10.0 (FINAL - 100% TERMINÉE ✅)  
**Date :** 30 Juillet 2025

---

## 🎯 **PRÉSENTATION**

Athalia est un système d'intelligence artificielle avancé qui automatise l'analyse, l'optimisation et la génération de projets de développement. Ce guide vous accompagne dans l'utilisation de toutes les fonctionnalités.

### **🏆 FONCTIONNALITÉS PRINCIPALES**
- **🤖 Génération automatique** de projets et de code
- **🔍 Analyse intelligente** de la qualité du code
- **⚡ Optimisation automatique** des performances
- **🛡️ Sécurité avancée** avec validation des commandes
- **🧪 Tests complets** et automatisés

---

## 🚀 **DÉMARRAGE RAPIDE**

### **Interface en Ligne de Commande**
```bash
# Lancement principal
python athalia_unified.py

# Mode dry-run (simulation)
python athalia_unified.py --dry-run

# Mode verbose (détails)
python athalia_unified.py --verbose

# Aide
python athalia_unified.py --help
```

### **Scripts Utilitaires**
```bash
# Linting et qualité du code
./bin/ath-lint.py

# Tests automatisés
./bin/ath-test.py

# Audit de sécurité
./bin/ath-audit.py

# Nettoyage du projet
./bin/ath-clean

# Couverture de tests
./bin/ath-coverage.py

# Build du projet
./bin/ath-build.py
```

---

## 🔧 **CONFIGURATION**

### **Fichier de Configuration Principal**
```yaml
# config.yml
app:
  name: athalia
  version: "10.0"
  debug: false
  environment: production

security:
  validate_commands: true
  allowed_directories:
    - /usr/bin
    - /usr/local/bin
    - /opt/homebrew/bin

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: logs/athalia.log

performance:
  cache_enabled: true
  cache_size: 1000
  timeout: 30
```

### **Variables d'Environnement**
```bash
# Configuration de base
export ATHALIA_ENV=production
export ATHALIA_DEBUG=false
export ATHALIA_LOG_LEVEL=INFO

# Configuration de sécurité
export ATHALIA_VALIDATE_COMMANDS=true
export ATHALIA_ALLOWED_DIRS="/usr/bin,/usr/local/bin"

# Configuration de performance
export ATHALIA_CACHE_ENABLED=true
export ATHALIA_TIMEOUT=30
```

---

## 🤖 **FONCTIONNALITÉS PRINCIPALES**

### **1. Génération de Projets**

#### **Génération Automatique**
```python
from athalia_core.generation import generate_project

# Générer un projet complet
result = generate_project(
    project_name="mon-projet",
    project_type="api",
    template="fastapi",
    dry_run=False
)
```

#### **Génération de Requirements**
```python
from athalia_core.generation import generate_requirements

# Générer requirements.txt
requirements = generate_requirements(
    project_type="web",
    include_dev=True,
    include_test=True
)
```

### **2. Analyse de Code**

#### **Audit de Projet**
```python
from athalia_core.audit import audit_project

# Analyser un projet
audit_result = audit_project(
    project_path="./mon-projet",
    include_security=True,
    include_quality=True,
    include_performance=True
)
```

#### **Analyse de Sécurité**
```python
from athalia_core.security_auditor import SecurityAuditor

auditor = SecurityAuditor()
security_report = auditor.audit_project("./mon-projet")
```

### **3. Optimisation de Performance**

#### **Analyse de Performance**
```python
from athalia_core.performance_analyzer import PerformanceAnalyzer

analyzer = PerformanceAnalyzer()
performance_report = analyzer.analyze_project("./mon-projet")
```

#### **Optimisation Automatique**
```python
from athalia_core.correction_optimizer import CorrectionOptimizer

optimizer = CorrectionOptimizer()
optimizations = optimizer.optimize_project("./mon-projet")
```

### **4. Tests et Validation**

#### **Tests Automatiques**
```python
from athalia_core.auto_tester import AutoTester

tester = AutoTester()
test_results = tester.run_tests("./mon-projet")
```

#### **Validation de Qualité**
```python
from athalia_core.code_linter import CodeLinter

linter = CodeLinter()
lint_results = linter.lint_project("./mon-projet")
```

---

## 🛡️ **SÉCURITÉ AVANCÉE**

### **Validation des Commandes**
```python
from athalia_core.security_validator import validate_and_run, SecurityError

try:
    # Exécution sécurisée
    result = validate_and_run(["ls", "-la"], capture_output=True)
    print(result.stdout)
except SecurityError as e:
    print(f"Commande non autorisée: {e}")
```

### **Audit de Sécurité**
```python
from athalia_core.security_auditor import SecurityAuditor

auditor = SecurityAuditor()
security_issues = auditor.audit_project("./mon-projet")

for issue in security_issues:
    print(f"Problème: {issue.severity} - {issue.description}")
```

---

## 🧪 **TESTS ET VALIDATION**

### **Tests Unitaires**
```bash
# Tests de base
python -m pytest tests/test_basic.py -v

# Tests de sécurité
python -m pytest tests/test_security_validator.py -v

# Tests d'intégration
python -m pytest tests/integration/ -v

# Tous les tests
python -m pytest tests/ -v
```

### **Tests de Performance**
```bash
# Tests de benchmark
python -m pytest tests/test_benchmark_critical.py -v

# Tests de performance
python -m pytest tests/test_performance_phase3.py -v
```

### **Couverture de Tests**
```bash
# Générer rapport de couverture
python -m pytest tests/ --cov=athalia_core --cov-report=html

# Voir la couverture
open htmlcov/index.html
```

---

## 📊 **MONITORING ET LOGS**

### **Logs de l'Application**
```bash
# Consulter les logs
tail -f logs/athalia.log

# Logs d'erreur
tail -f logs/errors.log

# Logs de performance
tail -f logs/performance.log
```

### **Dashboard de Monitoring**
```bash
# Ouvrir le dashboard
open dashboard/analytics_dashboard.html

# Dashboard interactif
open dashboard/dashboard_interactif_avance.html
```

---

## 🔧 **MAINTENANCE**

### **Nettoyage Automatique**
```bash
# Nettoyage complet
./bin/ath-clean

# Nettoyage des caches
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
```

### **Mise à Jour**
```bash
# Mettre à jour les dépendances
pip install -r requirements.txt --upgrade

# Vérifier les mises à jour
./bin/ath-audit.py --check-updates
```

---

## 🎯 **EXEMPLES D'UTILISATION**

### **Exemple 1 : Créer un Projet API**
```bash
# Générer un projet API FastAPI
python athalia_unified.py --generate --type api --template fastapi --name mon-api

# Analyser le projet généré
python athalia_unified.py --audit --path ./mon-api

# Lancer les tests
python athalia_unified.py --test --path ./mon-api
```

### **Exemple 2 : Optimiser un Projet Existant**
```bash
# Analyser le projet
python athalia_unified.py --audit --path ./projet-existant

# Optimiser automatiquement
python athalia_unified.py --optimize --path ./projet-existant

# Valider les optimisations
python athalia_unified.py --validate --path ./projet-existant
```

### **Exemple 3 : Audit de Sécurité**
```bash
# Audit complet de sécurité
python athalia_unified.py --security-audit --path ./mon-projet

# Générer rapport détaillé
python athalia_unified.py --security-report --path ./mon-projet --output security_report.html
```

---

## 📚 **RESSOURCES ADDITIONNELLES**

- **[Documentation API](API.md)** - Référence complète de l'API
- **[Guides développeur](DEVELOPER/)** - Guides pour contribuer
- **[Rapports d'audit](REPORTS/)** - Analyses et audits
- **[FAQ](GUIDES/FAQ.md)** - Questions fréquentes

---

## 🎉 **SUPPORT**

Pour toute question ou problème :
1. Consultez la **[FAQ](GUIDES/FAQ.md)**
2. Vérifiez les **[logs](logs/)** pour les erreurs
3. Consultez la **[documentation API](API.md)**
4. Ouvrez une issue sur GitHub

---

**📅 Dernière mise à jour :** 30 Juillet 2025  
**🎯 Projet prêt pour la production !**
