# Guide de Déploiement Athalia/Arkalia

## 🚀 Déploiement Local

### Prérequis
- **Python** : 3.10+
- **Pip** : Dernière version
- **Ollama** : Pour Qwen/Mistral/LLaVA
- **Git** : Pour cloner le repository

### Installation Complète
```bash
# 1. Cloner le repository
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# 2. Créer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Sur macOS/Linux
# ou .venv\Scripts\activate  # Sur Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Vérifier l'installation
python3 athalia_core/utilities/ready_check.py
```

### Lancement des Services
```bash
# Interface principale
python3 athalia_core/core/main.py

# Orchestrateur unifié
python3 bin/core/athalia_unified.py --help

# Dashboard Streamlit
streamlit run athalia_core/utilities/dashboard.py

# API REST (si configurée)
python3 athalia_core/api_server.py
```

## 🐳 Déploiement Docker

### Build de l'Image
```bash
# Build simple
docker build -t athalia:latest .

# Build avec cache optimisé
docker build --build-arg BUILDKIT_INLINE_CACHE=1 -t athalia:latest .

# Build multi-stage pour production
docker build -f Dockerfile.prod -t athalia:prod .
```

### Lancement du Container
```bash
# Container simple
docker run -p 8501:8501 athalia:latest

# Container avec volumes persistants
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  -e ENVIRONMENT=production \
  athalia:latest

# Container avec Docker Compose
docker-compose up -d
```

### Configuration Docker Compose
```yaml
# docker-compose.yml
version: '3.8'
services:
  athalia:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
    restart: unless-stopped
```

## ☁️ Déploiement Cloud

### Cas d'Usage 1 : VM Linux (Ubuntu/Debian)
```bash
# 1. Préparer la VM
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip git docker.io

# 2. Cloner et configurer
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# 3. Configuration production
cp config/athalia_config.yaml config/athalia_config_prod.yaml
# Modifier les chemins, sécurité, logs

# 4. Déploiement Docker
docker build -t athalia:prod .
docker run -d -p 8501:8501 --name athalia-prod athalia:prod
```

### Cas d'Usage 2 : Kubernetes
```yaml
# athalia-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: athalia
spec:
  replicas: 3
  selector:
    matchLabels:
      app: athalia
  template:
    metadata:
      labels:
        app: athalia
    spec:
      containers:
      - name: athalia
        image: athalia:latest
        ports:
        - containerPort: 8501
        env:
        - name: ENVIRONMENT
          value: "production"
        volumeMounts:
        - name: athalia-data
          mountPath: /app/data
      volumes:
      - name: athalia-data
        persistentVolumeClaim:
          claimName: athalia-pvc
```

### Cas d'Usage 3 : AWS ECS
```json
{
  "family": "athalia",
  "containerDefinitions": [
    {
      "name": "athalia",
      "image": "athalia:latest",
      "portMappings": [
        {
          "containerPort": 8501,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "ENVIRONMENT",
          "value": "production"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/athalia",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

## 🔒 Bonnes Pratiques Production

### Sécurité
```bash
# 1. Reverse Proxy Nginx
sudo apt install nginx
# Configuration nginx.conf pour proxy vers port 8501

# 2. SSL/TLS avec Let's Encrypt
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d votre-domaine.com

# 3. Firewall
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 22
sudo ufw enable
```

### Monitoring
```bash
# 1. Monitoring système
sudo apt install htop iotop nethogs

# 2. Monitoring application
python3 athalia_core/performance_analyzer.py --monitor

# 3. Logs centralisés
# Configurer rsyslog ou logrotate
```

### Sauvegarde
```bash
# 1. Sauvegarde automatique des données
python3 athalia_core/backup_system.py --auto-backup

# 2. Script de sauvegarde cron
# Ajouter dans crontab -e
0 2 * * * /chemin/vers/athalia/scripts/backup.sh

# 3. Sauvegarde cloud (AWS S3)
aws s3 sync ./data s3://votre-bucket/athalia-backup/
```

## 📊 Configuration Avancée

### Variables d'Environnement
```bash
# Production
export ENVIRONMENT=production
export LOG_LEVEL=INFO
export DATABASE_URL=postgresql://user:pass@localhost/athalia
export REDIS_URL=redis://localhost:6379
export SECRET_KEY=votre-cle-secrete

# Développement
export ENVIRONMENT=development
export LOG_LEVEL=DEBUG
export DATABASE_URL=sqlite:///athalia_dev.db
```

### Configuration Fichier
```yaml
# config/athalia_config_prod.yaml
general:
  lang: fr
  verbose: false
  auto_fix: true
  dry_run: false
  log_level: INFO
  log_file: /var/log/athalia/athalia.log

database:
  path: /app/data/athalia_prod.db
  backup: true
  backup_retention: 30

ai:
  models:
    - ollama_mistral
    - ollama_llama
    - mock
  timeout: 30
  max_retries: 3
  fallback_enabled: true

security:
  enabled: true
  auth_required: true
  ssl_enabled: true
```

## 🚨 Troubleshooting

### Problèmes Courants

#### 1. Port déjà utilisé
```bash
# Vérifier les ports utilisés
sudo netstat -tulpn | grep :8501

# Changer le port
streamlit run athalia_core/utilities/dashboard.py --server.port 8502
```

#### 2. Problèmes de mémoire
```bash
# Vérifier l'utilisation mémoire
free -h
htop

# Optimiser pour les LLM
export OLLAMA_HOST=0.0.0.0
export OLLAMA_ORIGINS=*
```

#### 3. Problèmes de permissions
```bash
# Corriger les permissions
sudo chown -R $USER:$USER /chemin/vers/athalia
chmod +x scripts/*.sh
```

### Logs et Debug
```bash
# Voir les logs en temps réel
tail -f logs/athalia.log

# Debug mode
python3 athalia_core/core/main.py --debug

# Validation complète
python3 athalia_core/utilities/ready_check.py --verbose
```

## 📋 Checklist de Déploiement

### Pré-déploiement
- [ ] Tests unitaires passent
- [ ] Tests d'intégration validés
- [ ] Configuration production prête
- [ ] Variables d'environnement définies
- [ ] Base de données configurée

### Déploiement
- [ ] Build de l'image Docker
- [ ] Tests de l'image
- [ ] Déploiement en staging
- [ ] Tests de validation
- [ ] Déploiement en production

### Post-déploiement
- [ ] Monitoring configuré
- [ ] Alertes définies
- [ ] Sauvegarde automatique
- [ ] Documentation mise à jour
- [ ] Équipe formée

---

**🚀 Athalia - Prêt pour la Production !**
