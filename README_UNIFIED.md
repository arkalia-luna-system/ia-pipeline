# 🚀 Athalia Unified - Industrialisation IA Complète

## 📋 Vue d'ensemble

**Athalia Unified** est la version unifiée qui combine toutes les fonctionnalités d'Athalia dans un seul pipeline complet d'industrialisation IA.

## 🎯 Fonctionnalités intégrées

### 🔍 **Audit Intelligent**
- Analyse complète du projet avec score de qualité
- Détection de vulnérabilités et anti-patterns
- Recommandations d'amélioration

### 🧹 **Nettoyage Automatique**
- Suppression des fichiers parasites (macOS, cache, etc.)
- Optimisation de la structure du projet
- Nettoyage des environnements virtuels

### 📚 **Documentation Automatique**
- Génération de README personnalisés
- Documentation API automatique
- Guides d'utilisation et d'installation

### 🧪 **Tests Automatiques**
- Création de tests unitaires
- Tests d'intégration
- Configuration de pytest

### 🚀 **CI/CD Automatique**
- Configuration GitHub Actions
- Workflows de déploiement
- Intégration continue

### 🔧 **Auto-correction Avancée**
- Correction syntaxique automatique
- Optimisation du code
- Refactoring intelligent

### 👤 **Profils Utilisateur**
- Gestion des préférences
- Historique des actions
- Statistiques d'utilisation

### 📊 **Dashboard Unifié**
- Visualisations des métriques
- Rapports consolidés
- Interface web interactive

## 🚀 Installation

```bash
# Cloner le projet
git clone <repository>
cd athalia-dev-setup

# Installer les dépendances
pip install -r requirements.txt

# Rendre le script exécutable
chmod +x athalia_unified.py
```

## 📖 Utilisation

### 🎯 **Industrialisation complète d'un projet**

```bash
# Industrialisation complète
python athalia_unified.py /chemin/vers/projet

# Mode simulation (pas de suppression)
python athalia_unified.py /chemin/vers/projet --dry-run

# Industrialisation partielle
python athalia_unified.py /chemin/vers/projet --no-clean --no-cicd
```

### 🔍 **Actions spécifiques**

```bash
# Audit uniquement
python athalia_unified.py /chemin/vers/projet --action audit

# Auto-correction uniquement
python athalia_unified.py /chemin/vers/projet --action correction

# Affichage du profil utilisateur
python athalia_unified.py /chemin/vers/projet --action profil --utilisateur monnom

# Génération du dashboard
python athalia_unified.py /chemin/vers/projet --action dashboard
```

### 🔍 **Scan de projets**

```bash
# Scanner tous les projets dans un répertoire
python athalia_unified.py /chemin/vers/repertoire --scan
```

## ⚙️ Options disponibles

| Option | Description |
|--------|-------------|
| `--action` | Action spécifique (complete, audit, correction, profil, dashboard) |
| `--scan` | Scanner les projets au lieu d'industrialiser |
| `--dry-run` | Mode simulation - aucun fichier supprimé |
| `--auto-fix` | Correction automatique du code |
| `--utilisateur` | Nom de l'utilisateur pour les profils |
| `--no-audit` | Passer l'étape d'audit |
| `--no-clean` | Passer l'étape de nettoyage |
| `--no-doc` | Passer l'étape de documentation |
| `--no-test` | Passer l'étape de tests |
| `--no-cicd` | Passer l'étape CI/CD |
| `--verbose` | Mode verbeux |
| `--lang` | Langue (fr/en) |

## 📁 Structure du projet

```
athalia-dev-setup/
├── athalia_unified.py          # Script principal unifié
├── athalia_core/               # Modules historiques
│   ├── athalia_orchestrator.py # Orchestrateur principal
│   ├── intelligent_auditor.py  # Audit intelligent
│   ├── auto_cleaner.py         # Nettoyage automatique
│   ├── auto_documenter.py      # Documentation automatique
│   ├── auto_tester.py          # Tests automatiques
│   └── auto_cicd.py            # CI/CD automatique
├── modules/                    # Modules avancés
│   ├── auto_correction_avancee.py    # Auto-correction avancée
│   ├── profils_utilisateur_avances.py # Profils utilisateur
│   ├── dashboard_unifie_simple.py    # Dashboard unifié
│   └── orchestrateur_principal.py    # Orchestrateur modulaire
├── templates/                  # Templates de génération
├── plugins/                    # Plugins disponibles
├── tests/                      # Tests unitaires
└── docs/                       # Documentation
```

## 🎯 Exemples concrets

### 1. **Industrialisation d'un projet Python**

```bash
python athalia_unified.py /chemin/vers/mon-projet-python --dry-run
```

### 2. **Audit de sécurité**

```bash
python athalia_unified.py /chemin/vers/projet --action audit --verbose
```

### 3. **Correction automatique**

```bash
python athalia_unified.py /chemin/vers/projet --action correction --auto-fix
```

### 4. **Gestion du profil utilisateur**

```bash
python athalia_unified.py /chemin/vers/projet --action profil --utilisateur athalia
```

### 5. **Dashboard et rapports**

```bash
python athalia_unified.py /chemin/vers/projet --action dashboard
```

## 🔧 Configuration

### Variables d'environnement

```bash
# Clé API pour les fonctionnalités avancées
export ATHALIA_API_KEY="votre_cle_api"

# Configuration de la base de données
export ATHALIA_DB_PATH="/chemin/vers/base.db"

# Langue par défaut
export ATHALIA_LANG="fr"
```

### Fichier de configuration

Créer un fichier `athalia_config.yaml` :

```yaml
# Configuration générale
general:
  lang: fr
  verbose: true
  auto_fix: true

# Modules
modules:
  audit: true
  clean: true
  document: true
  test: true
  cicd: true
  correction: true
  profiles: true
  dashboard: true

# Base de données
database:
  path: ./athalia_data.db
  backup: true

# Templates
templates:
  path: ./templates
  custom: true
```

## 🧪 Tests

```bash
# Lancer tous les tests
python -m pytest tests/

# Tests spécifiques
python -m pytest tests/test_audit.py
python -m pytest tests/test_correction.py
```

## 📊 Métriques et Analytics

Le dashboard fournit des métriques détaillées :

- **Score de qualité** : Évaluation globale du projet
- **Vulnérabilités** : Nombre de problèmes détectés
- **Couverture de tests** : Pourcentage de code testé
- **Documentation** : Qualité et complétude
- **Performance** : Temps d'exécution et optimisations

## 🚀 Déploiement

### Docker

```bash
# Build de l'image
docker build -t athalia-unified .

# Exécution
docker run -v $(pwd):/workspace athalia-unified /workspace/mon-projet
```

### CI/CD

Le module CI/CD génère automatiquement :

- GitHub Actions workflows
- Configuration de déploiement
- Tests automatisés
- Documentation automatique

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature
3. Ajouter des tests
4. Soumettre une pull request

## 📄 Licence

MIT License - voir le fichier LICENSE pour plus de détails.

## 🆘 Support

- **Documentation** : `docs/`
- **Issues** : GitHub Issues
- **Discussions** : GitHub Discussions

## 🎉 Remerciements

Merci à tous les contributeurs qui ont participé au développement d'Athalia Unified !

---

**Athalia Unified** - Industrialisation IA complète et unifiée 🚀 