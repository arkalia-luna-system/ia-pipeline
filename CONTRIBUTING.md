# 🤝 Guide de Contribution - Athalia

Merci de votre intérêt pour contribuer à **Athalia** ! Ce guide vous aidera à participer efficacement au projet.

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.10+
- Git
- pip ou poetry

### Installation du développement
```bash
# Cloner le repository
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Installer les dépendances
pip install -r requirements.txt
pip install -e .
```

## 🔧 Workflow de Développement

### 1. Créer une branche
```bash
git checkout -b feature/nom-de-la-fonctionnalite
# ou
git checkout -b fix/nom-du-bug
```

### 2. Développer et tester
```bash
# Lancer les tests
python -m pytest

# Vérifier le formatage
black .
ruff check .

# Vérifier les types
mypy athalia_core/
```

### 3. Commiter et pousser
```bash
git add .
git commit -m "feat: ajouter nouvelle fonctionnalité"
git push origin feature/nom-de-la-fonctionnalite
```

## 📝 Standards de Code

### Formatage
- **Black** pour le formatage automatique
- **Ruff** pour le linting
- **MyPy** pour la vérification des types

### Messages de commit
Utilisez [Conventional Commits](https://www.conventionalcommits.org/):

```bash
feat: ajouter nouvelle fonctionnalité
fix: corriger bug dans le module X
docs: mettre à jour la documentation
test: ajouter tests pour la fonction Y
refactor: refactoriser le code Z
```

### Tests
- **Couverture minimale** : 80%
- **Tests unitaires** : obligatoires pour les nouvelles fonctionnalités
- **Tests d'intégration** : pour les modules critiques

## 🐛 Signaler un Bug

1. Vérifiez que le bug n'a pas déjà été signalé
2. Utilisez le template [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md)
3. Incluez des étapes de reproduction claires
4. Ajoutez des captures d'écran si pertinent

## 🚀 Demander une Fonctionnalité

1. Utilisez le template [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md)
2. Décrivez clairement le besoin métier
3. Expliquez pourquoi cette fonctionnalité est importante
4. Proposez une solution si possible

## 🔄 Pull Request

### Avant de soumettre
- [ ] Tests passent (`python -m pytest`)
- [ ] Code formaté (`black .`)
- [ ] Linting OK (`ruff check .`)
- [ ] Types vérifiés (`mypy athalia_core/`)
- [ ] Documentation mise à jour

### Processus de review
1. **Draft PR** : marquez comme brouillon si en cours
2. **Tests CI** : attendez que tous les jobs passent
3. **Review** : demandez une review à l'équipe
4. **Merge** : après approbation et tests OK

## 📚 Documentation

### Structure
- **README.md** : vue d'ensemble du projet
- **docs/** : documentation technique détaillée
- **examples/** : exemples d'utilisation
- **CHANGELOG.md** : historique des changements

### Mise à jour
- Documentez toutes les nouvelles fonctionnalités
- Mettez à jour les exemples si nécessaire
- Vérifiez que la doc est à jour avec le code

## 🛡️ Sécurité

### Signaler une vulnérabilité
- **NE PAS** créer d'issue publique
- Contactez directement l'équipe de sécurité
- Nous traiterons en priorité

### Bonnes pratiques
- Validez toutes les entrées utilisateur
- Utilisez les modules de sécurité d'Athalia
- Testez les scénarios d'attaque

## 🎯 Zones de Contribution

### Priorité Haute
- [ ] Amélioration de la sécurité
- [ ] Optimisation des performances
- [ ] Correction de bugs critiques
- [ ] Tests de couverture

### Priorité Moyenne
- [ ] Nouvelles fonctionnalités
- [ ] Amélioration de l'UX
- [ ] Documentation
- [ ] Outils de développement

### Priorité Basse
- [ ] Refactoring cosmétique
- [ ] Optimisations mineures
- [ ] Badges et métriques

## 🤝 Communauté

### Code de Conduite
- Respectez tous les contributeurs
- Soyez constructif dans les critiques
- Aidez les nouveaux contributeurs
- Restez professionnel

### Support
- **Issues** : pour les bugs et fonctionnalités
- **Discussions** : pour les questions générales
- **Wiki** : pour la documentation communautaire

## 📊 Métriques de Contribution

Nous valorisons tous les types de contribution :
- 🐛 **Bug fixes** : amélioration de la stabilité
- 🚀 **Features** : extension des capacités
- 📚 **Documentation** : amélioration de l'expérience
- 🧪 **Tests** : garantie de la qualité
- 🔧 **Tools** : amélioration du workflow

---

**Merci de contribuer à Athalia !** 🎉

Pour toute question, n'hésitez pas à ouvrir une issue ou une discussion.
