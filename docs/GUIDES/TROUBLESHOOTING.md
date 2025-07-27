# 🆘 Guide de Dépannage - Athalia

**Date de mise à jour :** 27 juillet 2025  
**Version :** 3.0 - Dépannage Professionnel

---

## 🎯 **Vue d'Ensemble**

Ce guide vous aide à résoudre les problèmes courants et à diagnostiquer les erreurs dans Athalia.

---

## 🔍 **Diagnostic Rapide**

### ⚡ **Vérification Système**
```bash
# Vérifier l'installation
python athalia_unified.py --version

# Vérifier la configuration
python athalia_unified.py config --validate

# Vérifier les modules
python athalia_unified.py modules --check

# Vérifier la connectivité
python athalia_unified.py network --test
```

### 📊 **Statut du Système**
```bash
# Statut complet
python athalia_unified.py status

# Logs en temps réel
python athalia_unified.py logs --follow

# Métriques système
python athalia_unified.py metrics --system
```

---

## ❌ **Problèmes Courants**

### 🐍 **Erreurs Python**

#### **ImportError: No module named 'athalia_core'**
```bash
# Solution 1 : Vérifier l'environnement virtuel
source venv/bin/activate
pip list | grep athalia

# Solution 2 : Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall

# Solution 3 : Vérifier le PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python -c "import athalia_core; print('✅ OK')"
```

#### **ModuleNotFoundError: No module named 'yaml'**
```bash
# Installer les dépendances manquantes
pip install pyyaml

# Ou réinstaller toutes les dépendances
pip install -r requirements.txt
```

#### **PermissionError: [Errno 13] Permission denied**
```bash
# Vérifier les permissions
ls -la athalia_unified.py
chmod +x athalia_unified.py

# Vérifier les permissions des dossiers
chmod -R 755 athalia_core/
chmod -R 755 bin/
```

### 🔧 **Erreurs de Configuration**

#### **FileNotFoundError: config.yaml not found**
```bash
# Créer la configuration par défaut
mkdir -p ~/.athalia
cp config/athalia_config.yaml ~/.athalia/config.yaml

# Ou utiliser la configuration par défaut
python athalia_unified.py config --init
```

#### **YAMLError: Invalid YAML syntax**
```bash
# Valider la syntaxe YAML
python athalia_unified.py config --validate

# Corriger la configuration
python athalia_unified.py config --edit
```

#### **ConfigurationError: Invalid configuration**
```bash
# Réinitialiser la configuration
python athalia_unified.py config --reset

# Utiliser la configuration par défaut
python athalia_unified.py config --default
```

### 💾 **Erreurs de Mémoire et Performance**

#### **MemoryError: Not enough memory**
```bash
# Augmenter la limite mémoire
export ATHALIA_MAX_MEMORY="8GB"
python athalia_unified.py audit . --memory-limit 8GB

# Réduire la charge de travail
python athalia_unified.py audit . --quick --max-files 1000
```

#### **TimeoutError: Operation timed out**
```bash
# Augmenter le timeout
python athalia_unified.py audit . --timeout 1800

# Utiliser le mode rapide
python athalia_unified.py audit . --quick
```

#### **ResourceWarning: Unclosed file**
```bash
# Nettoyer les ressources
python athalia_unified.py clean --force

# Redémarrer le processus
pkill -f athalia
python athalia_unified.py audit .
```

### 🌐 **Erreurs de Réseau et Connectivité**

#### **ConnectionError: Failed to connect**
```bash
# Vérifier la connectivité
python athalia_unified.py network --check

# Mode hors ligne
python athalia_unified.py audit . --offline

# Vérifier les proxies
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"
```

#### **SSLError: Certificate verify failed**
```bash
# Désactiver la vérification SSL (temporaire)
export ATHALIA_SSL_VERIFY="false"

# Ou configurer les certificats
export SSL_CERT_FILE="/path/to/cert.pem"
```

### 🤖 **Erreurs Robotiques**

#### **ReachyConnectionError: Cannot connect to Reachy**
```bash
# Vérifier l'IP de Reachy
python athalia_unified.py robotics --check-reachy

# Configurer l'IP manuellement
python athalia_unified.py robotics --setup-reachy --ip 192.168.1.100

# Mode simulation
python athalia_unified.py robotics --simulation
```

#### **ROS2Error: ROS2 not found**
```bash
# Vérifier l'installation ROS2
which ros2

# Installer ROS2 (Ubuntu)
sudo apt update
sudo apt install ros-humble-desktop

# Configurer le chemin ROS2
export ROS2_PATH="/opt/ros/humble"
```

---

## 🔧 **Problèmes Avancés**

### 📊 **Erreurs de Dashboard**

#### **PortAlreadyInUseError: Port 8501 is already in use**
```bash
# Changer le port
python athalia_unified.py dashboard --port 8502

# Tuer le processus existant
lsof -ti:8501 | xargs kill -9

# Vérifier les processus
ps aux | grep streamlit
```

#### **StreamlitError: Failed to start dashboard**
```bash
# Réinstaller Streamlit
pip install streamlit --upgrade

# Vérifier les dépendances
pip install -r requirements.txt

# Mode debug
python athalia_unified.py dashboard --debug
```

### 🧪 **Erreurs de Tests**

#### **TestFailureError: Tests failed**
```bash
# Lancer les tests en mode verbose
python athalia_unified.py test --verbose

# Lancer un test spécifique
python athalia_unified.py test --module audit

# Ignorer les tests échoués
python athalia_unified.py test --ignore-failures
```

#### **CoverageError: Coverage below threshold**
```bash
# Augmenter le seuil de couverture
python athalia_unified.py test --coverage-threshold 70

# Générer un rapport de couverture
python athalia_unified.py test --coverage-report
```

### 💾 **Erreurs de Sauvegarde**

#### **BackupError: Failed to create backup**
```bash
# Vérifier l'espace disque
df -h

# Nettoyer l'espace
python athalia_unified.py clean --force

# Changer le dossier de sauvegarde
export ATHALIA_BACKUP_DIR="/autre/chemin"
```

#### **RestoreError: Backup not found**
```bash
# Lister les sauvegardes disponibles
python athalia_unified.py backup --list

# Restaurer une sauvegarde spécifique
python athalia_unified.py restore --backup-id 20250727_143022
```

---

## 🛠️ **Outils de Diagnostic**

### 📋 **Commandes de Diagnostic**
```bash
# Diagnostic complet
python athalia_unified.py diagnose

# Diagnostic système
python athalia_unified.py diagnose --system

# Diagnostic réseau
python athalia_unified.py diagnose --network

# Diagnostic performance
python athalia_unified.py diagnose --performance
```

### 📊 **Rapports de Diagnostic**
```bash
# Générer un rapport complet
python athalia_unified.py diagnose --report diagnostic_report.json

# Rapport HTML
python athalia_unified.py diagnose --report-html diagnostic_report.html

# Rapport détaillé
python athalia_unified.py diagnose --verbose --report detailed_report.json
```

### 🔍 **Logs et Debugging**
```bash
# Activer le mode debug
export ATHALIA_LOG_LEVEL="DEBUG"
python athalia_unified.py audit . --debug

# Suivre les logs en temps réel
python athalia_unified.py logs --follow --level DEBUG

# Analyser les logs
python athalia_unified.py logs --analyze --output log_analysis.json
```

---

## 🔄 **Récupération et Réparation**

### 🔧 **Réparation Automatique**
```bash
# Réparation complète
python athalia_unified.py repair --full

# Réparation des modules
python athalia_unified.py repair --modules

# Réparation de la configuration
python athalia_unified.py repair --config
```

### 🔄 **Restauration Système**
```bash
# Restaurer depuis une sauvegarde
python athalia_unified.py restore --system

# Réinitialiser complètement
python athalia_unified.py reset --full

# Réinstaller les dépendances
python athalia_unified.py repair --dependencies
```

### 🧹 **Nettoyage Complet**
```bash
# Nettoyage complet
python athalia_unified.py clean --all

# Nettoyage des caches
python athalia_unified.py clean --cache

# Nettoyage des logs
python athalia_unified.py clean --logs
```

---

## 📞 **Support et Aide**

### 🆘 **Quand Demander de l'Aide**

#### **Problèmes Critiques**
- ❌ **Système ne démarre pas**
- ❌ **Perte de données**
- ❌ **Erreurs de sécurité**
- ❌ **Problèmes de performance majeurs**

#### **Informations à Fournir**
```bash
# Collecter les informations système
python athalia_unified.py diagnose --report system_info.json

# Collecter les logs
python athalia_unified.py logs --export logs_export.json

# Collecter la configuration
python athalia_unified.py config --export config_export.yaml
```

### 📋 **Checklist de Diagnostic**
- [ ] **Version d'Athalia** : `python athalia_unified.py --version`
- [ ] **Version Python** : `python --version`
- [ ] **Système d'exploitation** : `uname -a`
- [ ] **Espace disque** : `df -h`
- [ ] **Mémoire disponible** : `free -h`
- [ ] **Logs d'erreur** : `python athalia_unified.py logs --errors`
- [ ] **Configuration** : `python athalia_unified.py config --validate`

### 🌐 **Ressources de Support**
- **Documentation :** [Guides complets](../README.md)
- **FAQ :** [Questions fréquentes](FAQ.md)
- **API :** [Documentation API](../API/INDEX.md)
- **Issues :** [GitHub Issues](https://github.com/arkalia-luna-system/ia-pipeline/issues)
- **Discussions :** [GitHub Discussions](https://github.com/arkalia-luna-system/ia-pipeline/discussions)

---

## 🎯 **Prévention des Problèmes**

### ✅ **Bonnes Pratiques**
1. **Toujours utiliser un environnement virtuel**
2. **Vérifier la configuration avant utilisation**
3. **Faire des sauvegardes régulières**
4. **Monitorer les performances**
5. **Mettre à jour régulièrement**

### 🔄 **Maintenance Préventive**
```bash
# Maintenance quotidienne
python athalia_unified.py maintenance --daily

# Maintenance hebdomadaire
python athalia_unified.py maintenance --weekly

# Maintenance mensuelle
python athalia_unified.py maintenance --monthly
```

---

## 🎉 **Conclusion**

Ce guide couvre les problèmes les plus courants. Si votre problème persiste :

1. **Consultez** la [FAQ](FAQ.md)
2. **Recherchez** dans les [Issues GitHub](https://github.com/arkalia-luna-system/ia-pipeline/issues)
3. **Créez** une nouvelle issue avec toutes les informations

---

*Guide de dépannage Athalia - Version 3.0 - Dépannage Professionnel* 