import sys
steps = [
    "Cloner le repo : git clone <repo_url>",
    "Installer les dépendances : pip install -r requirements.txt",
    "Lancer les tests : pytest",
    "Lancer l’API : python src/main.py",
    "Générer la doc : cat DOC.md",
    "CI/CD : Voir .github/workflows/ci.yaml",
    "Swagger : Utiliser openapi.yaml avec Swagger UI",
]
def main():
    for i, step in enumerate(steps, 1):
        input(f"[Étape {i}] {step} (Entrée pour continuer)")
if __name__ == "__main__":
    main()
