# Dockerfile pour web
FROM python:3.9-slim

WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port
EXPOSE 8000

# Commande par défaut
CMD ["python", "main.py"]
