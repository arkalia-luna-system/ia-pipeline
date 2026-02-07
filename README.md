# 🔧 **ATHALIA** - Plateforme Professionnelle d'Automatisation DevOps

<div align="center">

![Athalia Logo](https://img.shields.io/badge/ATHALIA-DevOps%20Platform-blue?style=for-the-badge&logo=python)

[![Python Version](https://img.shields.io/badge/python-3.10+-brightgreen.svg?style=flat-square)](https://python.org)
[![CI Matrix](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/ci-matrix.yml/badge.svg)](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/ci-matrix.yml)
[![Code Coverage (develop)](https://codecov.io/gh/arkalia-luna-system/ia-pipeline/branch/develop/graph/badge.svg)](https://app.codecov.io/gh/arkalia-luna-system/ia-pipeline/branch/develop)
[![Security](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/security.yml/badge.svg)](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/security.yml)
[![Documentation](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/docs.yml/badge.svg)](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/docs.yml)
[![GitHub Pages](https://img.shields.io/badge/pages-available-brightgreen.svg?style=flat-square)](https://arkalia-luna-system.github.io/ia-pipeline)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

**Plateforme d'automatisation DevOps de niveau entreprise pour la génération sécurisée de projets, le nettoyage intelligent et la gestion d'infrastructure.**

[🔍 **Latest CI Status**](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/ci-matrix.yml) | [📊 **Security Reports**](https://github.com/arkalia-luna-system/ia-pipeline/actions/workflows/security.yml) | [🌐 **Live Demo**](https://arkalia-luna-system.github.io/ia-pipeline)

</div>

---

## 📊 **Aperçu du Projet**

**Athalia** est une plateforme d'automatisation DevOps de niveau entreprise conçue pour la génération sécurisée de projets, le nettoyage intelligent et la gestion d'infrastructure.

🏗️ **Architecture Principale** : Orchestrateur unifié, validateur de sécurité, générateur de projets, nettoyeur automatisé  
🛡️ **Couche de Sécurité** : Validation des commandes (62 commandes sécurisées), audit de sécurité, protection contre les injections  
🔧 **Automatisation** : Tests automatisés, documentation automatisée, gestion du cache  

**[📋 View complete architecture](docs/DEVELOPER/ARCHITECTURE/ATHALIA_ARCHITECTURE_DIAGRAMS.md)**

---

## 🎯 **Métriques Clés** *(Mises à jour automatiquement)*

<div align="center">

| **Composant** | **Valeur** | **Statut** | **Vérifié** |
|:-------------:|:---------:|:----------:|:------------:|
| **🐍 Fichiers Python** | `352 modules` | ![Actif](https://img.shields.io/badge/status-active-brightgreen) | ✅ **COMPTÉS** |
| **📝 Lignes de Code** | `84,876 lignes` | ![Maintenu](https://img.shields.io/badge/status-maintained-blue) | ✅ **MESURÉES** |
| **🧪 Tests** | `2,180 tests` | ![Testé](https://img.shields.io/badge/status-tested-green) | ✅ **COLLECTÉS** |
| **🛡️ Score Sécurité** | `85.3/100` | ![Sécurisé](https://img.shields.io/badge/status-secure-green) | ✅ **CALCULÉ** |
| **📊 Vulnérabilités** | `7 HIGH, 264 MEDIUM` | ![Surveillé](https://img.shields.io/badge/status-monitored-green) | ✅ **ANALYSÉES** |
| **🔧 Scripts Utilitaires** | `60 outils` | ![Disponible](https://img.shields.io/badge/status-available-purple) | ✅ **LISTÉS** |
| **📚 Documentation** | `918 fichiers` | ![Complet](https://img.shields.io/badge/status-complete-yellow) | ✅ **ORGANISÉS** |

</div>

*Métriques collectées automatiquement (dernier audit : 7 février 2026) par le [Collecteur de Métriques Athalia](data/metrics.md)*

**📊 Note importante** : Ces métriques sont générées automatiquement par le script Athalia et reflètent l'état réel du projet. Les valeurs sont mises à jour à chaque exécution du collecteur de métriques.

---

## 🚀 **Démarrage Rapide**

### **Pour les Utilisateurs Finaux**
```bash
# Clone the repository
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# Vérification rapide
python -m athalia_core.demo.quickcheck && echo "✅ Athalia is ready!"
```

### **Pour les Développeurs**
```bash
# Setup development environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run tests
python -m pytest tests/ --cov=athalia_core --cov-report=html

# Qualité du code (optionnel)
python -m ruff check . && python -m ruff format --check . && python -m mypy athalia_core
```

### **Commandes installables (après `pip install -e .`)**
| Commande | Description |
|----------|-------------|
| `athalia` | Menu interactif principal (génération, nettoyage, CI, audit, etc.) |
| `athalia-cli` | Interface CLI avancée |
| `athalia-dashboard` | Lance le dashboard Streamlit des métriques |

### **CLI unifié (sans installation en mode éditable)**
```bash
python bin/core/athalia_unified.py . --action audit    # Audit intelligent
python bin/core/athalia_unified.py . --action complete # Industrialisation complète
python bin/core/athalia_unified.py . --action dashboard # Rapport dashboard
python bin/core/athalia_unified.py . --action api     # Serveur API REST (uvicorn)
python bin/core/athalia_unified.py . --action benchmark # Benchmarks
python bin/core/athalia_unified.py . --action security-dashboard # Dashboard sécurité
python bin/core/athalia_unified.py . --action tutorials # Tutoriels interactifs
python bin/core/athalia_unified.py . --scan            # Scanner le projet
```

**[📋 Complete setup guide](docs/USER_GUIDES/GETTING_STARTED_DETAILED.md)** · **[📋 Modules avancés (API, benchmarks, sécurité)](docs/USER_GUIDES/LANCEMENT_MODULES_AVANCES.md)**

---

## 🏗️ **Structure du Projet**

```
.
├── 🏗️ athalia_core/              # Core modules
│   ├── unified_orchestrator.py   # Main coordinator
│   ├── validation/               # Security validation (CommandSecurityValidator)
│   ├── quality/                  # Code quality tools
│   ├── automation/               # Automation modules
│   └── ...                      # Additional modules
├── 🧪 tests/                     # Test framework
├── 📚 docs/                      # Documentation
├── 📊 dashboard/                 # Monitoring dashboards
├── 🔧 scripts/                   # Utilities
└── ⚙️ bin/                       # CLI tools
```

**[📋 Detailed structure](docs/ARCHITECTURE/STRUCTURE_PROJET_EXPLICATION.md)**

---

## 🆕 **Nouveaux Modules Avancés** *(v12.0.0)*

**Athalia inclut maintenant de nouveaux modules puissants étendant ses capacités :**

- **🚀 Serveur API** : API REST complète avec FastAPI - **INTÉGRÉ** avec composants Athalia réels
- **📊 Système de Benchmark** : Tests de performance avancés - **INTÉGRÉ** avec composants Athalia réels  
- **🛡️ Tableau de Bord Sécurité** : Surveillance de sécurité en temps réel - **INTÉGRÉ** avec composants Athalia réels
- **🎥 Tutoriels Interactifs** : Système d'apprentissage étape par étape (845 lignes) - **INTÉGRÉ** avec composants Athalia réels

**Total nouveau code : 2,673 lignes** - [📋 Documentation complète](docs/API/NEW_MODULES_INDEX.md)

**Note** : Tous les modules avancés (API, Benchmark, Security Dashboard, Video Tutorials) sont maintenant **100% fonctionnels** et utilisent les vrais composants Athalia (orchestrateur, validateur de sécurité, linter, cache, collecteur de métriques).

---

## 📊 **Tableaux de Bord et Interfaces** *(v12.0.0)*

**Athalia fournit plusieurs interfaces et tableaux de bord :**

- **🖥️ Dashboard Principal** : Interface unifiée pour la gestion des projets
- **📈 Dashboard Métriques** : Visualisation des performances et statistiques
- **🛡️ Dashboard Sécurité** : Surveillance en temps réel de la sécurité
- **📊 Dashboard Benchmark** : Rapports de performance détaillés
- **🎯 Dashboard Qualité** : Analyse de la qualité du code
- **🔍 Dashboard Audit** : Rapports d'audit et de validation
- **📚 Dashboard Documentation** : Gestion et visualisation de la documentation
- **⚡ Dashboard Performance** : Monitoring des performances système
- **🔄 Dashboard Cache** : Gestion et statistiques du cache
- **🧪 Dashboard Tests** : Couverture et résultats des tests
- **🔧 Dashboard Utilitaires** : Outils et scripts disponibles
- **📋 Dashboard Projets** : Gestion des projets générés
- **🎨 Dashboard Templates** : Gestion des templates et blueprints

**Total : 130+ fichiers HTML et 15+ dashboards fonctionnels** - Chaque dashboard est spécialisé et intégré au système Athalia.

---

## 🔒 **Fonctionnalités de Sécurité**

- ✅ **Validation des Commandes** : Liste blanche de 62 commandes sécurisées
- ✅ **Protection contre les Injections** : Sécurité complète des sous-processus
- ✅ **Exécution Zero-Trust** : Toutes les commandes validées
- ✅ **Traçabilité** : Journalisation de sécurité complète

**[📋 Security documentation](docs/DEVELOPER/GUIDES/SECURITY_LINTING_GUIDE.md)**

---

## 📚 **Documentation**

**Athalia fournit une documentation complète pour tous les types d'utilisateurs :**

👤 **Utilisateurs** : Démarrage Rapide, Guide Utilisateur, FAQ, Dépannage  
👨‍💻 **Développeurs** : Architecture, Référence API, Contribution, Tests  
🎯 **Spécialisés** : Sécurité, Analytique, Automatisation, Performance

**[📋 Complete documentation structure](docs/DEVELOPER/ARCHITECTURE/ATHALIA_ARCHITECTURE_DIAGRAMS.md#structure-de-documentation)**  
**All guides available in the `/docs` directory**

---

## 🚀 **Pour Commencer**

**Athalia s'adapte à tous les types d'utilisateurs avec des guides spécialisés et des exemples pratiques.**

👥 **Utilisateurs Finaux** : Installation (5 min), Exemples (2 min), Exploration des fonctionnalités  
👨‍💻 **Développeurs** : Documentation d'architecture, Référence API, Directives de contribution  
🖥️ **Administrateurs Système** : Configuration de sécurité, Guide de déploiement, Intégration

**[📋 Complete getting started guide](docs/USER_GUIDES/GETTING_STARTED_DETAILED.md)**

---

## 📞 **Support et Communauté**

<div align="center">

| **Ressource** | **Objectif** | **Accès** |
|:-------------|:------------|:-----------|
| 📖 **Documentation** | Guides complets | Répertoire `/docs` |
| 🐛 **Problèmes** | Signalement de bugs | GitHub Issues |
| 💬 **Discussions** | Support communautaire | GitHub Discussions |
| 📧 **Sécurité** | Rapports de vulnérabilités | Contact sécurité |

</div>

---

## 📄 **Licence et Légal**

**Licence MIT** - Voir le fichier [LICENSE](LICENSE) pour les termes complets.

Ce projet est publié sous licence MIT, permettant l'utilisation commerciale et non-commerciale avec attribution appropriée.

---

<div align="center">

## 🎯 **Plateforme DevOps Athalia**

**Automatisation professionnelle pour les équipes de développement.**

*Construite avec un focus sur la sécurité, la fiabilité et l'expérience développeur.*

[![GitHub](https://img.shields.io/badge/GitHub-arkalia--luna--system%2Fia--pipeline-black?style=for-the-badge&logo=github)](https://github.com/arkalia-luna-system/ia-pipeline)
[![Documentation](https://img.shields.io/badge/Docs-Complete-blue?style=for-the-badge&logo=gitbook)](docs/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=open-source-initiative)](LICENSE)

**Dernière Mise à Jour :** 7 Février 2026 | **Version :** 12.0.0 | **Statut :** Prêt pour la Production

</div>
