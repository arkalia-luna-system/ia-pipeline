# CHANGELOG Athalia/Arkalia



## [1.0.0] - 2025-07-18
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

## [11.0.0] - 2025-07-31
### 🔧 **Corrections CI/CD et Documentation**
- **Correction des workflows CI Professional** : Ajout de pytest aux outils de sécurité
- **Correction du hook de prévention Python** : Regex corrigée pour éviter la détection erronée de Python 3.10
- **Nettoyage des fichiers AppleDouble** : Suppression de 110+ fichiers système indésirables
- **Synchronisation des branches** : main, develop et backup-20250731 synchronisées
- **Correction majeure de la documentation** : Synchronisation avec l'état réel du projet
- **Mise à jour des statistiques** : **1372 tests collectés**, **79 modules** dans athalia_core
- **Nettoyage des branches obsolètes** : Suppression de fix-python-version-support, backup-20250730, ci-cd-professional
- **1372 tests collectés** : Validation complète du système en amélioration continue

## [Unreleased]
- Améliorations futures : personnalisation dashboard, feedback live, couverture >90%, nouveaux modèles IA, plugins avancés
