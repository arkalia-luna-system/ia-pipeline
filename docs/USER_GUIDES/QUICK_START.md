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
python -m venv .venv

# Activer (macOS/Linux)
source .venv/bin/activate

# Activer (Windows)
.venv\Scripts\activate
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
python athalia_unified.py /chemin/vers/votre/projet --action audit

# Exemple
python athalia_unified.py ./mon-projet --action audit
```

### 🧪 **Industrialisation Complète**
```bash
# Industrialisation complète
python athalia_unified.py /chemin/vers/votre/projet

# Mode simulation (dry-run)
python athalia_unified.py /chemin/vers/votre/projet --dry-run
```

### 📊 **Voir le Dashboard**
```bash
# Lancer le dashboard
python athalia_unified.py /chemin/vers/votre/projet --action dashboard

# Ouvrir dans le navigateur
open http://localhost:8501
```

---

## 🛠️ **Fonctionnalités Essentielles**

### 🔧 **Auto-Correction**
```bash
# Correction automatique
python athalia_unified.py /chemin/vers/votre/projet --action fix

# Correction avec mode simulation
python athalia_unified.py /chemin/vers/votre/projet --action fix --dry-run
```

### 🔍 **Scan de Projets**
```bash
# Scanner un répertoire
python athalia_unified.py /chemin/repertoire --scan

# Scan avec mode verbeux
python athalia_unified.py /chemin/repertoire --scan --verbose
```

### 👤 **Profils Utilisateur**
```bash
# Utiliser un profil spécifique
python athalia_unified.py /chemin/projet --utilisateur monnom

# Mode verbeux pour plus de détails
python athalia_unified.py /chemin/projet --verbose
```

---

## 📈 **Métriques de Performance**

### ⚡ **Industrialisation avec Options**
```bash
# Industrialisation complète
python athalia_unified.py /chemin/projet --action complete

# Industrialisation sans audit
python athalia_unified.py /chemin/projet --action complete --no-audit

# Industrialisation sans nettoyage
python athalia_unified.py /chemin/projet --action complete --no-clean
```

### 📊 **Mode Simulation et Auto-Correction**
```bash
# Mode simulation (dry-run)
python athalia_unified.py /chemin/projet --dry-run

# Auto-correction
python athalia_unified.py /chemin/projet --auto-fix

# Combiner les deux
python athalia_unified.py /chemin/projet --dry-run --auto-fix
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
# Solution : Tuer le processus existant
lsof -ti:8501 | xargs kill -9

# Relancer le dashboard
python athalia_unified.py /chemin/projet --action dashboard
```

### 📞 **Support**
- **Documentation complète :** [Guides](GUIDES/)
- **Dépannage détaillé :** [FAQ](GUIDES/FAQ.md)
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
