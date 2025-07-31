## Onglet Benchmarks IA

L’onglet **Benchmarks** du dashboard permet de visualiser et comparer les performances des différents modèles IA (Qwen, Mistral, Mock, etc.) sur des prompts réels.

- **Tableau interactif** : affiche les résultats bruts du benchmark (source : `benchmark_results.csv`).
- **Filtre par modèle** : sélectionnez un modèle IA pour filtrer les résultats.
- **Graphiques dynamiques** :
    - Temps de réponse moyen par prompt
    - Score qualité moyen par modèle
    - Mémoire consommée par modèle
- **Analyse comparative automatique** : surbrillance des écarts, identification du meilleur modèle.

Pour mettre à jour les résultats, régénérez le fichier `benchmark_results.csv` puis rechargez la page.
