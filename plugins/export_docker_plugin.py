"""
Plugin d'export Docker pour projet Python.
"""
import os

def run(project_path='.'):
    dockerfile = os.path.join(project_path, 'Dockerfile')
    composefile = os.path.join(project_path, 'docker-compose.yml')
    # Dockerfile basique
    docker_content = '''
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt || true
CMD ["python3", "src/main.py"]
'''
    with open(dockerfile, 'w') as f:
        f.write(docker_content)
    # docker-compose.yml basique
    compose_content = '''
version: '3'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - PYTHONUNBUFFERED=1
'''
    with open(composefile, 'w') as f:
        f.write(compose_content)
    return f"Dockerfile et docker-compose.yml générés dans {project_path}" 