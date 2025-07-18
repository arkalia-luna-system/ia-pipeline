# BENCHMARK Athalia/Arkalia

## Objectif
Documenter les performances des modèles IA (Qwen, Mistral, LLaVA, fallback, distillation) sur des prompts réels du pipeline Athalia.

## Méthodologie
- Description des prompts utilisés
- Environnement d’exécution (CPU/GPU, RAM, version des modèles)
- Critères d’évaluation (temps, coût, qualité, robustesse)

## Prompts de test
- [À compléter] Liste des prompts utilisés pour le benchmark

## Résultats (extrait)

| Prompt | Modèle | Durée (s) | Mémoire (KB) | Qualité |
|---|---|---|---|---|
| Explique le concept de distillation en IA... | Qwen | 8.2 | 512 | 120 |
| Explique le concept de distillation en IA... | Mistral | 6.5 | 480 | 110 |
| Explique le concept de distillation en IA... | Mock | 0.01 | 10 | 30 |
| ... | ... | ... | ... | ... |

> **Voir le fichier benchmark_results.md pour le tableau complet généré automatiquement.**

## Interprétation des scores
- **Qualité** : score heuristique (longueur, pertinence, à affiner avec feedback utilisateur).
- **Durée** : temps d’inférence réel, dépend du prompt et du modèle.
- **Mémoire** : pic mémoire mesuré (utile pour dimensionner l’infra).

## Visualisation dans le dashboard
- Les résultats sont intégrés dans le dashboard (onglet « Benchmarks »).
- Graphiques comparatifs par prompt, modèle, score qualité, temps, coût.
- Export CSV/Markdown pour analyse externe.

## Analyse comparative (exemple)
- Qwen : rapide, bonnes réponses sur les prompts analytiques, parfois verbeux.
- Mistral : plus concis, très robuste sur la correction de code, temps de réponse stable.
- Mock : instantané, utile pour les tests, mais pas pertinent pour la qualité réelle.
- Cas d’usage : privilégier Qwen pour la génération, Mistral pour la correction, fallback pour la robustesse.

## Conclusions et recommandations
- Pour les tâches analytiques : Qwen > Mistral > Mock
- Pour la correction de code : Mistral > Qwen
- Pour la rapidité : Mock (test), sinon Mistral
- Utiliser la distillation pour combiner les forces des deux modèles.

## FAQ
- **Comment interpréter le score qualité ?**
  - C’est une heuristique (longueur, pertinence, à affiner avec du feedback utilisateur).
- **Pourquoi certains prompts sont plus lents ?**
  - Les modèles chargent en RAM, certains prompts sont plus complexes.
- **Comment ajouter un nouveau modèle ?**
  - Ajouter la fonction d’appel dans le script, relancer le benchmark.

## Best Practices
- Toujours lancer le benchmark sur une machine « au repos » pour des mesures fiables.
- Comparer sur des prompts variés (analyse, génération, correction, traduction).
- Intégrer les résultats dans le dashboard pour suivi continu. 