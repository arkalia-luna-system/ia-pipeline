# Contribuer à Athalia/Arkalia

Merci de contribuer à ce projet open source !

## 🚀 Démarrage rapide

### Prérequis
```bash
# Cloner le repository
git clone <repository-url>
cd athalia-dev-setup

# Créer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou .venv\Scripts\activate  # Sur Windows

# Installer les dépendances
pip install -r requirements.txt
```

### Workflow de Contribution
```bash
# 1. Forkez le repo et clonez votre fork
git clone https://github.com/arkalia-luna-system/ia-pipeline.git

# 2. Créez une branche pour vos modifications
git checkout -b feature/nouvelle-fonctionnalite

# 3. Ajoutez vos modules/tests dans la structure existante
# 4. Vérifiez que tous les tests passent
python3 -m pytest tests/ --verbose

# 5. Soumettez une pull request claire et documentée
```

## 🧪 Processus de Tests

### Tests Unitaires
```bash
# Lancer tous les tests unitaires
python3 -m pytest tests/ --verbose

# Tests avec couverture
python3 -m pytest tests/ --cov=athalia_core --cov-report=html

# Tests spécifiques
python3 -m pytest tests/test_intelligent_auditor.py -v
python3 -m pytest tests/test_auto_cleaner.py -v
```

### Tests d'Intégration
```bash
# Tests d'intégration complets
python3 -m pytest tests/integration/ --verbose

# Tests end-to-end
python3 -m pytest tests/integration/test_end_to_end.py -v
```

### Tests de Performance
```bash
# Benchmarks de performance
python3 athalia_core/performance_analyzer.py --benchmark

# Tests de charge
python3 -m pytest tests/performance/ --verbose
```

### Validation de Qualité
```bash
# Linting du code
flake8 athalia_core/ --max-line-length=100
black athalia_core/ --check
isort athalia_core/ --check

# Vérification de la documentation
python3 athalia_core/auto_documenter.py --validate
```

## 📋 Bonnes pratiques

### Structure Modulaire
- Respectez la structure existante (core, modules, distillation, tests, docs)
- Ajoutez vos modules dans le bon dossier
- Suivez les conventions de nommage

### Tests Obligatoires
- Ajoutez des tests pour toute nouvelle fonctionnalité
- Maintenez une couverture de tests >90%
- Testez les cas d'erreur et les edge cases

### Documentation
- Documentez vos ajouts dans le README ou la documentation développeur
- Ajoutez des docstrings pour toutes les fonctions
- Mettez à jour la documentation API si nécessaire

### Code Quality
- Privilégiez la clarté, la robustesse et l'extensibilité
- Utilisez les outils de linting (flake8, black, isort)
- Suivez les conventions PEP 8

## 🔧 Outils de Développement

### Scripts Utilitaires
```bash
# Audit automatique
python3 athalia_core/audit.py --project /chemin/projet

# Nettoyage automatique
python3 athalia_core/auto_cleaner.py --project /chemin/projet

# Documentation automatique
python3 athalia_core/auto_documenter.py --module votre_module
```

### Validation Avant Commit
```bash
# Script de validation complète
./scripts/validate_before_commit.sh

# Ou validation manuelle
python3 -m pytest tests/ --cov=athalia_core
flake8 athalia_core/
python3 athalia_core/auto_documenter.py --validate
```

## 📝 Pull Request Guidelines

### Contenu Requis
- Description claire de la fonctionnalité/bugfix
- Tests ajoutés ou modifiés
- Documentation mise à jour
- Exemples d'utilisation si applicable

### Template de PR
```markdown
## Description
Brève description des changements

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Amélioration de la documentation
- [ ] Refactoring

## Tests
- [ ] Tests unitaires ajoutés
- [ ] Tests d'intégration passent
- [ ] Couverture de tests >90%

## Documentation
- [ ] README mis à jour
- [ ] API documentée
- [ ] Exemples ajoutés
```

## 🆘 Support et Contact

### Questions Techniques
- Ouvrez une issue pour les bugs
- Utilisez les discussions GitHub pour les questions
- Consultez la documentation dans `docs/`

### Équipe de Développement
- **Mainteneurs** : @athalia-team
- **Documentation** : @docs-team
- **Tests** : @qa-team

### Ressources
- [Documentation API](../API/README.md)
- [Guide d'Installation](INSTALLATION.md)
- [Best Practices](../DEVELOPER/BEST_PRACTICES.md)
- [Guide de Maintenance](../DEVELOPER/DOCUMENTATION_MAINTENANCE.md)

---

**Merci de contribuer à Athalia ! 🚀**
