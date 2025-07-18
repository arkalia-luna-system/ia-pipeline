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

## Utilisation de l’onglet Benchmarks du Dashboard

L’onglet **Benchmarks** permet de comparer les performances des modèles IA (Qwen, Mistral, Mock, etc.) sur des prompts réels.

- **Tableau interactif** : affiche les résultats bruts du benchmark (source : `benchmark_results.csv`).
- **Filtre par modèle** : sélectionnez un modèle IA pour filtrer dynamiquement les résultats.
- **Graphiques dynamiques** :
    - Temps de réponse moyen par prompt
    - Score qualité moyen par modèle
    - Mémoire consommée par modèle
- **Analyse automatique** : le dashboard affiche le meilleur modèle, le nombre de prompts testés et le nombre total de runs.

Pour mettre à jour les résultats :
1. Relancez le script de benchmark pour générer un nouveau `benchmark_results.csv`.
2. Rechargez la page du dashboard dans votre navigateur.

Vous pouvez personnaliser l’analyse ou le style en modifiant le code HTML/JS du dashboard. 