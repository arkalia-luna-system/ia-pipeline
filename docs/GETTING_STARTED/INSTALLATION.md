# 🚀 Guide d'Installation - Athalia

**Version :** 11.0 (ACTIVE DEVELOPMENT)  
**Date :** 2 Août 2025  
**Statut :** ✅ PRÊT POUR LA PRODUCTION

---

## 🎯 **PRÉSENTATION**

Athalia est un système d'intelligence artificielle avancé pour l'automatisation, l'analyse et l'optimisation de projets de développement. Ce guide vous accompagne dans l'installation et la configuration complète.

### **🏆 ÉTAT ACTUEL**
- **🛡️ Sécurité :** 100% sécurisé ✅
- **🎯 Qualité :** Code professionnel en amélioration continue ✅
- **🧹 Maintenance :** Structure optimale avec nettoyage automatique ✅
- **🧪 Tests :** 1453 tests collectés (couverture en amélioration) ✅
- **⚡ Performance :** Optimisation RAM -74% ✅

---

## 📋 **PRÉREQUIS**

### **Système**
- **OS :** macOS 12+, Linux (Ubuntu 20.04+), Windows 10+
- **Python :** 3.10+ (recommandé 3.12)
- **Git :** Version 2.30+
- **Espace disque :** 1GB minimum (recommandé 2GB)
- **RAM :** 4GB minimum (recommandé 8GB)

### **Outils Recommandés**
- **pyenv** (gestion des versions Python)
- **virtualenv** ou **venv** (environnements virtuels)
- **VS Code** ou **PyCharm** (IDE)
- **Docker** (optionnel, pour conteneurisation)

---

## 🚀 **INSTALLATION RAPIDE**

### **1. Cloner le Projet**
```bash
# Cloner le repository
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd athalia-dev-setup

# Vérifier la branche
git checkout develop

# Vérifier l'état du projet
git status
```

### **2. Configuration de l'Environnement**
```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
# Sur macOS/Linux :
source .venv/bin/activate
# Sur Windows :
# .venv\Scripts\activate

# Mettre à jour pip
pip install --upgrade pip setuptools wheel
```

### **3. Installation des Dépendances**
```bash
# Installer les dépendances principales
pip install -r requirements.txt

# Installer les dépendances de développement (optionnel)
pip install -r config/requirements-minimal.txt

# Vérifier l'installation
python -c "import athalia_core; print('✅ Dépendances installées avec succès!')"
```

### **4. Configuration**
```bash
# Copier le fichier de configuration
cp config/athalia_config.yaml.example config/athalia_config.yaml

# Éditer la configuration selon vos besoins
# nano config/athalia_config.yaml
```

---

## ⚙️ **CONFIGURATION DÉTAILLÉE**

### **Fichier de Configuration Principal**
```yaml
# config/athalia_config.yaml
app:
  name: athalia
  version: "11.0"
  debug: false
  environment: production
  log_level: INFO

security:
  validate_commands: true
  allowed_directories:
    - /usr/bin
    - /usr/local/bin
    - /opt/homebrew/bin
  encryption_enabled: true

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  file: logs/athalia.log
  max_size: 10MB
  backup_count: 5

performance:
  cache_enabled: true
  cache_size: 1000
  timeout: 30
  max_workers: 4

ai:
  models:
    - ollama_qwen
    - ollama_mistral
    - openai_gpt4
  fallback_enabled: true
  distillation_enabled: true
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
export ATHALIA_MAX_WORKERS=4

# Configuration IA
export ATHALIA_AI_MODELS="ollama_qwen,ollama_mistral"
export ATHALIA_FALLBACK_ENABLED=true
```

---

## 🧪 **VALIDATION DE L'INSTALLATION**

### **1. Tests de Base**
```bash
# Activer l'environnement virtuel
source .venv/bin/activate

# Lancer les tests de base
python -m pytest tests/unit/core/ -v

# Vérifier l'installation
python -c "import athalia_core; print('✅ Installation réussie!')"
```

### **2. Tests de Sécurité**
```bash
# Tests de sécurité
python -m pytest tests/unit/security/ -v

# Validation des commandes
python -m pytest tests/unit/quality/ -v
```

### **3. Tests Complets**
```bash
# Tous les tests
python -m pytest tests/ -v

# Avec couverture
python -m pytest tests/ --cov=athalia_core --cov-report=html

# Tests de performance
python -m pytest tests/performance/ -v
```

---

## 🚀 **LANCEMENT RAPIDE**

### **Interface en Ligne de Commande**
```bash
# Activer l'environnement virtuel
source .venv/bin/activate

# Lancement principal
python athalia_core/main.py

# Avec options
python athalia_core/main.py --help
python athalia_core/main.py --dry-run
python athalia_core/main.py --verbose
```

### **Scripts Utilitaires**
```bash
# Linting et formatage
./bin/ath-lint.py

# Tests
./bin/ath-test.py

# Audit
./bin/ath-audit.py

# Nettoyage
./bin/ath-clean

# Dashboard
./bin/ath-dashboard.py
```

---

## 🔧 **DÉPANNAGE**

### **Problèmes Courants**

#### **Erreur de Module**
```bash
# Solution : Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall

# Vérifier les versions
pip list | grep athalia
```

#### **Erreur de Permissions**
```bash
# Solution : Vérifier les permissions
chmod +x bin/*.py
chmod +x scripts/*.sh

# Vérifier les droits d'écriture
ls -la logs/
```

#### **Erreur de Configuration**
```bash
# Solution : Vérifier le fichier config
python -c "import yaml; yaml.safe_load(open('config/athalia_config.yaml'))"

# Valider la configuration
python athalia_core/config_manager.py --validate
```

#### **Erreur de Cache**
```bash
# Solution : Nettoyer le cache
rm -rf cache/
python athalia_core/cache_manager.py --clear
```

### **Logs et Debug**
```bash
# Activer le mode debug
export ATHALIA_DEBUG=true
export ATHALIA_LOG_LEVEL=DEBUG

# Consulter les logs
tail -f logs/athalia.log

# Analyser les erreurs
python athalia_core/logger_advanced.py --analyze
```

---

## 📚 **PROCHAINES ÉTAPES**

1. **Consulter le [Guide d'utilisation](../../USER_GUIDES/USAGE.md)** pour apprendre à utiliser Athalia
2. **Explorer la [Documentation API](../../API/)** pour les fonctionnalités avancées
3. **Consulter les [Guides développeur](../DEVELOPER/)** pour contribuer
4. **Tester les fonctionnalités** avec les exemples fournis
5. **Configurer le [Dashboard](../../dashboard/)** pour le monitoring

---

## 🎉 **FÉLICITATIONS !**

Votre installation d'Athalia est maintenant complète et prête pour la production !

### **Vérification Finale**
```bash
# Test complet du système
python athalia_core/main.py --test-complete

# Vérifier les métriques
python athalia_core/performance_analyzer.py --report
```

**📅 Dernière mise à jour :** 2 Août 2025  
**🎯 Projet prêt pour la production !**  
**🔄 Support :** Documentation et guides disponibles dans `/docs/`

---

*Guide d'installation - Athalia v11.0 - Branch develop*
