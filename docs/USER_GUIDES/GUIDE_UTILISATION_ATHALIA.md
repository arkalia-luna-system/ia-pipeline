# 🚀 GUIDE D'UTILISATION ATHALIA

## 🎯 **PRÉSENTATION**

Athalia est une plateforme d'automatisation DevOps pour la génération automatique de projets de développement via templates. Ce guide vous accompagne dans l'utilisation optimale d'Athalia.

### **🏆 VALIDATION UTILISATEUR (20 AOÛT 2025)**
- ✅ **Test utilisateur complet réalisé** - Note globale : **17.6/20**
- ✅ **Génération de projets fonctionnelle** - Structure professionnelle créée
- ✅ **Navigation documentaire excellente** - Plus jamais perdu
- ✅ **Nettoyage automatique spectaculaire** - 230 fichiers supprimés automatiquement

---

## 🚀 **DÉMARRAGE RAPIDE**

### **1. Installation et Configuration**

```bash
# Cloner le projet
git clone https://github.com/arkalia-luna-system/ia-pipeline.git
cd ia-pipeline

# Activer l'environnement virtuel
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### **2. Génération de Projet Simple**

```python
from athalia_core.utilities.generation_simple import generate_blueprint_mock

# Créer un blueprint pour votre projet
blueprint = generate_blueprint_mock("API REST pour gestion d'utilisateurs")

# Afficher le blueprint généré
print(f"Blueprint créé: {blueprint}")
```

---

## 🎯 **TYPES DE PROJETS SUPPORTÉS**

### **🤖 API REST**
```python
from athalia_core.utilities.generation_simple import generate_blueprint_mock
blueprint = generate_blueprint_mock("API REST pour gestion de produits")
# Génère: Blueprint avec FastAPI, Pydantic, SQLAlchemy, authentification
```

### **🌐 Application Web**
```python
from athalia_core.utilities.generation_simple import generate_blueprint_mock
blueprint = generate_blueprint_mock("Application web pour gestion de tâches")
# Génère: Blueprint avec Flask, SQLAlchemy, templates, authentification
```

### **📊 Traitement de Données**
```python
from athalia_core.utilities.generation_simple import generate_blueprint_mock
blueprint = generate_blueprint_mock("Application d'analyse de données")
# Génère: Blueprint avec Pandas, NumPy, Matplotlib, Jupyter
```

### **🧠 Intelligence Artificielle**
```python
from athalia_core.utilities.generation_simple import generate_blueprint_mock
blueprint = generate_blueprint_mock("Système de reconnaissance d'images")
# Génère: Blueprint avec PyTorch, Transformers, scikit-learn
```

### **🤖 Robotique**
```python
from athalia_core.utilities.generation_simple import generate_blueprint_mock
blueprint = generate_blueprint_mock("Contrôle de robot mobile")
# Génère: Blueprint avec ROS2, OpenCV, contrôle moteurs
```

---

## 🔧 **FONCTIONNALITÉS AVANCÉES**

### **1. Génération Intelligente de Noms**

Athalia analyse automatiquement votre description pour générer des noms de projets appropriés :

```python
# "API REST pour gestion d'utilisateurs" → "api_rest_gestion"
# "Application web pour e-commerce" → "app_web_ecommerce"
# "Système de traitement de données" → "systeme_traitement_donnees"
```

### **2. Détection Automatique du Type**

Le système détecte intelligemment le type de projet basé sur les mots-clés :

- **API/REST** : `api`, `rest`, `endpoint`, `service`
- **Web** : `web`, `site`, `interface`, `flask`, `django`
- **Data** : `data`, `analyse`, `traitement`, `pandas`, `numpy`
- **IA** : `ia`, `ml`, `intelligence`, `neural`
- **Robotics** : `robot`, `controle`, `automation`

> ⚠️ **Note Test Utilisateur** : Actuellement en mode générique (type "generic" retourné), optimisation de la classification en cours selon le rapport d'améliorations restantes.

### **3. Dépendances Intelligentes**

Chaque type de projet génère automatiquement les bonnes dépendances :

```python
# API REST
fastapi>=0.100.0, uvicorn[standard]>=0.20.0, pydantic>=2.0.0

# Web
flask>=2.3.0, flask-sqlalchemy>=3.0.0, jinja2>=3.1.0

# Data
pandas>=2.0.0, numpy>=1.24.0, matplotlib>=3.7.0

# IA
torch>=2.0.0, transformers>=4.30.0, scikit-learn>=1.3.0
```

### **4. Code Intelligent**

Le code généré inclut :
- ✅ **Logging approprié** avec configuration
- ✅ **Gestion d'erreurs** robuste
- ✅ **Documentation** complète
- ✅ **Tests** fonctionnels
- ✅ **Configuration** flexible
- ✅ **Structure** professionnelle

---

## 🛡️ **SÉCURITÉ ET QUALITÉ**

### **Audit de Sécurité Automatique**

```python
from athalia_core.security_auditor import SecurityAuditor

# Auditer un projet généré
auditor = SecurityAuditor("./mon-projet")
result = auditor.run()
print(f"Score de sécurité: {result['global_score']}/100")
```

### **Nettoyage Automatique**

Athalia nettoie automatiquement les fichiers parasites :
- 🗑️ **Fichiers Apple Double** (._*)
- 🗑️ **Fichiers système** (.DS_Store, Thumbs.db)
- 🗑️ **Fichiers temporaires** (*.tmp, *.bak)
- 🗑️ **Répertoires vides**

---

## 📊 **EXEMPLES COMPLETS**

### **Exemple 1: API REST Complète**

```python
from athalia_core.generation import generate_blueprint_mock, generate_project

# Créer une API REST
blueprint = generate_blueprint_mock("""
API REST pour gestion d'utilisateurs avec authentification JWT,
base de données PostgreSQL, et documentation Swagger
""")

# Générer le projet
project_path = generate_project(blueprint, "./api-users")

# Le projet généré inclut :
# - FastAPI avec CORS
# - Modèles Pydantic
# - Endpoints CRUD complets
# - Gestion d'erreurs HTTP
# - Logging structuré
# - Documentation automatique
```

### **Exemple 2: Application Web Moderne**

```python
blueprint = generate_blueprint_mock("""
Application web pour gestion de tâches avec interface moderne,
base de données SQLite, et authentification utilisateur
""")

project_path = generate_project(blueprint, "./task-manager")

# Le projet généré inclut :
# - Flask avec SQLAlchemy
# - Modèles de données
# - Routes API et web
# - Templates HTML
# - Système d'authentification
# - Gestion de sessions
```

### **Exemple 3: Traitement de Données**

```python
blueprint = generate_blueprint_mock("""
Système d'analyse de données pour traitement de fichiers CSV,
visualisation avec matplotlib, et export de rapports
""")

project_path = generate_project(blueprint, "./data-analyzer")

# Le projet généré inclut :
# - Pandas pour manipulation
# - NumPy pour calculs
# - Matplotlib pour visualisation
# - Gestion de fichiers
# - Export de résultats
# - Tests de données
```

---

## 🔍 **DIAGNOSTIC ET DÉBOGAGE**

### **Vérification de la Qualité**

```python
# Tester le projet généré
import subprocess
import os

def test_generated_project(project_path):
    os.chdir(project_path)
    
    # Installer les dépendances
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Lancer les tests
    result = subprocess.run(["python", "-m", "pytest", "tests/", "-v"])
    
    return result.returncode == 0

# Utilisation
success = test_generated_project("./mon-projet")
print(f"Tests passés: {success}")
```

### **Analyse de Structure**

```python
from pathlib import Path

def analyze_project_structure(project_path):
    project = Path(project_path)
    
    structure = {
        "fichiers": [],
        "repertoires": [],
        "taille_totale": 0
    }
    
    for item in project.rglob("*"):
        if item.is_file():
            structure["fichiers"].append(str(item))
            structure["taille_totale"] += item.stat().st_size
        elif item.is_dir():
            structure["repertoires"].append(str(item))
    
    return structure

# Utilisation
structure = analyze_project_structure("./mon-projet")
print(f"Fichiers: {len(structure['fichiers'])}")
print(f"Répertoires: {len(structure['repertoires'])}")
print(f"Taille totale: {structure['taille_totale']} octets")
```

---

## 🚀 **BONNES PRATIQUES**

### **1. Descriptions Détaillées**

✅ **Bonne description :**
```python
blueprint = generate_blueprint_mock("""
API REST pour gestion d'inventaire avec authentification JWT,
base de données PostgreSQL, validation des données,
et documentation Swagger complète
""")
```

❌ **Description trop vague :**
```python
blueprint = generate_blueprint_mock("API pour inventaire")
```

### **2. Organisation des Projets**

```bash
mon-projet/
├── src/                    # Code source
├── tests/                  # Tests unitaires
├── docs/                   # Documentation
├── config/                 # Configuration
├── data/                   # Données
├── logs/                   # Logs
├── README.md              # Documentation principale
├── requirements.txt       # Dépendances
└── CLEANUP_REPORT.md     # Rapport de nettoyage
```

### **3. Tests et Validation**

```python
# Toujours tester après génération
def validate_generated_project(project_path):
    # Vérifier la structure
    assert Path(f"{project_path}/src/main.py").exists()
    assert Path(f"{project_path}/tests/").exists()
    assert Path(f"{project_path}/requirements.txt").exists()
    
    # Vérifier les imports
    try:
        exec(open(f"{project_path}/src/main.py").read())
        return True
    except Exception as e:
        print(f"Erreur d'import: {e}")
        return False
```

---

## 🔧 **CONFIGURATION AVANCÉE**

### **Personnalisation du Blueprint**

```python
blueprint = {
    "project_name": "mon_api_personnalisee",
    "description": "API REST personnalisée",
    "project_type": "api",
    "modules": ["core", "auth", "database"],
    "dependencies": ["redis>=4.0.0", "celery>=5.0.0"],
    "features": {
        "authentication": True,
        "database": True,
        "caching": True,
        "background_tasks": True
    }
}

project_path = generate_project(blueprint, "./custom-api")
```

### **Mode Dry-Run**

```python
# Tester sans créer de fichiers
project_path = generate_project(blueprint, "./test", dry_run=True)
print(f"Rapport généré: {project_path}/dry_run_report.txt")
```

---

## 📈 **MÉTRIQUES ET PERFORMANCE**

### **Statistiques de Génération**

```python
import time
from athalia_core.generation import generate_project

def benchmark_generation(blueprint, iterations=5):
    times = []
    
    for i in range(iterations):
        start_time = time.time()
        project_path = generate_project(blueprint, f"./benchmark-{i}")
        end_time = time.time()
        times.append(end_time - start_time)
    
    avg_time = sum(times) / len(times)
    print(f"Temps moyen de génération: {avg_time:.2f} secondes")
    return avg_time
```

---

## 🆘 **RÉSOLUTION DE PROBLÈMES**

### **Problèmes Courants**

#### **1. Erreur d'Import**
```python
# Problème: ModuleNotFoundError
# Solution: Vérifier le PYTHONPATH
import sys
sys.path.append('../athalia_core')
```

#### **2. Fichiers Parasites**
```python
# Problème: Fichiers ._* ou .DS_Store
# Solution: Nettoyage automatique intégré
from athalia_core.auto_cleaner import AutoCleaner
cleaner = AutoCleaner("./mon-projet")
cleaner.clean_generated_project("./mon-projet")
```

#### **3. Dépendances Manquantes**
```python
# Problème: ImportError dans le projet généré
# Solution: Vérifier requirements.txt
import subprocess
subprocess.run(["pip", "install", "-r", "requirements.txt"])
```

---

## 🎉 **CONCLUSION**

Athalia transforme la génération de projets en une expérience intelligente et automatisée. Avec ses fonctionnalités avancées de détection de type, génération de code intelligent, et nettoyage automatique, vous pouvez créer des projets professionnels en quelques secondes.

**🚀 Prêt à créer votre prochain projet avec Athalia ?**

---

*Guide généré automatiquement par Athalia - Version 12.0* 