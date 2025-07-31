# 🤖 GUIDE D'INSTALLATION REACHY + ATHALIA

## 🎯 **OBJECTIF**
Configurer ton environnement pour contribuer au projet Reachy avec ton outil Athalia.

## 📋 **PRÉREQUIS**

### **1. Système d'exploitation recommandé**
- **Ubuntu 22.04+** (optimal pour ROS2 Humble)
- **macOS** (pour développement, simulation limitée)
- **Windows avec WSL2** (pour développement)

### **2. Ressources système**
- **RAM** : 8GB minimum, 16GB recommandé
- **Stockage** : 20GB minimum pour ROS2 + Docker
- **CPU** : 4 cœurs minimum

## 🚀 **INSTALLATION ÉTAPE PAR ÉTAPE**

### **Étape 1 : Installation de base**

#### **Ubuntu 22.04+**
```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation des dépendances de base
sudo apt install -y git curl wget build-essential cmake
```

#### **macOS**
```bash
# Installation de Homebrew si pas déjà fait
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installation des dépendances de base
brew install git curl wget cmake
```

### **Étape 2 : Installation de ROS2 Humble**

#### **Ubuntu 22.04+**
```bash
# Ajout du repository ROS2
sudo apt update && sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Installation de ROS2 Humble
sudo apt update
sudo apt install ros-humble-desktop -y

# Configuration de l'environnement
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

#### **macOS (simulation limitée)**
```bash
# Installation via Homebrew
brew install ros2

# Configuration de l'environnement
echo "source /opt/homebrew/share/ros2/setup.zsh" >> ~/.zshrc
source ~/.zshrc
```

### **Étape 3 : Installation de Docker**

#### **Ubuntu 22.04+**
```bash
# Installation de Docker
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Redémarrer la session ou exécuter :
newgrp docker
```

#### **macOS**
```bash
# Installation de Docker Desktop
brew install --cask docker
# Ou télécharger depuis https://www.docker.com/products/docker-desktop
```

### **Étape 4 : Installation de Rust**

#### **Toutes plateformes**
```bash
# Installation de Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Configuration de l'environnement
source ~/.cargo/env
echo "source ~/.cargo/env" >> ~/.bashrc  # ou ~/.zshrc pour macOS
```

### **Étape 5 : Installation d'Athalia avec modules robotiques**

```bash
# Cloner ton projet Athalia
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# Installation des dépendances robotiques
pip install -r config/requirements_robotics.txt

# Vérification de l'installation
python3 athalia_robotics_integration.py . audit
```

## 🔧 **CONFIGURATION POUR REACHY**

### **1. Cloner le dépôt Reachy**
```bash
# Créer un répertoire de travail
mkdir ~/reachy-workspace
cd ~/reachy-workspace

# Cloner le dépôt principal
git clone https://github.com/pollen-robotics/reachy_2023.git
cd reachy_2023

# Fork du dépôt (pour tes contributions)
# 1. Aller sur https://github.com/pollen-robotics/reachy_2023
# 2. Cliquer sur "Fork"
# 3. Cloner ton fork
git clone https://github.com/TON_USERNAME/reachy_2023.git
cd reachy_2023
```

### **2. Configuration de l'environnement ROS2**
```bash
# Source ROS2
source /opt/ros/humble/setup.bash

# Build du workspace Reachy
colcon build

# Source du workspace
source install/setup.bash
```

### **3. Test avec Athalia**
```bash
# Audit complet du projet Reachy
python3 /path/to/athalia/athalia_robotics_integration.py . audit

# Audit spécifique ROS2
python3 /path/to/athalia/athalia_robotics_integration.py . ros2

# Audit Docker
python3 /path/to/athalia/athalia_robotics_integration.py . docker
```

## 🧪 **VALIDATION DE L'INSTALLATION**

### **Test 1 : ROS2**
```bash
# Vérifier que ROS2 fonctionne
ros2 --help

# Lancer un exemple
ros2 run demo_nodes_cpp talker
# Dans un autre terminal : ros2 run demo_nodes_cpp listener
```

### **Test 2 : Docker**
```bash
# Vérifier Docker
docker --version
docker run hello-world
```

### **Test 3 : Rust**
```bash
# Vérifier Rust
rustc --version
cargo --version
```

### **Test 4 : Athalia Robotique**
```bash
# Test complet
python3 athalia_robotics_integration.py . all

# Résultat attendu : Score > 80/100
```

## 🎯 **WORKFLOW DE CONTRIBUTION**

### **1. Préparation d'une contribution**
```bash
# 1. Créer une branche pour ta feature
git checkout -b feature/amélioration-robotique

# 2. Audit avec Athalia
python3 athalia_robotics_integration.py . audit

# 3. Analyser les recommandations
# 4. Implémenter les améliorations
# 5. Tester avec Athalia
python3 athalia_robotics_integration.py . all

# 6. Commit et push
git add .
git commit -m "feat: amélioration robotique validée par Athalia"
git push origin feature/amélioration-robotique
```

### **2. Création d'une Pull Request**
1. Aller sur ton fork GitHub
2. Créer une Pull Request
3. Décrire les améliorations apportées
4. Mentionner l'utilisation d'Athalia pour la validation
5. Attendre la review

## 🔍 **DIAGNOSTIC DES PROBLÈMES**

### **Problème : ROS2 non trouvé**
```bash
# Solution : Vérifier l'installation
ls /opt/ros/humble/
source /opt/ros/humble/setup.bash
```

### **Problème : Docker non accessible**
```bash
# Solution : Vérifier les permissions
sudo usermod -aG docker $USER
newgrp docker
```

### **Problème : Rust non trouvé**
```bash
# Solution : Recharger l'environnement
source ~/.cargo/env
```

### **Problème : Athalia ne fonctionne pas**
```bash
# Solution : Vérifier les dépendances
pip install -r config/requirements_robotics.txt
python3 -c "import yaml, toml, lxml; print('OK')"
```

## 📊 **MÉTRIQUES DE SUCCÈS**

### **Score Athalia attendu pour Reachy :**
- **Score global** : > 85/100
- **ROS2** : Valid
- **Docker** : Prêt
- **Rust** : Optimisé
- **CI/CD** : Fonctionnel

### **Indicateurs de qualité :**
- Tests unitaires : > 80% de couverture
- Documentation : Complète
- Performance : Optimisée
- Sécurité : Validée

## 🚀 **PROCHAINES ÉTAPES**

### **Immédiat (1-2 semaines)**
1. **Tester l'installation** complète
2. **Auditer le dépôt Reachy** avec Athalia
3. **Identifier les améliorations** prioritaires
4. **Proposer une première PR**

### **Court terme (1-2 mois)**
1. **Contribuer régulièrement** au projet Reachy
2. **Améliorer Athalia** selon les besoins
3. **Partager ton expertise** avec la communauté

### **Long terme (3-6 mois)**
1. **Devenir contributeur régulier** Reachy
2. **Étendre Athalia** pour d'autres robots
3. **Créer des outils** pour la communauté robotique

---

## 🎉 **CONCLUSION**

Avec cette configuration, tu es maintenant **parfaitement équipé** pour :

- ✅ **Contribuer au projet Reachy** de manière professionnelle
- ✅ **Utiliser Athalia** pour valider tes contributions
- ✅ **Développer tes compétences** en robotique
- ✅ **Te faire connaître** dans la communauté

**Bonne chance pour tes contributions au projet Reachy !** 🤖✨
