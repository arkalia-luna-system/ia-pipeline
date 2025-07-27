# 🤖 Documentation des Prompts IA - Athalia

**Date :** 20/07/2025  
**Version :** 1.0  
**Auteur :** Athalia Dev Setup

---

## 📋 **Vue d'ensemble**

Les prompts IA d'Athalia sont des instructions spécialisées pour guider les modèles d'intelligence artificielle dans la génération de code, l'analyse et l'amélioration de projets. Ils sont utilisés par le système d'IA robuste pour fournir des réponses contextuelles et pertinentes.

---

## 🏗️ **Architecture des Prompts**

### **Structure des Dossiers**

```
prompts/
├── code_refactor.yaml          # Refactorisation de code
├── custom_prompts.yaml         # Prompts personnalisés
├── design_review.md            # Review de design
├── dev_debug.yaml             # Débogage développement
├── security_audit.md          # Audit de sécurité
├── test_strategy.md           # Stratégie de tests
└── ux_fun_boost.md            # Amélioration UX
```

### **Types de Prompts**

1. **Prompts de Génération** - Création de code et documentation
2. **Prompts d'Analyse** - Audit et review de code
3. **Prompts d'Amélioration** - Refactorisation et optimisation
4. **Prompts de Sécurité** - Audit de sécurité et vulnérabilités
5. **Prompts de Tests** - Stratégies et génération de tests

---

## 🔧 **Utilisation des Prompts**

### **Utilisation via CLI**

```bash
# Test de l'IA avec prompts
python -m athalia_core.cli test-ai "Mon idée de projet"

# Statut de l'IA robuste
python -m athalia_core.cli ai-status
```

### **Utilisation Programmatique**

```python
from athalia_core.ai_robust import RobustAI, PromptContext

# Initialiser l'IA robuste
ai = RobustAI()

# Utiliser un prompt spécifique
response = ai.generate_response(
    context=PromptContext.BLUEPRINT,
    idea="API REST pour gestion de tâches",
    project_type="web_api",
    complexity="medium"
)

print(response)
```

---

## 📝 **Contextes de Prompts Disponibles**

### **1. BLUEPRINT - Génération de Blueprints**

**Objectif :** Générer des blueprints YAML complets pour les projets.

**Variables disponibles :**
- `idea` - Description du projet
- `project_type` - Type de projet détecté
- `complexity` - Complexité estimée

**Exemple d'utilisation :**
```python
response = ai.generate_response(
    context=PromptContext.BLUEPRINT,
    idea="Application de gestion de tâches avec API REST",
    project_type="web_api",
    complexity="medium"
)
```

### **2. CODE_REVIEW - Analyse de Code**

**Objectif :** Analyser et améliorer le code existant.

**Variables disponibles :**
- `code` - Code à analyser
- `filename` - Nom du fichier
- `project_type` - Type de projet
- `current_score` - Score actuel

**Exemple d'utilisation :**
```python
response = ai.generate_response(
    context=PromptContext.CODE_REVIEW,
    code=code_content,
    filename="main.py",
    project_type="web_api",
    current_score=75
)
```

### **3. DOCUMENTATION - Génération de Documentation**

**Objectif :** Générer de la documentation technique.

**Variables disponibles :**
- `code` - Code à documenter
- `project_type` - Type de projet
- `doc_type` - Type de documentation

**Exemple d'utilisation :**
```python
response = ai.generate_response(
    context=PromptContext.DOCUMENTATION,
    code=code_content,
    project_type="web_api",
    doc_type="api_docs"
)
```

### **4. TESTING - Génération de Tests**

**Objectif :** Créer des tests unitaires et d'intégration.

**Variables disponibles :**
- `code` - Code à tester
- `project_type` - Type de projet
- `test_framework` - Framework de test

**Exemple d'utilisation :**
```python
response = ai.generate_response(
    context=PromptContext.TESTING,
    code=code_content,
    project_type="web_api",
    test_framework="pytest"
)
```

### **5. SECURITY - Audit de Sécurité**

**Objectif :** Analyser la sécurité du code.

**Variables disponibles :**
- `code` - Code à analyser
- `project_type` - Type de projet
- `environment` - Environnement de déploiement

**Exemple d'utilisation :**
```python
response = ai.generate_response(
    context=PromptContext.SECURITY,
    code=code_content,
    project_type="web_api",
    environment="production"
)
```

---

## 🎯 **Prompts Spécialisés**

### **1. Code Refactor (`code_refactor.yaml`)**

**Objectif :** Améliorer la qualité et la structure du code.

**Caractéristiques :**
- Analyse de la complexité cyclomatique
- Suggestions de refactorisation
- Amélioration de la lisibilité
- Optimisation des performances

**Utilisation :**
```yaml
# Dans le fichier prompts/code_refactor.yaml
context: "Tu es un expert en refactorisation de code Python"
task: "Analyse et améliore le code fourni"
output_format: "yaml"
```

### **2. Design Review (`design_review.md`)**

**Objectif :** Évaluer et améliorer le design des interfaces.

**Caractéristiques :**
- Analyse UX/UI
- Suggestions d'amélioration
- Bonnes pratiques de design
- Accessibilité

### **3. Security Audit (`security_audit.md`)**

**Objectif :** Identifier et corriger les vulnérabilités de sécurité.

**Caractéristiques :**
- Détection d'injections
- Analyse des permissions
- Gestion des secrets
- Validation des entrées

### **4. Test Strategy (`test_strategy.md`)**

**Objectif :** Définir une stratégie de tests complète.

**Caractéristiques :**
- Planification des tests
- Couverture de code
- Tests d'intégration
- Tests de performance

### **5. UX Fun Boost (`ux_fun_boost.md`)**

**Objectif :** Améliorer l'expérience utilisateur et l'engagement.

**Caractéristiques :**
- Gamification
- Animations et transitions
- Feedback utilisateur
- Interface intuitive

---

## 🛠️ **Personnalisation des Prompts**

### **Créer un Nouveau Prompt**

1. **Créer le fichier prompt :**
```bash
# Créer un nouveau prompt
touch prompts/my_custom_prompt.yaml
```

2. **Définir la structure :**
```yaml
# prompts/my_custom_prompt.yaml
context: "Tu es un expert en [domaine]"
task: "Tâche spécifique à accomplir"
input_variables:
  - variable1
  - variable2
output_format: "yaml|json|text"
examples:
  - input: "exemple d'entrée"
    output: "exemple de sortie"
```

3. **Enregistrer dans le système :**
```python
# Ajouter à athalia_core/ai_robust.py
class PromptContext(Enum):
    # ... autres contextes ...
    CUSTOM = "custom"

# Dans _load_prompt_templates()
PromptContext.CUSTOM.value: """
[Contenu du prompt personnalisé]
"""
```

### **Modifier un Prompt Existant**

1. **Localiser le prompt :**
```bash
# Voir tous les prompts
ls prompts/

# Éditer un prompt
nano prompts/code_refactor.yaml
```

2. **Tester les modifications :**
```python
# Test du prompt modifié
ai = RobustAI()
response = ai.generate_response(
    context=PromptContext.CODE_REVIEW,
    code="def test(): pass",
    filename="test.py"
)
print(response)
```

---

## 🧪 **Tests des Prompts**

### **Tests Automatiques**

```bash
# Exécuter les tests de prompts
python -m pytest tests/test_prompts_documentation.py -v

# Tests spécifiques
python -m pytest tests/test_prompts_documentation.py::TestPrompts::test_code_refactor_prompt -v
```

### **Tests Manuels**

```python
# Test de génération de réponse
from athalia_core.ai_robust import RobustAI, PromptContext

ai = RobustAI()

# Test avec différents contextes
contexts = [
    PromptContext.BLUEPRINT,
    PromptContext.CODE_REVIEW,
    PromptContext.DOCUMENTATION,
    PromptContext.TESTING,
    PromptContext.SECURITY
]

for context in contexts:
    try:
        response = ai.generate_response(
            context=context,
            idea="Test project",
            project_type="test"
        )
        print(f"✅ {context.value}: OK")
    except Exception as e:
        print(f"❌ {context.value}: {e}")
```

---

## 📊 **Métriques et Performance**

### **Métriques de Qualité**

- **Pertinence** - Réponses adaptées au contexte
- **Cohérence** - Réponses cohérentes entre les exécutions
- **Complétude** - Réponses complètes et détaillées
- **Précision** - Réponses exactes et correctes

### **Optimisation des Prompts**

1. **Clarté des instructions** - Instructions précises et non ambiguës
2. **Exemples concrets** - Exemples pour guider le modèle
3. **Format de sortie** - Format structuré pour faciliter le parsing
4. **Gestion d'erreurs** - Instructions pour les cas d'erreur

---

## 📚 **Documentation Associée**

- **[REFERENCE.md](REFERENCE.md)** - Référence technique des prompts
- **[BEST_PRACTICES.md](GUIDES/BEST_PRACTICES.md)** - Bonnes pratiques
- **[EXAMPLES/](EXAMPLES/)** - Exemples par catégorie

---

## 🚨 **Dépannage**

### **Problèmes Courants**

1. **Prompt non trouvé :**
   - Vérifier le nom du contexte dans `PromptContext`
   - S'assurer que le prompt est chargé dans `_load_prompt_templates()`

2. **Variable manquante :**
   - Vérifier toutes les variables requises dans le prompt
   - Utiliser des valeurs par défaut si possible

3. **Réponse incohérente :**
   - Améliorer la clarté des instructions
   - Ajouter des exemples concrets
   - Spécifier le format de sortie attendu

### **Logs de Debug**

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Les logs afficheront les détails de génération
ai = RobustAI()
response = ai.generate_response(...)
```

---

## 🔄 **Mise à Jour**

Pour mettre à jour cette documentation :

1. **Modifier le fichier README.md**
2. **Tester les exemples**
3. **Mettre à jour les tests**
4. **Valider avec `python -m pytest tests/test_prompts_documentation.py`**

---

**📞 Support :** Consultez la documentation complète dans `docs/prompts/` ou créez une issue pour toute question. 