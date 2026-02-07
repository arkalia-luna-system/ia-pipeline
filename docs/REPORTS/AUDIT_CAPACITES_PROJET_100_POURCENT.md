# Audit : utilisation des capacités du projet Athalia

**Date :** 2025-02-07  
**Objectif :** Vérifier si le projet utilise 100 % de ses capacités (modules, CLI, API, dashboards, scripts, workflows).

---

## Résumé exécutif

| Catégorie | Statut | Taux d’utilisation estimé |
|-----------|--------|---------------------------|
| CLI unifié (`athalia_unified.py`) | **Corrigé** | ~95 % (UnifiedOrchestrator utilisé, fix/dashboard/scan corrigés, actions api/benchmark/security-dashboard/tutorials ajoutées) |
| Entry points installables (`athalia`, `athalia-cli`, `athalia-dashboard`) | Documentés + dashboard corrigé | ~90 % (README, guide LANCEMENT_MODULES_AVANCES, `athalia-dashboard` → `main()` qui génère et ouvre le HTML) |
| Modules avancés (API, Benchmark, Security Dashboard, Tutoriels) | Intégrés au CLI | ~90 % (`--action api`, `--action benchmark`, `--action security-dashboard`, `--action tutorials`) |
| Scripts `bin/` et `scripts/` | Partiellement utilisés | ~70 % (logger créé, debug_correction corrigé ; certains scripts restent à valider) |
| Workflows CI/CD | Actifs | ~100 % |
| Dépendances optionnelles | Cohérentes | requirements.txt aligné avec l’usage |

**Verdict (mis à jour fév. 2026) :** Les correctifs appliqués (CLI, entry points, intégration des modules avancés, documentation) portent l’utilisation des capacités du projet à un niveau élevé. Des améliorations mineures restent possibles (scripts isolés, options CLI additionnelles).

---

## 1. CLI unifié (`bin/core/athalia_unified.py`)

### Problèmes critiques

1. **Action `complete`**  
   - Import : `athalia_core.athalia_orchestrator.AthaliaOrchestrator`  
   - Ce module **n’existe pas**. L’orchestrateur réel est `athalia_core.core.unified_orchestrator.UnifiedOrchestrator`.  
   - Conséquence : le code bascule toujours sur une classe mock ; **UnifiedOrchestrator n’est jamais utilisé** depuis ce script.

2. **Action `fix`**  
   - Import : `modules.auto_correction_avancee.AutoCorrectionAvancee`  
   - Le package `modules` à la racine n’existe pas.  
   - Le bon module est `athalia_core.advanced_modules.auto_correction_advanced` (avec les classes/fonctions adaptées).

3. **Action `dashboard`**  
   - Import : `modules.dashboard_unifie_simple.DashboardUnifieSimple`  
   - Même erreur : `modules` inexistant.  
   - Le bon module est `athalia_core.advanced_modules.dashboard_unified.DashboardUnifieSimple`.

4. **Action `scan`**  
   - Import : `modules.orchestrateur_principal.AthaliaOrchestrator`  
   - Même erreur.  
   - Il faudrait utiliser `UnifiedOrchestrator` (ex. `athalia_core.core.unified_orchestrator`) et sa méthode de scan.

### Recommandations

- Remplacer `AthaliaOrchestrator` par `UnifiedOrchestrator` pour `complete` et `scan`.
- Remplacer tous les imports `modules.*` par les chemins `athalia_core.*` indiqués ci-dessus (et adapter les noms de classes/fonctions si besoin).

---

## 2. Entry points définis dans `pyproject.toml`

- `athalia` → `athalia_core.core.main:main`  
- `athalia-cli` → `athalia_core.utilities.cli:cli`  
- `athalia-dashboard` → `athalia_core.utilities.dashboard:main` (génère le dashboard HTML et l’ouvre dans le navigateur)

Dans la doc (ex. DEPLOYMENT.md), le dashboard est lancé avec :

```bash
streamlit run athalia_core/utilities/dashboard.py
```

et non avec `athalia-dashboard`. Les entry points sont donc sous-exploités et peu visibles pour les utilisateurs.

**Recommandation :** Documenter clairement `athalia`, `athalia-cli` et `athalia-dashboard` dans le README et les guides (installation, démarrage rapide, déploiement).

**✅ Fait (février 2026) :** README mis à jour avec un tableau des commandes installables et exemples du CLI unifié ; guide [LANCEMENT_MODULES_AVANCES.md](../USER_GUIDES/LANCEMENT_MODULES_AVANCES.md) créé et lié depuis GETTING_STARTED_DETAILED et USER_GUIDES/INDEX.

---

## 3. Modules avancés (API, Benchmark, Security Dashboard, Tutoriels)

| Module | Fichier | Utilisation actuelle |
|--------|---------|----------------------|
| API REST | `athalia_core/api/main_api_server.py` | Tests d’intégration/e2e, doc ; **pas appelé par le CLI** |
| Benchmarks | `athalia_core/benchmarks/advanced_benchmark_system.py` | Doc ; **pas dans le flux principal** |
| Security Dashboard | `athalia_core/security/security_dashboard.py` | Doc ; **pas dans le flux principal** |
| Tutoriels interactifs | `athalia_core/tutorials/interactive_tutorial_system.py` | Tests unitaires, doc ; **pas dans le flux principal** |

Ces quatre blocs sont documentés et testés mais ne sont pas exposés via le CLI unifié ni via un menu/script unique.

**Recommandation :**  
- Soit ajouter des sous-commandes ou options au CLI (ex. `--api`, `--benchmark`, `--security-dashboard`, `--tutorials`),  
- Soit documenter explicitement les commandes pour les lancer (ex. `uvicorn`, `python -m athalia_core.security.security_dashboard`, etc.) et les indiquer dans le README / GETTING_STARTED.

**✅ Fait (février 2026) :** Guide [docs/USER_GUIDES/LANCEMENT_MODULES_AVANCES.md](../USER_GUIDES/LANCEMENT_MODULES_AVANCES.md) créé avec toutes les commandes (API, benchmarks, security dashboard, tutoriels, Streamlit, génération dashboards HTML), lié depuis README et index des guides. **CLI unifié étendu :** les actions `--action api`, `--action benchmark`, `--action security-dashboard`, `--action tutorials` ont été ajoutées ; les modules avancés sont donc lancables directement depuis le CLI.

---

## 4. Scripts et imports incorrects

### 4.1 `athalia_core.core.logger`

- **Référencé par :**  
  - `scripts/maintenance_navigation_quality.py`  
  - `scripts/documentation/correct_internal_links.py`  
  - `scripts/maintenance/auto_navigation_validator.py`  
- **Problème :** `athalia_core/core/` ne contient **pas** de `logger.py`. Existe seulement `athalia_core/utilities/logger_advanced.py`.  
- **Conséquence :** ImportError pour ces trois scripts.

**Recommandation :** Créer `athalia_core/core/logger.py` (réexport ou façade vers `logger_advanced`) ou remplacer les imports par `athalia_core.utilities.logger_advanced` (et adapter l’API si besoin).

### 4.2 `athalia_core.correction_optimizer`

- **Référencé par :** `scripts/debug_correction.py`  
- **Problème :** Le module réel est `athalia_core.quality.correction_optimizer` (avec `optimize_correction`).  
- **Conséquence :** ImportError pour `debug_correction.py`.

**Recommandation :** Corriger l’import en `athalia_core.quality.correction_optimizer` et utiliser la fonction/API existante.

### 4.3 Autocomplete server

- **Fichier :** `athalia_core/autocomplete/autocomplete_server.py`  
- **Import actuel :** `from athalia_core.autocomplete_engine import AutocompleteEngine`  
- **Problème :** Le moteur est dans `athalia_core.autocomplete.autocomplete_engine`, pas à la racine `athalia_core.autocomplete_engine`.  
- **Conséquence :** ImportError au lancement du serveur d’autocomplete.

**Recommandation :** Remplacer par `from athalia_core.autocomplete.autocomplete_engine import AutocompleteEngine` (ou `from athalia_core.autocomplete import AutocompleteEngine` si exporté dans `__init__.py`).

---

## 5. Dashboards HTML

- La doc (NEW_MODULES_INDEX, métriques) mentionne des dashboards HTML (ex. `dashboard/html/dashboard_interactif_avance.html`, `analytics_dashboard.html`).
- Ces fichiers sont **générés** par des modules (ex. `AdvancedAnalytics`, `Dashboard`, `DashboardUnifieSimple`, `SecurityDashboard`) plutôt que versionnés à la racine.
- Aucun dossier `dashboard/` avec HTML n’a été trouvé à la racine du dépôt dans l’état actuel.

**Recommandation :** Considérer soit d’ajouter un script ou une commande CLI qui génère ces dashboards dans un répertoire connu (ex. `dashboard/` ou `data/dashboard/`), soit de documenter la procédure de génération et le chemin de sortie.

**✅ Fait (février 2026) :** Section « Génération des dashboards HTML » ajoutée dans [LANCEMENT_MODULES_AVANCES.md](../USER_GUIDES/LANCEMENT_MODULES_AVANCES.md) avec table des modules, exemples Python (DashboardUnifieSimple, AdvancedAnalytics, SecurityDashboard) et chemins de sortie.

---

## 6. Workflows GitHub Actions

- **Présents :** `ci-matrix.yml`, `docs.yml`, `metrics.yml`, `release.yml`, `security.yml`, `sbom.yml`.  
- **Statut :** Tous semblent actifs et cohérents avec la structure du projet (validation, tests, docs, métriques, sécurité, release, SBOM).

Aucune sous-utilisation évidente des capacités CI/CD.

---

## 7. Dépendances

- **requirements.txt** : Inclut streamlit, bandit, safety, pip-audit, mkdocs, pytest, etc., alignés avec l’usage (dashboard, sécurité, doc, tests).
- **pyproject.toml** : Dépendances optionnelles `dashboard` (streamlit, plotly, matplotlib), `docs`, `security`, `ai`. Les dépendances de base (sans extras) suffisent pour le cœur du projet ; les extras sont cohérents avec les fonctionnalités avancées.

Les dépendances IA (openai, anthropic) sont commentées dans requirements.txt alors qu’elles sont dans `[project]` de pyproject.toml ; à clarifier selon la politique (optionnelles vs requises pour certaines features).

---

## 8. Plan d’action pour tendre vers 100 % d’utilisation

| Priorité | Action | Statut |
|----------|--------|--------|
| P0 | Corriger `bin/core/athalia_unified.py` : utiliser `UnifiedOrchestrator` et les vrais modules `athalia_core.*` pour `complete`, `fix`, `dashboard`, `scan`. | ✅ Fait |
| P0 | Corriger l’import dans `athalia_core/autocomplete/autocomplete_server.py` (autocomplete_engine). | ✅ Fait |
| P1 | Résoudre `athalia_core.core.logger` : créer le module ou remplacer par `logger_advanced` dans les 3 scripts. | ✅ Fait (module `core/logger.py` créé) |
| P1 | Corriger l’import dans `scripts/debug_correction.py` (quality.correction_optimizer). | ✅ Fait |
| P2 | Documenter et promouvoir les entry points `athalia`, `athalia-cli`, `athalia-dashboard` dans README et guides. | ✅ Fait |
| P2 | Intégrer ou documenter explicitement le lancement de l’API, du benchmark, du security dashboard et des tutoriels (CLI ou procédure claire). | ✅ Fait (actions CLI + guide LANCEMENT_MODULES_AVANCES) |
| P3 | Documenter ou automatiser la génération des dashboards HTML (répertoire de sortie et commande/script). | ✅ Fait (section dans LANCEMENT_MODULES_AVANCES) |

**Rétrocompatibilité :** Un lanceur `bin/athalia_unified.py` redirige vers `bin/core/athalia_unified.py` pour que les anciennes références continuent de fonctionner.

---

*Rapport généré par audit du dépôt Athalia (structure, imports, CLI, scripts, workflows et documentation).*
