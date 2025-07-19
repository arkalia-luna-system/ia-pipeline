# Guide Utilisateur Athalia/Arkalia

## 🚀 Prise en main rapide

### Installation et lancement
```bash
# Installation
git clone https://github.com/arkalia-luna-system/athalia-dev-setup.git
cd athalia-dev-setup
pip install -r requirements.txt

# Lancement du pipeline principal
python athalia_core/main.py

# Lancement du dashboard
python athalia_core/dashboard.py

# CLI unifiée
python athalia_unified.py
```

### Alias utiles (après `source setup/alias.sh`)
```bash
ath-test      # Lancer les tests
ath-dashboard # Ouvrir le dashboard
ath-smart     # Prompt contextuel IA
ath-clean     # Nettoyer le projet
ath-audit     # Audit intelligent
ath-coverage  # Couverture de tests
```

## 💡 Exemples d'usage réels

### 1. Distillation IA Multi-Modèles

```python
from athalia_core.athalia_orchestrator import AthaliaOrchestrator

# Créer l'orchestrateur
orch = AthaliaOrchestrator()

# Distiller avec plusieurs modèles et stratégies
result = orch.distill_ia_responses(
    "Explique la distillation IA en 2 phrases.",
    models=["ollama_qwen", "ollama_mistral", "mock"],
    strategy="voting"  # voting, stacking, bagging, consensus, creative
)
print(result)

# Distillation adaptative (apprend de vos préférences)
adaptive_result = orch.distill_ia_responses(
    "Génère une fonction Python pour trier une liste",
    strategy="adaptive",
    user_feedback={"preferred_style": "functional", "complexity": "medium"}
)
print(adaptive_result)
```

### 2. Multimodalité avec LLaVA

```python
from athalia_core.distillation.multimodal_distiller import MultimodalDistiller

# Analyser une image avec du texte
distiller = MultimodalDistiller()

# Analyse d'architecture système
result = distiller.distill(
    ["Décris cette architecture système et propose des améliorations"],
    ["diagramme_architecture.png"]
)
print(result)

# Analyse de code avec screenshot
result = distiller.distill(
    ["Identifie les problèmes dans ce code et propose des corrections"],
    ["screenshot_code.png"]
)
print(result)
```

### 3. Code Genetics - Évolution de Solutions

```python
from athalia_core.distillation.code_genetics import CodeGenetics

# Créer des solutions initiales
genetics = CodeGenetics()
solutions = [
    "def hello(): return 'world'",
    "def greet(): print('hello')", 
    "message = 'hello world'",
    "class Greeter: def say_hello(self): return 'hello'"
]

# Définir un scoreur personnalisé
def code_quality_scorer(code):
    score = 0
    if 'def' in code: score += 2  # Fonction
    if 'class' in code: score += 3  # Classe
    if 'return' in code: score += 1  # Retour
    if len(code) > 30: score += 1  # Complexité
    return score

# Évoluer les solutions
evolved = genetics.evolve(
    solutions,
    scorer=code_quality_scorer,
    generations=5,
    population_size=10,
    mutation_rate=0.1
)
print("Meilleure solution évoluée:", evolved[0])
```

### 4. Orchestration AutoGen Multi-Agents

```python
from agents.agent_network import AuditAgent, CorrectionAgent, SynthesisAgent

# Créer le réseau d'agents
audit = AuditAgent()
correction = CorrectionAgent()
synth = SynthesisAgent()

# Workflow de correction automatique
prompt = """
def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
"""

# Audit du code
audit_result = audit.act(prompt)
print("Audit:", audit_result)

# Correction automatique
correction_result = correction.act(prompt)
print("Correction:", correction_result)

# Synthèse finale
final_result = synth.act(prompt, [audit_result, correction_result])
print("Synthèse:", final_result)
```

### 5. Predictive Caching

```python
from athalia_core.distillation.predictive_cache import PredictiveCache

# Créer le cache prédictif
cache = PredictiveCache()

# Analyser les patterns d'usage
cache.analyze_patterns([
    "génère une fonction Python",
    "crée une classe pour",
    "écris un test pour",
    "documente cette fonction"
])

# Obtenir des suggestions prédictives
suggestions = cache.get_predictions("génère une")
print("Suggestions prédictives:", suggestions)

# Cache avec TTL
cached_result = cache.get_or_compute(
    "prompt_complexe",
    compute_func=lambda: "résultat_calculé",
    ttl_seconds=3600
)
```

### 6. Benchmark Multi-Modèles

```python
# Lancer le benchmark Qwen/Mistral
python benchmark_qwen_mistral.py

# Ou utiliser le script de benchmark
python setup/benchmark_distillation.py

# Résultats disponibles dans :
# - benchmark_results.csv
# - benchmark_results.md
# - Dashboard web (onglet Benchmarks)
```

### 7. Dashboard et Analytics

```bash
# Lancer le dashboard
python athalia_core/dashboard.py

# Ouvrir dans le navigateur
open http://localhost:8080
```

**Onglets disponibles :**
- **Overview** : Vue d'ensemble du projet
- **Benchmarks** : Comparaison des modèles IA
- **Analytics** : Métriques de complexité et performance
- **Feedback** : Collecte et analyse des retours utilisateur

### 8. CLI Avancée

```bash
# Industrialisation complète d'un projet
python athalia_unified.py /chemin/projet --action complete

# Créer un profil utilisateur
python athalia_unified.py /chemin/projet --action profil --utilisateur "développeur_senior"

# Auto-correction avancée
python athalia_unified.py /chemin/projet --action correction --strategy "comprehensive"

# Audit de sécurité
python athalia_unified.py /chemin/projet --action security --level "strict"
```

## 🎯 Best Practices

### Performance
- **Benchmarks** : Toujours lancer les benchmarks sur une machine dédiée
- **Cache** : Utiliser le predictive caching pour les prompts répétitifs
- **Modèles** : Choisir le bon modèle selon la complexité (Qwen pour complexe, Mistral pour rapide)

### Qualité
- **Dashboard** : Monitorer les performances et collecter le feedback utilisateur
- **Tests** : Lancer `pytest` après chaque modification importante
- **Documentation** : Mettre à jour la documentation avec les nouvelles fonctionnalités

### Maintenance
- **Mise à jour** : Mettre à jour régulièrement les modèles et dépendances
- **Logs** : Sauvegarder les logs et les feedbacks pour l'amélioration continue
- **Backup** : Sauvegarder les configurations et profils utilisateur

## 🔧 FAQ Avancée

### Distillation IA
- **Comment ajouter un nouveau modèle IA ?**
  - Ajouter la fonction d'appel dans `athalia_core/ai_robust.py`
  - Mettre à jour la chaîne de fallback
  - Relancer le benchmark

- **Comment personnaliser la distillation ?**
  - Modifier la stratégie dans `ResponseDistiller`
  - Utiliser l'orchestrateur avec des paramètres personnalisés
  - Créer un nouveau distiller personnalisé

### Multimodalité
- **Comment intégrer LLaVA ?**
  - Installer Ollama et télécharger le modèle LLaVA
  - Utiliser `MultimodalDistiller` avec des images
  - Configurer les chemins dans `athalia_config.yaml`

### Code Genetics
- **Comment optimiser l'évolution ?**
  - Ajuster les paramètres (mutation_rate, population_size)
  - Créer des scoreurs personnalisés selon vos critères
  - Utiliser des populations initiales de qualité

### AutoGen
- **Comment créer un nouvel agent ?**
  - Hériter de la classe `BaseAgent`
  - Implémenter la méthode `act()`
  - L'enregistrer dans le réseau d'agents

### Plugins
- **Comment intégrer un plugin personnalisé ?**
  - Placer le fichier dans `athalia_core/plugins/`
  - L'enregistrer via le manager de plugins
  - Utiliser l'alias `ath-plugin-[nom]`

### Dashboard
- **Comment exporter les résultats ?**
  - Utiliser les fonctions d'export CSV/JSON intégrées
  - Accéder aux données via l'API du dashboard
  - Configurer l'export automatique

## 📊 Métriques et Monitoring

### Couverture de Tests
```bash
# Générer le rapport de couverture
pytest --cov=athalia_core --cov-report=html

# Ouvrir le rapport
open htmlcov/index.html
```

### Performance
- **Temps de réponse** : Monitorer via le dashboard
- **Mémoire** : Surveiller l'utilisation RAM des modèles
- **CPU** : Optimiser selon les ressources disponibles

### Qualité
- **Score de distillation** : Mesurer la qualité des fusions
- **Feedback utilisateur** : Collecter via le dashboard
- **Erreurs** : Analyser les logs d'erreur

---

*Guide utilisateur mis à jour le 2025-07-18* 