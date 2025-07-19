# Organisation du Projet Athalia

## Structure des Dossiers

### 📁 **Racine du Projet**
- `README.md` - Documentation principale
- `requirements.txt` - Dépendances Python
- `athalia_unified.py` - Point d'entrée unifié
- `CHANGELOG.md` - Historique des changements
- `DASHBOARD.md` - Guide du dashboard
- `LICENSE` - Licence du projet
- `progress_optimisation.md` - Suivi de l'optimisation
- `GUIDE_OPTIMISATION_MANUEL.md` - Guide de migration manuelle
- `PLAN_OPTIMISATION_COMPLET.md` - Plan d'optimisation détaillé

### 📁 **docs/** - Documentation
- `analyses/` - Analyses complètes du système
  - `ANALYSE_INTELLIGENCE_COMPLETE.md`
  - `ANALYSE_ARCHITECTURE_COMPLETE.md`
  - `SYSTEME_INTELLIGENT_ATHALIA.md`
  - `SUPER_CERVEAU_ATHALIA_FINAL.md`
- `roadmaps/` - Plans de développement
  - `ROADMAP.md`
  - `ROADMAP_REALISTE.md`
- `benchmarks/` - Tests de performance
  - `BENCHMARK.md`
- `robotics/` - Documentation robotique
  - `ROBOTICS_INTEGRATION_SUMMARY.md`
  - `ROBOTICS_QUICK_START.md`
  - `reachy_audit_20250719_*.md`

### 📁 **scripts/** - Scripts utilitaires
- `robotics/` - Scripts robotiques
  - `athalia_robotics_integration.py`
  - `demo_robotics.py`
- `debug/` - Scripts de débogage
  - `debug_correction.py`

### 📁 **data/** - Données
- `athalia_analytics.db` - Base de données analytiques
- `profils_utilisateur.db` - Profils utilisateurs

### 📁 **config/** - Configuration
- `Cargo.toml` - Configuration Rust
- `athalia_config.yaml` - Configuration principale
- `pyproject.toml` - Configuration Python
- `requirements.txt` - Dépendances

### 📁 **dashboard/** - Dashboards
- `dashboard.html` - Dashboard principal
- `analytics_dashboard.html` - Dashboard analytique

## Règles d'Organisation

### ✅ **Fichiers en Racine**
- Seulement les fichiers essentiels au projet
- Documentation principale (README, CHANGELOG, LICENSE)
- Points d'entrée principaux
- Fichiers de configuration globaux

### ✅ **Documentation**
- Toutes les analyses → `docs/analyses/`
- Tous les roadmaps → `docs/roadmaps/`
- Tous les benchmarks → `docs/benchmarks/`
- Documentation spécialisée → `docs/[domaine]/`

### ✅ **Scripts**
- Scripts utilitaires → `scripts/[catégorie]/`
- Scripts de débogage → `scripts/debug/`
- Scripts spécialisés → `scripts/[domaine]/`

### ✅ **Données**
- Bases de données → `data/`
- Logs → `logs/`
- Archives → `archive/`

### ✅ **Configuration**
- Fichiers de config → `config/`
- Templates → `templates/`
- Prompts → `prompts/`

## Maintenance

### 🔄 **Ajout de Nouveaux Fichiers**
1. Identifier la catégorie appropriée
2. Placer dans le bon dossier
3. Mettre à jour cette documentation

### 🧹 **Nettoyage Régulier**
- Supprimer les fichiers `.DS_Store` et `._*`
- Archiver les anciens rapports
- Maintenir la cohérence de l'organisation

### 📝 **Documentation**
- Mettre à jour ce fichier lors des changements
- Maintenir les index dans chaque dossier
- Documenter les nouvelles conventions 