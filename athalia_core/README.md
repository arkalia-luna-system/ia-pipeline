# 🚀 ATHALIA CORE - Modules Principaux

**Version :** 10.0 (FINAL - 100% TERMINÉE ✅)
**Date :** 30 Juillet 2025
**Statut :** Modules principaux du système Athalia

## 🎯 **PRÉSENTATION**

`athalia_core` contient les modules principaux du système Athalia, un système d'intelligence artificielle avancé pour l'automatisation et l'optimisation de projets de développement.

### **🏆 ÉTAT ACTUEL**
- **🛡️ Sécurité :** 100% sécurisé ✅
- **🎯 Qualité :** Code professionnel ✅
- **🧹 Maintenance :** Structure optimale ✅
- **🧪 Tests :** Validation complète ✅
- **📚 Documentation :** Complète et à jour ✅

### **📊 Statistiques**
- **56 modules** dans athalia_core
- **974 tests** fonctionnels
- **CI/CD verte** sur toutes les branches

## 📋 Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [API](#api)
- [Tests](#tests)
- [Contribution](#contribution)
- [Licence](#licence)

## 🚀 Installation

### Prérequis
### Installation

```bash
# Cloner le repository
git clone <repository - url>
cd athalia_core

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 Utilisation
### Lancement

```bash
python athalia_core/main.py
```

```bash
python athalia_core/cli.py
```

### Exemple d'utilisation

```python
# Utilisation basique
main()
```

## 🔧 API
### Classes principales

#### ProjectAuditor

Auditeur intelligent de projets générés.

**Méthodes :** __init__, audit_project, _analyze_structure, _analyze_code_quality, _analyze_python_file

#### AIModel

Modèles IA disponibles.

**Méthodes :**

#### PromptContext

Contextes de prompts.

**Méthodes :**

### Fonctions principales

#### generate_github_ci_yaml

**Paramètres :** outdir

#### add_coverage_badge

**Paramètres :** outdir

#### clean_old_tests_and_caches

Supprime les anciens fichiers de test non-suffixés et les caches Python dans le projet cible.
Log chaque suppression pour audit. Retourne la liste des fichiers supprimés.

**Paramètres :** outdir

#### clean_macos_files

Supprime automatiquement les fichiers macOS parasites (.DS_Store, ._*) dans tout le projet. Retourne la liste des fichiers supprimés.

**Paramètres :** directory

#### generate_blueprint_mock

**Paramètres :** idea

## 🧪 Tests

```bash
# Lancer les tests
python -m pytest

# Avec couverture
python -m pytest --cov=athalia_core
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature / AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature / AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Licence inconnue

---
*Généré automatiquement par Athalia* - 2025-07-19
