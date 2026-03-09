# Guide Développeur Athalia/Arkalia

**Dernière mise à jour :** 20 Août 2025  
**Version :** v12.0.0  
**Statut :** ✅ ACTIF ET MAINTENU

## 🏗️ Architecture du Projet

### Structure Modulaire
```
athalia_core/
├── ai_robust.py                    # IA robuste multi-modèles
├── unified_orchestrator.py         # Orchestrateur principal
├── distillation/                   # Modules de distillation
│   ├── __init__.py
│   ├── response_distiller.py       # Fusion multi-IA
│   ├── adaptive_distillation.py    # Apprentissage préférences
│   ├── code_genetics.py           # Évolution de solutions
│   ├── predictive_cache.py        # Cache prédictif
│   └── multimodal_distiller.py    # Fusion texte+image
├── auto_*                         # Modules automatiques
│   ├── auto_tester.py             # Génération tests
│   ├── auto_documenter.py         # Documentation auto
│   ├── auto_cleaner.py            # Nettoyage auto
│   ├── auto_cicd.py               # CI/CD auto
│   └── security_auditor.py        # Audit sécurité
├── dashboard.py                   # Dashboard web
├── cli.py                         # Interface CLI
└── plugins/                       # Système de plugins
    ├── __init__.py
    ├── plugins_manager.py
    └── plugins_validator.py
```

### Modules Principaux

#### 1. IA Robuste (`ai_robust.py`)
```python
from athalia_core.ai.ai_robust_enhanced import RobustAI, PromptContext

# Créer l'instance IA robuste
ai = RobustAI()

# Exemple : génération de blueprint (tâche simple → Groq priorisé si dispo)
result = ai.generate_response(
    context=PromptContext.BLUEPRINT,
    description="Application FastAPI pour gérer des utilisateurs",
    project_name="user-api",
    project_type="api",
)
print(result["response"])

# Exemple : revue de code (tâche complexe → Gemini Flash priorisé si dispo)
code = open("mon_module.py").read()
review = ai.generate_response(
    context=PromptContext.CODE_REVIEW,
    code=code,
    project_type="api",
)
print(review["response"])
```

#### 2. Orchestrateur Principal (`unified_orchestrator.py`)
```python
from athalia_core.unified_orchestrator import UnifiedOrchestrator

# Créer l'orchestrateur
orch = UnifiedOrchestrator()

# Distillation multi-IA
result = orch.distill_ia_responses(
    "Prompt complexe",
    models=["ollama_qwen", "ollama_mistral"],
    strategy="voting"
)

# Industrialisation de projet
orch.industrialize_project("/chemin/projet", config={})

# Audit automatique
orch.audit_project("/chemin/projet")
```

#### 3. Distillation Avancée
```python
# Distillation adaptative
from athalia_core.distillation.adaptive_distillation import AdaptiveDistiller

distiller = AdaptiveDistiller()
result = distiller.distill(
    "Prompt",
    user_feedback={"style": "functional", "complexity": "high"}
)

# Génétique de Code
from athalia_core.distillation.code_genetics import CodeGenetics

genetics = CodeGenetics()
evolved = genetics.evolve(
    solutions=["code1", "code2", "code3"],
    scorer=lambda x: len(x),
    generations=5
)

# Cache Prédictif
from athalia_core.distillation.predictive_cache import PredictiveCache

cache = PredictiveCache()
cached = cache.get_or_compute("key", compute_func, ttl=3600)
```

## 🧪 Tests et Qualité

### Lancer les Tests
```bash
# Tous les tests (1696 tests) ✅ VÉRIFIÉ
pytest

# Avec couverture
pytest --cov=athalia_core --cov-report=html

# Tests spécifiques
pytest tests/test_ai_robust.py -v
pytest tests/test_distillation.py -v
pytest tests/test_orchestrator.py -v

# Tests d'intégration
pytest tests/integration/ -v

# Tests de performance
pytest tests/test_performance_*.py -v
```

### Exemple de Test d'Intégration
```python
import pytest
from athalia_core.unified_orchestrator import UnifiedOrchestrator

class TestOrchestratorIntegration:
    def setup_method(self):
        self.orch = AthaliaOrchestrator()

    def test_distillation_integration(self):
        """Test d'intégration de la distillation"""
        result = self.orch.distill_ia_responses(
            "Test prompt",
            models=["mock"],  # Utiliser mock pour les tests
            strategy="voting"
        )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_adaptive_distillation(self):
        """Test de la distillation adaptative"""
        result = self.orch.distill_ia_responses(
            "Test prompt",
            strategy="adaptive",
            user_feedback={"style": "simple"}
        )
        assert isinstance(result, str)
```

### Couverture de Code
```bash
# Générer le rapport de couverture
pytest --cov=athalia_core --cov-report=html --cov-report=term

# Objectif : >90% de couverture
# Actuel : >75% de couverture

# Ouvrir le rapport HTML
open htmlcov/index.html
```

## 🔧 Développement de Modules

### Créer un Nouveau Module de Distillation
```python
# athalia_core/distillation/custom_distiller.py
from abc import ABC, abstractmethod

class CustomDistiller(ABC):
    """Distiller personnalisé"""

    @abstractmethod
    def distill(self, prompt: str, **kwargs) -> str:
        """Méthode principale de distillation"""
        pass

    def validate_input(self, prompt: str) -> bool:
        """Validation des entrées"""
        return isinstance(prompt, str) and len(prompt) > 0

# Implémentation
class MyCustomDistiller(CustomDistiller):
    def distill(self, prompt: str, **kwargs) -> str:
        if not self.validate_input(prompt):
            raise ValueError("Prompt invalide")

        # Logique de distillation personnalisée
        return f"Résultat personnalisé: {prompt}"
```

### Créer un Nouveau Module Auto
```python
# athalia_core/auto_custom.py
from athalia_core.auto_base import AutoBase

class AutoCustom(AutoBase):
    """Module automatique personnalisé"""

    def __init__(self):
        super().__init__()
        self.name = "AutoCustom"

    def process_project(self, project_path: str, config: dict = None) -> dict:
        """Traiter un projet"""
        result = {
            "status": "success",
            "files_processed": 0,
            "custom_metric": 0
        }

        # Logique personnalisée
        # ...

        return result

    def validate_config(self, config: dict) -> bool:
        """Valider la configuration"""
        return True
```

### Créer un Plugin
```python
# athalia_core/plugins/custom_plugin.py
from athalia_core.plugins.base_plugin import BasePlugin

class CustomPlugin(BasePlugin):
    """Plugin personnalisé"""

    def __init__(self):
        super().__init__()
        self.name = "CustomPlugin"
        self.version = "11.0.0"
        self.description = "Plugin personnalisé pour Athalia"

    def execute(self, context: dict) -> dict:
        """Exécuter le plugin"""
        # Logique du plugin
        return {"status": "success", "data": "custom_data"}

    def validate(self, context: dict) -> bool:
        """Valider le contexte"""
        return True
```

## 📊 Métriques et Monitoring

### Métriques de Performance
```python
import time
import psutil
from athalia_core.analytics import PerformanceMonitor

# Monitorer les performances
monitor = PerformanceMonitor()

# Mesurer le temps d'exécution
with monitor.timer("distillation"):
    result = orch.distill_ia_responses("Prompt")

# Mesurer l'utilisation mémoire
memory_usage = monitor.get_memory_usage()
cpu_usage = monitor.get_cpu_usage()

print(f"Mémoire: {memory_usage}MB, CPU: {cpu_usage}%")
```

### Logs et Debugging
```python
import logging
from athalia_core.logging_config import setup_logging

# Configuration des logs
setup_logging(level=logging.DEBUG)

# Utiliser les logs
logger = logging.getLogger(__name__)
logger.info("Début de distillation")
logger.debug(f"Prompt: {prompt}")
logger.error("Erreur de distillation", exc_info=True)
```

## 🚀 Déploiement et CI/CD

### Configuration CI/CD
```yaml
# .github/workflows/ci.yml
name: CI/CD Athalia

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest --cov=athalia_core --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### Docker
```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python", "athalia_core/utilities/dashboard.py"]
```

## 📚 Documentation

### Standards de Documentation
- **Docstrings** : Utiliser le format Google/NumPy
- **Type Hints** : Toujours inclure les types
- **Exemples** : Fournir des exemples d'usage
- **Tests** : Documenter les cas de test

### Exemple de Documentation
```python
def distill_ia_responses(
    self,
    prompt: str,
    models: List[str] = None,
    strategy: str = "voting"
) -> str:
    """
    Distille les réponses de plusieurs modèles IA.

    Args:
        prompt: Le prompt à traiter
        models: Liste des modèles à utiliser (défaut: tous disponibles)
        strategy: Stratégie de distillation ('voting', 'stacking', etc.)

    Returns:
        str: Réponse distillée

    Raises:
        ValueError: Si le prompt est vide
        ModelNotFoundError: Si aucun modèle n'est disponible

    Example:
        >>> orch = AthaliaOrchestrator()
        >>> result = orch.distill_ia_responses("Hello", strategy="voting")
        >>> print(result)
        "Hello, how can I help you?"
    """
    # Implémentation...
```

## 🔍 Debugging et Troubleshooting

### Debugging des Modules
```python
# Activer le mode debug
import logging
logging.basicConfig(level=logging.DEBUG)

# Utiliser pdb pour le debugging
import pdb; pdb.set_trace()

# Utiliser le debugger intégré
from athalia_core.debug import Debugger
debugger = Debugger()
debugger.breakpoint()
```

### Problèmes Courants
1. **Modèles non trouvés** : Vérifier l'installation d'Ollama
2. **Erreurs de mémoire** : Réduire la taille des modèles
3. **Timeouts** : Augmenter les timeouts dans la config
4. **Tests qui échouent** : Vérifier les mocks et les dépendances

## 🤝 Contribution

### Workflow de Contribution
1. **Fork** le projet
2. **Créer** une branche feature
3. **Développer** avec tests
4. **Documenter** les changements
5. **Tester** localement
6. **Soumettre** une PR

### Standards de Code
- **PEP 8** : Style de code Python
- **Black** : Formatage automatique
- **Flake8** : Linting
- **MyPy** : Vérification de types

### Tests Obligatoires
- **Tests unitaires** : Pour chaque fonction
- **Tests d'intégration** : Pour les modules
- **Tests de performance** : Pour les optimisations
- **Tests de régression** : Pour les bugs fixes

---

*Guide développeur mis à jour le 2025-08-20*
