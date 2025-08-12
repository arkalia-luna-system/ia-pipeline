# 📋 Templates Athalia

## Vue d'ensemble

Le dossier `templates/` contient tous les modèles de code générés automatiquement par Athalia. Ces templates servent de base pour créer rapidement de nouveaux projets avec une architecture professionnelle et des bonnes pratiques intégrées.

## 🏗️ Structure

```
templates/
├── api/                    # Templates pour les APIs
│   └── main.py.j2         # Template FastAPI complet
├── memory/                 # Templates pour la gestion mémoire
│   └── memory.py.j2       # Gestionnaire de mémoire intelligent
├── tts/                    # Templates pour Text-to-Speech
│   └── tts.py.j2          # Gestionnaire TTS avancé
└── README.md               # Ce fichier
```

## 🚀 Templates Disponibles

### 1. **API Template** (`api/main.py.j2`)

**Description :** Template complet pour une API FastAPI professionnelle.

**Fonctionnalités :**
- ✅ Configuration FastAPI avec CORS
- ✅ Modèles Pydantic pour la validation
- ✅ Routes de base (/, /health, /api/items)
- ✅ Gestion d'erreurs globale
- ✅ Configuration par variables d'environnement
- ✅ Documentation automatique (Swagger/ReDoc)

**Utilisation :**
```bash
# Génération d'un nouveau projet API
athalia generate api --name mon-api --template api/main.py.j2
```

### 2. **Memory Template** (`memory/memory.py.j2`)

**Description :** Gestionnaire de mémoire intelligent avec cache et persistance.

**Fonctionnalités :**
- ✅ Cache en mémoire avec TTL configurable
- ✅ Sauvegarde automatique sur disque
- ✅ Nettoyage automatique des éléments expirés
- ✅ Statistiques et monitoring
- ✅ Gestion de la taille maximale du cache

**Utilisation :**
```python
from templates.memory.memory import MemoryManager

# Initialisation
memory = MemoryManager(storage_path="cache", max_size=1000)

# Stockage avec TTL
memory.store("user_data", user_info, ttl=3600)  # 1 heure

# Récupération
data = memory.retrieve("user_data")
```

### 3. **TTS Template** (`tts/tts.py.j2`)

**Description :** Gestionnaire Text-to-Speech avec support multi-voix.

**Fonctionnalités :**
- ✅ Support multi-voix configurable
- ✅ Cache intelligent des synthèses
- ✅ Traitement asynchrone avec queue
- ✅ Gestion des paramètres de voix (vitesse, pitch, volume)
- ✅ Export dans différents formats

**Utilisation :**
```python
from templates.tts.tts import TTSManager

# Initialisation
tts = TTSManager(output_dir="audio", cache_size=100)

# Synthèse synchrone
audio_file = tts.synthesize("Bonjour, comment allez-vous ?")

# Synthèse asynchrone
tts.synthesize("Long texte...", async_mode=True)
```

## 🎯 Personnalisation

### Variables de Template

Tous les templates utilisent des variables Jinja2 :

- `{{ project_name }}` : Nom du projet
- `{{ author }}` : Auteur du projet
- `{{ version }}` : Version du projet
- `{{ description }}` : Description du projet

### Exemple de Personnalisation

```bash
# Génération avec variables personnalisées
athalia generate api \
  --name mon-projet \
  --template api/main.py.j2 \
  --vars project_name="MonAPI" \
  --vars author="Développeur" \
  --vars version="2.0.0"
```

## 🔧 Intégration avec Athalia

### Génération Automatique

Les templates sont utilisés par le système de génération d'Athalia :

```python
from athalia_core.template_engine import TemplateEngine

engine = TemplateEngine()
engine.generate_from_template(
    template_path="templates/api/main.py.j2",
    output_path="mon_projet/main.py",
    variables={"project_name": "MonProjet"}
)
```

### Validation des Templates

Chaque template est validé avant utilisation :

```bash
# Validation syntaxique
athalia validate template templates/api/main.py.j2

# Test de génération
athalia test template templates/api/main.py.j2
```

## 📚 Développement de Nouveaux Templates

### Structure Recommandée

```python
"""
Template pour [Type de Module] - {{ project_name }}

Ce fichier est généré automatiquement par Athalia.
Modifiez-le selon vos besoins spécifiques.
"""

# Imports standards
import os
import logging
from typing import Dict, Any, Optional
from pathlib import Path

# Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MonModule:
    """Description de la classe principale."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialisation du module."""
        self.config = config or {}
        logger.info("Module initialisé")
    
    def main_function(self) -> bool:
        """Fonction principale du module."""
        try:
            # Logique du module
            return True
        except Exception as e:
            logger.error(f"Erreur: {e}")
            return False

if __name__ == "__main__":
    # Exemple d'utilisation
    module = MonModule()
    success = module.main_function()
    print(f"Succès: {success}")
```

### Bonnes Pratiques

1. **Documentation complète** : Docstrings pour toutes les classes et méthodes
2. **Gestion d'erreurs** : Try/catch avec logging approprié
3. **Configuration flexible** : Variables d'environnement et paramètres
4. **Tests intégrés** : Exemples d'utilisation dans `if __name__ == "__main__"`
5. **Logging professionnel** : Configuration et niveaux appropriés

## 🧪 Tests et Validation

### Tests Automatiques

```bash
# Exécution des tests de templates
pytest tests/templates/ -v

# Validation de la syntaxe
python -m py_compile templates/api/main.py.j2
```

### Validation Manuelle

1. **Génération de test** : Créer un projet de test
2. **Vérification syntaxique** : Importer et exécuter
3. **Tests fonctionnels** : Vérifier les fonctionnalités
4. **Documentation** : Vérifier la génération des docs

## 📊 Métriques et Monitoring

### Statistiques d'Utilisation

- **Templates générés** : Nombre de projets créés
- **Taux de succès** : Pourcentage de générations réussies
- **Temps de génération** : Performance des templates
- **Erreurs communes** : Problèmes récurrents

### Monitoring en Temps Réel

```python
from athalia_core.monitoring import TemplateMonitor

monitor = TemplateMonitor()
stats = monitor.get_template_stats("api/main.py.j2")
print(f"Utilisations: {stats['usage_count']}")
print(f"Taux de succès: {stats['success_rate']}%")
```

## 🚨 Dépannage

### Problèmes Communs

#### 1. **Erreur de Syntaxe Jinja2**
```bash
# Vérification de la syntaxe
athalia validate template templates/api/main.py.j2
```

#### 2. **Variables Manquantes**
```bash
# Liste des variables requises
athalia template info templates/api/main.py.j2
```

#### 3. **Génération Échouée**
```bash
# Logs détaillés
athalia generate api --name test --verbose --debug
```

### Solutions

1. **Vérifier la syntaxe** : Python et Jinja2
2. **Variables obligatoires** : Toutes les variables requises
3. **Permissions** : Droits d'écriture dans le dossier de sortie
4. **Dépendances** : Modules Python requis installés

## 🔗 Liens Utiles

- **Documentation Athalia** : [docs/README.md](../docs/README.md)
- **Guide des Templates** : [docs/DEVELOPER/TEMPLATES/README.md](../docs/DEVELOPER/TEMPLATES/README.md)
- **Exemples d'Utilisation** : [docs/EXAMPLES/](../docs/EXAMPLES/)
- **Support** : [docs/SUPPORT/](../docs/SUPPORT/)

## 📝 Maintenance

### Mise à Jour des Templates

1. **Versioning** : Incrémenter la version dans les commentaires
2. **Tests** : Vérifier la compatibilité avec les projets existants
3. **Documentation** : Mettre à jour ce README
4. **Migration** : Fournir des scripts de migration si nécessaire

### Nettoyage

```bash
# Suppression des templates obsolètes
athalia cleanup templates --obsolete

# Archivage des anciennes versions
athalia archive templates --older-than 30d
```

---

**Dernière mise à jour :** 12 août 2025  
**Version :** 2.0.0  
**Maintenu par :** Équipe Athalia 