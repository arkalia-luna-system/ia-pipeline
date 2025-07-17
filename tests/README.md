# Stratégie de tests Athalia/Arkalia

Ce dossier contient tous les tests du pipeline IA.

## Tests unitaires
- Vérifient chaque fonction/module individuellement.
- Fichiers : `test_*.py` à la racine de ce dossier.

## Tests d'intégration
- Vérifient le fonctionnement global de plusieurs modules ensemble.
- Dossier : `integration/`

## Lancement
- Tous les tests : `pytest tests/`
- Uniquement unitaires : `pytest tests/ --ignore=tests/integration`
- Uniquement intégration : `pytest tests/integration/`

## Couverture
- Générer un rapport de couverture : `pytest --cov=athalia_core tests/` 