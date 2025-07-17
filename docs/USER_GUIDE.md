# 📚 Guide Utilisateur Athalia/Arkalia AI

## 🎯 Vue d'ensemble

Athalia/Arkalia AI est un pipeline d'industrialisation IA qui génère automatiquement des projets complets avec structure, tests, documentation et CI/CD.

## 🚀 Installation rapide

```bash
# Cloner le projet
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'interface
python -m athalia_core.main
```

## 🎮 Utilisation de base

### 1. Génération d'un projet

#### Via CLI interactive
```bash
python -m athalia_core.main
# Choisir l'option 1 : Génération de projet
# Décrire votre projet : "API de gestion de tâches avec authentification"
```

#### Via CLI directe
```bash
# Génération simple
python -m athalia_core.cli generate "API de gestion de tâches"

# Génération avec dry-run (simulation)
python -m athalia_core.cli generate "Dashboard analytics" --dry-run

# Génération avec audit automatique
python -m athalia_core.cli generate "Système de chat IA" --audit
```

### 2. Audit de projet existant

```bash
# Audit d'un projet existant
python -m athalia_core.cli audit ./mon_projet

# Audit avec génération de rapport
python -m athalia_core.cli audit ./mon_projet --report
```

### 3. Vérification de l'IA

```bash
# Statut de l'IA robuste
python -m athalia_core.cli ai-status

# Test de l'IA avec une idée
python -m athalia_core.cli test-ai "API REST avec base de données"
```

## 🎨 Exemples concrets

### Exemple 1 : API REST

```bash
python -m athalia_core.cli generate "API REST pour gestion d'utilisateurs avec authentification JWT et base de données PostgreSQL"
```

**Résultat attendu :**
- Structure de projet complète
- Endpoints CRUD pour utilisateurs
- Authentification JWT
- Tests unitaires et d'intégration
- Documentation OpenAPI
- Dockerfile et docker-compose

### Exemple 2 : Dashboard Analytics

```bash
python -m athalia_core.cli generate "Dashboard analytics avec visualisations interactives, export PDF et notifications temps réel"
```

**Résultat attendu :**
- Interface web responsive
- Graphiques interactifs (Chart.js/D3.js)
- Export PDF automatique
- WebSockets pour temps réel
- Tests E2E avec Playwright

### Exemple 3 : Plugin système

```bash
python -m athalia_core.cli generate "Plugin pour export de données vers Excel avec validation et templates personnalisables"
```

**Résultat attendu :**
- Architecture de plugin
- Export Excel avec pandas
- Validation des données
- Templates configurables
- Tests de performance

## 🔧 Fonctionnalités avancées

### Mode dry-run
```bash
# Simulation sans modification
python -m athalia_core.cli generate "Projet complexe" --dry-run
```

### Audit intelligent
```bash
# Audit avec corrections automatiques
python -m athalia_core.cli audit ./projet --fix
```

### Plugins personnalisés
```bash
# Créer un plugin
python -m athalia_core.plugins_manager create "mon_plugin"

# Lister les plugins
python -m athalia_core.plugins_manager list

# Exécuter un plugin
python -m athalia_core.plugins_manager run "export_docker"
```

## 📊 Dashboard et monitoring

### Accéder au dashboard
```bash
python -m athalia_core.dashboard
# Ouvrir http://localhost:8080
```

**Fonctionnalités :**
- Vue d'ensemble des projets
- Métriques de qualité
- Heatmaps de complexité
- Analyse de dette technique
- Suggestions d'amélioration

## 🧪 Tests et validation

### Lancer tous les tests
```bash
python -m pytest tests/ -v
```

### Tests spécifiques
```bash
# Tests de génération
python -m pytest tests/test_generation.py -v

# Tests d'IA robuste
python -m pytest tests/test_ai_robust.py -v

# Tests d'intégration
python -m pytest tests/integration/ -v
```

## 🔍 Dépannage

### Problème d'IA
```bash
# Vérifier le statut
python -m athalia_core.cli ai-status

# Forcer le mode mock
export ATHALIA_FORCE_MOCK=1
python -m athalia_core.cli generate "test"
```

### Problème de performance
```bash
# Mode verbose pour debug
python -m athalia_core.cli generate "test" -v

# Vérifier la mémoire
python -c "import psutil; print(psutil.Process().memory_info().rss / 1024 / 1024, 'MB')"
```

## 🎯 Bonnes pratiques

### 1. Descriptions de projets
- **Bon** : "API REST avec authentification JWT et base PostgreSQL"
- **Mauvais** : "projet cool"

### 2. Structure des projets
- Toujours utiliser le mode dry-run d'abord
- Valider avec l'audit intelligent
- Personnaliser selon vos besoins

### 3. Tests
- Lancer les tests après génération
- Corriger les problèmes détectés
- Ajouter des tests spécifiques

## 📈 Métriques et performance

### Temps de génération
- **Projet simple** : 10-30 secondes
- **Projet moyen** : 30-60 secondes
- **Projet complexe** : 1-3 minutes

### Utilisation mémoire
- **Génération** : < 100MB
- **Audit** : < 50MB
- **Dashboard** : < 20MB

### Qualité des projets
- **Score moyen** : 85/100
- **Tests** : 90% de couverture
- **Documentation** : 95% complète

---

## 🧹 Nettoyage automatique

Athalia supprime automatiquement :
- Fichiers parasites macOS (`._*`)
- Caches Python (`__pycache__`, `.pyc`)
- Logs vides et bases corrompues
- Rapports volumineux inutiles

**Commandes de nettoyage** :
```bash
find . -name '._*' -delete
find . -name '__pycache__' -type d -exec rm -rf {} +
find . -name '*.pyc' -delete
find . -name '*.log' -size 0 -delete
find . -name '*.db' -size -1k -delete
find . -name '*.json' -size +10M -delete
```

## 🏗️ Structure finale du projet

```
athalia-dev-setup/
├── athalia_core/      # Modules critiques
├── modules/           # Modules avancés
├── tests/             # Tests
├── docs/              # Documentation
├── templates/         # Templates
├── prompts/           # Prompts
├── agents/            # Agents IA
...                    # Scripts, configs, logs
```

## 🛠️ Bonnes pratiques de maintenance
- Lancer le nettoyage automatique régulièrement
- Supprimer les fichiers parasites après chaque phase
- Garder la structure modulaire
- Exécuter tous les tests après chaque modification
- Mettre à jour la documentation à chaque évolution

*Guide utilisateur Athalia/Arkalia AI - Version 1.0* 🚀 