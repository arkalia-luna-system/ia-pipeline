# 🔧 Guide de Dépannage - Athalia

**Date :** 27 janvier 2025  
**Version :** 1.0

---

## 🎯 **Vue d'Ensemble**

Ce guide vous aide à résoudre les problèmes courants rencontrés avec Athalia.

---

## 🚨 **Problèmes Courants**

### **❌ Erreur d'Import**
```bash
ModuleNotFoundError: No module named 'athalia_core'
```

**✅ Solution :**
```bash
# Vérifier l'installation
pip install -r requirements.txt

# Vérifier l'environnement virtuel
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

### **❌ Erreur de Permission**
```bash
PermissionError: [Errno 13] Permission denied
```

**✅ Solution :**
```bash
# Vérifier les permissions
chmod +x athalia_unified.py

# Ou exécuter avec sudo si nécessaire
sudo python athalia_unified.py --help
```

### **❌ Erreur de Configuration**
```bash
FileNotFoundError: config/athalia_config.yaml
```

**✅ Solution :**
```bash
# Vérifier l'existence du fichier
ls -la config/athalia_config.yaml

# Créer une configuration par défaut si nécessaire
cp config/athalia_config.yaml.example config/athalia_config.yaml
```

---

## 🔍 **Diagnostic**

### **1. Vérification de l'Installation**
```bash
# Tester l'import principal
python -c "import athalia_core; print('✅ Import réussi')"

# Vérifier la CLI
python athalia_unified.py --help

# Tester un audit rapide
python athalia_unified.py . --action audit --dry-run
```

### **2. Vérification des Dépendances**
```bash
# Lister les packages installés
pip list | grep athalia

# Vérifier les versions
pip show athalia-core
```

### **3. Vérification de l'Environnement**
```bash
# Vérifier Python
python --version

# Vérifier pip
pip --version

# Vérifier l'environnement virtuel
which python
```

---

## 🛠️ **Solutions Avancées**

### **Problème de Performance**
```bash
# Mode verbose pour diagnostiquer
python athalia_unified.py . --action audit --verbose

# Mode dry-run pour tester
python athalia_unified.py . --action complete --dry-run
```

### **Problème de Tests**
```bash
# Nettoyer les caches
find . -name "__pycache__" -delete
find . -name "*.pyc" -delete

# Relancer les tests
python -m pytest tests/ -v
```

### **Problème de Documentation**
```bash
# Régénérer la documentation
python athalia_unified.py . --action complete --no-audit --no-clean
```

---

## 📞 **Support**

### **Logs Utiles**
```bash
# Voir les logs
tail -f logs/athalia.log

# Logs d'erreur
tail -f logs/errors.log
```

### **Contact**
- **Documentation :** [Guides](../GUIDES/)
- **API :** [Référence API](../API/)
- **Issues :** GitHub Issues

---

## 🔄 **Restauration**

### **Rollback de Configuration**
```bash
# Restaurer la configuration précédente
cp config/athalia_config.yaml.backup config/athalia_config.yaml
```

### **Restauration Complète**
```bash
# Cloner à nouveau le projet
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd athalia-dev-setup

# Réinstaller
pip install -r requirements.txt
```

---

*Guide de dépannage pour résoudre les problèmes courants avec Athalia* 