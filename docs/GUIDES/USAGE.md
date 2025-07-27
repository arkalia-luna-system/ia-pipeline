# 📖 Guide d'Utilisation - Athalia

**Date de mise à jour :** 27 juillet 2025  
**Version :** 3.0 - Utilisation Professionnelle

---

## 🎯 **Vue d'Ensemble**

Ce guide vous accompagne dans l'utilisation complète d'Athalia, depuis les fonctionnalités de base jusqu'aux cas d'usage avancés.

---

## 🚀 **Interface en Ligne de Commande (CLI)**

### 📋 **Commandes Principales**

#### **Audit de Projet**
```bash
# Audit complet d'un projet
python athalia_unified.py audit /chemin/vers/projet

# Audit rapide
python athalia_unified.py audit . --quick

# Audit avec options spécifiques
python athalia_unified.py audit . --output json --verbose

# Audit de sécurité
python athalia_unified.py audit . --security

# Audit de performance
python athalia_unified.py audit . --performance
```

#### **Tests et Validation**
```bash
# Lancer tous les tests
python athalia_unified.py test --full

# Tests rapides seulement
python athalia_unified.py test --quick

# Tests spécifiques
python athalia_unified.py test --module audit
python athalia_unified.py test --module performance

# Tests avec couverture
python athalia_unified.py test --coverage
```

#### **Organisation et Nettoyage**
```bash
# Organiser le workspace
python athalia_unified.py organize

# Nettoyer les fichiers temporaires
python athalia_unified.py clean

# Nettoyer avec options
python athalia_unified.py clean --dry-run --verbose
```

#### **Sauvegarde et Restauration**
```bash
# Sauvegarde automatique
python athalia_unified.py backup

# Sauvegarde incrémentale
python athalia_unified.py backup --incremental

# Restaurer une sauvegarde
python athalia_unified.py restore --date 2025-07-27

# Lister les sauvegardes
python athalia_unified.py backup --list
```

#### **Dashboard et Interface Web**
```bash
# Lancer le dashboard
python athalia_unified.py dashboard

# Dashboard sur port spécifique
python athalia_unified.py dashboard --port 8502

# Mode développement
python athalia_unified.py dashboard --dev
```

#### **Benchmarks et Performance**
```bash
# Benchmark rapide
python athalia_unified.py benchmark --quick

# Benchmark complet
python athalia_unified.py benchmark --full

# Analyse de performance
python athalia_unified.py benchmark --analyze
```

---

## 🎮 **Utilisation Interactive**

### 📊 **Dashboard Web**

#### **Accès au Dashboard**
1. Lancer : `python athalia_unified.py dashboard`
2. Ouvrir : http://localhost:8501
3. Interface : Interface Streamlit moderne

#### **Fonctionnalités du Dashboard**
- **Métriques en temps réel** : Performance, tests, audits
- **Graphiques interactifs** : Évolution des métriques
- **Rapports détaillés** : Export PDF, JSON, CSV
- **Configuration** : Interface de configuration
- **Logs en direct** : Visualisation des logs

### 🔧 **Configuration Interactive**
```bash
# Configuration guidée
python athalia_unified.py config --interactive

# Éditer la configuration
python athalia_unified.py config --edit

# Valider la configuration
python athalia_unified.py config --validate
```

---

## 🐍 **Utilisation Programmée**

### 📚 **Import et Utilisation de Base**

#### **Audit de Projet**
```python
from athalia_core.audit import ProjectAuditor

# Créer un auditeur
auditor = ProjectAuditor()

# Auditer un projet
result = auditor.audit_project("/chemin/vers/projet")

# Analyser les résultats
print(f"Score global: {result.score}")
print(f"Problèmes détectés: {len(result.issues)}")
print(f"Recommandations: {len(result.recommendations)}")
```

#### **Analyse de Performance**
```python
from athalia_core.performance_analyzer import PerformanceAnalyzer

# Créer un analyseur
analyzer = PerformanceAnalyzer()

# Analyser un projet
performance = analyzer.analyze_project("/chemin/vers/projet")

# Obtenir les métriques
print(f"Temps d'exécution: {performance.execution_time}")
print(f"Utilisation mémoire: {performance.memory_usage}")
print(f"Bottlenecks: {performance.bottlenecks}")
```

#### **Système de Sauvegarde**
```python
from athalia_core.backup_system import BackupSystem

# Créer un système de sauvegarde
backup = BackupSystem()

# Créer une sauvegarde
backup.create_backup("/chemin/vers/projet")

# Restaurer une sauvegarde
backup.restore_backup("2025-07-27_143022")
```

### 🔧 **Configuration Programmée**

#### **Chargement de Configuration**
```python
from athalia_core.config_manager import ConfigManager

# Charger la configuration
config = ConfigManager()
config.load_config("~/.athalia/config.yaml")

# Accéder aux paramètres
project_name = config.get("project.name")
max_memory = config.get("performance.max_memory")
```

#### **Logging Avancé**
```python
from athalia_core.logging_system import LoggingSystem

# Configurer le logging
logger = LoggingSystem()
logger.setup_logging(level="INFO", format="detailed")

# Utiliser le logger
logger.info("Démarrage de l'audit")
logger.warning("Problème détecté")
logger.error("Erreur critique")
```

---

## 🎯 **Cas d'Usage Avancés**

### 🏢 **Environnement d'Équipe**

#### **Configuration d'Équipe**
```yaml
# config/team_config.yaml
team:
  name: "Équipe Développement"
  members: ["dev1", "dev2", "dev3"]
  
workflow:
  code_review: true
  automated_testing: true
  continuous_integration: true
  
quality:
  min_test_coverage: 80
  max_complexity: 10
  security_scan: true
```

#### **Intégration CI/CD**
```yaml
# .github/workflows/athalia.yml
name: Athalia Quality Check

on: [push, pull_request]

jobs:
  athalia-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Athalia
        run: |
          pip install -r requirements.txt
      - name: Run Audit
        run: |
          python athalia_unified.py audit . --output json
      - name: Run Tests
        run: |
          python athalia_unified.py test --coverage
```

### 🤖 **Intégration Robotique**

#### **Configuration Reachy**
```python
from athalia_core.robotics.reachy_auditor import ReachyAuditor

# Configurer l'auditeur Reachy
reachy = ReachyAuditor(ip="192.168.1.100")

# Vérifier la connectivité
if reachy.check_connection():
    print("✅ Reachy connecté")
    
    # Auditer le système robotique
    audit_result = reachy.audit_system()
    print(f"Score robotique: {audit_result.score}")
else:
    print("❌ Reachy non accessible")
```

#### **Tests Robotiques**
```python
from athalia_core.robotics.robotics_ci import RoboticsCI

# Configurer les tests robotiques
robotics_ci = RoboticsCI()

# Lancer les tests
results = robotics_ci.run_tests()

# Analyser les résultats
for test, result in results.items():
    print(f"{test}: {'✅' if result.passed else '❌'}")
```

### 📊 **Analyse de Données**

#### **Métriques de Performance**
```python
from athalia_core.performance_analyzer import PerformanceAnalyzer

# Analyser les performances
analyzer = PerformanceAnalyzer()
metrics = analyzer.get_detailed_metrics()

# Exporter les métriques
analyzer.export_metrics("performance_report.json")
analyzer.generate_charts("performance_charts/")
```

#### **Rapports Automatisés**
```python
from athalia_core.reporting import ReportGenerator

# Générer un rapport complet
reporter = ReportGenerator()
report = reporter.generate_comprehensive_report()

# Exporter en différents formats
reporter.export_pdf("rapport_complet.pdf")
reporter.export_html("rapport_complet.html")
reporter.export_json("rapport_complet.json")
```

---

## 🔧 **Configuration Avancée**

### ⚙️ **Fichier de Configuration Complet**
```yaml
# ~/.athalia/config.yaml
project:
  name: "mon-projet-avance"
  version: "2.0.0"
  environment: "production"

paths:
  workspace: "/workspace/projets"
  backups: "/backups/athalia"
  logs: "/logs/athalia"
  cache: "/cache/athalia"
  reports: "/reports/athalia"

performance:
  max_memory: "8GB"
  max_cpu_cores: 16
  timeout: 600
  cache_size: "2GB"
  optimization_level: "high"

logging:
  level: "DEBUG"
  format: "json"
  rotation: "hourly"
  retention: "90 days"
  compression: true

security:
  encryption: true
  backup_encryption: true
  ssl_verify: true
  api_keys_encryption: true

robotics:
  enabled: true
  reachy_ip: "192.168.1.100"
  ros2_path: "/opt/ros/humble"
  simulation_mode: false

quality:
  min_test_coverage: 85
  max_complexity: 8
  security_scan: true
  code_style_check: true

notifications:
  email:
    enabled: true
    smtp_server: "smtp.gmail.com"
    smtp_port: 587
    username: "user@example.com"
  slack:
    enabled: true
    webhook_url: "https://hooks.slack.com/..."
```

### 🔑 **Variables d'Environnement Avancées**
```bash
# Configuration système
export ATHALIA_ENV="production"
export ATHALIA_LOG_LEVEL="DEBUG"
export ATHALIA_MAX_MEMORY="16GB"

# Chemins personnalisés
export ATHALIA_WORKSPACE="/custom/workspace"
export ATHALIA_BACKUP_DIR="/custom/backups"
export ATHALIA_CACHE_DIR="/custom/cache"

# Configuration robotique
export ATHALIA_REACHY_IP="192.168.1.200"
export ATHALIA_ROS2_PATH="/opt/ros/humble"

# Configuration de sécurité
export ATHALIA_ENCRYPTION_KEY="your-secret-key"
export ATHALIA_SSL_VERIFY="true"
```

---

## 🆘 **Dépannage et Support**

### ❌ **Problèmes Courants**

#### **Erreur de Mémoire**
```bash
# Augmenter la limite mémoire
export ATHALIA_MAX_MEMORY="16GB"
python athalia_unified.py audit . --memory-limit 16GB
```

#### **Timeout d'Exécution**
```bash
# Augmenter le timeout
python athalia_unified.py audit . --timeout 1800
```

#### **Problèmes de Connexion**
```bash
# Vérifier la connectivité réseau
python athalia_unified.py network --check

# Mode hors ligne
python athalia_unified.py audit . --offline
```

### 📞 **Support et Aide**
- **Documentation :** [Guides complets](../README.md)
- **Dépannage :** [Guide de dépannage](TROUBLESHOOTING.md)
- **FAQ :** [Questions fréquentes](FAQ.md)
- **API :** [Documentation API](../API/INDEX.md)

---

## 🎉 **Conclusion**

Vous maîtrisez maintenant l'utilisation complète d'Athalia !

### 🚀 **Prochaines Étapes**
1. **Explorer** les [cas d'usage avancés](../DEVELOPER/)
2. **Configurer** selon vos besoins spécifiques
3. **Automatiser** vos workflows
4. **Contribuer** à l'amélioration

---

*Guide d'utilisation Athalia - Version 3.0 - Utilisation Professionnelle*
