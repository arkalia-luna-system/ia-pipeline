# 🚀 Guide d'Installation - Athalia

**Version :** 10.0 (FINAL - 100% TERMINÉE ✅)
**Date :** 30 Juillet 2025

---

## 🎯 **Vue d'Ensemble**

Ce guide explique comment installer et configurer Athalia, le système d'intelligence artificielle avancé pour l'automatisation de projets.

---

## 📋 **Prérequis**

### **Système**
- **Python :** 3.10+ (recommandé)
- **Git :** Pour cloner le repository
- **Pip :** Dernière version
- **Espace disque :** 500MB minimum

### **Optionnel**
- **Ollama :** Pour les modèles IA locaux (Qwen, Mistral)
- **Docker :** Pour le déploiement conteneurisé

---

## 🚀 **Installation Complète**

### **1. Cloner le Repository**
```bash
git clone https://github.com/arkalia-luna-system/athalia-dev-setup.git
cd athalia-dev-setup
```

### **2. Créer l'Environnement Virtuel**
```bash
# Créer l'environnement virtuel
python3 -m venv .venv

# Activer l'environnement (macOS/Linux)
source .venv/bin/activate

# Activer l'environnement (Windows)
# .venv\Scripts\activate
```

### **3. Installer les Dépendances**
```bash
# Installation complète
pip install -r requirements.txt

# Ou installation minimale
pip install -r requirements-minimal.txt
```

### **4. Vérifier l'Installation**
```bash
# Test de validation
python athalia_core/ready_check.py

# Test des fonctionnalités principales
python -m pytest tests/ -v --tb=short
```

---

## ⚙️ **Configuration**

### **Fichier de Configuration Principal**
```yaml
# config/athalia_config.yaml
app:
  name: athalia-dev-setup
  version: "10.0.0"
  debug: false
  port: 8000

security:
  validate_commands: true
  allowed_paths:
    - "/usr/bin"
    - "/opt/homebrew"

logging:
  level: "INFO"
  file: "logs/athalia.log"
  max_size: "10MB"
```

### **Variables d'Environnement**
```bash
# Configuration de base
export ATHALIA_ENV=production
export ATHALIA_DEBUG=false
export ATHALIA_LOG_LEVEL=INFO

# Configuration IA (optionnel)
export OLLAMA_HOST=http://localhost:11434
export OLLAMA_MODEL=qwen2.5:7b
```

---

## 🧪 **Validation de l'Installation**

### **Tests Automatiques**
```bash
# Tests complets
python -m pytest tests/ -v

# Tests de sécurité
python -m pytest tests/test_security_validator.py -v

# Tests de performance
python scripts/quick_performance_test.py
```

### **Test Manuel**
```bash
# Audit d'un projet
python athalia_unified.py . --action audit --dry-run

# Dashboard
python athalia_core/dashboard.py

# CLI principal
python athalia_core/cli.py --help
```

---

## 🔧 **Dépannage**

### **Problèmes Courants**

#### **Erreur de Permissions**
```bash
# Corriger les permissions
chmod +x bin/*.py
chmod +x bin/*.sh
```

#### **Dépendances Manquantes**
```bash
# Réinstaller les dépendances
pip install --force-reinstall -r requirements.txt
```

#### **Problèmes de Python**
```bash
# Vérifier la version
python3 --version

# Utiliser pyenv si nécessaire
pyenv install 3.10.14
pyenv local 3.10.14
```

---

## 🎯 **Prochaines Étapes**

1. **Lire le [Guide d'utilisation](USAGE.md)**
2. **Explorer les [Guides développeur](../DEVELOPER/)**
3. **Consulter la [Documentation API](../API/)**
4. **Tester avec un projet réel**

---

*Installation validée et testée - Prêt pour la production !* ✅
