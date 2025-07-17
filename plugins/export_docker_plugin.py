"""
Plugin d'export Docker pour projet Python.
"""
import os
import subprocess

def export_docker(project_path: str, output_path: str = "Dockerfile"):
    """Génère un Dockerfile optimisé pour le projet donné."""
    requirements = os.path.join(project_path, "requirements.txt")
    base_image = "python:3.11-slim"
    with open(output_path, "w") as f:
        f.write(f"FROM {base_image}\n")
        f.write("WORKDIR /app\n")
        if os.path.exists(requirements):
            f.write("COPY requirements.txt .\n")
            f.write("RUN pip install --no-cache-dir -r requirements.txt\n")
        f.write("COPY . .\n")
        f.write("CMD [\"python\", \"-m\", \"athalia_core.main\"]\n")
    print(f"Dockerfile généré dans {output_path}")

# Optionnel : analyse rapide des dépendances

def analyze_dependencies(project_path: str):
    """Affiche les dépendances du projet."""
    req = os.path.join(project_path, "requirements.txt")
    if os.path.exists(req):
        with open(req) as f:
            print("Dépendances :")
            for line in f:
                print("-", line.strip())
    else:
        print("Aucune requirements.txt trouvée.") 