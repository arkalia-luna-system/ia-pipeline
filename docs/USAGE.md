# 💻 Guide d'Utilisation Athalia/Arkalia

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8+
- Git
- pip

### Installation
```bash
# Cloner le repository
git clone <repository-url>
cd athalia-dev-setup

# Installer les dépendances
pip install -r config/requirements.txt

# Charger les alias
source setup/alias-unified.sh
```

## 🎯 Utilisation Quotidienne

### 1. Génération de Projet
```bash
# Générer un projet simple
ath-generate 'calculatrice simple'

# Générer avec industrialisation automatique
ath-generate 'API REST pour gestion de tâches' -o mon-projet -i

# Mode simulation
ath-generate 'dashboard web interactif' -d
```

### 2. Industrialisation de Projet
```bash
# Industrialisation complète
ath-unified mon-projet --action complete

# Audit uniquement
ath-unified mon-projet --action audit

# Tests uniquement
ath-unified mon-projet --action test
```

### 3. Développement
```bash
# Menu de développement
ath-dev-boost

# Dashboard interactif
ath-dashboard

# Tests rapides
ath-test
```

## 🔧 Fonctionnalités Avancées

### Système Intelligent
```bash
# Charger le système intelligent
ath-intelligent

# Aide contextuelle
ath-help-intelligent

# Diagnostic du système
ath-diagnostic

# Mise à jour automatique
ath-update-intelligent
```

### Coordination Intelligente
```bash
# Analyser le système
ath-coordinator-analyze

# Obtenir des insights
ath-coordinator-insights

# Mettre à jour la documentation
ath-coordinator-update-docs
```

### Modules Spécialisés
```bash
# Auto-correction avancée
ath-auto-correct

# Dashboard unifié
ath-dashboard-unified

# Profils utilisateur avancés
ath-profile-advanced
```

## 📊 Workflow Recommandé

### 1. Création de Projet
```bash
# 1. Générer le projet
ath-generate 'mon-projet' -o ./mon-projet -i

# 2. Vérifier le résultat
cd mon-projet
ls -la

# 3. Tester le projet
python main.py
```

### 2. Développement
```bash
# 1. Charger les alias
source ../setup/alias-unified.sh

# 2. Menu de développement
ath-dev-boost

# 3. Tests continus
ath-test
```

### 3. Industrialisation
```bash
# 1. Industrialisation complète
ath-unified . --action complete

# 2. Vérifier les résultats
open athalia_report_*.json
open analytics_dashboard.html
```

## 🎨 Personnalisation

### Configuration
Le fichier de configuration principal se trouve dans `config/athalia_config.yaml`.

### Alias Personnalisés
Vous pouvez ajouter vos propres alias dans `setup/alias.sh`.

### Prompts Personnalisés
Créez vos prompts dans le dossier `prompts/`.

## 🔗 Ressources

- [Guide des Alias](ALIAS.md) - Tous les alias disponibles
- [Guide du Développeur](DEVELOPER_GUIDE.md) - Développement avancé
- [Guide des Tests](TESTS_GUIDE.md) - Tests et qualité
- [Troubleshooting](TROUBLESHOOTING.md) - Résolution de problèmes

---

*Guide généré automatiquement*
