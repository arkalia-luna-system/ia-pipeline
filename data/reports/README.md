# 📊 Rapports et Métriques du Projet Athalia

## 📁 Structure des Rapports

### 🔒 Rapports de Sécurité (`security/`)
- `security_audit.txt` - Audit de sécurité principal
- `bandit-*.txt` - Rapports d'analyse de sécurité Bandit
- `bandit_report*.json` - Données JSON des analyses de sécurité

### 🎯 Rapports de Qualité (`quality/`)
- `quality_report.json` - Rapport de qualité du code
- `doc_quality_report.*` - Rapports de qualité de la documentation

### 🧪 Rapports de Test (`testing/`)
- `test-metrics/` - Métriques des tests
- `metrics.*` - Fichiers de métriques générales

## 📈 Utilisation

Ces rapports sont générés automatiquement par les workflows CI/CD et les outils de qualité.
Ils ne doivent PAS être modifiés manuellement.

## 🗂️ Organisation

- **Racine** : Fichiers de configuration et documentation principale
- **`data/reports/`** : Tous les rapports et métriques
- **`athalia_core/`** : Code source principal
- **`tests/`** : Tests unitaires et d'intégration

## 🚫 Fichiers à ne PAS committer

- Rapports temporaires
- Fichiers de cache
- Logs de développement
- Métriques en cours de génération
