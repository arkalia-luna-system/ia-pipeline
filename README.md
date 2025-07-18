# Athalia/Arkalia

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](./resultats_tests.txt)

Orchestrateur IA modulaire, open source, avec fallback multi-IA, distillation, dashboard, API REST, CLI, et intégration VS Code.

## Présentation
Athalia/Arkalia est un pipeline IA ultra-modulaire permettant d’orchestrer plusieurs modèles (Qwen, Mistral, LLaVA, Mock), avec fallback, distillation, et modules avancés (multimodalité, code genetics, predictive caching).

## Installation
```bash
pip install -r requirements.txt
```

## Usage rapide
- Lancer le pipeline : `python athalia_core/main.py`
- Lancer les tests : `pytest`
- Lancer le dashboard : `python athalia_core/dashboard.py`

## Exemple d'usage réel
```python
from athalia_core.athalia_orchestrator import AthaliaOrchestrator
orch = AthaliaOrchestrator()
result = orch.distill_ia_responses("Explique la distillation IA en 2 phrases.")
print(result)
```

## Déploiement rapide
- Docker :
```bash
docker build -t athalia .
docker run -p 8501:8501 athalia
```
- Cloud : voir [docs/DEPLOYMENT.md](./docs/DEPLOYMENT.md)

## Modules clés
- Fallback multi-IA
- Distillation adaptative
- Multimodalité (LLaVA)
- Dashboard web
- API REST, CLI, plugins
- Dashboard interactif avec onglet **Benchmarks** (visualisation, comparaison, filtres, graphiques dynamiques)

## Guides et documentation
- [BENCHMARK.md](./BENCHMARK.md)
- [ROADMAP.md](./ROADMAP.md)
- [CHANGELOG.md](./CHANGELOG.md)
- [DASHBOARD.md](./DASHBOARD.md)
- [docs/USER_GUIDE.md](./docs/USER_GUIDE.md)
- [docs/API_REFERENCE.md](./docs/API_REFERENCE.md)

## Contribution
Voir [docs/DEVELOPER_GUIDE.md](./docs/DEVELOPER_GUIDE.md)

## Comment utiliser l’onglet Benchmarks ?

Consultez le guide utilisateur ([docs/USER_GUIDE.md](docs/USER_GUIDE.md)) pour découvrir comment exploiter l’onglet Benchmarks du dashboard, filtrer les résultats, lire les graphiques et personnaliser l’analyse.

---
Projet sous licence MIT. Contact : [à compléter] 