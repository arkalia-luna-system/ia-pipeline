# 🗂️ ORGANISATION DU WORKSPACE ATHALIA/ARKALIA

**Dernière mise à jour :** 20 Août 2025  
**Version :** v12.0.0  
**Statut :** ✅ **ACTIF ET MAINTENU**  
**Catégorie :** Architecture et Organisation

## 🎯 **RÉSUMÉ EXÉCUTIF**

Ce document décrit la structure officielle et à jour du workspace Athalia/Arkalia, organisé pour une meilleure structure modulaire et une maintenance facilitée.

---

## 📋 **STRUCTURE DU WORKSPACE**

### **🏗️ Dossiers Principaux**
- **`athalia_core/`** - Modules principaux du système
- **`modules/`** - Modules additionnels et extensions
- **`plugins/`** - Plugins et extensions tierces
- **`templates/`** - Templates pour la génération de projets
- **`prompts/`** - Prompts IA et configurations
- **`agents/`** - Agents IA spécialisés

### **💾 Dossiers de Données et Configuration**
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

### **🚀 Dossiers de Projets et Tests**
- **`projects/`** - Projets générés par Athalia
- **`tests/`** - Tests automatisés
- **`setup/`** - Scripts de configuration et maintenance
  - `cleanup_workspace.py` - Nettoyage automatique
  - `run_tests.sh` - Exécution des tests

### **📚 Dossiers de Documentation et Interface**
- **`docs/`** - Documentation complète et organisée
- **`dashboard/`** - Fichiers HTML du dashboard
- **`logs/`** - Fichiers de logs système

### **🔧 Dossiers de Build et Cache**
- **`blueprints_history/`** - Historique des blueprints
- **`.github/`** - Configuration GitHub Actions

---

## 🚀 **SCRIPTS ET EXÉCUTABLES**

### **⚡ Scripts d'Exécution Principaux**
- **`bin/core/athalia_unified.py`** - Script principal unifié
- **`bin/core/athalia_launcher.py`** - Lanceur principal
- **`bin/core/ath-demo.py`** - Démonstrations interactives

### **📄 Fichiers de Documentation Principaux**
- **`README.md`** - Documentation principale du projet
- **`CHANGELOG.md`** - Historique des versions et changements

---

## 🔧 **MAINTENANCE AUTOMATIQUE**

### **🧹 Script de Nettoyage Principal**
Le script principal d'Athalia maintient automatiquement l'organisation :

```bash
python bin/core/athalia_unified.py . --action fix --auto-fix
```

#### **✨ Fonctionnalités Automatiques :**
- **Suppression des fichiers parasites** macOS (._*)
- **Nettoyage des dossiers de cache** temporaires
- **Organisation automatique** des fichiers
- **Suppression des fichiers vides** et obsolètes
- **Validation de l'intégrité** de la structure

### **📋 Configuration Centralisée des Chemins**
Le fichier `config/paths.yaml` centralise tous les chemins du projet pour une maintenance facilitée et une cohérence garantie.

---

## 🎯 **BONNES PRATIQUES D'ORGANISATION**

### **✅ Organisation des Nouveaux Fichiers**
1. **Scripts Python** → À la racine (scripts principaux) ou dans `setup/` (utilitaires)
2. **Fichiers de configuration** → `config/`
3. **Données et bases** → `data/`
4. **Logs** → `logs/`
5. **Documentation** → `docs/`
6. **Tests** → `tests/`
7. **Projets générés** → `projects/`

### **🚫 Éléments à Éviter**
- **Fichiers parasites macOS** (._*)
- **Fichiers de cache dans la racine**
- **Fichiers vides** et temporaires
- **Duplication** de contenu entre dossiers
- **Noms de fichiers** non descriptifs

---

## 🔍 **VALIDATION ET MAINTENANCE**

### **📅 Maintenance Régulière**
- **Vérification hebdomadaire** de l'intégrité de la structure
- **Nettoyage automatique** via le script principal
- **Validation mensuelle** de l'organisation des dossiers
- **Audit trimestriel** de la cohérence globale

### **✅ Critères de Validation**
- **Structure logique** et intuitive
- **Séparation claire** des responsabilités
- **Navigation facile** entre les composants
- **Maintenance simplifiée** et automatisée

---

## 📚 **RESSOURCES ET RÉFÉRENCES**

### **🔗 Documentation Connexe**
- **Structure du projet :** [STRUCTURE_PROJET_EXPLICATION.md](STRUCTURE_PROJET_EXPLICATION.md)
- **Dashboard :** [dashboard/README.md](dashboard/README.md)
- **Guide principal :** [../INDEX_FINAL_DOCUMENTATION_ATHALIA.md](../INDEX_FINAL_DOCUMENTATION_ATHALIA.md)

### **🛠️ Outils de Maintenance**
- **Script de nettoyage :** `bin/core/athalia_unified.py`
- **Analyse de qualité :** `scripts/analyze_documentation_quality.py`
- **Guide de maintenance :** [DOCUMENTATION_MAINTENANCE.md](../DEVELOPER/DOCUMENTATION_MAINTENANCE.md)

---

## 📝 **INFORMATIONS TECHNIQUES**

**Dernière mise à jour :** 20 Août 2025  
**Version actuelle :** v12.0.0  
**Statut :** ✅ **ACTIF ET MAINTENU**  
**Mainteneur :** Équipe Athalia/Arkalia  
**Documentation :** [Guide de maintenance](../DEVELOPER/DOCUMENTATION_MAINTENANCE.md)

**🎯 Une organisation claire et logique garantit une maintenance efficace et un développement fluide ! 🚀**
