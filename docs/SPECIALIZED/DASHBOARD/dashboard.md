# DASHBOARD Athalia/Arkalia

## Présentation
Dashboard web pour visualiser l’activité du pipeline IA, la distillation, les modules avancés, et l’état des modèles.

## Fonctionnalités principales
- Visualisation des requêtes IA et du fallback
- Suivi de la distillation multi-IA
- Monitoring des performances
- (À venir) Visualisation multimodale (images, diagrammes)
- (À venir) Scoring adaptatif, préférences utilisateur

## Utilisation
- Lancer le dashboard : `python athalia_core/dashboard.py`
- Accès : http://localhost:8501 (par défaut)
- Prérequis : Python 3.10+, dépendances installées (`pip install -r requirements.txt`)

## Exemples d'usage
- Visualiser les requêtes IA en temps réel
- Suivre l’évolution du score de distillation
- Analyser les performances par modèle

## Feedback utilisateur (template)
- Formulaire intégré dans le dashboard :
  - Note (1-10)
  - Commentaire libre
  - Type de tâche (génération, correction, audit, multimodal)
- Export CSV/JSON des feedbacks pour analyse
- Visualisation des retours dans le dashboard (graphiques, nuages de mots)

## Collecte de métriques (template)
- Temps de réponse par modèle
- Taux de hit du cache prédictif
- Score de distillation adaptative
- Nombre de requêtes par type
- Export CSV/JSON pour analyse externe

## FAQ
- **Comment changer le port du dashboard ?**
  - Modifier la variable d’environnement ou le paramètre de lancement.
- **Comment ajouter une nouvelle visualisation ?**
  - Ajouter un module dans `athalia_core/dashboard.py` et relancer.
- **Comment intégrer la multimodalité ?**
  - Activer LLaVA et brancher le module multimodal dans le dashboard.

## Best Practices
- Toujours lancer le dashboard sur une machine dédiée pour éviter les ralentissements.
- Mettre à jour régulièrement les modules de visualisation selon les besoins utilisateurs.
- Utiliser les feedbacks pour affiner la distillation adaptative et le scoring.

## Roadmap dashboard
- Ajout visualisation distillation adaptative
- Intégration multimodalité
- Personnalisation avancée
