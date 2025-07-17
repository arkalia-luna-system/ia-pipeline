# Guide d'onboarding

*Généré automatiquement le 2025-07-17 03:44*

## 1. Cloner le repo

    git clone <repo_url>

## 2. Installer les dépendances

    pip install -r requirements.txt

## 3. Lancer les tests

    pytest

## 4. Lancer l'API (exemple)

    python src/main.py

## 5. Générer la doc

    cat DOC.md

## 6. CI/CD

    Voir .github/workflows/ci.yaml

## 7. Swagger

    Utiliser openapi.yaml avec Swagger UI

## FAQ Onboarding

- **Problème d'installation de dépendances ?**
  - Vérifie ta version de Python (3.10+ recommandé)
  - Utilise un environnement virtuel (venv)
  - Mets à jour pip : `pip install --upgrade pip`

- **Tests qui échouent ?**
  - Lance `pytest` pour voir les erreurs détaillées
  - Vérifie que tous les fichiers nécessaires sont présents

- **API ne démarre pas ?**
  - Vérifie que les dépendances sont bien installées
  - Lance `python src/main.py` et regarde les logs

- **Swagger ne s'affiche pas ?**
  - Vérifie que `openapi.yaml` est bien généré et valide
  - Utilise un validateur YAML en ligne

