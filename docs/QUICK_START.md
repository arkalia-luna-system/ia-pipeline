# 🚀 Guide de Démarrage Rapide - Athalia

**Temps estimé :** 5 minutes  
**Niveau :** Débutant à Intermédiaire

---

## 🎯 **Objectif**

Ce guide vous permettra de **démarrer avec Athalia en 5 minutes** et de comprendre les fonctionnalités essentielles.

---

## 📋 **Prérequis**

### ✅ **Système Requis**
- **OS :** macOS, Linux, Windows (WSL)
- **Python :** 3.8+ 
- **Git :** 2.20+
- **Espace disque :** 2GB minimum

### 🔧 **Outils Recommandés**
- **Éditeur :** VS Code, Cursor, PyCharm
- **Terminal :** iTerm2 (macOS), Windows Terminal
- **Navigateur :** Chrome, Firefox, Safari

---

## ⚡ **Installation Express**

### 1️⃣ **Cloner le Projet**
```bash
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd athalia-dev-setup
```

### 2️⃣ **Activer l'Environnement Virtuel**
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer (macOS/Linux)
source venv/bin/activate

# Activer (Windows)
venv\Scripts\activate
```

### 3️⃣ **Installer les Dépendances**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Vérifier l'Installation**
```bash
python athalia_unified.py --help
```

---

## 🎮 **Premiers Pas**

### 🔍 **Audit Rapide de Votre Projet**
```bash
# Analyser un projet existant
python athalia_unified.py audit /chemin/vers/votre/projet

# Exemple
python athalia_unified.py audit ./mon-projet
```

### 🧪 **Lancer les Tests**
```bash
# Tests rapides
python athalia_unified.py test --quick

# Tests complets
python athalia_unified.py test --full
```

### 📊 **Voir le Dashboard**
```bash
# Lancer le dashboard
python athalia_unified.py dashboard

# Ouvrir dans le navigateur
open http://localhost:8501
```

---

## 🛠️ **Fonctionnalités Essentielles**

### 📁 **Organisation Automatique**
```bash
# Organiser votre workspace
python athalia_unified.py organize

# Nettoyer les fichiers temporaires
python athalia_unified.py clean
```

### 🔄 **Sauvegarde Intelligente**
```bash
# Sauvegarde automatique
python athalia_unified.py backup

# Restaurer une sauvegarde
python athalia_unified.py restore --date 2025-07-27
```

### 🤖 **Intégration Robotique** (Optionnel)
```bash
# Vérifier la compatibilité robotique
python athalia_unified.py robotics --check

# Configurer Reachy
python athalia_unified.py robotics --setup-reachy
```

---

## 📈 **Métriques de Performance**

### ⚡ **Tests de Performance**
```bash
# Benchmark rapide
python athalia_unified.py benchmark --quick

# Analyse complète
python athalia_unified.py benchmark --full
```

### 📊 **Rapports de Qualité**
```bash
# Rapport de qualité
python athalia_unified.py report --quality

# Rapport de sécurité
python athalia_unified.py report --security
```

---

## 🎯 **Cas d'Usage Typiques**

### 🚀 **Développeur Individuel**
1. **Audit** de votre projet existant
2. **Organisation** automatique du workspace
3. **Tests** et validation de qualité
4. **Sauvegarde** régulière

### 👥 **Équipe de Développement**
1. **Standardisation** des pratiques
2. **Tests** automatisés en CI/CD
3. **Documentation** générée automatiquement
4. **Monitoring** des performances

### 🤖 **Projet Robotique**
1. **Configuration** Reachy
2. **Tests** robotiques spécialisés
3. **Intégration** ROS2
4. **Validation** hardware

---

## 🔧 **Configuration Avancée**

### ⚙️ **Fichier de Configuration**
```yaml
# config/athalia_config.yaml
project:
  name: "mon-projet"
  version: "1.0.0"
  
performance:
  max_memory: "2GB"
  timeout: 300
  
robotics:
  enable: true
  reachy_ip: "192.168.1.100"
```

### 🔑 **Variables d'Environnement**
```bash
export ATHALIA_LOG_LEVEL=INFO
export ATHALIA_CACHE_DIR=/tmp/athalia
export ATHALIA_BACKUP_DIR=~/athalia-backups
```

---

## 🆘 **Dépannage Rapide**

### ❌ **Problèmes Courants**

#### **Import Error**
```bash
# Solution : Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

#### **Permission Denied**
```bash
# Solution : Vérifier les permissions
chmod +x athalia_unified.py
```

#### **Port Already in Use**
```bash
# Solution : Changer le port
python athalia_unified.py dashboard --port 8502
```

### 📞 **Support**
- **Documentation complète :** [Guides](GUIDES/)
- **Dépannage détaillé :** [Troubleshooting](GUIDES/TROUBLESHOOTING.md)
- **FAQ :** [Questions fréquentes](GUIDES/FAQ.md)

---

## 🎉 **Félicitations !**

Vous avez maintenant :
- ✅ **Installé** Athalia avec succès
- ✅ **Testé** les fonctionnalités de base
- ✅ **Compris** les cas d'usage principaux
- ✅ **Configuré** votre environnement

### 🚀 **Prochaines Étapes**

1. **Explorer** la [documentation complète](README.md)
2. **Tester** sur vos projets existants
3. **Configurer** selon vos besoins
4. **Contribuer** à l'amélioration

---

## 📊 **Métriques de Démarrage**

| Action | Temps Estimé | Difficulté |
|--------|--------------|------------|
| Installation | 2 min | ⭐ |
| Premiers tests | 1 min | ⭐ |
| Configuration | 1 min | ⭐⭐ |
| Premier audit | 1 min | ⭐⭐ |

**Total : 5 minutes pour être opérationnel !**

---

*Guide de démarrage rapide Athalia - Version 3.0* 