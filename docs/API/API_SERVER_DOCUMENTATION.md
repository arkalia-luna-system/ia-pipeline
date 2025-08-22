# 📡 **Serveur API Principal d'Athalia**

## 📋 **Vue d'ensemble**

Le module `main_api_server.py` est le serveur API REST principal d'Athalia, fournissant une interface complète pour l'intégration et l'automatisation DevOps.

## 🏗️ **Architecture**

### **Technologies utilisées**
- **FastAPI** : Framework web moderne et rapide
- **Pydantic** : Validation et sérialisation des données
- **Uvicorn** : Serveur ASGI haute performance
- **CORS** : Support cross-origin pour l'intégration web

### **Structure du serveur**
```
main_api_server.py
├── Modèles Pydantic (BaseModel)
├── Configuration FastAPI
├── Middleware CORS
├── Routes API
├── Gestionnaires d'erreurs
└── Fonctions utilitaires
```

## 🔌 **Endpoints API**

### **1. Vérification de santé**
- **GET** `/health` - Statut de l'API  
- **GET** `/` - Page d'accueil HTML

### **2. Gestion des projets**
- **GET** `/api/projects` - Liste des projets
- **POST** `/api/projects/generate` - Génération de projet

### **3. Sécurité**
- **POST** `/api/security/scan` - Scan de sécurité

### **4. Métriques et monitoring**
- **GET** `/api/metrics` - Métriques du système
- **GET** `/api/plugins` - Liste des plugins

## 📊 **Modèles de données**

### **HealthResponse**
```python
{
    "status": "healthy",
    "timestamp": "2024-01-01T00:00:00",
    "version": "12.0.0",
    "uptime": 3600.0
}
```

### **ProjectBlueprint**
```python
{
    "name": "mon_projet",
    "description": "Description du projet",
    "project_type": "web",
    "dependencies": ["fastapi", "sqlalchemy"],
    "modules": ["auth", "database"]
}
```

### **SecurityScanResponse**
```python
{
    "scan_id": "scan_20240101_120000",
    "status": "completed",
    "vulnerabilities": {"high": 0, "medium": 1, "low": 2},
    "score": 95,
    "recommendations": ["Mettre à jour les dépendances"]
}
```

## 🚀 **Utilisation**

### **Démarrage du serveur**
```bash
# Démarrage simple
python athalia_core/api/main_api_server.py

# Démarrage avec port personnalisé
PORT=8080 python athalia_core/api/main_api_server.py

# Mode debug
DEBUG=true python athalia_core/api/main_api_server.py
```

### **Variables d'environnement**
- `PORT` : Port du serveur (défaut: 8000)
- `DEBUG` : Mode debug (défaut: false)

## 🔧 **Configuration**

### **CORS**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```

### **Documentation automatique**
- **Swagger UI** : `/docs`
- **ReDoc** : `/redoc`
- **OpenAPI JSON** : `/openapi.json`

## 📈 **Métriques et monitoring**

### **Métriques système**
- Version Python et FastAPI
- Utilisation mémoire et CPU
- Temps de fonctionnement

### **Métriques projet**
- Nombre total de fichiers
- Lignes de code
- Fichiers de test

## 🛡️ **Sécurité**

### **Gestion des erreurs**
- Gestionnaire d'erreurs HTTP personnalisé
- Gestionnaire d'erreurs générales
- Logging structuré des erreurs

### **Validation des données**
- Validation automatique avec Pydantic
- Gestion des erreurs de validation
- Réponses d'erreur standardisées

## 🔄 **Tâches en arrière-plan**

### **Génération de projet**
```python
background_tasks.add_task(
    generate_project_files, 
    blueprint, 
    output_path
)
```

### **Fonctionnalités**
- Création de fichiers README
- Génération de structure de projet
- Installation des dépendances

## 📝 **Logs et debugging**

### **Niveaux de log**
- **INFO** : Opérations normales
- **ERROR** : Erreurs et exceptions
- **DEBUG** : Informations détaillées (mode debug)

### **Format des logs**
```
[INFO] 🚀 Démarrage du serveur API Athalia sur le port 8000
[INFO] 📖 Documentation disponible sur http://localhost:8000/docs
[INFO] 📊 Dashboard disponible sur http://localhost:8000/dashboard
```

## 🔗 **Intégration**

### **Clients supportés**
- Applications web (JavaScript/TypeScript)
- Outils CLI
- Services microservices
- Intégrations CI/CD

### **Formats de réponse**
- **JSON** : Données structurées
- **HTML** : Interface web
- **OpenAPI** : Spécification API

## 🚧 **Développement**

### **Ajout de nouveaux endpoints**
1. Définir le modèle Pydantic
2. Créer la fonction de route
3. Ajouter la gestion d'erreurs
4. Tester avec la documentation automatique

### **Tests**
```bash
# Tests unitaires
pytest tests/unit/api/

# Tests d'intégration
pytest tests/integration/api/

# Tests de performance
pytest tests/performance/api/
```

## 📚 **Ressources**

### **Documentation officielle**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

### **Exemples d'utilisation**
- [Exemples FastAPI](https://github.com/tiangolo/fastapi/tree/master/docs_src)
- [Patterns d'API](https://fastapi.tiangolo.com/tutorial/best-practices/)

---

**Version** : 12.0.0  
**Dernière mise à jour** : 2024-01-01  
**Mainteneur** : Équipe Athalia
