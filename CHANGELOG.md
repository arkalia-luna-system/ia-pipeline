# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

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
