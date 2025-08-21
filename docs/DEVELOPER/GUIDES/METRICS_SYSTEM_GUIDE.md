# Guide du Système de Métriques Athalia

## Vue d'ensemble

Le système de métriques Athalia fournit une collecte automatique et fiable des métriques du projet, garantissant que les statistiques affichées dans le README et les dashboards sont toujours exactes et à jour.

## Architecture

### Modules principaux

1. **`athalia_core/metrics/collector.py`** - Collecte les métriques du projet
2. **`athalia_core/metrics/exporter.py`** - Exporte les métriques vers différents formats
3. **`athalia_core/metrics/validator.py`** - Valide la cohérence des métriques
4. **`scripts/metrics/collect_metrics.py`** - Script principal d'orchestration

### Workflow CI/CD

Le workflow `.github/workflows/metrics.yml` automatise :
- Collecte quotidienne des métriques
- Validation des données
- Export vers JSON, Markdown, HTML et CSV
- Création de badges automatiques
- Commentaires sur les PR avec les nouvelles métriques

## Utilisation

### Collecte manuelle

```bash
# Depuis la racine du projet
python3 scripts/metrics/collect_metrics.py

# Avec un répertoire personnalisé
python3 scripts/metrics/collect_metrics.py /path/to/project
```

### Intégration dans le code

```python
from athalia_core.metrics import MetricsCollector, MetricsExporter, MetricsValidator

# Collecte
collector = MetricsCollector(project_root=".")
collector.collect_all_metrics()

# Validation
validator = MetricsValidator()
is_valid = validator.validate(collector.metrics)

# Export
exporter = MetricsExporter(output_dir="data")
files = exporter.export_all_formats(collector.metrics)
```

## Métriques collectées

### Résumé (Summary)
- `total_python_files` - Nombre total de fichiers Python
- `lines_of_code` - Lignes de code totales (sans commentaires/lignes vides)
- `collected_tests` - Nombre de fichiers de test
- `documentation_files` - Nombre de fichiers de documentation

### Détails par fichier
- **Python files** : nom, chemin, nombre de lignes
- **Tests** : nom, chemin
- **Documentation** : nom, chemin

## Formats de sortie

### JSON (`metrics.json`)
Format structuré pour l'automatisation et les APIs.

### Markdown (`metrics.md`)
Rapport lisible pour la documentation.

### HTML (`metrics.html`)
Dashboard interactif avec graphiques.

### CSV (`metrics.csv`)
Format tabulaire pour les analyses.

## Validation des métriques

Le validateur vérifie :
- **Cohérence** : les comptages correspondent aux listes de fichiers
- **Validité** : pas de valeurs négatives ou nulles incorrectes
- **Réalisme** : avertissements pour des valeurs irréalistes

### Règles de validation

1. Tous les champs requis doivent être présents
2. Les valeurs numériques doivent être positives ou nulles
3. Les comptages doivent correspondre aux listes de fichiers
4. Les chemins de fichiers doivent être cohérents avec les noms

## Configuration

### Variables d'environnement

- `ATHALIA_METRICS_DEBUG` - Active les logs détaillés
- `ATHALIA_METRICS_OUTPUT` - Répertoire de sortie personnalisé

### Exclusions

Le système exclut automatiquement :
- Répertoires : `.git`, `__pycache__`, `.pytest_cache`, `node_modules`
- Fichiers : `.pyc`, `.pyo`, `.DS_Store`
- Tests dans la collecte de code principal

## Tests

Le système dispose de tests complets :

```bash
# Tests unitaires pour tous les modules
python -m pytest tests/unit/metrics/ -v

# Test spécifique du collecteur
python -m pytest tests/unit/metrics/test_metrics_collector.py -v

# Test spécifique de l'exporteur
python -m pytest tests/unit/metrics/test_metrics_exporter.py -v

# Test spécifique du validateur
python -m pytest tests/unit/metrics/test_metrics_validator.py -v
```

## Intégration GitHub Actions

### Workflow quotidien

Le workflow s'exécute :
- Tous les jours à 2h00 UTC
- Sur push vers `main` ou `develop`
- Manuellement via `workflow_dispatch`

### Artefacts générés

- `athalia-metrics-{sha}` - Contient tous les fichiers de métriques
- Badges automatiques avec les métriques principales
- Commentaires sur PR avec résumé des métriques

### Permissions requises

```yaml
permissions:
  contents: read
  pull-requests: write  # Pour les commentaires
  pages: write         # Pour le déploiement du dashboard
  id-token: write      # Pour GitHub Pages
```

## Dépannage

### Erreurs communes

1. **Fichiers manquants** : Vérifier les permissions et les chemins
2. **Validation échouée** : Consulter les logs pour les détails
3. **Export impossible** : Vérifier l'espace disque et les permissions

### Logs de debug

```bash
# Activer les logs détaillés
export ATHALIA_METRICS_DEBUG=1
python3 scripts/metrics/collect_metrics.py
```

### Vérification manuelle

```bash
# Valider le JSON généré
python3 -c "import json; print(json.load(open('data/metrics.json')))"

# Compter manuellement les fichiers Python
find . -name "*.py" -not -path "./.git/*" | wc -l
```

## Évolution et maintenance

### Ajout de nouvelles métriques

1. Modifier `MetricsCollector.collect_all_metrics()`
2. Mettre à jour `MetricsValidator._validate_summary()`
3. Adapter les templates d'export dans `MetricsExporter`
4. Ajouter les tests correspondants

### Performance

Le système est optimisé pour :
- Projets jusqu'à 10 000 fichiers Python
- Collecte en moins de 30 secondes
- Mémoire limitée (< 100 MB)

## Exemples d'utilisation

### Script personnalisé

```python
#!/usr/bin/env python3
from athalia_core.metrics import MetricsCollector

collector = MetricsCollector()
collector.collect_all_metrics()

summary = collector.get_metrics_summary()
print(f"Projet : {summary['total_python_files']} modules Python")
print(f"Code : {summary['lines_of_code']:,} lignes")
```

### Intégration continue

```yaml
- name: Collect Metrics
  run: python3 scripts/metrics/collect_metrics.py
  
- name: Upload Metrics
          uses: actions/upload-artifact@v4
  with:
    name: project-metrics
    path: data/metrics.*
```

---

**Note** : Ce système remplace l'ancien script `scripts/utilities/correct_all_metrics.py` qui utilisait des valeurs codées en dur et incorrectes.
