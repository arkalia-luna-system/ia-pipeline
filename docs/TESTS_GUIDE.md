# Guide des Tests Unitaires - Athalia Core

> **Note de mise à jour (19/07/2025) :**
> 
> - La couverture de tests est complète sur tous les modules critiques, y compris la correction avancée, la distillation, l’orchestration, etc.
> - Les tests couvrent tous les cas d’usage réels et edge cases connus.

## Vue d'ensemble

Ce document décrit les tests unitaires créés pour les modules `athalia_core` afin d'assurer la robustesse et la fiabilité du système CI/CD.

## Modules Testés

### ✅ auto_cicd.py
- **Couverture** : 84%
- **Tests** : 14 tests unitaires
- **Fonctionnalités testées** :
  - `AutoCICD` (constructeur, setup_cicd)
  - Détection de type de projet (Python, Node.js)
  - Détection des langages
  - Extraction des dépendances
  - Recherche des points d'entrée
  - Vérification de présence de tests/documentation
  - Génération de configurations (GitHub Actions, Docker, K8s)
  - Fonction `generate_github_ci_yaml`

### ✅ auto_cleaner.py
- **Couverture** : 70%
- **Tests** : 14 tests unitaires
- **Fonctionnalités testées** :
  - `AutoCleaner` (constructeur, clean_project)
  - Nettoyage des fichiers système (.DS_Store, Thumbs.db)
  - Nettoyage des fichiers de cache (__pycache__, *.pyc)
  - Nettoyage des fichiers de backup (*.bak, *~)
  - Nettoyage des fichiers temporaires (*.tmp)
  - Détection de fichiers dupliqués
  - Nettoyage des répertoires vides
  - Nettoyage des fichiers anciens/volumineux
  - Utilitaires (is_code_file, is_important_file, calculate_file_hash)
  - Optimisation de structure de projet

### ✅ auto_tester.py
- **Couverture** : 61%
- **Tests** : 7 tests unitaires
- **Fonctionnalités testées** :
  - `AutoTester` (constructeur, generate_tests)
  - Analyse de modules (.f files)
  - Génération de tests unitaires
  - Génération de tests d'intégration
  - Génération de tests de performance
  - Génération de rapports de tests

### ✅ auto_documenter.py
- **Couverture** : 86%
- **Tests** : 12 tests unitaires
- **Fonctionnalités testées** :
  - `AutoDocumenter` (constructeur, generate_documentation)
  - Analyse de projet
  - Génération de documentation HTML
  - Génération de documentation Markdown
  - Génération de documentation API
  - Génération de diagrammes
  - Utilitaires de documentation

### ✅ analytics.py
- **Couverture** : 86%
- **Tests** : 8 tests unitaires
- **Fonctionnalités testées** :
  - `audit_project_intelligent` (mock)
  - Génération de rapports HTML
  - Analyse de structure de projet
  - Utilitaires d'analyse

### ✅ ai_robust.py
- **Couverture** : 49%
- **Tests** : 10 tests unitaires
- **Fonctionnalités testées** :
  - `AIAuditor` (constructeur, audit_code)
  - `CodeAnalyzer` (analyse_syntax, analyse_complexity)
  - `SecurityChecker` (check_security)
  - `PerformanceAnalyzer` (analyze_performance)
  - Utilitaires d'analyse IA

### ✅ athalia_orchestrator.py
- **Couverture** : 35%
- **Tests** : 8 tests unitaires
- **Fonctionnalités testées** :
  - `AthaliaOrchestrator` (constructeur, orchestrate)
  - Gestion des workflows
  - Coordination des modules
  - Utilitaires d'orchestration

## Bonnes Pratiques Appliquées

### 1. Structure des Tests
```python
class TestModuleName(unittest.TestCase):
    def setUp(self):
        # Configuration initiale
        self.temp_dir = tempfile.mkdtemp()
        self.instance = ModuleClass()
    
    def tearDown(self):
        # Nettoyage
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_method_name(self):
        # Test spécifique
        pass
```

### 2. Gestion des Fichiers Temporaires
- Utilisation de `tempfile.mkdtemp()` pour les tests
- Nettoyage automatique dans `tearDown()`
- Création de fichiers de test réalistes

### 3. Mocks et Stubs
- Mock des fonctions externes (ex: `audit_project_intelligent`)
- Simulation de comportements complexes
- Isolation des unités testées

### 4. Assertions Robustes
- Vérification des types de retour
- Vérification de la présence de clés dans les dictionnaires
- Vérification de la structure des données

### 5. Gestion des Erreurs
- Tests des cas limites
- Vérification du comportement en cas d'erreur
- Tests de robustesse

## Exécution des Tests

### Tests Individuels
```bash
# Test d'un module spécifique
pytest tests/test_auto_cicd_unit.py --cov=athalia_core --cov-report=term

# Test avec couverture détaillée
pytest tests/test_auto_cleaner_unit.py --cov=athalia_core.auto_cleaner --cov-report=html
```

### Suite Complète
```bash
# Tous les tests unitaires
pytest tests/test_*_unit.py --cov=athalia_core --cov-report=term

# Avec rapport HTML
pytest tests/test_*_unit.py --cov=athalia_core --cov-report=html
```

## Métriques de Qualité

### Couverture Globale
- **Objectif** : > 80% pour les modules critiques
- **Actuel** : 5% (en progression grâce aux nouveaux tests)
- **Modules prioritaires** : auto_cicd, auto_cleaner, auto_tester, auto_documenter

### Critères de Validation
1. **Tous les tests passent** (100% de réussite)
2. **Couverture minimale** selon le module
3. **Tests de cas limites** inclus
4. **Documentation** à jour

## Prochaines Étapes

### Modules à Tester
- [ ] `advanced_analytics.py` (0% de couverture)
- [ ] `audit.py` (0% de couverture)
- [ ] `cli.py` (0% de couverture)
- [ ] `config_manager.py` (0% de couverture)
- [ ] `security_auditor.py` (0% de couverture)

### Améliorations
- [ ] Tests d'intégration entre modules
- [ ] Tests de performance
- [ ] Tests de sécurité
- [ ] Tests de régression

## Maintenance

### Ajout de Nouveaux Tests
1. Créer le fichier `tests/test_module_name_unit.py`
2. Suivre la structure standardisée
3. Inclure les cas de test critiques
4. Vérifier la couverture
5. Mettre à jour cette documentation

### Mise à Jour des Tests Existants
1. Identifier les changements dans l'API
2. Adapter les tests aux nouvelles signatures
3. Ajouter des tests pour les nouvelles fonctionnalités
4. Vérifier la régression

## Ressources

- [Documentation pytest](https://docs.pytest.org/)
- [Documentation coverage.py](https://coverage.readthedocs.io/)
- [Guide des bonnes pratiques de test](https://docs.pytest.org/en/stable/goodpractices.html) 