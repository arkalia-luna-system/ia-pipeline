# Guide Développeur Athalia/Arkalia

## Structure du projet
- Modules principaux dans `athalia_core/`
- Plugins dans `athalia_core/plugins/`
- Dashboard dans `athalia_core/dashboard.py`
- Tests dans `tests/`

## Tests & Couverture
- Lancer tous les tests :
```bash
pytest --maxfail=1 --disable-warnings -q
```
- Générer un rapport de couverture :
```bash
pytest --cov=athalia_core --cov-report=html
open htmlcov/index.html
```
- Exemple de test d'intégration :
```python
from athalia_core.athalia_orchestrator import AthaliaOrchestrator
orch = AthaliaOrchestrator()
result = orch.distill_ia_responses("Prompt test", strategy="voting")
assert isinstance(result, str)
```

## Conseils contribution
- Toujours ajouter des tests pour chaque nouvelle fonctionnalité.
- Documenter chaque module/fonction dans les guides Markdown.
- Utiliser les templates de feedback utilisateur pour améliorer l’UX.
- Proposer des issues/PR claires et documentées. 