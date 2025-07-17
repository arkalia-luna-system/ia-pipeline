# Organisation du Workspace Athalia

## Vue d'ensemble

Le workspace Athalia a été réorganisé pour une meilleure structure modulaire et une maintenance facilitée.

## Structure des dossiers

### 📁 Dossiers principaux
- **`athalia_core/`** - Modules principaux du système
- **`modules/`** - Modules additionnels et extensions
- **`plugins/`** - Plugins et extensions tierces
- **`templates/`** - Templates pour la génération de projets
- **`prompts/`** - Prompts IA et configurations
- **`agents/`** - Agents IA spécialisés

### 📁 Dossiers de données et configuration
- **`data/`** - Bases de données et fichiers de données
  - `profils_utilisateur.db` - Profils utilisateurs
  - `athalia_analytics.db` - Données d'analytics
  - `athalia_report_*.json` - Rapports générés
- **`config/`** - Fichiers de configuration
  - `athalia_config.yaml` - Configuration principale
  - `pytest.ini` - Configuration des tests
  - `pyproject.toml` - Configuration du projet
  - `requirements.txt` - Dépendances Python
  - `docker-compose.yml` - Configuration Docker
  - `paths.yaml` - Configuration des chemins
  - `Taskfile.yaml` - Configuration des tâches

### 📁 Dossiers de projets et tests
- **`projects/`** - Projets générés par Athalia
- **`tests/`** - Tests automatisés
- **`setup/`** - Scripts de configuration et maintenance
  - `cleanup_workspace.py` - Nettoyage automatique
  - `run_tests.sh` - Exécution des tests

### 📁 Dossiers de documentation et interface
- **`docs/`** - Documentation complète
- **`dashboard/`** - Fichiers HTML du dashboard
- **`logs/`** - Fichiers de logs

### 📁 Dossiers de build et cache
- **`blueprints_history/`** - Historique des blueprints
- **`.github/`** - Configuration GitHub Actions

## Scripts principaux

### 🚀 Scripts d'exécution
- **`athalia_unified.py`** - Script principal unifié
- **`athalia_unified_enhanced.py`** - Version améliorée
- **`athalia_quick_start.py`** - Démarrage rapide interactif

### 📄 Fichiers de documentation
- **`README.md`** - Documentation principale
- **`INVENTAIRE_COMPLET.md`** - Inventaire des fonctionnalités
- **`RAPPORT_FINAL.md`** - Rapport final du projet
- **`FINAL_SUMMARY.md`** - Résumé final
- **`GENESIS.md`** - Historique de développement
- **`CLEANUP_REPORT.md`** - Rapport de nettoyage
- **`TROUBLESHOOTING.md`** - Guide de dépannage
- **`INSTALL.md`** - Guide d'installation

## Maintenance automatique

### 🧹 Script de nettoyage
Le script `setup/cleanup_workspace.py` maintient automatiquement l'organisation :

```bash
python setup/cleanup_workspace.py
```

**Fonctionnalités :**
- Suppression des fichiers parasites macOS (._*)
- Nettoyage des dossiers de cache
- Organisation automatique des fichiers
- Suppression des fichiers vides

### 📋 Configuration des chemins
Le fichier `config/paths.yaml` centralise tous les chemins du projet pour une maintenance facilitée.

## Bonnes pratiques

### ✅ Organisation des nouveaux fichiers
1. **Scripts Python** → À la racine (scripts principaux) ou dans `setup/` (utilitaires)
2. **Fichiers de configuration** → `config/`
3. **Données et bases** → `data/`
4. **Logs** → `logs/`
5. **Documentation** → `docs/`
6. **Tests** → `tests/`
7. **Projets générés** → `projects/`

### 🚫 Éviter
- Fichiers parasites macOS
- Fichiers de cache dans la racine
- Fichiers vides
- Organisation incohérente

## Commandes utiles

```bash
# Nettoyage automatique
python setup/cleanup_workspace.py

# Exécution des tests
bash setup/run_tests.sh

# Démarrage rapide
python athalia_quick_start.py

# Script principal
python athalia_unified_enhanced.py
```

## Migration

Si vous avez des fichiers qui ne respectent pas cette organisation, le script de nettoyage les déplacera automatiquement vers les bons dossiers.

## Support

Pour toute question sur l'organisation, consultez :
- `docs/USER_GUIDE.md` - Guide utilisateur complet
- `TROUBLESHOOTING.md` - Solutions aux problèmes courants 