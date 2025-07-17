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
        f.write("CMD [\"python3\", \"src/main.py\"]\n")
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

def run(project_path):
    """Fonction d'entrée standard pour le plugin, attendue par les tests."""
    output_path = os.path.join(project_path, "Dockerfile")
    export_docker(project_path, output_path)
    
    # Générer aussi docker-compose.yml
    compose_path = os.path.join(project_path, "docker-compose.yml")
    with open(compose_path, "w") as f:
        f.write(f"""version: '3
services:
  app:
    build: .
    ports:
      - "5000:50    volumes:
      - .:/app
    environment:
      - PYTHONUNBUFFERED=1
""")
    
    return f"Dockerfile et docker-compose.yml générés pour {project_path}" 