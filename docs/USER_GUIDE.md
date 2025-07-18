# Guide Utilisateur Athalia/Arkalia

## Prise en main rapide
- Installation : `pip install -r requirements.txt`
- Lancer le pipeline : `python athalia_core/main.py`
- Lancer le dashboard : `python athalia_core/dashboard.py`

## Exemples d'usage réels
- Distillation IA :
```python
from athalia_core.athalia_orchestrator import AthaliaOrchestrator
orch = AthaliaOrchestrator()
result = orch.distill_ia_responses("Explique la distillation IA en 2 phrases.")
print(result)
```
- Multimodalité :
```python
from athalia_core.distillation.multimodal_distiller import MultimodalDistiller
distiller = MultimodalDistiller()
result = distiller.distill(["Décris cette image"], ["img1.png"])
print(result)
```
- Orchestration AutoGen :
```python
from agents.agent_network import AuditAgent, CorrectionAgent, SynthesisAgent
audit = AuditAgent()
correction = CorrectionAgent()
synth = SynthesisAgent()
prompt = "Test prompt"
r1 = audit.act(prompt)
r2 = correction.act(prompt)
result = synth.act(prompt, [r1, r2])
print(result)
```

## Best Practices
- Toujours lancer les benchmarks sur une machine dédiée.
- Utiliser le dashboard pour monitorer les performances et collecter le feedback utilisateur.
- Mettre à jour régulièrement les modèles et dépendances.
- Sauvegarder les logs et les feedbacks pour l’amélioration continue.

## FAQ avancée
- **Comment ajouter un nouveau modèle IA ?**
  - Ajouter la fonction d’appel dans le script, relancer le benchmark.
- **Comment personnaliser la distillation ?**
  - Modifier la stratégie dans `ResponseDistiller` ou via l’orchestrateur.
- **Comment intégrer un plugin personnalisé ?**
  - Placer le fichier dans `athalia_core/plugins/` et l’enregistrer via le manager de plugins.
- **Comment exporter les résultats du dashboard ?**
  - Utiliser les fonctions d’export CSV/JSON intégrées. 