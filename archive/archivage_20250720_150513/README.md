# 📝 Système de Logs - Athalia/Arkalia

## 🎯 Objectif

Ce dossier contient tous les logs du système Athalia/Arkalia pour le debugging, le monitoring et l'analyse des performances.

## 📁 Structure des Logs

```
logs/
├── README.md                    # Ce fichier
├── athalia.log                  # Log principal du système
├── validation.log              # Logs des validations
├── correction.log              # Logs des corrections automatiques
├── performance.log             # Logs de performance
├── errors.log                  # Logs d'erreurs
└── archive/                    # Logs archivés par date
    ├── 2025-07-19/
    ├── 2025-07-18/
    └── ...
```

## 🔧 Configuration

Les logs sont configurés dans `config/athalia_config.yaml` :

```yaml
general:
  log_level: INFO
  log_file: logs/athalia.log
```

## 📊 Types de Logs

### 1. **athalia.log** - Log Principal
- Démarrage/arrêt du système
- Actions utilisateur
- Événements système
- Niveau : INFO, WARNING, ERROR

### 2. **validation.log** - Logs de Validation
- Résultats des tests de validation
- Métriques de performance
- Scores de qualité
- Niveau : DEBUG, INFO

### 3. **correction.log** - Logs de Correction
- Corrections automatiques appliquées
- Erreurs de correction
- Statistiques de correction
- Niveau : DEBUG, INFO, WARNING

### 4. **performance.log** - Logs de Performance
- Temps d'exécution
- Utilisation mémoire
- Benchmarks
- Niveau : DEBUG, INFO

### 5. **errors.log** - Logs d'Erreurs
- Erreurs critiques
- Exceptions non gérées
- Problèmes système
- Niveau : ERROR, CRITICAL

## 🧹 Nettoyage Automatique

Les logs sont automatiquement nettoyés par `ath-clean` :
- Logs de plus de 30 jours → archivés
- Logs de plus de 90 jours → supprimés
- Taille maximale par fichier : 10MB

## 📈 Monitoring

Les logs sont analysés par le dashboard pour :
- Détecter les problèmes
- Mesurer les performances
- Générer des rapports
- Alertes automatiques

## 🔍 Utilisation

### Voir les logs en temps réel
```bash
# Log principal
tail -f logs/athalia.log

# Logs de validation
tail -f logs/validation.log

# Logs de correction
tail -f logs/correction.log
```

### Analyser les erreurs
```bash
# Erreurs récentes
grep "ERROR" logs/errors.log | tail -20

# Erreurs par date
grep "2025-07-19" logs/errors.log
```

### Statistiques des logs
```bash
# Nombre de lignes par fichier
wc -l logs/*.log

# Taille des fichiers
ls -lh logs/*.log
```

## 🚀 Intégration

Le système de logs est intégré dans tous les modules :
- Validation objective
- Correction automatique
- Dashboard temps réel
- CI/CD GitHub Actions

---

**Dernière mise à jour : 19/07/2025** 