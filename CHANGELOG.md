# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [12.0.1] - 2026-02-07

### Added
- **CLI unifié** : actions `--action api`, `--action benchmark`, `--action security-dashboard`, `--action tutorials` pour lancer les modules avancés depuis le même script.
- **Lanceur rétrocompatible** : `bin/athalia_unified.py` redirige vers `bin/core/athalia_unified.py` pour que les anciennes commandes restent valides.
- **Guide** : [LANCEMENT_MODULES_AVANCES.md](docs/USER_GUIDES/LANCEMENT_MODULES_AVANCES.md) pour API, benchmarks, security dashboard, tutoriels et dashboards HTML.
- **Entry point** : `athalia-dashboard` pointe vers `main()` qui génère le dashboard HTML et l’ouvre dans le navigateur.

### Fixed
- **CLI unifié** : utilisation de `UnifiedOrchestrator` et des vrais modules `athalia_core.*` pour les actions `complete`, `fix`, `dashboard`, `scan` (plus de mock).
- **Imports** : `athalia_core/autocomplete/autocomplete_server.py` (autocomplete_engine) ; `scripts/debug_correction.py` (quality.correction_optimizer).
- **Logger** : création de `athalia_core/core/logger.py` pour les scripts qui importent `athalia_core.core.logger`.
- **Documentation et scripts** : références CLI uniformisées vers `bin/core/athalia_unified.py` ; alias setup (alias.sh, alias-unified.sh) et robotics (ROBOTICS_QUICK_START) corrigés.
- **Dashboard** : exclusion des fichiers `._*` (macOS) dans la collecte métriques ; lecture des fichiers en `errors="ignore"` pour éviter les erreurs d’encodage.
- **Tests e2e** : skip automatique lorsque le réseau/localhost est indisponible (sandbox, CI restreint) ; racine du projet portable (plus de chemin en dur).
- **Script maintenance navigation** : import optionnel de `schedule`, suppression de la dépendance à `athalia_core.core.logger` (utilisation de `logging` standard) ; mode planifié affiche un message si `schedule` n’est pas installé.
- **API main_api_server** : annotations type pour basedpyright sur les appels conditionnels (hasattr) aux composants Athalia.
- **Tests unitaires ai_robust** : export de `validate_and_run` dans le module ; correction du patch (utilisation de `validateand_run`) ; typo `generate_bluelogger` → `generate_blueprint` ; test `validate_and_run` avec `capture_output=True` au lieu de `stdout`/`stderr`.
- **Tests unitaires ai_robust_enhanced** : nom du mock unifié en `mock_validate_and_run` dans `test_call_ollama` pour cohérence et éviter tout NameError.
- **Tests unitaires security** : import de `security_audit_project` depuis `athalia_core.validation.security` dans `test_security.py` ; clé `result["f"]` → `result["secure"]` dans `test_security_comprehensive.py` ; nom de fichier rapport `security_audit_report.json` → `security_report.json` et assertion sur le contenu dans `test_security_auditor_complete.py` ; test encryption sans chiffrement assoupli ; test `with_f_files` utilise un fichier `.py` pour être scanné ; assertion mot de passe / clé API assouplie dans `test_security_audit_python_files_only`.
- **validation/security_validator** : alias `SecurityValidator = CommandSecurityValidator` ; `validate_and_run` exécute après validation (lève `SecurityError` si commande non autorisée).
- **Tests security** : `test_validate_and_run_unsafe` OK ; `test_weak_crypto_patterns` ignore répertoires audit/tutorials/plugins/examples/docs ; `test_no_hardcoded_passwords` exclut benchmark/advanced_benchmark ; `test_no_macos_specific_paths` / `test_no_absolute_paths_in_whitelist` autorisent le répertoire de l'interpréteur actuel.
- **Tests integration** : `test_workflow_integration` encodage UTF-8 avec `errors="replace"`, clé `on` ou `True` pour YAML, chemin workflows portable, ignore fichiers AppleDouble `._*`.
- **Tests load/mutation** : skip si `locust` ou `mutmut` non installés ; `project_root` portable.

### Changed
- **Documentation** : dates de dernière mise à jour alignées au 7 février 2026 (SECURITY.md, README, USAGE.md).
- **UX utilisateur** : quickcheck sans RuntimeWarning (import paresseux dans `athalia_core.demo`) ; audit unifié affiche le score (`global_score`), la liste des problèmes et des suggestions ; menu principal résilient en environnement restreint (PermissionError/OSError sur `psutil.process_iter`) ; orthographe du menu CLI (d'onboarding, d'intégration, d'arrêt, etc.) ; README « Vérification rapide ».
- **Qualité** : dossier `typings/` pour `python.analysis.stubPath` ; `pyrightconfig.json` ; typage `secure_subprocess` et fallback `security_validator` pour mypy ; marqueurs pytest `load` et `mutation` ; section qualité du code dans le README (ruff, mypy).

## [12.0.0] - 2025-08-20

### Added
- **Workflows GitHub Actions dédiés**
  - Workflow de sécurité (`security.yml`) avec Bandit, Safety, pip-audit
  - Workflow de documentation (`docs.yml`) avec MkDocs
  - Workflow SBOM (`sbom.yml`) pour la génération de Software Bill of Materials
- **Configuration Dependabot** (`.github/dependabot.yml`)
  - Mises à jour automatiques des dépendances Python, GitHub Actions et npm
- **Système de sécurité amélioré**
  - Détection dynamique des chemins Python (plus de chemins macOS en dur)
  - Tests unitaires de validation des chemins de sécurité
- **Organisation des fichiers**
  - Fichiers de validation organisés dans `data/validation_reports/`
  - Templates d'issues et PR GitHub
  - Roadmap 2025 et planification des fonctionnalités

### Changed
- **Métriques unifiées** dans le README
  - 335 modules Python (mesurés automatiquement)
  - 83,065 lignes de code (mesurées automatiquement)
  - Métriques collectées par le MetricsCollector Athalia
- **Structure des branches**
  - Nettoyage de 12 branches → 4 branches propres
  - Synchronisation de toutes les branches au même niveau
- **Dépendances organisées** dans `pyproject.toml`
  - Séparation des dépendances prod/dev
  - Installation plus légère pour la production

### Fixed
- **Chemins de sécurité** spécifiques à l'environnement
- **Artefacts CI** en racine (nettoyage automatique)
- **Incohérences** dans la documentation

### Security
- **Validation des commandes** améliorée
- **Tests de sécurité** automatisés
- **Workflow de sécurité** dédié et isolé

## [11.0.0] - 2025-08-15

### Added
- **Système de validation** complet
- **Tests automatisés** pour tous les modules
- **Documentation API** complète

### Changed
- **Architecture** refactorisée pour la performance
- **Interface utilisateur** modernisée

## [10.0.0] - 2025-08-10

### Added
- **Première version stable** d'Athalia
- **Modules de base** : génération, validation, sécurité
- **Documentation** complète

---

## Notes de version

- **Version majeure** : Changements incompatibles avec les versions précédentes
- **Version mineure** : Nouvelles fonctionnalités compatibles
- **Version patch** : Corrections de bugs compatibles

## Support

Pour toute question ou problème, consultez :
- [Documentation](docs/)
- [Issues GitHub](https://github.com/arkalia-luna-system/ia-pipeline/issues)
- [Discussions](https://github.com/arkalia-luna-system/ia-pipeline/discussions)
