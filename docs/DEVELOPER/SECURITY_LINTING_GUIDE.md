# Guide de Linting et Sécurité - Athalia

## 🛡️ Vue d'ensemble

Ce guide décrit l'utilisation des outils de linting et de sécurité configurés pour le projet Athalia.

## 📦 Outils Installés

### Outils de Formatage
- **Black**: Formatage automatique du code Python
- **isort**: Organisation automatique des imports

### Outils d'Analyse Statique
- **Flake8**: Analyse statique avec extensions
  - flake8-bugbear: Détection de bugs courants
  - flake8-builtins: Conflits avec les builtins
  - flake8-quotes: Vérification des guillemets
  - pep8-naming: Conventions de nommage
  - mccabe: Complexité cyclomatique
- **MyPy**: Vérification des types statiques

### Outils de Sécurité
- **Bandit**: Détection de vulnérabilités de sécurité
- **Safety**: Vérification des vulnérabilités des dépendances
- **pip-audit**: Audit des dépendances

### Outils d'Automatisation
- **Pre-commit**: Hooks Git automatiques
- **pyupgrade**: Mise à jour automatique de la syntaxe Python

## 🚀 Installation Rapide

```bash
# Installer tous les outils
./bin/install-security-tools

# Ou manuellement
pip install -e ".[dev,security]"
pre-commit install
```

## 🔧 Utilisation

### Linting Complet
```bash
# Exécuter tous les outils de linting
./bin/ath-lint-secure

# Ou avec pre-commit
pre-commit run --all-files
```

### Outils Individuels

#### Formatage
```bash
# Formater le code
black .

# Vérifier le formatage
black --check --diff .

# Organiser les imports
isort .

# Vérifier l'organisation des imports
isort --check-only --diff .
```

#### Analyse Statique
```bash
# Flake8 avec configuration personnalisée
flake8 --config=config/.flake8

# MyPy avec vérification des types
mypy --config-file=config/pyproject.toml

# Bandit pour la sécurité
bandit -c config/.bandit -r athalia_core scripts tools
```

#### Sécurité
```bash
# Vérifier les vulnérabilités des dépendances
safety check

# Audit complet des dépendances
pip-audit

# Mise à jour de la syntaxe Python
pyupgrade --py310-plus .
```

## 📋 Configuration

### Flake8 (config/.flake8)
- Longueur de ligne: 88 caractères (compatible Black)
- Règles de sécurité activées (Bandit)
- Règles de qualité strictes
- Exclusions pour les tests et archives

### Black (pyproject.toml)
- Longueur de ligne: 88 caractères
- Mode preview activé
- Exclusions pour les dossiers non pertinents

### MyPy (pyproject.toml)
- Vérification stricte des types
- Exclusions pour les tests et archives
- Configuration détaillée des erreurs

### Bandit (config/.bandit)
- Exclusions pour les tests et environnements
- Cibles: athalia_core, scripts, tools
- Rapport JSON dans logs/

## 🎯 Bonnes Pratiques

### Avant chaque commit
1. Exécuter `./bin/ath-lint-secure`
2. Corriger les erreurs critiques
3. Vérifier les avertissements de sécurité

### Workflow de développement
```bash
# 1. Formater le code
black . && isort .

# 2. Vérifier la qualité
flake8 --config=config/.flake8

# 3. Vérifier les types
mypy --config-file=config/pyproject.toml

# 4. Vérifier la sécurité
bandit -c config/.bandit -r athalia_core

# 5. Tester
pytest

# 6. Commiter
git add . && git commit -m "feat: nouvelle fonctionnalité"
```

### Gestion des erreurs

#### Erreurs Critiques (à corriger immédiatement)
- Violations de sécurité (Bandit)
- Erreurs de syntaxe (Flake8)
- Vulnérabilités (Safety, pip-audit)

#### Erreurs Non-Critiques (à corriger progressivement)
- Warnings de formatage
- Warnings de types (MyPy)
- Complexité élevée (McCabe)

## 🔍 Interprétation des Rapports

### Flake8
- **E**: Erreurs de style (pycodestyle)
- **W**: Avertissements de style
- **F**: Erreurs de logique (pyflakes)
- **C**: Complexité (mccabe)
- **B**: Bugs courants (bugbear)
- **S**: Sécurité (bandit)
- **N**: Nommage (pep8-naming)
- **T**: Builtins (flake8-builtins)
- **Q**: Guillemets (flake8-quotes)
- **I**: Imports (isort)
- **UP**: Syntaxe Python (pyupgrade)

### Bandit
- **B101**: assert_used
- **B102**: exec_used
- **B103**: set_bad_file_permissions
- **B104**: hardcoded_bind_all_interfaces
- **B105**: hardcoded_password_string
- **B106**: hardcoded_password_funcarg
- **B107**: hardcoded_password_default
- **B108**: hardcoded_tmp_directory
- **B110**: try_except_pass
- **B112**: try_except_continue
- **B201**: flask_debug_true
- **B301**: pickle
- **B302**: marshal
- **B303**: md5
- **B304**: md5_insecure
- **B305**: sha1
- **B306**: mktemp_q
- **B307**: eval
- **B308**: mark_safe
- **B309**: httpsconnection
- **B310**: urllib_urlopen
- **B311**: random
- **B312**: telnetlib
- **B313**: xml_bad_cElementTree
- **B314**: xml_bad_ElementTree
- **B315**: xml_bad_expatreader
- **B316**: xml_bad_expatbuilder
- **B317**: xml_bad_sax
- **B318**: xml_bad_minidom
- **B319**: xml_bad_pulldom
- **B320**: xml_bad_etree
- **B321**: ftplib
- **B322**: input
- **B323**: unverified_context
- **B324**: hashlib_new_insecure_functions
- **B325**: tempnam
- **B401**: import_telnetlib
- **B402**: import_ftplib
- **B403**: import_pickle
- **B404**: import_subprocess
- **B405**: import_xml_etree
- **B406**: import_xml_sax
- **B407**: import_xml_expat
- **B408**: import_xml_minidom
- **B409**: import_xml_pulldom
- **B410**: import_lxml
- **B411**: import_xmlrpclib
- **B412**: import_httpoxy
- **B413**: import_pycrypto
- **B501**: request_with_no_cert_validation
- **B601**: paramiko_calls
- **B602**: subprocess_popen_with_shell_equals_true
- **B603**: subprocess_without_shell_equals_true
- **B604**: any_other_function_with_shell_equals_true
- **B605**: start_process_with_a_shell
- **B606**: start_process_with_no_shell
- **B607**: start_process_with_partial_path
- **B608**: hardcoded_sql_expressions
- **B609**: linux_commands_wildcard_injection
- **B701**: jinja2_autoescape_false

## 🚨 Résolution des Problèmes Courants

### Erreurs de Formatage
```bash
# Corriger automatiquement
black .
isort .
```

### Erreurs de Types
```python
# Ajouter des annotations de type
def my_function(param: str) -> bool:
    return param.startswith("test")

# Ou ignorer temporairement
# type: ignore
```

### Erreurs de Sécurité
```python
# Remplacer eval() par ast.literal_eval()
import ast
result = ast.literal_eval(safe_string)

# Utiliser secrets au lieu de random
import secrets
token = secrets.token_urlsafe(32)
```

### Complexité Élevée
```python
# Diviser les fonctions complexes
def complex_function():
    return step1() + step2() + step3()

def step1():
    # Logique simple
    pass
```

## 📊 Métriques de Qualité

### Objectifs
- **Couverture de code**: ≥80%
- **Complexité cyclomatique**: ≤10
- **Erreurs de sécurité**: 0
- **Vulnérabilités**: 0
- **Conformité PEP8**: 100%

### Surveillance Continue
```bash
# Rapport de qualité complet
./bin/ath-lint-secure > logs/quality_report.txt

# Métriques de couverture
pytest --cov=athalia_core --cov-report=html
```

## 🔗 Ressources

- [Documentation Black](https://black.readthedocs.io/)
- [Documentation Flake8](https://flake8.pycqa.org/)
- [Documentation MyPy](https://mypy.readthedocs.io/)
- [Documentation Bandit](https://bandit.readthedocs.io/)
- [Documentation Pre-commit](https://pre-commit.com/)
- [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [PEP 484](https://www.python.org/dev/peps/pep-0484/)
