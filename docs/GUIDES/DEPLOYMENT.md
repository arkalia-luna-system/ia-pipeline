# Guide de Déploiement Athalia/Arkalia

## Déploiement local
- Prérequis : Python 3.10+, pip, Ollama (pour Qwen/Mistral/LLaVA)
- Installation :
```bash
pip install -r requirements.txt
```
- Lancement :
```bash
python athalia_core/main.py
```

## Déploiement Docker
- Build de l’image :
```bash
docker build -t athalia .
```
- Lancement du container :
```bash
docker run -p 8501:8501 athalia
```

## Déploiement cloud (exemple)
- Prérequis : VM Linux, Docker, ports ouverts
- Copier le repo, builder l’image, lancer le container
- Adapter les variables d’environnement pour la prod (chemins, sécurité, logs)

## Bonnes pratiques production
- Utiliser un reverse proxy (nginx) pour exposer le dashboard/API
- Sécuriser les accès (authentification, HTTPS)
- Monitorer la RAM/CPU (surtout pour les LLM locaux)
- Sauvegarder les logs et les feedbacks utilisateur
- Mettre à jour régulièrement les modèles et dépendances

## FAQ déploiement
- **Comment changer le port du dashboard ?**
  - Modifier le paramètre `--server.port` de Streamlit ou la variable d’environnement.
- **Comment activer/désactiver des modules ?**
  - Modifier le fichier de config ou les options CLI.
- **Comment scaler horizontalement ?**
  - Utiliser plusieurs containers, load balancer, et un cache partagé. 