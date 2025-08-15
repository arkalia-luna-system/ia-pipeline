# 🎭 **PROJET DÉMO ATHALIA** - Cycle Complet en 1 Commande

## 🎯 **Objectif**

Ce projet démo montre le **cycle complet** d'Athalia en **1 seule commande** :
1. **Génération** d'un projet
2. **Tests** automatiques
3. **Dashboard** en temps réel
4. **Documentation** générée

## 🚀 **Démo Ultra-Rapide (1 commande)**

```bash
# Démo complète en 1 commande
make -f ../../config/makefile/Makefile demo

# Ou avec Docker (encore plus simple)
docker-compose -f ../../config/docker/docker-compose.yml up athalia
```

## 📁 **Structure du Projet Démo**

```
demo_project/
├── README.md              # Ce fichier
├── config/                # Configuration du projet
│   ├── athalia.yml        # Config Athalia
│   └── templates/         # Templates personnalisés
├── data/                  # Données de test
│   ├── sample_data.csv    # Dataset fictif
│   └── config.json        # Configuration
├── tests/                 # Tests automatiques
│   ├── test_generation.py # Test génération
│   └── test_dashboard.py  # Test dashboard
└── expected_output/        # Résultats attendus
    ├── generated_code/     # Code généré
    ├── test_results/       # Résultats tests
    └── dashboard/          # Dashboard final
```

## 🎬 **Scénario de Démo**

### **1. 🏗️ Génération de Projet**
- **Input** : Configuration YAML + templates
- **Output** : Code Python + tests + documentation
- **Temps** : < 30 secondes

### **2. 🧪 Tests Automatiques**
- **Input** : Code généré
- **Output** : Rapport de couverture + résultats
- **Temps** : < 1 minute

### **3. 📊 Dashboard en Temps Réel**
- **Input** : Résultats des tests
- **Output** : Interface web interactive
- **Temps** : < 10 secondes

### **4. 📚 Documentation Générée**
- **Input** : Code + tests + métriques
- **Output** : Site web complet
- **Temps** : < 20 secondes

## 🔧 **Configuration Démo**

### **Fichier de Configuration :**
```yaml
# config/athalia.yml
project:
  name: "demo-project"
  type: "web-api"
  framework: "fastapi"
  database: "postgresql"
  testing: "pytest"
  documentation: "mkdocs"

generation:
  templates: "custom"
  output_dir: "generated"
  overwrite: true

testing:
  framework: "pytest"
  coverage: 80
  parallel: true

dashboard:
  type: "streamlit"
  port: 8501
  auto_refresh: true
```

### **Templates Personnalisés :**
- **FastAPI** : API REST moderne
- **PostgreSQL** : Base de données robuste
- **Pytest** : Tests professionnels
- **MkDocs** : Documentation élégante

## 📊 **Métriques de Démo**

| **Métrique** | **Valeur** | **Objectif** |
|--------------|------------|--------------|
| **Temps Total** | < 2 minutes | Rapidité |
| **Code Généré** | 500+ lignes | Qualité |
| **Tests** | 20+ tests | Robustesse |
| **Couverture** | ≥80% | Qualité |
| **Dashboard** | Temps réel | Interactivité |

## 🌐 **Accès aux Services**

### **Services Locaux :**
- **API** : http://localhost:8000
- **Dashboard** : http://localhost:8501
- **Documentation** : http://localhost:8000/docs

### **Services Docker :**
- **Athalia** : http://localhost:8000
- **Redis** : localhost:6379
- **PostgreSQL** : localhost:5432
- **Prometheus** : http://localhost:9090
- **Grafana** : http://localhost:3000

## 🎯 **Points Clés de la Démo**

### **1. Rapidité**
- **Génération** : < 30 secondes
- **Tests** : < 1 minute
- **Dashboard** : < 10 secondes

### **2. Qualité**
- **Code** : Standards PEP8
- **Tests** : Couverture ≥80%
- **Documentation** : Automatique

### **3. Simplicité**
- **1 commande** : `make demo`
- **0 configuration** : Tout automatique
- **0 erreur** : Gestion d'erreurs robuste

## 🚀 **Utilisation Avancée**

### **Personnalisation :**
```bash
# Modifier la configuration
vim config/athalia.yml

# Ajouter des templates
cp -r templates/custom templates/my_templates

# Lancer avec config personnalisée
ATHALIA_CONFIG=config/my_config.yml make demo
```

### **Intégration CI/CD :**
```yaml
# .github/workflows/demo.yml
- name: Demo Test
  run: |
    make -f config/makefile/Makefile demo
    # Vérifier que la démo fonctionne
```

## 🏆 **Objectif de la Démo**

**Montrer qu'Athalia peut :**
1. **Générer** un projet complet en 30 secondes
2. **Tester** automatiquement avec couverture ≥80%
3. **Dashboard** en temps réel avec métriques
4. **Documenter** automatiquement le projet

**Résultat :** Le recruteur voit **immédiatement** ce que tu peux faire ! 🎯

---

*Projet démo maintenu par l'équipe Athalia - DevOps Automation Platform*
*Objectif : Démonstration en 1 commande*
