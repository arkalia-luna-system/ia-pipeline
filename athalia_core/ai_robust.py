"""
Module d'IA robuste avec prompts dynamiques et fallback intelligent.
"""

import os
import subprocess
import logging
import yaml
import time
from typing import Dict, Any, Optional, List
from enum import Enum

class AIModel(Enum):
    """Modèles IA disponibles."""
    OLLAMA_MISTRAL = "ollama_mistral"
    OLLAMA_LLAMA = "ollama_llama"
    OLLAMA_CODEGEN = "ollama_codegen"
    MOCK = "mock"

class PromptContext(Enum):
    """Contextes de prompts."""
    BLUEPRINT = "blueprint"
    CODE_REVIEW = "code_review"
    DOCUMENTATION = "documentation"
    TESTING = "testing"
    SECURITY = "security"

class RobustAI:
    """IA robuste avec prompts dynamiques et fallback intelligent."""
    
    def __init__(self):
        self.available_models = self._detect_available_models()
        self.fallback_chain = self._build_fallback_chain()
        self.prompt_templates = self._load_prompt_templates()
    
    def _detect_available_models(self) -> List[AIModel]:
        """Détecte les modèles IA disponibles."""
        available = []
        
        # Vérifier Ollama
        try:
            result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                output = result.stdout.lower()
                if 'mistral' in output:
                    available.append(AIModel.OLLAMA_MISTRAL)
                if 'llama' in output:
                    available.append(AIModel.OLLAMA_LLAMA)
                if 'codegen' in output:
                    available.append(AIModel.OLLAMA_CODEGEN)
        except Exception as e:
            logging.warning(f"Ollama non détecté: {e}")
        
        # Mock toujours disponible
        available.append(AIModel.MOCK)
        
        logging.info(f"Modèles IA disponibles: {[m.value for m in available]}")
        return available
    
    def _build_fallback_chain(self) -> List[AIModel]:
        """Construit la chaîne de fallback."""
        chain = []
        
        # Priorité: Mistral > Llama > Codegen > Mock
        priority_models = [
            AIModel.OLLAMA_MISTRAL,
            AIModel.OLLAMA_LLAMA,
            AIModel.OLLAMA_CODEGEN,
            AIModel.MOCK
        ]
        
        for model in priority_models:
            if model in self.available_models:
                chain.append(model)
        
        return chain
    
    def _load_prompt_templates(self) -> Dict[str, str]:
        """Charge les templates de prompts dynamiques."""
        return {
            PromptContext.BLUEPRINT.value: """
Tu es un architecte logiciel expert spécialisé dans la création de projets IA.

CONTEXTE DU PROJET:
- Description: {idea}
- Type détecté: {project_type}
- Complexité estimée: {complexity}

TÂCHE:
Génère un blueprint YAML complet et fonctionnel pour ce projet.

REQUIS:
- project_name: nom unique et descriptif
- description: description détaillée
- modules: liste des modules fonctionnels
- structure: architecture des dossiers/fichiers
- dependencies: dépendances Python appropriées
- prompts: prompts spécialisés pour le type de projet
- booster_ia: true/false selon la complexité
- docker: true/false selon les besoins

FORMAT:
```yaml
project_name: nom_du_projet
description: description détaillée
project_type: {project_type}
modules: [module1, module2, ...]
structure: [dossier1/, fichier1.py, ...]
dependencies: [dep1, dep2, ...]
prompts: [prompt1.yaml, prompt2.md]
booster_ia: true
docker: false
api_spec:
  endpoint1:
    params: {{"param1": "string"}}
    response: {{"result": "string"}}
    description: "description de l'endpoint"
```
""",
            
            PromptContext.CODE_REVIEW.value: """
Tu es un expert en revue de code Python.

CODE À ANALYSER:
{code}

CONTEXTE:
- Fichier: {filename}
- Type de projet: {project_type}
- Score actuel: {current_score}/100

TÂCHE:
Analyse ce code et propose des améliorations spécifiques.

POINTS À ÉVALUER:
1. Qualité du code (lisibilité, structure)
2. Bonnes pratiques Python
3. Gestion d'erreurs
4. Performance
5. Sécurité
6. Tests

FORMAT DE RÉPONSE:
```yaml
score: 75
issues:
  - "Problème 1: description"
  - "Problème 2: description"
suggestions:
  - "Suggestion 1: action concrète"
  - "Suggestion 2: action concrète"
improvements:
  - "Amélioration 1: code corrigé"
  - "Amélioration 2: code corrigé"
```
""",
            
            PromptContext.DOCUMENTATION.value: """
Tu es un expert en documentation technique.

CONTEXTE:
- Projet: {project_name}
- Type: {project_type}
- Modules: {modules}

TÂCHE:
Génère une documentation technique complète et professionnelle.

SECTIONS REQUISES:
1. Vue d'ensemble du projet
2. Architecture et modules
3. Installation et configuration
4. Utilisation et exemples
5. API Reference
6. Développement et contribution
7. Troubleshooting

STYLE:
- Professionnel et technique
- Exemples concrets
- Structure claire avec sections
- Code snippets appropriés
""",
            
            PromptContext.TESTING.value: """
Tu es un expert en tests logiciels.

CONTEXTE:
- Module: {module_name}
- Fonctionnalités: {features}
- Type de projet: {project_type}

TÂCHE:
Génère des tests unitaires et d'intégration complets.

REQUIS:
1. Tests unitaires pour chaque fonction
2. Tests d'intégration pour les workflows
3. Tests de cas limites et d'erreurs
4. Mocks appropriés
5. Assertions pertinentes

FORMAT:
```python
import pytest
from unittest.mock import Mock, patch

def test_function_name():
    # Arrange
    # Act
    # Assert
    pass
```
""",
            
            PromptContext.SECURITY.value: """
Tu es un expert en sécurité informatique.

CONTEXTE:
- Code: {code}
- Type d'application: {app_type}
- Environnement: {environment}

TÂCHE:
Analyse les vulnérabilités de sécurité potentielles.

POINTS À VÉRIFIER:
1. Injection (SQL, commande, etc.)
2. Authentification et autorisation
3. Gestion des secrets
4. Validation des entrées
5. Chiffrement des données
6. Logs et audit

FORMAT:
```yaml
vulnerabilities:
  - severity: "HIGH"
    type: "SQL Injection"
    description: "Description du problème"
    location: "ligne X"
    fix: "Solution proposée"
recommendations:
  - "Recommandation 1"
  - "Recommandation 2"
```
"""
        }
    
    def _get_dynamic_prompt(self, context: PromptContext, **kwargs) -> str:
        """Génère un prompt dynamique selon le contexte."""
        template = self.prompt_templates.get(context.value, "")
        return template.format(**kwargs)
    
    def _classify_project_complexity(self, idea: str) -> str:
        """Classifie la complexité du projet."""
        complexity_keywords = {
            'simple': ['simple', 'basic', 'test', 'demo', 'hello'],
            'medium': ['api', 'web', 'data', 'analysis', 'tool'],
            'complex': ['ai', 'ml', 'neural', 'distributed', 'microservice', 'real-time']
        }
        
        idea_lower = idea.lower()
        for complexity, keywords in complexity_keywords.items():
            if any(keyword in idea_lower for keyword in keywords):
                return complexity
        
        return 'medium'
    
    def _call_ollama(self, model: AIModel, prompt: str, timeout: int = 60) -> Optional[str]:
        """Appelle Ollama avec gestion d'erreurs robuste."""
        try:
            model_name = model.value.replace('ollama_', '')
            result = subprocess.run([
                'ollama', 'run', model_name, prompt
            ], capture_output=True, text=True, timeout=timeout)
            
            if result.returncode == 0:
                content = result.stdout.strip()
                # Nettoyer et extraire le YAML si présent
                if '```yaml' in content:
                    start = content.find('```yaml') + 7
                    end = content.find('```', start)
                    if end != -1:
                        content = content[start:end].strip()
                elif '---' in content:
                    yaml_start = content.find('---')
                    yaml_end = content.find('---', yaml_start + 3)
                    if yaml_end != -1:
                        content = content[yaml_start:yaml_end + 3]
                
                return content
            else:
                logging.warning(f"Ollama {model_name} échoué: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            logging.warning(f"Ollama {model.value} timeout après {timeout}s")
            return None
        except Exception as e:
            logging.warning(f"Erreur Ollama {model.value}: {e}")
            return None
    
    def generate_blueprint(self, idea: str, context: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """Génère un blueprint avec fallback intelligent."""
        context = context or {}
        
        # Analyse du contexte
        project_type = context.get('project_type', 'generic')
        complexity = self._classify_project_complexity(idea)
        
        # Prompt dynamique
        prompt = self._get_dynamic_prompt(
            PromptContext.BLUEPRINT,
            idea=idea,
            project_type=project_type,
            complexity=complexity
        )
        
        # Essayer chaque modèle dans la chaîne de fallback
        for model in self.fallback_chain:
            logging.info(f"Tentative avec {model.value}")
            
            if model == AIModel.MOCK:
                # Utiliser le mock amélioré
                from .generation import generate_blueprint_mock
                return generate_blueprint_mock(idea)
            
            # Appeler Ollama
            content = self._call_ollama(model, prompt)
            if content:
                try:
                    blueprint = yaml.safe_load(content)
                    if blueprint and isinstance(blueprint, dict):
                        logging.info(f"Blueprint généré avec {model.value}")
                        return blueprint
                except yaml.YAMLError as e:
                    logging.warning(f"YAML invalide de {model.value}: {e}")
                    continue
        
        # Fallback final vers mock
        logging.warning("Tous les modèles IA ont échoué, utilisation du mock")
        from .generation import generate_blueprint_mock
        return generate_blueprint_mock(idea)
    
    def review_code(self, code: str, filename: str, project_type: str, current_score: int) -> Dict[str, Any]:
        """Revue de code avec IA."""
        prompt = self._get_dynamic_prompt(
            PromptContext.CODE_REVIEW,
            code=code,
            filename=filename,
            project_type=project_type,
            current_score=current_score
        )
        
        for model in self.fallback_chain:
            if model == AIModel.MOCK:
                return {
                    'score': current_score,
                    'issues': ['Analyse automatique non disponible'],
                    'suggestions': ['Utiliser un outil de linting comme flake8'],
                    'improvements': []
                }
            
            content = self._call_ollama(model, prompt)
            if content:
                try:
                    review = yaml.safe_load(content)
                    if review and isinstance(review, dict):
                        return review
                except yaml.YAMLError:
                    continue
        
        return {'error': 'Impossible de générer une revue de code'}
    
    def generate_documentation(self, project_name: str, project_type: str, modules: List[str]) -> str:
        """Génère de la documentation avec IA."""
        prompt = self._get_dynamic_prompt(
            PromptContext.DOCUMENTATION,
            project_name=project_name,
            project_type=project_type,
            modules=', '.join(modules)
        )
        
        for model in self.fallback_chain:
            if model == AIModel.MOCK:
                modules_list = '\n- '.join(modules)
                return f"""# Documentation pour {project_name}

## Documentation technique du projet {project_name}

Ce projet de type {project_type} comprend les modules suivants : {', '.join(modules)}.

## Installation
```bash
pip install -r requirements.txt
```

## Utilisation
Documentation générée automatiquement pour {project_name}.

## Modules
- {modules_list}

## Développement
Pour contribuer au projet, consultez les guides de développement.
"""
            
            content = self._call_ollama(model, prompt)
            if content:
                return content
        
        return f"# Documentation pour {project_name}\n\nDocumentation générée automatiquement."

# Instance globale
robust_ai = RobustAI() 