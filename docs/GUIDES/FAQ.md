# FAQ Athalia/Arkalia

## Utilisation
- **Comment lancer le pipeline IA ?**
  - `python athalia_core/main.py`
- **Comment lancer le dashboard ?**
  - `python athalia_core/dashboard.py`
- **Comment lancer les tests ?**
  - `pytest`

## Déploiement
- **Comment déployer en production ?**
  - Voir [docs/DEPLOYMENT.md](./DEPLOYMENT.md)
- **Comment changer le port du dashboard ?**
  - Modifier le paramètre Streamlit ou la variable d’environnement.

## Personnalisation
- **Comment ajouter un modèle IA ?**
  - Ajouter la fonction d’appel dans le script, relancer le benchmark.
- **Comment personnaliser la distillation ?**
  - Modifier la stratégie dans `ResponseDistiller` ou via l’orchestrateur.
- **Comment intégrer un plugin ?**
  - Placer le fichier dans `athalia_core/plugins/` et l’enregistrer via le manager de plugins.

## Contribution
- **Comment contribuer au projet ?**
  - Forker le repo, créer une branche, proposer une PR documentée.
- **Comment ajouter un test d’intégration ?**
  - Voir [docs/DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md)
- **Comment suivre la couverture de code ?**
  - Générer le rapport avec pytest-cov, ouvrir `htmlcov/index.html`. 