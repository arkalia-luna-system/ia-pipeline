#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plugin d'export Docker pour projet Python.
"""
import os
import subprocess
import logging

logger = logging.getLogger(__name__)


def export_docker(project_path: str, output_path: str = "Dockerfile"):
    """Génère un Dockerfile optimisé pour le projet donné."""
    requirements = os.path.join(project_path, "requirements.txt")
    base_image = "python:3.11"
    
    with open(output_path, "w") as file_handle:
        file_handle.write(f"FROM {base_image}\n")
        file_handle.write("WORKDIR /app\n")
        if os.path.exists(requirements):
            file_handle.write("COPY requirements.txt .\n")
            file_handle.write("RUN pip install --no-cache-dir -r requirements.txt\n")
        file_handle.write("COPY . .\n")
        file_handle.write('CMD ["python3", "src/main.py"]\n')
    
    logger.info(f"Dockerfile généré dans {output_path}")


def analyze_dependencies(project_path: str):
    """Affiche les dépendances du projet."""
    req = os.path.join(project_path, "requirements.txt")
    if os.path.exists(req):
        with open(req) as file_handle:
            logger.info("Dépendances :")
            for line in file_handle:
                logger.info(f"- {line.strip()}")
    else:
        logger.info("Aucune requirements.txt trouvée.")


def run(project_path):
    """Fonction d'entrée standard pour le plugin."""
    dockerfile = os.path.join(project_path, 'Dockerfile')
    with open(dockerfile, 'w') as f:
        f.write('FROM python:3.11\n')
        f.write('WORKDIR /app\n')
        f.write('COPY . .\n')
        f.write('CMD ["python", "src/main.py"]\n')
    
    docker_compose = os.path.join(project_path, 'docker-compose.yml')
    with open(docker_compose, 'w') as f:
        f.write('version: "3.8"\n')
        f.write('services:\n')
        f.write('  app:\n')
        f.write('    build: .\n')
        f.write('    ports:\n')
        f.write('      - "8000:8000"\n')
    
    return "Docker files generated successfully"