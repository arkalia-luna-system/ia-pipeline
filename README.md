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

#### ValidationContinue

**Méthodes :** __init__, test_rapide, test_demarrage, test_imports, test_generation_mini

#### ValidationDashboardHandler

**Méthodes :** do_GET, do_POST, send_validation_result, send_history, end_headers

#### ValidationObjective

**Méthodes :** __init__, test_generation_et_compilation, test_correction_reelle, test_robustesse_cas_limites, test_performance_benchmark

### Fonctions principales

#### __init__

**Paramètres :** intervalle_minutes

#### test_rapide

Test rapide pour validation continue (5-10 secondes)

#### test_demarrage

Test: Athalia démarre-t-il ?

#### test_imports

Test: Les imports fonctionnent-ils ?

#### test_generation_mini

Test: Génération d'un mini-projet

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
*Généré automatiquement par Athalia* - 2025-07-20
