# Dossier Archive - Athalia Dev Setup

Ce dossier contient les fichiers temporaires, obsolètes et de test qui ont été archivés pour maintenir la propreté du projet principal.

## Contenu archivé

### Fichiers de couverture de tests
- `.coverage.*` - Fichiers de couverture de tests générés automatiquement
- `._*` - Fichiers cachés macOS (métadonnées)

### Résultats de tests
- `resultat_tests_*.txt` - Résultats de tests unitaires et d'intégration
- `resultat_test_aliases*.txt` - Résultats de tests des alias
- `resultats_tests.txt` - Résultats de tests généraux
- `test_complet.log` - Logs de tests

### Rapports et audits
- `athalia_report_*.json` - Rapports générés automatiquement
- `audit_report.yaml` - Rapports d'audit

### Fichiers temporaires
- `*.f` - Fichiers temporaires de formatage
- `security_audit.f(f` - Audit de sécurité temporaire
- `athalia_analytics.f(f` - Analytics temporaires

### Dossiers temporaires
- `.f/` - Dossier de fichiers temporaires
- `test-improved-f/` - Tests d'amélioration

### Dashboards de test
- `test_dashboard_simple.html` - Dashboard de test simple

## Pourquoi ces fichiers sont archivés

1. **Fichiers temporaires** : Générés automatiquement lors des tests et du développement
2. **Résultats de tests** : Conservés pour référence mais pas nécessaires dans le repo principal
3. **Rapports automatiques** : Générés par les outils d'audit et d'analyse
4. **Fichiers de couverture** : Régénérés à chaque exécution de tests

## Récupération

Si vous avez besoin de récupérer un fichier spécifique :
```bash
# Exemple : récupérer un rapport de test
cp archive/resultat_tests_auto_cleaner_unit_only.txt ./
```

## Maintenance

Ce dossier est ignoré par Git (voir `.gitignore`). Les fichiers peuvent être supprimés définitivement si l'espace disque devient un problème.

**Date de création** : $(date)
**Raison** : Nettoyage du projet principal pour améliorer la lisibilité et les performances 