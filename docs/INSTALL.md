# Installation

## Prérequis
- Python 3.10+ 
- pip (gestionnaire de paquets Python)
- Git (pour cloner le repo)

## Installation rapide

1. **Cloner le repo**
   ```bash
   git clone https://github.com/arkalia-luna-system/ia-pipeline.git
   cd ia-pipeline
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r ia_project/requirements.txt
   ```

3. **Lancer le pipeline**
   ```bash
   python3 -m athalia_core.main
   ```

## Première utilisation

1. **Choisir l'option 1** dans le menu CLI
2. **Décrire votre projet** en une phrase (ex: "API de gestion de tâches")
3. **Attendre la génération** (quelques secondes)
4. **Consulter les fichiers générés** :
   - `ia_project/README.md` : présentation du projet
   - `ia_project/ONBOARDING.md` : guide d'installation
   - `ia_project/DOC.md` : documentation technique
   - `ia_project/openapi.yaml` : spécification API

## Utilisation avancée

- **Générer la CI** : option 3 du menu
- **Dashboard global** : option 4 du menu  
- **Nettoyer un projet** : option 2 du menu
- **Mode dry-run** : option 8 du menu (simulation sans modification)

## Dépannage

- **Erreur de dépendances** : `pip install --upgrade pip`
- **Problème de permissions** : utiliser un environnement virtuel
- **CLI qui plante** : vérifier Python 3.10+

---

*Guide d'installation mis à jour le 2024-06-27*
