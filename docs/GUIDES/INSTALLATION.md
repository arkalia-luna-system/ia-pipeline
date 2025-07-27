# 📦 Guide d'Installation - Athalia

**Date de mise à jour :** 27 juillet 2025  
**Version :** 3.0 - Installation Professionnelle

---

## 🎯 **Vue d'Ensemble**

Ce guide vous accompagne dans l'installation complète d'Athalia, un système d'industrialisation IA avancé pour projets de développement.

---

## 📋 **Prérequis Système**

### ✅ **Système d'Exploitation**
- **macOS :** 10.15+ (Catalina)
- **Linux :** Ubuntu 20.04+, CentOS 8+, Debian 11+
- **Windows :** Windows 10+ avec WSL2 recommandé

### 🐍 **Python et Environnement**
- **Python :** 3.8, 3.9, 3.10, 3.11, 3.12
- **pip :** 21.0+
- **venv :** Inclus avec Python 3.3+

### 🔧 **Outils Requis**
- **Git :** 2.20+
- **Make :** 4.0+ (Linux/macOS)
- **curl/wget :** Pour téléchargements

### 💾 **Espace Disque**
- **Minimum :** 2GB
- **Recommandé :** 5GB+
- **Cache :** 1GB supplémentaire

---

## 🚀 **Installation Rapide**

### 1️⃣ **Cloner le Repository**
```bash
# Cloner le projet
git clone https://github.com/arkalia-luna-system/ia-pipeline.git

# Accéder au dossier
cd athalia-dev-setup

# Vérifier la structure
ls -la
```

### 2️⃣ **Créer l'Environnement Virtuel**
```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement (macOS/Linux)
source venv/bin/activate

# Activer l'environnement (Windows)
venv\Scripts\activate

# Vérifier l'activation
which python
# Doit afficher : /chemin/vers/athalia-dev-setup/venv/bin/python
```

### 3️⃣ **Installer les Dépendances**
```bash
# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances principales
pip install -r requirements.txt

# Installer les dépendances de développement (optionnel)
pip install -r requirements-dev.txt 2>/dev/null || echo "Fichier dev non trouvé"
```

### 4️⃣ **Vérifier l'Installation**
```bash
# Tester l'import principal
python -c "import athalia_core; print('✅ Import réussi')"

# Vérifier la CLI
python athalia_unified.py --help

# Tester un audit rapide
python athalia_unified.py . --action audit --dry-run
```

---

## ⚙️ **Configuration Avancée**

### 📁 **Structure de Configuration**
```bash
# Créer le dossier de configuration
mkdir -p ~/.athalia

# Copier la configuration par défaut (si elle existe)
cp config/athalia_config.yaml ~/.athalia/config.yaml 2>/dev/null || echo "Configuration par défaut non trouvée"
```

### 🔧 **Fichier de Configuration Principal**
```yaml
# ~/.athalia/config.yaml
project:
  name: "athalia-dev-setup"
  version: "3.0.0"
  environment: "development"

paths:
  workspace: "/chemin/vers/votre/workspace"
  backups: "~/athalia-backups"
  logs: "~/athalia-logs"
  cache: "/tmp/athalia-cache"

performance:
  max_memory: "4GB"
  max_cpu_cores: 8
  timeout: 300
  cache_size: "1GB"

logging:
  level: "INFO"
  format: "detailed"
  rotation: "daily"
  retention: "30 days"

robotics:
  enabled: false
  reachy_ip: "192.168.1.100"
  ros2_path: "/opt/ros/humble"

security:
  encryption: true
  backup_encryption: true
  ssl_verify: true
```

### 🔑 **Variables d'Environnement**
```bash
# Ajouter à votre ~/.bashrc ou ~/.zshrc
export ATHALIA_HOME="/chemin/vers/athalia-dev-setup"
export ATHALIA_CONFIG="$HOME/.athalia/config.yaml"
export ATHALIA_LOG_LEVEL="INFO"
export ATHALIA_CACHE_DIR="/tmp/athalia-cache"
export ATHALIA_BACKUP_DIR="$HOME/athalia-backups"

# Recharger la configuration
source ~/.bashrc  # ou source ~/.zshrc
```

---

## 🧪 **Tests de Validation**

### ✅ **Tests Automatiques**
```bash
# Lancer les tests avec pytest
python -m pytest tests/ -v

# Tests avec couverture
python -m pytest tests/ --cov=athalia_core

# Tests spécifiques
python -m pytest tests/test_audit.py -v
python -m pytest tests/test_performance.py -v
```

### 🔍 **Validation Manuelle**
```bash
# Vérifier les modules principaux
python -c "
import athalia_core.audit
import athalia_core.performance_analyzer
import athalia_core.analytics
print('✅ Tous les modules importés avec succès')
"

# Tester les fonctionnalités CLI
python athalia_unified.py --help
python athalia_unified.py . --action audit
python athalia_unified.py . --scan
```

---

## 🤖 **Configuration Robotique** (Optionnel)

### 🔧 **Prérequis Robotiques**
```bash
# Installer ROS2 (Ubuntu)
sudo apt update
sudo apt install ros-humble-desktop

# Installer les dépendances Python robotiques
pip install -r requirements-robotics.txt 2>/dev/null || echo "Fichier robotics non trouvé"
```

### 🤖 **Configuration Reachy**
```bash
# Vérifier la connectivité Reachy manuellement
ping 192.168.1.100

# Ou utiliser un script de test
python -c "import socket; print('Reachy accessible' if socket.socket().connect_ex(('192.168.1.100', 22)) == 0 else 'Reachy non accessible')"
```

---

## 📊 **Dashboard et Interface Web**

### 🚀 **Lancement du Dashboard**
```bash
# Lancer le dashboard
python athalia_unified.py /chemin/projet --action dashboard

# Lancer avec utilisateur spécifique
python athalia_unified.py /chemin/projet --action dashboard --utilisateur monnom

# Lancer en mode verbeux
python athalia_unified.py /chemin/projet --action dashboard --verbose
```

### 🌐 **Accès au Dashboard**
- **URL :** http://localhost:8501
- **Interface :** Interface Streamlit moderne
- **Fonctionnalités :** Métriques en temps réel, graphiques, rapports

---

## 🔧 **Installation pour Développement**

### 🛠️ **Dépendances de Développement**
```bash
# Installer les outils de développement
pip install -r requirements-dev.txt

# Installer les outils de test
pip install pytest pytest-cov pytest-mock
pip install black flake8 mypy

# Installer les outils de documentation
pip install sphinx sphinx-rtd-theme
```

### 📝 **Configuration de Développement**
```bash
# Configurer Git hooks
cp scripts/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit

# Configurer l'environnement de développement
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export ATHALIA_DEV_MODE=true
```

---

## 🆘 **Dépannage**

### ❌ **Problèmes Courants**

#### **Import Error - Module not found**
```bash
# Solution : Vérifier l'environnement virtuel
source venv/bin/activate
pip install -r requirements.txt --force-reinstall
```

#### **Permission Denied**
```bash
# Solution : Vérifier les permissions
chmod +x athalia_unified.py
chmod +x bin/*.py
```

#### **Port Already in Use**
```bash
# Solution : Vérifier les processus
lsof -i :8501
kill -9 <PID>

# Ou utiliser un autre port pour le dashboard
# (Configuration dans le fichier de config)
```

#### **Memory Error**
```bash
# Solution : Augmenter la mémoire
export ATHALIA_MAX_MEMORY="8GB"

# Ou utiliser le mode dry-run pour économiser la mémoire
python athalia_unified.py /chemin/projet --dry-run
```

### 📞 **Support et Aide**
- **Documentation :** [Guides complets](../README.md)
- **Dépannage :** [FAQ](FAQ.md)
- **FAQ :** [Questions fréquentes](FAQ.md)
- **Issues :** [GitHub Issues](https://github.com/arkalia-luna-system/ia-pipeline/issues)

---

## ✅ **Validation Finale**

### 🎯 **Checklist d'Installation**
- [ ] Repository cloné avec succès
- [ ] Environnement virtuel créé et activé
- [ ] Dépendances installées sans erreur
- [ ] Configuration créée et validée
- [ ] Tests de base passés
- [ ] CLI fonctionnelle
- [ ] Dashboard accessible
- [ ] Variables d'environnement configurées

### 🚀 **Test Final**
```bash
# Test complet d'installation
python athalia_unified.py . --action audit --dry-run

# Résultat attendu : ✅ Installation validée avec succès
```

---

## 🎉 **Installation Terminée !**

Votre installation d'Athalia est maintenant **complète et fonctionnelle** !

### 🚀 **Prochaines Étapes**
1. **Explorer** le [Guide de démarrage rapide](../QUICK_START.md)
2. **Configurer** selon vos besoins spécifiques
3. **Tester** sur vos projets existants
4. **Contribuer** à l'amélioration du système

---

*Guide d'installation Athalia - Version 3.0 - Installation Professionnelle*
