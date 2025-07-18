# Athalia/Arkalia

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](./resultats_tests.txt) [![Release](https://img.shields.io/github/v/release/arkalia-luna-system/ia-pipeline?label=latest%20release)](../../releases)

> Orchestrateur IA modulaire, open source, avec fallback multi-IA, distillation, dashboard interactif, API REST, CLI, plugins, et intégration VS Code. **Ultra-modulaire, documenté, prêt pour l’industrialisation et la contribution.**

## Présentation
Athalia/Arkalia est un pipeline IA ultra-modulaire permettant d’orchestrer plusieurs modèles (Qwen, Mistral, LLaVA, Mock), avec fallback, distillation, et modules avancés (multimodalité, génétique du code, mise en cache prédictive).

## Installation
```bash
pip install -r requirements.txt
```

## Utilisation rapide
- Lancer le pipeline : `python athalia_core/main.py`
- Lancer les tests : `pytest`
- Tableau de bord : `python athalia_core/dashboard.py`

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

## Fonctionnalités principales
- Orchestration multi-IA (Qwen, Mistral, LLaVA, Mock, fallback)
- Distillation adaptative, code genetics, predictive caching
- Dashboard interactif avec onglet Benchmarks (visualisation, analyse, filtres)
- API REST, CLI, plugins, intégration VS Code
- Documentation exhaustive, tests automatisés, guides utilisateur/développeur

## Comment utiliser l’onglet Benchmarks ?
Consultez le guide utilisateur ([docs/USER_GUIDE.md](docs/USER_GUIDE.md)) pour découvrir comment exploiter l’onglet Benchmarks du dashboard, filtrer les résultats, lire les graphiques et personnaliser l’analyse.

---

## Contribution
Voir [docs/DEVELOPER_GUIDE.md](./docs/DEVELOPER_GUIDE.md) 