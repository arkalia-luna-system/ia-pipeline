# Lancement des modules avancés Athalia

Ce guide décrit comment lancer l’API REST, les benchmarks, le dashboard de sécurité, les tutoriels interactifs et la génération des dashboards HTML.

---

## Prérequis

- Environnement Python 3.10+ avec les dépendances installées (`pip install -r requirements.txt`).
- Pour le dashboard Streamlit et les graphiques : `streamlit`, `plotly` (inclus ou optionnels selon l’installation).

---

## 1. API REST (FastAPI)

Serveur principal intégré qui expose l’orchestrateur, le cache, les métriques, le linter et le validateur de sécurité.

**Lancement :**
```bash
# Depuis la racine du projet
uvicorn athalia_core.api.main_api_server:app --reload --host 0.0.0.0 --port 8000
# ou
python -m uvicorn athalia_core.api.main_api_server:app --reload --port 8000
```

**Accès :**  
- API : http://localhost:8000  
- Docs Swagger : http://localhost:8000/docs  
- ReDoc : http://localhost:8000/redoc  

**Référence :** [API_SERVER_DOCUMENTATION.md](../API/API_SERVER_DOCUMENTATION.md)

---

## 2. Système de benchmarks

Évalue les performances (CPU, mémoire, I/O), la sécurité, la qualité du code et les capacités IA.

**Lancement :**
```bash
python -m athalia_core.benchmarks.advanced_benchmark_system
# ou en script direct
python athalia_core/benchmarks/advanced_benchmark_system.py
```

**Référence :** [BENCHMARK_SYSTEM_DOCUMENTATION.md](../API/BENCHMARK_SYSTEM_DOCUMENTATION.md)

---

## 3. Dashboard de sécurité

Interface web pour le monitoring de la sécurité (métriques, alertes, rapports).

**Lancement :**
```bash
python -m athalia_core.security.security_dashboard
# ou
python athalia_core/security/security_dashboard.py
```

Génération du HTML uniquement (sans serveur) :
```python
from athalia_core.security.security_dashboard import SecurityDashboard
dashboard = SecurityDashboard("./mon_projet")
dashboard.generate_security_dashboard()
dashboard.open_dashboard()  # ouvre le fichier dans le navigateur
```

**Référence :** [SECURITY_DASHBOARD_DOCUMENTATION.md](../API/SECURITY_DASHBOARD_DOCUMENTATION.md)

---

## 4. Tutoriels interactifs

Système de tutoriels interactifs pour la formation et l’apprentissage.

**Lancement :**
```bash
python -m athalia_core.tutorials.interactive_tutorial_system
# ou
python athalia_core/tutorials/interactive_tutorial_system.py
```

**Référence :** [INTERACTIVE_TUTORIAL_SYSTEM_DOCUMENTATION.md](../API/INTERACTIVE_TUTORIAL_SYSTEM_DOCUMENTATION.md)

---

## 5. Dashboard Streamlit (métriques)

Dashboard unifié avec métriques collectées en temps réel.

**Lancement :**
```bash
# Avec l’entry point (après pip install -e .)
athalia-dashboard

# Ou directement avec Streamlit
streamlit run athalia_core/utilities/dashboard.py --server.port 8501
```

**Via le CLI unifié (rapport texte) :**
```bash
python bin/core/athalia_unified.py . --action dashboard
```

---

## 6. Génération des dashboards HTML

Plusieurs modules peuvent générer des fichiers HTML de type dashboard.

| Module / action | Commande / usage | Sortie typique |
|-----------------|------------------|----------------|
| **Dashboard unifié (rapport)** | `python bin/core/athalia_unified.py . --action dashboard` | Rapport consolidé en texte (console) |
| **Dashboard unifié (HTML)** | Appel Python à `DashboardUnifieSimple` | `dashboard/index.html` (par défaut) |
| **Security Dashboard** | Voir section 3 ci‑dessus | Fichier HTML généré par `SecurityDashboard` |
| **Advanced Analytics** | Utilisation de `AdvancedAnalytics(project_path).generate_dashboard()` | `dashboard/html/analytics_dashboard.html` |
| **Dashboard utilitaires** | `athalia_core.utilities.dashboard.Dashboard` | HTML généré selon les widgets fournis |

**Exemple : générer le dashboard unifié HTML et l’ouvrir :**
```python
from athalia_core.advanced_modules.dashboard_unified import DashboardUnifieSimple
d = DashboardUnifieSimple()
d.generer_dashboard_html("dashboard/index.html")  # génère le fichier
d.ouvrir_dashboard()  # ouvre dans le navigateur
```

**Exemple : dashboard analytics (analyse de projet) :**
```python
from pathlib import Path
from athalia_core.analytics.advanced_analytics import AdvancedAnalytics
aa = AdvancedAnalytics(Path("."))
aa.run()  # analyse puis génère dashboard/html/analytics_dashboard.html
```

Les fichiers générés se trouvent en général sous `dashboard/` ou `<project_path>/dashboard/` selon le projet cible.

---

## Via le CLI unifié

Tous les modules ci‑dessus peuvent aussi être lancés via le CLI unifié :

```bash
python bin/core/athalia_unified.py . --action api
python bin/core/athalia_unified.py . --action benchmark
python bin/core/athalia_unified.py . --action security-dashboard
python bin/core/athalia_unified.py . --action tutorials
```

Le chemin du projet (`.`) est passé automatiquement aux modules qui le supportent.

## Récapitulatif des commandes

| Module | Commande rapide | Via CLI unifié |
|--------|------------------|----------------|
| API REST | `uvicorn athalia_core.api.main_api_server:app --reload --port 8000` | `--action api` |
| Benchmarks | `python -m athalia_core.benchmarks.advanced_benchmark_system` | `--action benchmark` |
| Security Dashboard | `python -m athalia_core.security.security_dashboard` | `--action security-dashboard` |
| Tutoriels | `python -m athalia_core.tutorials.interactive_tutorial_system` | `--action tutorials` |
| Dashboard Streamlit | `streamlit run athalia_core/utilities/dashboard.py` | — |
| CLI unifié (audit / complete / dashboard / scan) | `python bin/core/athalia_unified.py . --action <action>` | — |

---

*Dernière mise à jour : février 2026*
