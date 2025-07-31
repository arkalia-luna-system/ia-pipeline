# 📊 Organisation des Données - Athalia/Arkalia

Ce dossier contient toutes les données générées par le système Athalia/Arkalia.

## 📁 Structure des Dossiers

### `benchmarks/`
Résultats des benchmarks et tests de performance des modèles IA.
- `benchmark_results.csv` - Résultats bruts des benchmarks
- `benchmark_results.md` - Rapport formaté des benchmarks
- `benchmark_qwen_mistral.py` - Script de benchmark Qwen/Mistral

### `reports/`
Rapports générés par le système.
- `athalia_report_*.json` - Rapports d'analyse de projets
- `audit_report.yaml` - Rapport d'audit de sécurité
- `test_prompts_results.json` - Résultats des tests de prompts

### `databases/`
Bases de données du système.
- `profils_utilisateur.db` - Base de données des profils utilisateur
- `athalia_analytics.db` - Base de données des analytics

## 📋 Fichiers à la Racine

### Inventaires et Listes
- `core_liste.txt` - Liste des modules core
- `modules_liste.txt` - Liste des modules disponibles
- `inventaire_obsolete.txt` - Inventaire des fichiers obsolètes

### Bases de Données (Déplacées)
- `profils_utilisateur.db` - **Déplacé vers** `databases/`
- `athalia_analytics.db` - **Déplacé vers** `databases/`

## 🔄 Maintenance

### Nettoyage Automatique
Les fichiers de rapports et benchmarks sont automatiquement nettoyés :
- Rapports > 30 jours → Archivés
- Benchmarks > 7 jours → Archivés
- Logs > 7 jours → Supprimés

### Sauvegarde
- Bases de données sauvegardées quotidiennement
- Rapports critiques sauvegardés hebdomadairement
- Benchmarks sauvegardés après chaque exécution

## 📈 Utilisation

### Accès aux Données
```python
# Accès aux benchmarks
from pathlib import Path
benchmark_data = Path("data/benchmarks/benchmark_results.csv")

# Accès aux rapports
reports_dir = Path("data/reports/")

# Accès aux bases de données
db_path = Path("data/databases/profils_utilisateur.db")
```

### Dashboard
Les données sont automatiquement intégrées dans le dashboard :
- Onglet "Benchmarks" → `data/benchmarks/`
- Onglet "Analytics" → `data/databases/`
- Onglet "Reports" → `data/reports/`

---

*Organisation mise à jour le 2025-07-18*
