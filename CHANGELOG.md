# CHANGELOG Athalia/Arkalia

## [12.0.0] - 2025-08-20
### 🔧 **Amélioration de la Portabilité et Qualité du Code**
- **Correction des chemins hardcodés** : Remplacement de tous les chemins absolus `/Volumes/T7/athalia-dev-setup` par des chemins relatifs
- **Amélioration de la portabilité** : Le projet peut maintenant être cloné n'importe où
- **Correction des erreurs de linting** : Suppression des imports `typing` dépréciés (Dict, List, Tuple)
- **Nettoyage des fichiers système** : Suppression des fichiers `.DS_Store` et `.before_100`
- **Mise à jour de la documentation** : Index principal et guides utilisateur synchronisés
- **Structure des scripts d'optimisation** : Amélioration de la portabilité des scripts bash
- **Validation complète** : Black et Ruff appliqués, tous les tests passent
- **Push sur GitHub** : Changements sauvegardés sur la branche develop

## [11.0.0] - 2025-07-18
- Première release candidate open source
- Architecture modulaire complète, orchestrateur IA robuste
- Fallback multi-IA (Qwen, Mistral, Mock)
- Distillation multi-IA réelle (voting, stacking, bagging, consensus, creative)
- Distillation adaptative (apprentissage préférences, feedback, historique)
- Multimodalité (LLaVA, fusion texte+image)
- Code Genetics (croisement, mutation, évolution)
- Predictive caching (anticipation contextuelle, stats)
- Dashboard web (visualisation, benchmarks, feedback utilisateur)
- Benchmarks avancés (Qwen/Mistral/Mock, prompts réels)
- API REST, CLI, plugins, intégration VS Code
- 180+ tests automatisés, couverture >75%
- Documentation exhaustive, guides, best practices, déploiement rapide

## [10.0.0] - 2025-07-30
### 🔒 **Corrections de Sécurité et Tests**
- **Validateur de sécurité corrigé** : Autorisation des chemins Python pyenv
- **Tests de propreté adaptés** : Correction des tests de fichiers polluants
- **Script de test amélioré** : Résolution du conflit -v/--version
- **Synchronisation main-develop** : Branches principales synchronisées
- **Nettoyage des branches** : Suppression des branches inutiles
- **Backup de sécurité** : Branche backup-20250730 créée
- **Tests fonctionnels** : Validation complète du système
- **CI/CD verte** : Tous les tests passent sur main et develop

## [Unreleased]
- Améliorations futures : personnalisation dashboard, feedback live, couverture >90%, nouveaux modèles IA, plugins avancés
- **Prochaines étapes recommandées** :
  - Diviser le workflow CI/CD pour améliorer la lisibilité
  - Séparer les dépendances dev/prod pour un packaging plus propre
  - Créer un workflow de sécurité dédié pour les badges spécifiques
