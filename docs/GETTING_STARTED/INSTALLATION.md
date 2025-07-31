# 🚀 Guide d'Installation - Athalia

**Version :** 10.0 (FINAL - 100% TERMINÉE ✅)
**Date :** 30 Juillet 2025

---

## 🎯 **PRÉSENTATION**

Athalia est un système d'intelligence artificielle avancé pour l'automatisation, l'analyse et l'optimisation de projets de développement. Ce guide vous accompagne dans l'installation et la configuration complète.

### **🏆 ÉTAT ACTUEL**
- **🛡️ Sécurité :** 100% sécurisé ✅
- **🎯 Qualité :** Code professionnel ✅
- **🧹 Maintenance :** Structure optimale ✅
- **🧪 Tests :** Validation complète ✅

---

## 📋 **PRÉREQUIS**

### **Système**
- **OS :** macOS, Linux, Windows
- **Python :** 3.8+ (recommandé 3.10+)
- **Git :** Version récente
- **Espace disque :** 500MB minimum

### **Outils Recommandés**
- **pyenv** (gestion des versions Python)
- **virtualenv** ou **venv** (environnements virtuels)
- **VS Code** ou **PyCharm** (IDE)

---

## 🚀 **INSTALLATION RAPIDE**

### **1. Cloner le Projet**
```bash
# Cloner le repository
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# Vérifier la branche
git checkout develop
```

### **2. Configuration de l'Environnement**
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement
# Sur macOS/Linux :
source venv/bin/activate
# Sur Windows :
# venv\Scripts\activate

# Mettre à jour pip
pip install --upgrade pip
```

### **3. Installation des Dépendances**
```bash
# Installer les dépendances principales
pip install -r requirements.txt

# Installer les dépendances de développement (optionnel)
pip install -r config/requirements-minimal.txt
```

### **4. Configuration**
```bash
# Copier le fichier de configuration
cp config.yml.example config/config.yml

# Éditer la configuration selon vos besoins
# nano config/config.yml
```

---

## ⚙️ **CONFIGURATION DÉTAILLÉE**

### **Fichier de Configuration Principal**
```yaml
# config/config.yml
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

## 🧪 **VALIDATION DE L'INSTALLATION**

### **1. Tests de Base**
```bash
# Lancer les tests de base
python -m pytest tests/test_basic.py -v

# Vérifier l'installation
python -c "import athalia_core; print('✅ Installation réussie!')"
```

### **2. Tests de Sécurité**
```bash
# Tests de sécurité
python -m pytest tests/test_security_validator.py -v

# Validation des commandes
python -m pytest tests/test_linting_corrections.py -v
```

### **3. Tests Complets**
```bash
# Tous les tests
python -m pytest tests/ -v

# Avec couverture
python -m pytest tests/ --cov=athalia_core --cov-report=html
```

---

## 🚀 **LANCEMENT RAPIDE**

### **Interface en Ligne de Commande**
```bash
# Lancement principal
python athalia_unified.py

# Avec options
python athalia_unified.py --help
python athalia_unified.py --dry-run
python athalia_unified.py --verbose
```

### **Scripts Utilitaires**
```bash
# Linting
./bin/ath-lint.py

# Tests
./bin/ath-test.py

# Audit
./bin/ath-audit.py

# Nettoyage
./bin/ath-clean
```

---

## 🔧 **DÉPANNAGE**

### **Problèmes Courants**

#### **Erreur de Module**
```bash
# Solution : Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

#### **Erreur de Permissions**
```bash
# Solution : Vérifier les permissions
chmod +x bin/*.py
chmod +x scripts/*.sh
```

#### **Erreur de Configuration**
```bash
# Solution : Vérifier le fichier config.yml
python -c "import yaml; yaml.safe_load(open('config/config.yml'))"
```

### **Logs et Debug**
```bash
# Activer le mode debug
export ATHALIA_DEBUG=true

# Consulter les logs
tail -f logs/athalia.log
```

---

## 📚 **PROCHAINES ÉTAPES**

1. **Consulter le [Guide d'utilisation](USAGE.md)** pour apprendre à utiliser Athalia
2. **Explorer la [Documentation API](API.md)** pour les fonctionnalités avancées
3. **Consulter les [Guides développeur](DEVELOPER/)** pour contribuer
4. **Tester les fonctionnalités** avec les exemples fournis

---

## 🎉 **FÉLICITATIONS !**

Votre installation d'Athalia est maintenant complète et prête pour la production !

**📅 Dernière mise à jour :** 30 Juillet 2025
**🎯 Projet prêt pour la production !**
