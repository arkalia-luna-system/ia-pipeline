# 🚀 Athalia - Système d'Intelligence Artificielle Avancé

## 📋 Présentation

Athalia est un système d'intelligence artificielle avancé conçu pour l'analyse, l'optimisation et l'orchestration de projets de développement. Il intègre des modules d'auto-correction, de distillation multimodale, et de mémoire intelligente.

## 🏗️ Structure du Projet

```
athalia-dev-setup/
├── athalia_core/           # Modules principaux
│   ├── advanced_modules/   # Modules avancés (auto-correction, etc.)
│   ├── agents/            # Agents intelligents
│   ├── distillation/      # Distillation multimodale
│   ├── robotics/          # Modules robotiques
│   └── ...
├── bin/                   # Scripts exécutables
│   ├── ath-audit.py      # Audit du projet
│   ├── ath-backup.py     # Sauvegarde
│   ├── ath-clean         # Nettoyage
│   └── ark-process-check.sh # Monitoring processus
├── tools/                 # Outils de maintenance
│   ├── maintenance/      # Scripts de nettoyage
│   ├── analysis/         # Scripts d'analyse
│   └── monitoring/       # Scripts de surveillance
├── data/                  # Données et rapports
│   ├── reports/          # Rapports d'analyse
│   ├── analytics/        # Données d'analytics
│   └── cache/            # Cache temporaire
├── docs/                  # Documentation
│   ├── API/              # Documentation API
│   ├── ARCHITECTURE/     # Architecture du système
│   ├── DEVELOPER/        # Guide développeur
│   ├── DASHBOARD/        # Documentation dashboard
│   └── REPORTS/          # Rapports et audits
├── tests/                 # Tests unitaires et d'intégration
├── dashboard/             # Dashboards web
├── logs/                  # Fichiers de logs
├── backups/               # Sauvegardes automatiques
└── archive/               # Archives et anciennes versions
```

## 🚀 Installation

### Prérequis
- Python 3.10+
- Git
- Espace disque : 2GB minimum

### Installation rapide
```bash
# Cloner le projet
git clone <repository-url>
cd athalia-dev-setup

# Installer les dépendances
pip install -r requirements.txt

# Configuration initiale
python athalia_core/main.py --setup
```

## 🎯 Utilisation

### Commandes principales
```bash
# Audit complet du projet
python bin/ath-audit.py

# Sauvegarde automatique
python bin/ath-backup.py

# Nettoyage du projet
./bin/ath-clean

# Monitoring système
python tools/monitoring/system_monitor.py

# Lancement du dashboard
python athalia_core/dashboard_unified.py
```

### Modules principaux

#### 🔧 Auto-correction avancée
```python
from athalia_core.advanced_modules.auto_correction_advanced import AutoCorrectionAvancee

corrector = AutoCorrectionAvancee("./mon_projet")
resultats = corrector.analyser_et_corriger(dry_run=True)
```

#### 🧠 Mémoire intelligente
```python
from athalia_core.intelligent_memory import IntelligentMemory

memory = IntelligentMemory()
event_id = memory.learn_from_error(
    error_description="Fonction trop longue",
    code_snippet="def very_long_function(): ...",
    location="test.py:10"
)
```

#### 🎨 Distillation multimodale
```python
from athalia_core.distillation.multimodal_distiller import MultimodalDistiller

distiller = MultimodalDistiller()
response = distiller.distill(
    text_prompts=["Analyse cette image"],
    image_paths=["image.jpg"]
)
```

## 📊 Dashboard

Le dashboard web permet de visualiser :
- Activité du pipeline IA
- Distillation multimodale
- Performances système
- Métriques d'apprentissage

Accès : http://localhost:8080 (par défaut)

## 🧪 Tests

```bash
# Tests unitaires
python -m pytest tests/

# Tests avec couverture
python -m pytest --cov=athalia_core tests/

# Tests spécifiques
python -m pytest tests/test_intelligent_memory.py
```

## 🔧 Maintenance

### Nettoyage automatique
```bash
# Nettoyage des anciennes données
python tools/maintenance/cleanup_old_data.py

# Nettoyage de la documentation
python tools/maintenance/cleanup_documentation.py
```

### Monitoring système
```bash
# Vérification des processus
./bin/ark-process-check.sh

# Monitoring complet
python tools/monitoring/system_monitor.py
```

## 📚 Documentation

- **API** : `docs/API/`
- **Architecture** : `docs/ARCHITECTURE/`
- **Guide développeur** : `docs/DEVELOPER/`
- **Dashboard** : `docs/DASHBOARD/`

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

- **Issues** : [GitHub Issues](https://github.com/username/athalia-dev-setup/issues)
- **Documentation** : `docs/`
- **Logs** : `logs/`

## 🔄 Changelog

Voir `docs/CHANGELOG.md` pour l'historique des versions.

---

**Athalia** - Système d'Intelligence Artificielle Avancé 🚀
