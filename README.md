# athalia-dev-setup

# athalia-dev-setup

## 📋 Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [API](#api)
- [Tests](#tests)
- [Contribution](#contribution)
- [Licence](#licence)

## 🚀 Installation

### Prérequis
**Python :**
- requests>=2.28.0
- pyyaml>=6.0
- jinja2>=3.1.0
- click>=8.1.0
- rich>=12.0.0

### Installation

```bash
# Cloner le repository
git clone <repository - url>
cd athalia-dev-setup

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 Utilisation
### Exemple d'utilisation

```python
# Utilisation basique
main()
```

## 🔧 API
### Classes principales

#### AthaliaOrchestrator

**Méthodes :** industrialize_project, audit_project, scan_projects

#### ProjectAuditor

Auditeur intelligent de projets générés.

**Méthodes :** __init__, audit_project, _analyze_structure, _analyze_code_quality, _analyze_python_file

#### TestLoggingSystem

Tests pour le système de logging d'Athalia

**Méthodes :** setup_method, teardown_method, test_basic_logging_creation, test_advanced_logging_import, test_advanced_logging_functionality

### Fonctions principales

#### main

Fonction principale du CLI unifié

#### industrialize_project

**Paramètres :** project_path, config

#### audit_project

**Paramètres :** project_path

#### scan_projects

**Paramètres :** project_path

#### audit_project_intelligent

Fonction principale pour l'audit intelligent.

**Paramètres :** project_path

## 🧪 Tests

```bash
# Lancer les tests
python -m pytest

# Avec couverture
python -m pytest --cov=athalia-dev-setup
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature / AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature / AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Voir fichier LICENSE

---
*Généré automatiquement par Athalia* - 2025-07-29
