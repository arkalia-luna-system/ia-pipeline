# 🚀 ATHALIA CORE - Modules Principaux

**Version :** 11.0 (ACTIVE DEVELOPMENT)  
**Date :** 3 août 2025  
**Statut :** Modules opérationnels ✅

---

## 🎯 **PRÉSENTATION**

Les modules principaux d'Athalia, conçus pour l'automatisation intelligente et l'analyse de projets.

### **🏆 ÉTAT ACTUEL (VÉRIFIÉ)**
- **🛡️ Sécurité :** 100% sécurisé ✅
- **🎯 Qualité :** Code professionnel en amélioration continue ✅
- **🧹 Maintenance :** Structure optimisée avec nettoyage automatique ✅
- **🧪 Tests :** **1372 tests collectés** (couverture 10.21%) ✅ **VÉRIFIÉ**
- **📚 Documentation :** Complète et organisée ✅
- **🔄 CI/CD :** Workflows professionnels opérationnels ✅

### **📊 ARCHITECTURE**
- **79 modules** dans athalia_core/ ✅ **COMPTÉ**
- **1372 tests** collectés ✅ **MESURÉ**

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
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd athalia-dev-setup

# Activer l'environnement virtuel
source .venv/bin/activate

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
python -m pytest tests/ -v

# Avec couverture
python -m pytest --cov=athalia_core
```

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature depuis `develop` (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request vers `develop`

## 📄 Licence

Licence MIT - Voir le fichier [LICENSE](../LICENSE) pour plus de détails.

---

*Généré automatiquement par Athalia* - 2025-07-31
