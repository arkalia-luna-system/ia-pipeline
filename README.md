# Athalia Pipeline IA

Pipeline d'industrialisation IA pour génération automatique de projets, tests, docs, CI/CD.

## 🚀 Installation rapide

```bash
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline
pip install -r ia_project/requirements.txt
python3 -m athalia_core.main
```

## 📋 Fonctionnalités

- ✅ **Génération IA** : Projets complets avec structure, tests, docs
- ✅ **Tests unitaires** : Validation automatique sur projets legacy
- ✅ **CI/CD** : GitHub Actions, badges, coverage
- ✅ **Documentation** : README, ONBOARDING, DOC technique
- ✅ **Mode dégradé** : Fonctionne sans API (mode mock)
- ✅ **Nettoyage** : Suppression automatique des fichiers cachés
- ✅ **Rollback** : Sauvegarde et restauration automatiques

## 🔧 Utilisation

1. **Générer un projet** : Option 1 du CLI
2. **Nettoyer** : Option 2 du CLI  
3. **CI/CD** : Option 3 du CLI
4. **Dashboard** : Option 4 du CLI
5. **Mode dry-run** : Option 8 du CLI

## ⚠️ Problèmes d'API

Si vous rencontrez l'erreur **"credit balance is too low"** :

- **Solution immédiate** : Le pipeline passe automatiquement en mode mock
- **Solution permanente** : Rechargez vos crédits sur [Anthropic Console](https://console.anthropic.com/)
- **Plus d'infos** : Consultez [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 📚 Documentation

- [INSTALL.md](INSTALL.md) - Guide d'installation détaillé
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Dépannage et solutions
- [ia_project/ONBOARDING.md](ia_project/ONBOARDING.md) - Guide d'onboarding projet

## 🏗️ Architecture

```
athalia_core/
├── main.py          # CLI principal
├── generation.py    # Génération de projets
├── cleanup.py       # Nettoyage et maintenance
├── ci.py           # CI/CD et badges
├── dashboard.py    # Dashboard et visualisation
├── onboarding.py   # Guides d'onboarding
└── security.py     # Audit sécurité
```

## 🧪 Tests

```bash
cd ia_project
pytest tests/
```

## 📊 Dashboard

Généré automatiquement avec :
- Vue d'ensemble des projets
- Diagrammes Mermaid
- Métriques de qualité

---

*Pipeline Athalia - Industrialisation IA pro-ready* 🚀
