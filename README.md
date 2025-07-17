# 🌟 Athalia/Arkalia - Pipeline d’Industrialisation IA

[![Python 3.1ttps://img.shields.io/badge/python-3.1+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-52passed-brightgreen.svg)](https://github.com/arkalia-luna-system/ia-pipeline)
[![PyPI](https://img.shields.io/badge/PyPI-athalia--ai-blue.svg)](https://pypi.org/project/athalia-ai/)

> **Pipeline complet dindustrialisation IA** pour la génération automatique de projets, tests, documentation, audit, CI/CD et intégration dIA robuste locale.

## 🚀 Installation

```bash
# Installation depuis PyPI
pip install athalia-ai

# Ou installation depuis le code source
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd athalia-dev-setup
pip install -e .
```

## ⚡ Utilisation rapide

```bash
# Interface interactive
athalia

# Génération directe
athalia generate "Application web moderne avec React et Node.js"

# Audit dun projet
athalia audit ./mon_projet
```

## 🎯 Fonctionnalités principales

### 🤖 IA Robuste avec Fallback
- **Détection automatique** des modèles IA disponibles
- **Chaîne de fallback intelligente** (Ollama → Claude → GPT)
- **Classification de complexité** des projets
- **Prompts dynamiques** adaptés au contexte
- **Gestion d'erreurs robuste**

### 🚀 Génération de projets
- **Génération complète** à partir dune description
- **Templates multiples** (React, Vue, Python, Java, etc.)
- **Gestion intelligente** des fichiers existants
- **Options avancées** (framework, database, auth, etc.)
- **Backup automatique** des fichiers

### 🔍 Audit intelligent
- **Audit multi-dimensionnel** (structure, qualité, sécurité, performance)
- **Rapports détaillés** avec recommandations
- **Détection automatique** des vulnérabilités
- **Scores de qualité** normalisés

### 📊 Analytics et métriques
- **Analyse de complexité** des projets
- **Heatmaps interactives**
- **Dette technique** automatisée
- **Rapports HTML** générés

### 🔌 Système de plugins
- **Architecture modulaire** extensible
- **Plugins inclus** (Docker, Security, Documentation)
- **API simple** pour créer des plugins
- **Gestion automatique** des dépendances

## 🛠️ Configuration

### Prérequis
- Python310+
- Git
- Ollama (pour l'IA locale)

### Configuration Ollama
```bash
# Installer Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Télécharger le modèle Mistral
ollama pull mistral

# Vérifier l'installation
ollama list
```

### Variables d'environnement
Créez un fichier `.env` :
```bash
# API Keys (optionnelles pour l'IA locale)
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Configuration Ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral

# Configuration du projet
ATHALIA_LOG_LEVEL=INFO
ATHALIA_CACHE_DIR=./cache
```

## 📚 Documentation

- **[Guide utilisateur](docs/USER_GUIDE.md)** - Guide complet dutilisation
- **[Guide développeur](docs/DEVELOPER_GUIDE.md)** - Développement et contribution
- **[Documentation API](docs/API_REFERENCE.md)** - Référence API complète
- **[Guide des plugins](docs/PLUGINS_GUIDE.md)** - Création et utilisation de plugins
- **[FAQ](docs/FAQ.md)** - Questions fréquentes et dépannage

## 🧪 Tests

```bash
# Tous les tests
python -m pytest tests/ -v

# Tests avec couverture
python -m pytest tests/ --cov=athalia_core --cov-report=html

# Tests spécifiques
python -m pytest tests/test_ai_robust.py -v
```

## 🔌 Plugins inclus

### Docker Export Plugin
```bash
# Exporter un projet vers Docker
athalia plugins run docker_export --project-path ./mon_projet
```

### Security Audit Plugin
```bash
# Audit de sécurité automatisé
athalia plugins run security_audit --project-path ./mon_projet
```

### Documentation Generator Plugin
```bash
# Générer de la documentation
athalia plugins run doc_generator --project-path ./mon_projet --doc-type README
```

## 🎯 Exemples d'utilisation

### Génération dun projet complet
```python
from athalia_core import RobustAI, ProjectGenerator, AuditIntelligent

# Initialiser l'IA robuste
ai = RobustAI()

# Générer le projet
generator = ProjectGenerator(ai_robust=ai)
result = generator.generate_blueprint(
    description="API REST moderne avec authentification",
    output_dir="./api_project",
    options=[object Object]        backend":python",
        framework": fastapi",
       database": "postgresql,
     auth": "jwt",
     tests: True,
      docs: True
    }
)

# Auditer le projet généré
auditor = AuditIntelligent(ai_robust=ai)
audit_report = auditor.audit_project(./api_project)print(f"Projet généré avec succès: {result[status']})
print(f"Score d'audit: {audit_report[overall_score]}/100")```

### Analytics de plusieurs projets
```python
from athalia_core import Analytics

analytics = Analytics()

# Analyser plusieurs projets
projects = ["./project1",./project2./project3
all_data =[object Object]roject in projects:
    data = analytics.analyze_project(project)
    all_dataproject] = data

# Générer un rapport comparatif
analytics.generate_html_report(all_data, "./comparison_report.html")
```

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
├── athalia_core/      # Modules critiques (audit, génération, correction, CI/CD, etc.)
├── modules/           # Modules avancés (auto-correction, profils, dashboard, orchestrateur)
├── tests/             # Tests unitaires et d’intégration
├── docs/              # Documentation complète
├── templates/         # Templates de projets
├── prompts/           # Prompts IA
├── agents/            # Agents IA spécialisés
├── ...                # Scripts principaux, configs, logs, etc.
```

## 🛠️ Bonnes pratiques de maintenance
- Lancer le nettoyage automatique régulièrement
- Supprimer les fichiers parasites après chaque phase
- Garder la structure modulaire (pas de code spaghetti)
- Exécuter tous les tests après chaque modification
- Mettre à jour la documentation à chaque évolution

## 🚀 Commandes principales

### Créer un projet IA performant
```bash
python -m athalia_core.cli generate "Mon idée" --output ./mon-projet
```

### Corriger/améliorer un projet existant
```bash
python athalia_unified.py /chemin/projet --action correction --dry-run
```

### Auditer un projet
```bash
python -m athalia_core.cli audit /chemin/projet
```

### Dashboard, profils, scan
```bash
python athalia_unified.py /chemin/projet --action dashboard --utilisateur moi
python athalia_unified.py /chemin/projet --action profil --utilisateur moi
python athalia_unified.py /chemin/repertoire --scan
```

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- **Ollama** pour l'IA locale
- **Anthropic** pour Claude
- **OpenAI** pour GPT
- **La communauté open source** pour les outils et bibliothèques

---

**🌟 Athalia/Arkalia** - Industrialisez vos projets avec l'IA !

*Dernière mise à jour : $(date)*
