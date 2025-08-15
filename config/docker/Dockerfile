# Dockerfile Ultra-Professionnel pour Athalia
# Multi-stage build avec optimisations de sécurité et performance

# ========================================
# 🏗️ STAGE 1 - BUILD
# ========================================
FROM python:3.11-slim as builder

# Métadonnées
LABEL maintainer="Arkalia Luna System <contact@arkalia-luna.com>"
LABEL description="Athalia - DevOps Automation Platform"
LABEL version="0.1.0"
LABEL org.opencontainers.image.source="https://github.com/arkalia-luna-system/ia-pipeline"

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Création de l'utilisateur non-root
RUN groupadd -r athalia && useradd -r -g athalia athalia

# Création du répertoire de travail
WORKDIR /app

# Copie des fichiers de dépendances
COPY requirements.txt pyproject.toml ./

# Installation des dépendances Python
RUN pip install --user --no-cache-dir -r requirements.txt

# ========================================
# 🚀 STAGE 2 - RUNTIME
# ========================================
FROM python:3.11-slim as runtime

# Métadonnées runtime
LABEL maintainer="Arkalia Luna System <contact@arkalia-luna.com>"
LABEL description="Athalia Runtime - DevOps Automation Platform"

# Variables d'environnement runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/athalia/.local/bin:$PATH" \
    ATHALIA_ENV=docker

# Installation des dépendances runtime
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Création de l'utilisateur non-root
RUN groupadd -r athalia && useradd -r -g athalia athalia

# Création des répertoires nécessaires
RUN mkdir -p /app /home/athalia/.local /home/athalia/.cache \
    && chown -R athalia:athalia /app /home/athalia

# Changement vers l'utilisateur non-root
USER athalia
WORKDIR /app

# Copie des dépendances installées depuis le stage builder
COPY --from=builder --chown=athalia:athalia /root/.local /home/athalia/.local

# Copie du code source
COPY --chown=athalia:athalia . .

# Installation du projet en mode développement
RUN pip install --user --no-cache-dir -e .

# Exposition des ports
EXPOSE 8000 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Point d'entrée
ENTRYPOINT ["python", "-m", "athalia_core.core.main"]

# Commande par défaut
CMD ["--help"]
