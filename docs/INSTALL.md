# Guide d'Installation Athalia/Arkalia

## Prérequis
- **Python 3.10+** 
- **pip** (gestionnaire de paquets Python)
- **Git** (pour cloner le repo)
- **Ollama** (pour Qwen, Mistral, LLaVA) - [Installation Ollama](https://ollama.ai/)

## Installation rapide

1. **Cloner le repo**
   ```bash
   git clone https://github.com/arkalia-luna-system/athalia-dev-setup.git
   cd athalia-dev-setup
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Installer Ollama (optionnel mais recommandé)**
   ```bash
   # macOS/Linux
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Télécharger les modèles
   ollama pull mistral:instruct
   ollama pull qwen:7b
   ollama pull llava:latest
   ```

4. **Lancer le pipeline**
   ```bash
   python athalia_core/main.py
   ```

## Première utilisation

1. **Choisir l'option 1** dans le menu CLI
2. **Décrire votre projet** en une phrase (ex: "API de gestion de tâches")
3. **Attendre la génération** (quelques secondes)
4. **Consulter les fichiers générés** :
   - `projects/[nom_projet]/README.md` : présentation du projet
   - `projects/[nom_projet]/ONBOARDING.md` : guide d'installation
   - `projects/[nom_projet]/DOC.md` : documentation technique
   - `projects/[nom_projet]/openapi.yaml` : spécification API

## Utilisation avancée

### CLI Unifiée
```bash
# Industrialisation complète
python athalia_unified.py /chemin/projet --action complete

# Profils utilisateur
python athalia_unified.py /chemin/projet --action profil --utilisateur nom

# Auto-correction
python athalia_unified.py /chemin/projet --action correction
```

### Dashboard Web
```bash
# Lancer le dashboard
python athalia_core/dashboard.py

# Ouvrir dans le navigateur
open http://localhost:8080
```

### Tests et Benchmarks
```bash
# Lancer tous les tests
pytest

# Benchmark Qwen/Mistral
python benchmark_qwen_mistral.py

# Benchmark distillation
python setup/benchmark_distillation.py
```

### Alias Utiles
```bash
# Activer les alias
source setup/alias.sh

# Utiliser les commandes rapides
ath-test      # Lancer les tests
ath-dashboard # Ouvrir le dashboard
ath-smart     # Prompt contextuel IA
ath-clean     # Nettoyer le projet
```

## Dépannage

### Erreurs courantes

- **Erreur de dépendances** : 
  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt --force-reinstall
  ```

- **Problème de permissions** : 
  ```bash
  # Utiliser un environnement virtuel
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  # ou
  venv\Scripts\activate     # Windows
  ```

- **CLI qui plante** : 
  ```bash
  # Vérifier Python 3.10+
  python --version
  ```

- **Ollama non trouvé** :
  ```bash
  # Vérifier l'installation
  ollama --version
  
  # Redémarrer le service
  ollama serve
  ```

### Configuration

Le fichier `config/athalia_config.yaml` permet de personnaliser :
- Modules à activer/désactiver
- Modèles IA à utiliser
- Paramètres du dashboard
- Configuration des tests

## Support

- **Documentation** : Voir [docs/USER_GUIDE.md](USER_GUIDE.md)
- **FAQ** : Voir [docs/FAQ.md](FAQ.md)
- **Problèmes** : Ouvrir une issue sur GitHub
- **Discussions** : Utiliser les discussions GitHub

---

*Guide d'installation mis à jour le 2025-07-18*
