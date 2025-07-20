# API Documentation - 

## Vue d'ensemble

Cette documentation décrit l'API de .

## Modules

### module2

#### Fonctions

##### test2

---

### test_ci_configuration

Tests pour la configuration CI/CD
Version: 1.0
Auteur: Athalia Team

#### Classes

##### TestCIConfiguration

Tests pour la configuration CI/CD

Cette classe teste les aspects suivants :
- Import du module CI
- Existence de la configuration
- Environnement CI
- Dépendances CI
- Configuration des timeouts

**Méthodes :**

- `setUp()`
- `test_ci_module_import()`
- `test_ci_config_exists()`
- `test_ci_environment()`
- `test_ci_dependencies()`
- `test_ci_timeout_config()`
- `test_ci_generation_mock()`

#### Fonctions

##### test_ci_environment_variables

Test des variables d'environnement CI

Scénario : Vérification des variables d'environnement CI
Données : Variables d'environnement système
Résultat attendu : Les variables CI doivent être définies ou absentes

##### setUp

Initialisation avant chaque test

##### test_ci_module_import

Test que le module CI peut être importé

Scénario : Import du module athalia_core.ci
Données : Module CIConfig
Résultat attendu : Le module doit être importable

##### test_ci_config_exists

Test que la configuration CI existe

Scénario : Vérification de l'existence du fichier de config
Données : Chemin vers config/athalia_config.yaml
Résultat attendu : Le fichier de configuration doit exister

##### test_ci_environment

Test que l'environnement CI est détecté

Scénario : Détection de l'environnement CI
Données : Variables d'environnement CI et GITHUB_ACTIONS
Résultat attendu : L'environnement CI doit être détecté

##### test_ci_dependencies

Test que toutes les dépendances CI sont installées

Scénario : Vérification des dépendances CI
Données : Liste des packages CI requis
Résultat attendu : Tous les packages doivent être installés

##### test_ci_timeout_config

Test que pytest-timeout est configuré

Scénario : Vérification de la configuration pytest-timeout
Données : Module pytest_timeout
Résultat attendu : Le module doit avoir la fonctionnalité timeout

##### test_ci_generation_mock

Test de génération de configuration CI (mock)

Scénario : Création d'une instance CIConfig
Données : Classe CIConfig
Résultat attendu : L'instance doit être créée avec succès

---

### correction_chaînes

Script de correction des chaînes non terminées dans athalia_core

#### Fonctions

##### corriger_chaînes_fichier

Corrige les chaînes non terminées dans un fichier

**Paramètres :**

- `file_path`

##### main

Fonction principale

---

### correction_finale

Script de correction finale pour Athalia
Corrige toutes les erreurs restantes dans les fichiers principaux

#### Fonctions

##### corriger_fichier

Corrige un fichier en remplaçant les patterns problématiques

**Paramètres :**

- `file_path`

##### main

Fonction principale

---

### optimize_performance

Script d'optimisation des performances des tests
Version: 1.0
Auteur: Athalia Team

#### Classes

##### TestPerformanceOptimizer

Optimiseur de performances des tests

**Méthodes :**

- `__init__()`
- `analyze_test_performance()`
- `_parse_durations()`
- `_extract_duration()`
- `identify_slow_tests()`
- `identify_fast_tests()`
- `generate_optimization_report()`
- `save_report()`
- `run_fast_tests_only()`

#### Fonctions

##### main

Fonction principale

##### __init__

**Paramètres :**

- `test_dir`

##### analyze_test_performance

Analyse les performances de tous les tests

Returns:
    Dict avec les temps d'exécution par test

##### _parse_durations

Parse la sortie de pytest --durations

**Paramètres :**

- `output`

##### _extract_duration

Extrait la durée d'une ligne de test

**Paramètres :**

- `line`

##### identify_slow_tests

Identifie les tests lents

Args:
    threshold: Seuil en secondes pour considérer un test comme lent
    
Returns:
    Liste des tests lents

**Paramètres :**

- `threshold`

##### identify_fast_tests

Identifie les tests rapides

Args:
    threshold: Seuil en secondes pour considérer un test comme rapide
    
Returns:
    Liste des tests rapides

**Paramètres :**

- `threshold`

##### generate_optimization_report

Génère un rapport d'optimisation

Returns:
    Contenu du rapport

##### save_report

Sauvegarde le rapport d'optimisation

Args:
    filename: Nom du fichier de rapport

**Paramètres :**

- `filename`

##### run_fast_tests_only

Exécute seulement les tests rapides

Returns:
    True si tous les tests rapides passent

---

### test_adaptive_distillation

#### Classes

##### TestAdaptiveDistiller

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_majority_voting()`
- `test_empty()`
- `test_update_preferences()`
- `test_feedback_success_failure()`
- `test_save_and_load_history()`

#### Fonctions

##### setUp

##### tearDown

##### test_majority_voting

##### test_empty

##### test_update_preferences

##### test_feedback_success_failure

##### test_save_and_load_history

---

### test_advanced_analytics_unit

#### Classes

##### TestAdvancedAnalytics

**Méthodes :**

- `setUp()`
- `test_constructor()`
- `test_run()`
- `test_analyze_coverage()`
- `test_analyze_performance()`
- `test_generate_dashboard()`
- `test_generate_summary()`
- `test_print_report()`

#### Fonctions

##### setUp

##### test_constructor

##### test_run

##### test_analyze_coverage

##### test_analyze_performance

##### test_generate_dashboard

##### test_generate_summary

##### test_print_report

---

### test_agent_network

Tests pour les agents unifiés
Corrigé après consolidation des agents

#### Classes

##### TestAgentUnified

Tests pour les agents unifiés (corrigé)

**Méthodes :**

- `test_agent_unified_basic()`
- `test_agent_imports()`

#### Fonctions

##### test_agent_unified_basic

Test basique des agents unifiés

**Paramètres :**

- `mock_qwen`

##### test_agent_imports

Test des imports d'agents unifiés

---

### test_ai_robust

#### Classes

##### TestRobustAI

Tests pour list_data'IA robuste.

**Méthodes :**

- `setup_method()`
- `test_detect_available_models()`
- `test_build_fallback_chain()`
- `test_classify_project_complexity()`
- `test_get_dynamic_prompt()`
- `test_generate_blueprint_with_mock()`
- `test_review_code_with_mock()`
- `test_generate_documentation_with_mock()`
- `test_call_ollama_timeout()`
- `test_fallback_chain_behavior()`

#### Fonctions

##### test_robust_ai_integration

Test dict_data'intégration de list_data'IA robuste.

##### test_prompt_templates

Test que tous les templates de prompts sont chargés.

##### test_fallback_and_distillation_qwen_mistral

Teste la génération de réponse avec fallback et distillation (Qwen/Mistral).

##### test_fallback_ia_qwen_mistral

**Paramètres :**

- `monkeypatch`

##### setup_method

Initialise list_data'IA robuste pour les tests.

##### test_detect_available_models

Test la détection des modèles disponibles.

##### test_build_fallback_chain

Test la construction de la chaîne de fallback.

##### test_classify_project_complexity

##### test_get_dynamic_prompt

Test la génération de prompts dynamiques.

##### test_generate_blueprint_with_mock

Test la génération de blueprint avec fallback mock.

##### test_review_code_with_mock

Test la revue de code avec fallback mock.

##### test_generate_documentation_with_mock

Test la génération de documentation avec fallback mock.

##### test_call_ollama_timeout

Test la gestion du timeout dict_data'Ollama.

##### test_fallback_chain_behavior

Test le comportement de la chaîne de fallback.

##### mock_query_qwen

**Paramètres :**

- `prompt`

##### mock_query_mistral

**Paramètres :**

- `prompt`

##### mock_call_fail

**Paramètres :**

- `model`
- `prompt`
- `timeout`

##### fake_call

**Paramètres :**

- `model_name`
- `prompt`
- `timeout`

---

### test_distillation_optimized

Tests optimisés pour le système de distillation
Version consolidée - Doublons fusionnés et structure améliorée

#### Classes

##### TestResponseDistillerOptimized

Tests optimisés pour le distillateur de réponses

**Méthodes :**

- `test_majority_voting()`
- `test_stacking()`
- `test_consensus()`
- `test_consensus_divergents()`
- `test_empty_responses()`

##### TestAuditDistillerOptimized

Tests optimisés pour le distillateur d'audit

**Méthodes :**

- `test_weighted_average()`
- `test_empty_audits()`

##### TestCorrectionDistillerOptimized

Tests optimisés pour le distillateur de corrections

**Méthodes :**

- `test_best_score()`
- `test_empty_corrections()`

##### TestQualityScorerOptimized

Tests optimisés pour le scoreur de qualité

**Méthodes :**

- `test_score_default()`
- `test_score_various_inputs()`

#### Fonctions

##### test_majority_voting

Test du vote majoritaire

##### test_stacking

Test de l'empilement

##### test_consensus

Test du consensus

##### test_consensus_divergents

Test du consensus avec divergences

##### test_empty_responses

Test des réponses vides (fusionné)

##### test_weighted_average

Test de la moyenne pondérée

##### test_empty_audits

Test des audits vides (fusionné)

##### test_best_score

Test du meilleur score

##### test_empty_corrections

Test des corrections vides (fusionné)

##### test_score_default

Test du score par défaut

##### test_score_various_inputs

Test du score avec diverses entrées

---

### test_intelligent_modules

🧪 TESTS POUR LES MODULES D'ANALYSE INTELLIGENTE
================================================
Tests pour tous les modules d'analyse intelligente :
- AST Analyzer
- Pattern Detector  
- Architecture Analyzer
- Performance Analyzer
- Intelligent Analyzer (orchestrateur)

#### Classes

##### TestASTAnalyzer

Tests pour l'analyseur AST de base

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_analyze_file()`
- `test_extract_functions()`
- `test_extract_classes()`
- `test_complexity_calculation()`

##### TestPatternDetector

Tests pour le détecteur de patterns

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_analyze_project_patterns()`
- `test_duplicate_detection()`
- `test_antipattern_detection()`

##### TestArchitectureAnalyzer

Tests pour l'analyseur d'architecture

**Méthodes :**

- `setUp()`
- `tearDown()`
- `_create_test_modules()`
- `test_analyze_entire_architecture()`
- `test_module_analysis()`
- `test_dependency_analysis()`
- `test_get_optimization_plan()`

##### TestPerformanceAnalyzer

Tests pour l'analyseur de performance

**Méthodes :**

- `setUp()`
- `tearDown()`
- `_create_test_files()`
- `test_analyze_project_performance()`
- `test_performance_metrics()`
- `test_performance_issues_detection()`
- `test_get_performance_insights()`

##### TestIntelligentAnalyzer

Tests pour l'analyseur intelligent principal

**Méthodes :**

- `setUp()`
- `tearDown()`
- `_create_test_project()`
- `test_analyze_project_comprehensive()`
- `test_overall_score_calculation()`
- `test_recommendations_generation()`
- `test_optimization_plan_creation()`
- `test_get_learning_insights()`

#### Fonctions

##### run_tests

Exécuter tous les tests

##### setUp

##### tearDown

##### test_analyze_file

Test de l'analyse d'un fichier

##### test_extract_functions

Test de l'extraction des fonctions

##### test_extract_classes

Test de l'extraction des classes

##### test_complexity_calculation

Test du calcul de complexité

##### setUp

##### tearDown

##### test_analyze_project_patterns

Test de l'analyse des patterns d'un projet

##### test_duplicate_detection

Test de la détection de doublons

##### test_antipattern_detection

Test de la détection d'anti-patterns

##### setUp

##### tearDown

##### _create_test_modules

Créer des modules de test

##### test_analyze_entire_architecture

Test de l'analyse d'architecture complète

##### test_module_analysis

Test de l'analyse des modules

##### test_dependency_analysis

Test de l'analyse des dépendances

##### test_get_optimization_plan

Test de la génération du plan d'optimisation

##### setUp

##### tearDown

##### _create_test_files

Créer des fichiers de test

##### test_analyze_project_performance

Test de l'analyse de performance d'un projet

##### test_performance_metrics

Test des métriques de performance

##### test_performance_issues_detection

Test de la détection des problèmes de performance

##### test_get_performance_insights

Test de la génération d'insights de performance

##### setUp

##### tearDown

##### _create_test_project

Créer un projet de test

##### test_analyze_project_comprehensive

Test de l'analyse complète d'un projet

##### test_overall_score_calculation

Test du calcul du score global

##### test_recommendations_generation

Test de la génération de recommandations

##### test_optimization_plan_creation

Test de la création du plan d'optimisation

##### test_get_learning_insights

Test de la génération d'insights d'apprentissage

---

### test_ai_robust_integration

#### Classes

##### TestAIRobustIntegration

Tests d'intégration pour l'IA robuste.

**Méthodes :**

- `setup_method()`
- `test_complete_workflow_simple_project()`
- `test_fallback_chain_behavior()`
- `test_different_project_complexities()`
- `test_prompt_contexts()`
- `test_model_detection()`
- `test_error_handling()`

#### Fonctions

##### test_ai_robust_performance

Test de performance de l'IA robuste.

##### test_ai_robust_memory_usage

Test de l'utilisation mémoire de l'IA robuste.

##### setup_method

Initialise l'IA robuste pour les tests.

##### test_complete_workflow_simple_project

Test du workflow complet pour un projet simple.

##### test_fallback_chain_behavior

Test du comportement de la chaîne de fallback.

##### test_different_project_complexities

Test avec différents niveaux de complexité.

##### test_prompt_contexts

Test de tous les contextes de prompts.

##### test_model_detection

Test de la détection des modèles.

##### test_error_handling

Test de la gestion d'erreurs.

##### mock_call_fail

**Paramètres :**

- `model`
- `prompt`
- `timeout`

---

### test_ai_robust_unit

#### Classes

##### TestAiRobust

**Méthodes :**

- `test_robust_ai_instance()`
- `test_fallback_ia()`
- `test_query_qwen()`
- `test_query_mistral()`
- `test_robustai_generate_blueprint()`
- `test_robustai_review_code()`
- `test_robustai_generate_documentation()`
- `test_robustai_classify_project_complexity()`
- `test_robustai_get_dynamic_prompt()`

#### Fonctions

##### test_robust_ai_instance

##### test_fallback_ia

##### test_query_qwen

##### test_query_mistral

##### test_robustai_generate_blueprint

##### test_robustai_review_code

##### test_robustai_generate_documentation

##### test_robustai_classify_project_complexity

##### test_robustai_get_dynamic_prompt

---

### test_aliases

#### Fonctions

##### test_alias_presence

Vérifie que chaque alias défini dans setup/alias.sh est bien présent et correctement écrit.
Prépare la structure pour tester leur exécution réelle à l’avenir.

**Paramètres :**

- `alias_name`

---

### test_aliases_execution

#### Fonctions

##### test_alias_execution

Teste l'exécution de chaque alias non interactif dans un sous-shell interactif.
Vérifie que l'exit code est 0 (pas d'erreur fatale).

**Paramètres :**

- `alias_name`

---

### test_validation_complete

Test Complet de la Chaîne de Validation - Athalia/Arkalia
Vérifie que tous les composants fonctionnent ensemble

#### Fonctions

##### test_validation_objective

Test 1: Validation objective fonctionne

##### test_dashboard_api

Test 2: API du dashboard fonctionne

##### test_validation_express

Test 3: Validation express fonctionne

##### main

Test complet de la chaîne de validation

---

### test_analytics

Tests pour le module analytics

#### Fonctions

##### test_analytics_module_import

Test d'import du module analytics

##### test_analytics_functions

Test des fonctions analytics

##### test_analytics_config

Test de la configuration analytics

---

### test_ci

Tests pour la configuration CI/CD

#### Fonctions

##### test_ci_module_import

Test que le module CI peut être importé

##### test_ci_config_exists

Test que la configuration CI existe

##### test_ci_environment

Test que l'environnement CI est détecté

##### test_ci_dependencies

Test que toutes les dépendances CI sont installées

##### test_ci_timeout_config

Test que pytest-timeout est configuré

##### test_ci_generation_mock

Test de génération de configuration CI (mock)

---

### test_complet_athalia_syntax

Tests spécialisés pour la syntaxe Python
Extrait de test_complet_athalia.py pour améliorer la maintenabilité

#### Classes

##### TestSyntaxPython

Tests spécialisés pour la syntaxe Python

**Méthodes :**

- `__init__()`
- `safe_read_file()`
- `test_syntax_python()`
- `fix_syntax_error()`
- `get_results()`

#### Fonctions

##### test_syntax_python_basic

Test basique de syntaxe Python

##### test_syntax_python_specific_files

Test de syntaxe sur des fichiers spécifiques

##### __init__

**Paramètres :**

- `project_root`

##### safe_read_file

Lit un fichier en gérant différents encodages

**Paramètres :**

- `file_path`

##### test_syntax_python

Test de syntaxe Python sur tous les fichiers .py

##### fix_syntax_error

Tente de corriger une erreur de syntaxe

**Paramètres :**

- `file_path`
- `error_msg`

##### get_results

Retourne les résultats des tests de syntaxe

---

### test_dashboard_unified

Tests pour le dashboard unifié simple
Corrigé après réorganisation des modules

#### Classes

##### TestDashboardUnified

Tests pour le dashboard unifié (corrigé)

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_import_dashboard_unified()`
- `test_dashboard_structure()`
- `test_dashboard_functionality()`

#### Fonctions

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### test_import_dashboard_unified

Test d'import du dashboard unifié

##### test_dashboard_structure

Test de la structure du dashboard

##### test_dashboard_functionality

Test de la fonctionnalité du dashboard

---

### test_analytics_unit

#### Classes

##### TestAnalytics

**Méthodes :**

- `setUp()`
- `test_generate_heatmap_data()`
- `test_generate_technical_debt_analysis()`
- `test_generate_analytics_html()`
- `test_analyze_project()`

#### Fonctions

##### setUp

##### test_generate_heatmap_data

**Paramètres :**

- `mock_audit`

##### test_generate_technical_debt_analysis

**Paramètres :**

- `mock_audit`

##### test_generate_analytics_html

**Paramètres :**

- `mock_debt`
- `mock_heatmap`

##### test_analyze_project

---

### test_orchestrator_basic

Tests basiques pour l'orchestrateur Athalia
Extrait de test_athalia_orchestrator.py pour améliorer la maintenabilité

#### Classes

##### TestOrchestratorBasic

Tests basiques pour l'orchestrateur principal

**Méthodes :**

- `setup_method()`
- `teardown_method()`
- `test_orchestrator_initialization()`
- `test_industrialize_project_audit_only()`
- `test_industrialize_project_documentation_only()`
- `test_industrialize_project_complete()`
- `test_scan_projects()`
- `test_invalid_project_path()`
- `test_empty_project()`

#### Fonctions

##### test_orchestrator_import

Test d'import de l'orchestrateur

##### setup_method

Setup pour chaque test

##### teardown_method

Cleanup après chaque test

##### test_orchestrator_initialization

Test l'initialisation de l'orchestrateur

##### test_industrialize_project_audit_only

Test l'industrialisation avec audit seulement

##### test_industrialize_project_documentation_only

Test l'industrialisation avec documentation seulement

##### test_industrialize_project_complete

Test l'industrialisation complète en mode simulation

##### test_scan_projects

Test du scan de projets

##### test_invalid_project_path

Test avec un chemin de projet invalide

##### test_empty_project

Test avec un projet vide

---

### test_api_distillation

#### Fonctions

##### test_feedback

---

### test_ath_context_prompt_semantic

Test d'intégration sémantique pour ath_context_prompt

#### Fonctions

##### test_ath_context_prompt_semantic

Teste que le prompt sécurité est détecté par l'analyse sémantique/custom.

---

### test_ath_dev_boost_menu

Tests pour le menu ath-dev-boost
Version: 1.0
Auteur: Athalia Team

#### Classes

##### TestAthDevBoostMenu

Tests pour le menu ath-dev-boost

Cette classe teste les aspects suivants :
- Existence du script
- Exécutabilité du script
- Contenu du script
- Fonctionnalités du menu

**Méthodes :**

- `setUp()`
- `test_script_exists()`
- `test_script_executable()`
- `test_script_content_structure()`

#### Fonctions

##### test_script_path_validity

Test de la validité du chemin du script

Scénario : Vérification du chemin du script
Données : Chemin setup/ath-dev-boost.sh
Résultat attendu : Le chemin doit être valide

##### setUp

Initialisation avant chaque test

##### test_script_exists

Test que le script ath-dev-boost existe

Scénario : Vérification de l'existence du fichier
Données : Chemin vers setup/ath-dev-boost.sh
Résultat attendu : Le fichier doit exister

##### test_script_executable

Test que le script est exécutable

Scénario : Vérification de l'exécutabilité du script
Données : Fichier setup/ath-dev-boost.sh
Résultat attendu : Le script doit être exécutable

##### test_script_content_structure

Test de la structure du contenu du script

Scénario : Vérification de la structure du script
Données : Contenu du fichier setup/ath-dev-boost.sh
Résultat attendu : Le script doit avoir une structure valide

---

### test_athalia_orchestrator_unit

#### Classes

##### TestAthaliaOrchestrator

**Méthodes :**

- `setUp()`
- `test_constructor()`
- `test_run_cleanup()`
- `test_run_documentation()`
- `test_run_testing()`
- `test_run_cicd()`
- `test_generate_final_report()`
- `test_save_report()`

#### Fonctions

##### setUp

##### test_constructor

##### test_run_cleanup

##### test_run_documentation

##### test_run_testing

##### test_run_cicd

##### test_generate_final_report

##### test_save_report

---

### test_athalia_simple

Tests simples pour Athalia

#### Fonctions

##### test_athalia_core_import

Test d'import du module core

##### test_essential_files_exist

Test que les fichiers essentiels existent

##### test_project_structure

Test de la structure du projet

---

### test_audit_intelligent

Tests pour le système d'audit intelligent Athalia

#### Classes

##### TestAuditIntelligent

Tests pour l'audit intelligent.

**Méthodes :**

- `setup_method()`
- `teardown_method()`
- `create_test_project()`
- `test_audit_project_structure()`
- `test_audit_code_quality()`
- `test_audit_security()`
- `test_audit_performance()`
- `test_audit_complete()`
- `test_generate_audit_report()`
- `test_audit_project_not_found()`
- `test_audit_empty_project()`

#### Fonctions

##### test_audit_integration

Test d'intégration de l'audit avec un vrai projet.

##### setup_method

Prépare un projet de test pour l'audit.

##### teardown_method

Nettoie après les tests.

##### create_test_project

Crée un projet de test avec des problèmes connus.

##### test_audit_project_structure

##### test_audit_code_quality

##### test_audit_security

##### test_audit_performance

##### test_audit_complete

##### test_generate_audit_report

##### test_audit_project_not_found

##### test_audit_empty_project

---

### test_auto_cicd_unit

#### Classes

##### TestAutoCICD

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_constructor()`
- `test_setup_cicd()`
- `test_detect_project_type_python()`
- `test_detect_project_type_nodejs()`
- `test_detect_languages()`
- `test_extract_dependencies_python()`
- `test_find_entry_points()`
- `test_has_tests()`
- `test_has_documentation()`
- `test_generate_github_actions()`
- `test_generate_docker_config()`
- `test_generate_deployment_config()`
- `test_get_created_files()`

#### Fonctions

##### test_generate_github_ci_yaml

##### setUp

##### tearDown

##### test_constructor

##### test_setup_cicd

##### test_detect_project_type_python

##### test_detect_project_type_nodejs

##### test_detect_languages

##### test_extract_dependencies_python

##### test_find_entry_points

##### test_has_tests

##### test_has_documentation

##### test_generate_github_actions

##### test_generate_docker_config

##### test_generate_deployment_config

##### test_get_created_files

---

### test_auto_cleaner_unit

#### Classes

##### TestAutoCleaner

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_constructor()`
- `test_clean_project_dry_run()`
- `test_clean_system_files()`
- `test_clean_cache_files()`
- `test_clean_backup_files()`
- `test_clean_temp_files()`
- `test_clean_duplicate_files()`
- `test_clean_empty_directories()`
- `test_is_code_file()`
- `test_is_important_file()`
- `test_is_empty_directory()`
- `test_calculate_file_hash()`
- `test_generate_cleanup_report()`
- `test_optimize_project_structure()`

#### Fonctions

##### setUp

##### tearDown

##### test_constructor

##### test_clean_project_dry_run

##### test_clean_system_files

##### test_clean_cache_files

##### test_clean_backup_files

##### test_clean_temp_files

##### test_clean_duplicate_files

##### test_clean_empty_directories

##### test_is_code_file

##### test_is_important_file

##### test_is_empty_directory

##### test_calculate_file_hash

##### test_generate_cleanup_report

##### test_optimize_project_structure

---

### test_ci_consolidated

Tests CI consolidés - Fusion des tests CI ultra-rapides et robustes
Exécution: < 15 secondes
Consolidation des tests: test_ci_ultra_fast.py, test_ci_robust.py, test_ci_manual.py, test_ci_final.py

#### Classes

##### TestCIConsolidated

Tests CI consolidés pour validation complète

**Méthodes :**

- `test_python_version()`
- `test_essential_imports()`
- `test_config_files_exist()`
- `test_syntax_check_core()`
- `test_no_critical_errors()`
- `test_requirements_parseable()`
- `test_essential_structure()`
- `test_test_discovery()`
- `test_core_functionality()`
- `test_no_hardcoded_paths()`
- `test_git_clean()`
- `test_encoding_consistency()`
- `test_imports_all_modules()`
- `test_advanced_modules_imports()`
- `test_agents_imports()`
- `test_plugins_imports()`

#### Fonctions

##### test_python_version

Vérifie la version Python

##### test_essential_imports

Vérifie les imports essentiels

##### test_config_files_exist

Vérifie l'existence des fichiers de config essentiels

##### test_syntax_check_core

Vérifie la syntaxe des modules core

##### test_no_critical_errors

Vérifie qu'il n'y a pas d'erreurs critiques

##### test_requirements_parseable

Vérifie que requirements.txt est parseable

##### test_essential_structure

Vérifie la structure essentielle du projet

##### test_test_discovery

Vérifie que les tests peuvent être découverts

##### test_core_functionality

Test de fonctionnalités core essentielles

##### test_no_hardcoded_paths

Vérifie qu'il n'y a pas de chemins hardcodés problématiques

##### test_git_clean

Test que le projet est propre (pas de fichiers temporaires)

##### test_encoding_consistency

Test que tous les fichiers Python sont encodés en UTF-8

##### test_imports_all_modules

Vérifie les imports de tous les modules principaux

##### test_advanced_modules_imports

Vérifie les imports des modules avancés

##### test_agents_imports

Vérifie les imports des agents

##### test_plugins_imports

Vérifie les imports des plugins externes

---

### test_auto_correction_avancee

Tests pour le module d'auto-correction avancée
Corrigé après réorganisation des modules

#### Classes

##### TestAutoCorrectionAdvanced

Tests pour l'auto-correction avancée (corrigé)

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_import_auto_correction()`
- `test_import_dashboard_unified()`
- `test_import_user_profiles()`
- `test_advanced_modules_structure()`

#### Fonctions

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### test_import_auto_correction

Test d'import du module d'auto-correction

##### test_import_dashboard_unified

Test d'import du dashboard unifié

##### test_import_user_profiles

Test d'import des profils utilisateur

##### test_advanced_modules_structure

Test de la structure des modules avancés

---

### test_auto_documenter_unit

#### Classes

##### TestAutoDocumenter

**Méthodes :**

- `setUp()`
- `test_constructor()`
- `test_load_translations()`
- `test_document_project()`
- `test_generate_readme()`
- `test_generate_api_documentation()`
- `test_generate_setup_guide()`
- `test_generate_usage_guide()`
- `test_get_created_files()`

#### Fonctions

##### setUp

##### test_constructor

##### test_load_translations

##### test_document_project

##### test_generate_readme

##### test_generate_api_documentation

##### test_generate_setup_guide

##### test_generate_usage_guide

##### test_get_created_files

---

### test_auto_tester_unit

#### Classes

##### TestAutoTester

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_constructor()`
- `test_analyze_modules()`
- `test_generate_unit_tests()`
- `test_generate_integration_tests()`
- `test_generate_performance_tests()`
- `test_generate_test_report()`
- `test_generate_tests()`

#### Fonctions

##### setUp

##### tearDown

##### test_constructor

##### test_analyze_modules

##### test_generate_unit_tests

##### test_generate_integration_tests

##### test_generate_performance_tests

##### test_generate_test_report

##### test_generate_tests

---

### test_autocomplete_server

#### Classes

##### MockResp

**Méthodes :**

- `raise_for_status()`
- `json()`

#### Fonctions

##### test_autocomplete_nominal

##### test_autocomplete_empty_prompt

##### test_ollama_autocomplete_engine

**Paramètres :**

- `monkeypatch`

##### mock_post

##### raise_for_status

##### json

---

### test_benchmark_critical

#### Fonctions

##### import_critical_function

**Paramètres :**

- `module_name`
- `func_name`

##### test_critical_function_benchmark

**Paramètres :**

- `benchmark`
- `module_name`
- `func_name`
- `needs_path`

##### test_global_coverage_threshold

Ce test échoue si la couverture descend sous 80%.

---

### test_cleanup

Tests pour le module cleanup

#### Fonctions

##### test_clean_old_tests_and_caches

Test de nettoyage des anciens tests et caches

**Paramètres :**

- `tmp_path`

##### test_cleanup_module_import

Test d'import du module cleanup

---

### test_orchestrator_robotics

Tests spécialisés pour les fonctionnalités robotiques de l'orchestrateur
Extrait de test_athalia_orchestrator.py pour améliorer la maintenabilité

#### Classes

##### TestOrchestratorRobotics

Tests spécialisés pour les fonctionnalités robotiques

**Méthodes :**

- `setup_method()`
- `teardown_method()`
- `test_industrialize_project_with_robotics()`
- `test_robotics_module_only()`
- `test_robotics_module_on_non_robotics_project()`
- `test_robotics_module_import()`
- `test_robotics_audit_method()`

#### Fonctions

##### test_robotics_module_availability

Test de la disponibilité du module robotique

##### setup_method

Setup pour chaque test

##### teardown_method

Cleanup après chaque test

##### test_industrialize_project_with_robotics

Test l'industrialisation avec module robotique

##### test_robotics_module_only

Test l'industrialisation avec seulement le module robotique

##### test_robotics_module_on_non_robotics_project

Test le module robotique sur un projet non-robotique

##### test_robotics_module_import

Test l'import du module robotique

##### test_robotics_audit_method

Test de la méthode d'audit robotique

---

### test_final

Tests finaux pour athalia_unified.py

#### Fonctions

##### test_module_availability

Test que le module principal est disponible

##### test_help_command

Test de la commande d'aide

##### test_dashboard_command

Test de la commande dashboard

##### test_fix_command

Test de la commande fix

##### test_advanced_modules

Test des modules avancés

---

### test_aliases_basic

Tests basiques pour le système d'alias unifié
Extrait de test_aliases_unified.py pour améliorer la maintenabilité

#### Classes

##### TestAliasesBasic

Tests basiques pour le système d'alias unifié Athalia

**Méthodes :**

- `test_alias_file_exists()`
- `test_alias_file_readable()`
- `test_all_aliases_defined()`
- `test_git_aliases_present()`
- `test_athalia_core_aliases_present()`
- `test_athalia_functions_present()`
- `test_workflow_aliases_present()`
- `test_autocompletion_configured()`
- `test_syntax_validity()`

#### Fonctions

##### test_alias_file_structure

Test de la structure du fichier d'alias

##### test_alias_file_encoding

Test de l'encodage du fichier d'alias

##### test_alias_file_exists

Vérifie que le fichier d'alias unifié existe

##### test_alias_file_readable

Vérifie que le fichier d'alias est lisible

##### test_all_aliases_defined

Vérifie que tous les alias sont correctement définis

##### test_git_aliases_present

Vérifie la présence des alias Git essentiels

##### test_athalia_core_aliases_present

Vérifie la présence des alias Athalia essentiels

##### test_athalia_functions_present

Vérifie la présence des fonctions Athalia essentielles

##### test_workflow_aliases_present

Vérifie la présence des alias de workflow

##### test_autocompletion_configured

Vérifie que l'auto-complétion est configurée

##### test_syntax_validity

Vérifie la validité syntaxique du fichier d'alias

---

### test_code_genetics

#### Classes

##### TestCodeGenetics

**Méthodes :**

- `setUp()`
- `test_crossover()`
- `test_mutate()`
- `test_select()`
- `test_evolve()`
- `test_empty()`

#### Fonctions

##### setUp

##### test_crossover

##### test_mutate

##### test_select

##### test_evolve

##### test_empty

---

### test_continue_models

Test de présence des modèles dans la config Continue

#### Fonctions

##### test_models_presence

Vérifie la présence des modèles Claude et Mistral dans la config Continue.

---

### test_correction

Script de test pour la correction du projet EmotionSensingRoboticEyes

#### Fonctions

##### test_audit

Test de l'audit du f

##### test_correction

Test de la correction du f

##### test_generation_improvement

Test d'amélioration du service de f

##### main

Fonction principale de f

---

### test_coverage_threshold

Test de seuil de couverture de code
Vérifie que la couverture de code est suffisante

#### Classes

##### TestCoverageThreshold

Tests de seuil de couverture

**Méthodes :**

- `test_coverage_file_exists()`
- `test_minimum_coverage_threshold()`
- `test_core_modules_coverage()`
- `test_test_files_exist()`
- `test_test_coverage_structure()`
- `test_no_untested_critical_modules()`
- `test_coverage_report_readable()`
- `test_coverage_configuration()`
- `test_test_execution_coverage()`
- `test_coverage_quality_metrics()`

#### Fonctions

##### test_coverage_file_exists

Vérifie que le fichier de couverture existe

##### test_minimum_coverage_threshold

Vérifie le seuil minimum de couverture

##### test_core_modules_coverage

Vérifie la couverture des modules core

##### test_test_files_exist

Vérifie que les fichiers de test existent

##### test_test_coverage_structure

Vérifie la structure de couverture des tests

##### test_no_untested_critical_modules

Vérifie qu'il n'y a pas de modules critiques non testés

##### test_coverage_report_readable

Vérifie que le rapport de couverture est lisible

##### test_coverage_configuration

Vérifie la configuration de couverture

##### test_test_execution_coverage

Vérifie que les tests s'exécutent avec couverture

##### test_coverage_quality_metrics

Vérifie les métriques de qualité de la couverture

---

### test_dashboard

#### Fonctions

##### test_benchmarks_section_present

Vérifie que la section Benchmarks et les éléments clés existent dans le dashboard.

---

### test_aliases_advanced

Tests avancés pour le système d'alias unifié
Extrait de test_aliases_unified.py pour améliorer la maintenabilité

#### Classes

##### TestAliasesAdvanced

Tests avancés pour le système d'alias unifié Athalia

**Méthodes :**

- `test_placeholder_aliases_defined()`
- `test_plugin_aliases_configured()`
- `test_test_aliases_specific()`
- `test_docker_aliases_present()`
- `test_benchmark_aliases_present()`
- `test_documentation_aliases_present()`
- `test_security_aliases_present()`
- `test_development_aliases_present()`
- `test_configuration_aliases_present()`
- `test_modules_aliases_present()`
- `test_help_function_content()`
- `test_status_function_content()`
- `test_initialization_message()`

#### Fonctions

##### test_alias_file_completeness

Test de la complétude du fichier d'alias

##### test_alias_file_consistency

Test de la cohérence du fichier d'alias

##### test_placeholder_aliases_defined

Vérifie que les alias à implémenter sont définis

##### test_plugin_aliases_configured

Vérifie la configuration des alias de plugins

##### test_test_aliases_specific

Vérifie les alias de tests spécifiques

##### test_docker_aliases_present

Vérifie les alias Docker

##### test_benchmark_aliases_present

Vérifie les alias de benchmark

##### test_documentation_aliases_present

Vérifie les alias de documentation

##### test_security_aliases_present

Vérifie les alias de sécurité

##### test_development_aliases_present

Vérifie les alias de développement

##### test_configuration_aliases_present

Vérifie les alias de configuration

##### test_modules_aliases_present

Vérifie les alias de modules avancés

##### test_help_function_content

Vérifie le contenu de la fonction d'aide

##### test_status_function_content

Vérifie le contenu de la fonction de statut

##### test_initialization_message

Vérifie le message d'initialisation

---

### test_dashboard_unifie

#### Classes

##### TestDashboardUnifie

Tests pour le dashboard unifié

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_initialisation()`
- `test_enregistrement_metrique()`
- `test_enregistrement_evenement()`
- `test_generation_rapport()`
- `test_generation_html()`

#### Fonctions

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### test_initialisation

Test de l'initialisation du dashboard

##### test_enregistrement_metrique

Test de l'enregistrement d'une métrique

##### test_enregistrement_evenement

Test de l'enregistrement d'un événement

##### test_generation_rapport

Test de génération de rapport consolidé

##### test_generation_html

Test de génération du dashboard HTML

---

### test_correction_optimizer_optimized

Tests optimisés pour le système d'optimisation de correction automatique
Version consolidée - Doublons fusionnés et structure améliorée

#### Classes

##### TestCorrectionOptimizerOptimized

Tests optimisés pour le système d'optimisation de correction

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_basic_corrections()`
- `test_contextual_corrections()`
- `test_complex_correction()`
- `test_correction_stats()`
- `test_learning_from_corrections()`
- `test_error_handling()`
- `test_performance_logging()`
- `test_convenience_functions()`

##### TestCorrectionOptimizerIntegration

Tests d'intégration optimisés pour le système d'optimisation

**Méthodes :**

- `test_with_real_files()`

#### Fonctions

##### setUp

Initialisation avant chaque test

##### tearDown

Nettoyage après chaque test

##### test_basic_corrections

Test des corrections basiques (fusionné)

##### test_contextual_corrections

Test des corrections contextuelles (fusionné)

##### test_complex_correction

Test de correction complexe (fusionné)

##### test_correction_stats

Test des statistiques de correction (fusionné)

##### test_learning_from_corrections

Test de l'apprentissage des corrections (fusionné)

##### test_error_handling

Test de gestion des erreurs (fusionné)

##### test_performance_logging

Test du logging de performance (fusionné)

##### test_convenience_functions

Test des fonctions de convenance (fusionné)

##### test_with_real_files

Test avec de vrais fichiers (fusionné)

---

### test_encoding_utf8

Test de vérification de l'encodage UTF-8
Vérifie que tous les fichiers sont correctement encodés en UTF-8

#### Classes

##### TestEncodingUTF8

Tests de vérification de l'encodage UTF-8

**Méthodes :**

- `test_python_files_utf8()`
- `test_markdown_files_utf8()`
- `test_yaml_files_utf8()`
- `test_txt_files_utf8()`
- `test_requirements_utf8()`
- `test_config_utf8()`
- `test_no_bom_marker()`
- `test_consistent_line_endings()`

#### Fonctions

##### test_python_files_utf8

Vérifie que tous les fichiers Python sont en UTF-8

##### test_markdown_files_utf8

Vérifie que tous les fichiers Markdown sont en UTF-8

##### test_yaml_files_utf8

Vérifie que tous les fichiers YAML sont en UTF-8

##### test_txt_files_utf8

Vérifie que tous les fichiers TXT sont en UTF-8

##### test_requirements_utf8

Vérifie que requirements.txt est en UTF-8

##### test_config_utf8

Vérifie que les fichiers de config sont en UTF-8

##### test_no_bom_marker

Vérifie qu'il n'y a pas de marqueur BOM UTF-8

##### test_consistent_line_endings

Vérifie la cohérence des fins de ligne

---

### test_final_athalia

Test final pour Athalia - Vérification complète du projet

#### Fonctions

##### test_compilation_fichiers

Test de compilation des fichiers principaux

##### test_execution_principale

Test d'exécution du script principal

##### test_imports_modules

Test des imports des modules principaux

##### test_structure_projet

Test de la structure du projet

##### generer_rapport_final

Génère un rapport final

**Paramètres :**

- `erreurs_compilation`
- `erreurs_import`
- `erreurs_structure`
- `execution_ok`

##### main

Fonction principale

---

### test_generation

#### Fonctions

##### test_generate_blueprint_mock

##### test_save_and_inject

**Paramètres :**

- `tmp_path`

##### test_scan_existing_project

**Paramètres :**

- `tmp_path`

##### test_generate_project_dry_run

**Paramètres :**

- `tmp_path`

##### test_merge_or_suffix_file

**Paramètres :**

- `tmp_path`

##### test_merge_or_suffix_file_types

**Paramètres :**

- `tmp_path`

##### test_backup_file

**Paramètres :**

- `tmp_path`

---

### test_hardcoded_paths

Tests pour détecter les chemins hardcodés

#### Classes

##### TestHardcodedPaths

Tests pour détecter les chemins hardcodés

**Méthodes :**

- `test_no_absolute_paths_in_source()`
- `test_no_absolute_paths()`
- `test_no_desktop_paths()`
- `_is_acceptable_path()`

#### Fonctions

##### test_no_absolute_paths_in_source

Test qu'il n'y a pas de chemins absolus dans le code source (sauf tests)

##### test_no_absolute_paths

Test qu'il n'y a pas de chemins absolus hardcodés

##### test_no_desktop_paths

Test qu'il n'y a pas de chemins Desktop hardcodés

##### _is_acceptable_path

Vérifie si un chemin absolu est acceptable

**Paramètres :**

- `path`

---

### test_complet_athalia_imports

Tests spécialisés pour les imports Python
Extrait de test_complet_athalia.py pour améliorer la maintenabilité

#### Classes

##### TestImportsPython

Tests spécialisés pour les imports Python

**Méthodes :**

- `__init__()`
- `safe_read_file()`
- `test_imports()`
- `module_exists()`
- `test_imports_specific_modules()`
- `get_results()`

#### Fonctions

##### test_imports_basic

Test basique des imports

##### test_imports_specific

Test des imports de modules spécifiques

##### test_imports_athalia_core

Test des imports athalia_core

##### __init__

**Paramètres :**

- `project_root`

##### safe_read_file

Lit un fichier en gérant différents encodages

**Paramètres :**

- `file_path`

##### test_imports

Test des imports Python

##### module_exists

Vérifie si un module existe

**Paramètres :**

- `module_name`

##### test_imports_specific_modules

Test des imports de modules spécifiques

##### get_results

Retourne les résultats des tests d'imports

---

### test_ai_robust_standardized

Tests pour le module AI robuste
Version: 1.0
Auteur: Athalia Team

#### Classes

##### TestAIRobust

Tests pour l'IA robuste

Cette classe teste les aspects suivants :
- Détection des modèles disponibles
- Construction de la chaîne de fallback
- Classification de complexité de projet
- Génération de prompts dynamiques
- Génération de blueprints
- Revues de code
- Génération de documentation

**Méthodes :**

- `setUp()`
- `test_detect_available_models()`
- `test_build_fallback_chain()`
- `test_classify_project_complexity()`
- `test_get_dynamic_prompt()`
- `test_generate_blueprint_with_mock()`
- `test_review_code_with_mock()`
- `test_generate_documentation_with_mock()`
- `test_call_ollama_timeout()`
- `test_fallback_chain_behavior()`

#### Fonctions

##### test_robust_ai_integration

Test d'intégration de l'IA robuste

Scénario : Test complet du workflow AI
Données : Instance RobustAI
Résultat attendu : Workflow complet fonctionnel

##### test_prompt_templates

Test que tous les templates de prompts sont chargés

Scénario : Vérification de tous les templates de prompts
Données : Instance RobustAI
Résultat attendu : Tous les templates doivent être disponibles

##### setUp

Initialisation avant chaque test

##### test_detect_available_models

Test la détection des modèles disponibles

Scénario : Vérification des modèles AI disponibles
Données : Instance RobustAI
Résultat attendu : Liste non vide avec au moins le modèle MOCK

##### test_build_fallback_chain

Test la construction de la chaîne de fallback

Scénario : Vérification de la chaîne de fallback
Données : Instance RobustAI
Résultat attendu : Chaîne non vide avec au moins le modèle MOCK

##### test_classify_project_complexity

Test la classification de complexité de projet

Scénario : Classification de différents types de projets
Données : Descriptions de projets
Résultat attendu : Classification appropriée pour chaque type

##### test_get_dynamic_prompt

Test la génération de prompts dynamiques

Scénario : Génération de prompts avec différents contextes
Données : Contexte, idée, type et complexité de projet
Résultat attendu : Prompt contenant tous les éléments

##### test_generate_blueprint_with_mock

Test la génération de blueprint avec fallback mock

Scénario : Génération de blueprint avec modèle MOCK
Données : Idée de projet
Résultat attendu : Blueprint complet avec tous les champs requis

##### test_review_code_with_mock

Test la revue de code avec fallback mock

Scénario : Revue de code avec modèle MOCK
Données : Code à revoir
Résultat attendu : Revue complète avec score, problèmes et suggestions

##### test_generate_documentation_with_mock

Test la génération de documentation avec fallback mock

Scénario : Génération de documentation avec modèle MOCK
Données : Nom et type de projet, modules
Résultat attendu : Documentation non vide

##### test_call_ollama_timeout

Test la gestion du timeout d'Ollama

Scénario : Test de timeout avec Ollama
Données : Modèle Ollama avec timeout court
Résultat attendu : None ou réponse valide

##### test_fallback_chain_behavior

Test le comportement de la chaîne de fallback

Scénario : Simulation d'échec d'Ollama
Données : Mock de _call_ollama qui échoue
Résultat attendu : Utilisation du fallback MOCK

---

### test_i18n

Tests pour le module i18n

#### Fonctions

##### test_i18n_module_import

Test d'import du module i18n

##### test_french_translations

Test des traductions françaises

##### test_english_translations

Test des traductions anglaises

##### test_translation_consistency

Test de la cohérence des traductions

---

### test_imports_all

Test d'importation exhaustive de tous les modules
Vérifie que tous les modules peuvent être importés sans erreur

#### Classes

##### TestImportsAll

Tests d'importation exhaustive

**Méthodes :**

- `test_core_modules_import()`
- `test_distillation_modules_import()`
- `test_classification_modules_import()`
- `test_i18n_modules_import()`
- `test_plugins_modules_import()`
- `test_modules_import()`
- `test_agents_import()`
- `test_templates_import()`
- `test_all_python_files_importable()`
- `test_no_circular_imports()`
- `test_third_party_imports()`

#### Fonctions

##### test_core_modules_import

Test d'import des modules core

##### test_distillation_modules_import

Test d'import des modules de distillation

##### test_classification_modules_import

Test d'import des modules de classification

##### test_i18n_modules_import

Test d'import des modules i18n

##### test_plugins_modules_import

Test d'import des modules plugins

##### test_modules_import

Test d'import des modules externes

##### test_agents_import

Test que tous les modules agents peuvent être importés

##### test_templates_import

Test que tous les modules templates peuvent être importés

##### test_all_python_files_importable

Test que tous les fichiers Python peuvent être importés

##### test_no_circular_imports

Test qu'il n'y a pas d'imports circulaires

##### test_third_party_imports

Test des imports de bibliothèques tierces

---

### test_integration_1

#### Classes

##### TestIntegration

Tests dintégration

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_project_import()`
- `test_basic_functionality()`
- `test_error_handling()`

#### Fonctions

##### setUp

Configuration avant chaque test

##### tearDown

Nettoyage après chaque test

##### test_project_import

Test dimport du projet

##### test_basic_functionality

Test de fonctionnalité de base

##### test_error_handling

Test de gestion derreurs

---

### test_integration_autogen

#### Classes

##### TestIntegrationAutoGen

**Méthodes :**

- `setUp()`
- `test_autogen_orchestration()`

#### Fonctions

##### setUp

Initialisation avant chaque test

##### test_autogen_orchestration

Test d'orchestration avec AutoGen

Scénario : Test de l'orchestration des agents
Données : Agents d'audit, correction et synthèse
Résultat attendu : Synthèse contenant les résultats des agents

---

### test_performance_optimized

Tests optimisés pour les performances
Version: 1.0
Auteur: Athalia Team

#### Classes

##### TestPerformanceOptimized

Tests optimisés pour les performances

Cette classe utilise des techniques d'optimisation :
- Cache des objets coûteux
- Setup/teardown optimisés
- Tests parallélisables
- Réduction des I/O

**Méthodes :**

- `setUpClass()`
- `tearDownClass()`
- `setUp()`
- `tearDown()`
- `test_analytics_instantiation()`
- `test_audit_instantiation()`
- `test_cleanup_instantiation()`
- `test_analytics_basic_operations()`
- `test_audit_basic_operations()`
- `test_cleanup_basic_operations()`
- `test_analytics_with_cache()`
- `test_parallel_operations()`
- `test_memory_usage()`

#### Fonctions

##### test_import_performance

Test de performance des imports

Scénario : Import des modules principaux
Données : Modules athalia_core
Résultat attendu : Imports rapides

##### test_module_instantiation_performance

Test de performance d'instanciation

Scénario : Instanciation des modules principaux
Données : Classes principales
Résultat attendu : Instanciation rapide

##### setUpClass

Setup de classe - exécuté une seule fois pour tous les tests

**Paramètres :**

- `cls`

##### tearDownClass

Teardown de classe - nettoyage final

**Paramètres :**

- `cls`

##### setUp

Setup rapide pour chaque test

##### tearDown

Teardown rapide avec vérification de performance

##### test_analytics_instantiation

Test d'instanciation rapide d'Analytics

Scénario : Instanciation d'Analytics
Données : Instance Analytics
Résultat attendu : Instance valide créée rapidement

##### test_audit_instantiation

Test d'instanciation rapide d'Audit

Scénario : Instanciation d'Audit
Données : Instance Audit
Résultat attendu : Instance valide créée rapidement

##### test_cleanup_instantiation

Test d'instanciation rapide de Cleanup

Scénario : Instanciation de Cleanup
Données : Instance Cleanup
Résultat attendu : Instance valide créée rapidement

##### test_analytics_basic_operations

Test des opérations basiques d'Analytics

Scénario : Opérations basiques d'Analytics
Données : Instance Analytics
Résultat attendu : Opérations exécutées rapidement

##### test_audit_basic_operations

Test des opérations basiques d'Audit

Scénario : Opérations basiques d'Audit
Données : Instance Audit
Résultat attendu : Opérations exécutées rapidement

##### test_cleanup_basic_operations

Test des opérations basiques de Cleanup

Scénario : Opérations basiques de Cleanup
Données : Instance Cleanup
Résultat attendu : Opérations exécutées rapidement

##### test_analytics_with_cache

Test d'Analytics avec cache

Scénario : Utilisation du cache pour améliorer les performances
Données : Instance Analytics avec cache
Résultat attendu : Opérations plus rapides avec cache

##### test_parallel_operations

Test d'opérations parallèles

Scénario : Exécution d'opérations en parallèle
Données : Plusieurs instances
Résultat attendu : Opérations exécutées en parallèle

##### test_memory_usage

Test de l'utilisation mémoire

Scénario : Vérification de l'utilisation mémoire
Données : Opérations répétées
Résultat attendu : Utilisation mémoire stable

##### run_analytics

##### run_audit

##### run_cleanup

---

### test_integration_distillation

#### Classes

##### TestIntegrationDistillation

**Méthodes :**

- `setUp()`
- `test_distillation_voting()`
- `test_distillation_stacking()`
- `test_distillation_bagging()`
- `test_distillation_consensus()`
- `test_distillation_creative()`

#### Fonctions

##### setUp

##### test_distillation_voting

##### test_distillation_stacking

##### test_distillation_bagging

##### test_distillation_consensus

##### test_distillation_creative

---

### test_integration_finale_phase4

🧪 TESTS D'INTÉGRATION FINALE PHASE 4
======================================
Tests finaux pour valider l'intégration complète de la phase 4.

#### Classes

##### TestFinalIntegration

Tests d'intégration finale de la phase 4

**Méthodes :**

- `setUp()`
- `tearDown()`
- `create_test_project()`
- `test_final_orchestrator_imports()`
- `test_all_modules_integrated()`
- `test_final_integration_score()`
- `test_final_orchestrator_initialization()`
- `test_final_orchestrator_orchestration()`

##### TestFinalCompleteness

Tests de complétude finale de l'intégration

**Méthodes :**

- `test_final_modules_availability()`
- `test_final_integration_consistency()`
- `test_final_remaining_modules()`

#### Fonctions

##### main

Fonction principale

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### create_test_project

Créer un projet de test

##### test_final_orchestrator_imports

Test des imports de l'orchestrateur avec intégration finale

##### test_all_modules_integrated

Test que tous les modules sont intégrés

##### test_final_integration_score

Test du score d'intégration final

##### test_final_orchestrator_initialization

Test de l'initialisation de l'orchestrateur final

##### test_final_orchestrator_orchestration

Test d'orchestration finale complète

##### test_final_modules_availability

Test que tous les modules finaux sont disponibles

##### test_final_integration_consistency

Test de la cohérence de l'intégration finale

##### test_final_remaining_modules

Test des modules restants après intégration finale

---

### test_integration_multimodal

#### Classes

##### TestIntegrationMultimodal

**Méthodes :**

- `test_multimodal_distillation()`

#### Fonctions

##### test_multimodal_distillation

---

### test_integration_orchestrator

🧪 TESTS D'INTÉGRATION ORCHESTRATEUR
====================================
Tests pour valider l'intégration des modules dans l'orchestrateur unifié.

#### Classes

##### TestOrchestratorIntegration

Tests d'intégration de l'orchestrateur

**Méthodes :**

- `setUp()`
- `tearDown()`
- `create_test_project()`
- `test_orchestrator_imports()`
- `test_integrated_modules_imports()`
- `test_orchestrator_initialization()`
- `test_orchestrator_configuration()`
- `test_integration_score()`
- `test_module_functionality()`
- `test_orchestrator_orchestration()`

##### TestIntegrationCompleteness

Tests de complétude de l'intégration

**Méthodes :**

- `test_all_modules_available()`
- `test_integration_consistency()`

#### Fonctions

##### main

Fonction principale

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### create_test_project

Créer un projet de test

##### test_orchestrator_imports

Test des imports de l'orchestrateur

##### test_integrated_modules_imports

Test des imports des modules intégrés

##### test_orchestrator_initialization

Test de l'initialisation de l'orchestrateur avec modules intégrés

##### test_orchestrator_configuration

Test de la configuration de l'orchestrateur

##### test_integration_score

Test du score d'intégration

##### test_module_functionality

Test de la fonctionnalité des modules intégrés

##### test_orchestrator_orchestration

Test d'orchestration avec modules intégrés

##### test_all_modules_available

Test que tous les modules intégrés sont disponibles

##### test_integration_consistency

Test de la cohérence de l'intégration

---

### test_integration_phase3

🧪 TESTS D'INTÉGRATION PHASE 3
==============================
Tests pour valider l'intégration étendue de la phase 3.

#### Classes

##### TestPhase3Integration

Tests d'intégration de la phase 3

**Méthodes :**

- `setUp()`
- `tearDown()`
- `create_test_project()`
- `test_phase3_orchestrator_imports()`
- `test_functional_modules_imports()`
- `test_phase3_orchestrator_initialization()`
- `test_phase3_integration_score()`
- `test_functional_modules_availability()`
- `test_phase3_orchestrator_orchestration()`

##### TestPhase3Completeness

Tests de complétude de l'intégration Phase 3

**Méthodes :**

- `test_phase3_modules_availability()`
- `test_phase3_integration_consistency()`
- `test_phase3_remaining_modules()`

#### Fonctions

##### main

Fonction principale

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### create_test_project

Créer un projet de test

##### test_phase3_orchestrator_imports

Test des imports de l'orchestrateur avec modules Phase 3

##### test_functional_modules_imports

Test des imports des modules fonctionnels intégrés

##### test_phase3_orchestrator_initialization

Test de l'initialisation de l'orchestrateur Phase 3

##### test_phase3_integration_score

Test du score d'intégration Phase 3

##### test_functional_modules_availability

Test de la disponibilité des modules fonctionnels

##### test_phase3_orchestrator_orchestration

Test d'orchestration avec modules Phase 3

##### test_phase3_modules_availability

Test que tous les modules Phase 3 sont disponibles

##### test_phase3_integration_consistency

Test de la cohérence de l'intégration Phase 3

##### test_phase3_remaining_modules

Test des modules restants après Phase 3

---

### test_lint_flake8

Tests pour le linting flake8

#### Fonctions

##### test_flake8_clean

Test que le code passe flake8 sans erreurs

---

### test_multi_file_editor

#### Fonctions

##### test_apply_corrections_and_rollback

##### test_apply_corrections_error

##### corr_fn

**Paramètres :**

- `content`

##### corr_fn

**Paramètres :**

- `content`

---

### test_multimodal_distiller

#### Classes

##### TestMultimodalDistiller

**Méthodes :**

- `test_distill()`
- `test_empty()`

#### Fonctions

##### test_distill

**Paramètres :**

- `mock_llava`

##### test_empty

---

### test_no_polluting_files

Tests pour détecter les fichiers polluants

#### Classes

##### TestNoPollutingFiles

Tests pour détecter les fichiers polluants

**Méthodes :**

- `test_no_macos_hidden_files()`
- `test_no_python_cache_files()`
- `test_no_temp_files()`
- `test_no_corrupted_files()`
- `test_no_editor_files()`
- `test_no_archive_files()`
- `test_no_secret_files()`
- `test_no_large_files()`
- `test_no_duplicate_files()`
- `test_no_empty_directories()`

#### Fonctions

##### test_no_macos_hidden_files

Test qu'il n'y a pas de fichiers cachés macOS

##### test_no_python_cache_files

Test qu'il n'y a pas de fichiers cache Python

##### test_no_temp_files

Test qu'il n'y a pas de fichiers temporaires

##### test_no_corrupted_files

Test qu'il n'y a pas de fichiers corrompus

##### test_no_editor_files

Test qu'il n'y a pas de fichiers d'éditeur

##### test_no_archive_files

Test qu'il n'y a pas de fichiers d'archive

##### test_no_secret_files

Test qu'il n'y a pas de fichiers de secrets

##### test_no_large_files

Test qu'il n'y a pas de fichiers trop volumineux

##### test_no_duplicate_files

Test qu'il n'y a pas de fichiers dupliqués

##### test_no_empty_directories

Test qu'il n'y a pas de répertoires vides

---

### test_aliases_execution_optimized

Tests d'exécution d'alias optimisés
Version: 1.0
Auteur: Athalia Team

#### Classes

##### TestAliasesExecutionOptimized

Tests d'exécution d'alias optimisés

Cette classe utilise des techniques d'optimisation :
- Cache des alias
- Tests rapides uniquement
- Mock des commandes lentes
- Timeout strict

**Méthodes :**

- `setUpClass()`
- `_load_aliases()`
- `setUp()`
- `tearDown()`
- `test_alias_file_loading()`
- `test_fast_aliases_present()`
- `test_alias_syntax_validity()`
- `test_alias_paths_exist()`
- `test_alias_no_dangerous_commands()`
- `test_alias_execution_simulation()`
- `test_alias_consistency()`
- `test_alias_help_function()`

#### Fonctions

##### test_alias_file_performance

Test de performance du fichier d'alias

Scénario : Chargement rapide du fichier d'alias
Données : Fichier setup/alias.sh
Résultat attendu : Chargement rapide

##### test_alias_count_performance

Test de performance du comptage d'alias

Scénario : Comptage rapide des alias
Données : Fichier d'alias
Résultat attendu : Comptage rapide

##### setUpClass

Setup de classe - cache des alias

**Paramètres :**

- `cls`

##### _load_aliases

Charge les alias depuis le fichier

**Paramètres :**

- `cls`

##### setUp

Setup rapide pour chaque test

##### tearDown

Teardown avec vérification de performance

##### test_alias_file_loading

Test de chargement rapide du fichier d'alias

Scénario : Chargement du fichier d'alias
Données : Fichier setup/alias.sh
Résultat attendu : Alias chargés rapidement

##### test_fast_aliases_present

Test de présence des alias rapides

Scénario : Vérification des alias rapides
Données : Alias en cache
Résultat attendu : Alias rapides présents

##### test_alias_syntax_validity

Test de validité syntaxique des alias

Scénario : Vérification de la syntaxe des alias
Données : Alias chargés
Résultat attendu : Syntaxe valide

##### test_alias_paths_exist

Test d'existence des chemins référencés dans les alias

Scénario : Vérification des chemins des alias
Données : Alias avec chemins
Résultat attendu : Chemins existants

##### test_alias_no_dangerous_commands

Test d'absence de commandes dangereuses dans les alias

Scénario : Vérification de sécurité des alias
Données : Alias chargés
Résultat attendu : Aucune commande dangereuse

##### test_alias_execution_simulation

Test de simulation d'exécution d'alias

Scénario : Simulation d'exécution d'alias
Données : Alias en cache
Résultat attendu : Simulation réussie

##### test_alias_consistency

Test de cohérence des alias

Scénario : Vérification de la cohérence des alias
Données : Alias chargés
Résultat attendu : Alias cohérents

##### test_alias_help_function

Test de la fonction d'aide des alias

Scénario : Vérification de la fonction ath-help
Données : Fichier d'alias
Résultat attendu : Fonction d'aide présente

---

### test_onboarding

#### Fonctions

##### test_onboarding

**Paramètres :**

- `tmp_path`

---

### test_performance_1

#### Classes

##### TestPerformance

Tests de performance

**Méthodes :**

- `setUp()`
- `test_import_performance()`
- `test_memory_usage()`
- `test_execution_time()`

#### Fonctions

##### setUp

Configuration avant chaque test

##### test_import_performance

Test de performance des imports

##### test_memory_usage

Test dusage mémoire

##### test_execution_time

Test de temps dexécution

---

### test_plugin_complet

Test complet du plugin VS Code Athalia
Vérifie tous les composants nécessaires au fonctionnement

#### Fonctions

##### print_status

**Paramètres :**

- `message`
- `status`

##### test_vscode_installation

Test si VS Code est installé et accessible

##### test_plugin_compilation

Test si le plugin est compilé

##### test_package_json

Test la configuration package.json

##### test_ai_server

Test si le serveur d'autocomplétion IA fonctionne

##### test_apple_double_files

Test s'il y a des fichiers AppleDouble parasites

##### generate_test_report

Génère un rapport de test complet

---

### test_plugins

Tests pour le système de plugins dynamiques Athalia

#### Fonctions

##### test_list_plugins

##### test_load_plugin

##### test_run_all_plugins

##### test_export_docker_plugin

---

### test_plugins_validator

#### Fonctions

##### test_validate_plugin_ok

##### test_validate_plugin_fail

---

### test_predictive_cache

#### Classes

##### TestPredictiveCache

**Méthodes :**

- `test_set_get()`
- `test_predict_key()`
- `test_pre_generate()`
- `test_invalidate()`
- `test_stats()`
- `test_ttl()`

#### Fonctions

##### test_set_get

##### test_predict_key

##### test_pre_generate

##### test_invalidate

##### test_stats

##### test_ttl

##### gen

**Paramètres :**

- `ctx`

---

### test_profils_utilisateur_avances

Tests pour les profils utilisateur avancés
Corrigé après réorganisation des modules

#### Classes

##### TestUserProfilesAdvanced

Tests pour les profils utilisateur avancés (corrigé)

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_import_user_profiles()`
- `test_profiles_structure()`
- `test_profiles_functionality()`

#### Fonctions

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### test_import_user_profiles

Test d'import des profils utilisateur

##### test_profiles_structure

Test de la structure des profils

##### test_profiles_functionality

Test de la fonctionnalité des profils

---

### test_project_importer

#### Fonctions

##### test_project_import_concept

---

### test_ready_check

Tests pour ready_check.py

#### Fonctions

##### test_check_ready_ok

Test que le projet est prêt

##### test_check_ready_missing

Test avec un projet manquant

---

### test_requirements_consistency

Test de cohérence des dépendances
Vérifie que les fichiers de dépendances sont cohérents

#### Classes

##### TestRequirementsConsistency

Tests de cohérence des dépendances

**Méthodes :**

- `test_requirements_txt_exists()`
- `test_requirements_txt_readable()`
- `test_requirements_format()`
- `test_essential_dependencies()`
- `test_no_duplicate_dependencies()`
- `test_pyproject_toml_exists()`
- `test_pyproject_toml_readable()`
- `test_requirements_vs_pyproject_consistency()`
- `test_no_conflicting_versions()`
- `test_no_obsolete_dependencies()`
- `test_requirements_installable()`

#### Fonctions

##### test_requirements_txt_exists

Vérifie que requirements.txt existe

##### test_requirements_txt_readable

Vérifie que requirements.txt est lisible

##### test_requirements_format

Vérifie le format de requirements.txt

##### test_essential_dependencies

Vérifie que les dépendances essentielles sont présentes

##### test_no_duplicate_dependencies

Test qu'il n'y a pas de dépendances dupliquées

##### test_pyproject_toml_exists

Vérifie que pyproject.toml existe

##### test_pyproject_toml_readable

Vérifie que pyproject.toml est lisible

##### test_requirements_vs_pyproject_consistency

Vérifie la cohérence entre requirements.txt et pyproject.toml

##### test_no_conflicting_versions

Vérifie qu'il n'y a pas de versions conflictuelles

##### test_no_obsolete_dependencies

Vérifie qu'il n'y a pas de dépendances obsolètes

##### test_requirements_installable

Vérifie que requirements.txt est installable

---

### test_security

#### Fonctions

##### test_security_audit_project

**Paramètres :**

- `tmp_path`

---

### test_security_patterns

Test de détection des patterns de sécurité dangereux
Vérifie qu'il n'y a pas de code dangereux dans le projet

#### Classes

##### TestSecurityPatterns

Tests de détection des patterns de sécurité

**Méthodes :**

- `test_no_hardcoded_passwords()`
- `test_no_sql_injection_patterns()`
- `test_no_eval_usage()`
- `test_no_shell_injection()`
- `test_no_debug_code()`
- `test_no_hardcoded_urls()`
- `test_no_weak_crypto()`

#### Fonctions

##### test_no_hardcoded_passwords

Test qu'il n'y a pas de mots de passe hardcodés

##### test_no_sql_injection_patterns

Test qu'il n'y a pas de patterns d'injection SQL

##### test_no_eval_usage

Test qu'il n'y a pas d'utilisation de fonctions dangereuses

##### test_no_shell_injection

Test qu'il n'y a pas d'injection shell

##### test_no_debug_code

Test qu'il n'y a pas de code de debug

##### test_no_hardcoded_urls

Vérifie qu'il n'y a pas d'URLs hardcodées

##### test_no_weak_crypto

Vérifie qu'il n'y a pas de crypto faible

---

### test_unified

#### Fonctions

##### run_command

Exécute une commande et affiche le résultat

**Paramètres :**

- `cmd`
- `description`

##### test_unified_version

Test complet de la version unifiée

##### test_modules_availability

Test de la disponibilité des modules

##### main

Fonction principale

---

### test_unified_orchestrator

🧪 TESTS POUR L'ORCHESTRATEUR UNIFIÉ
====================================
Tests complets pour l'orchestrateur unifié Athalia.

#### Classes

##### TestUnifiedOrchestrator

Tests pour l'orchestrateur unifié

**Méthodes :**

- `setUp()`
- `tearDown()`
- `create_test_project()`
- `test_unified_orchestrator_import()`
- `test_unified_orchestrator_initialization()`
- `test_unified_orchestrator_config()`
- `test_unified_orchestrator_basic_orchestration()`
- `test_unified_orchestrator_insights()`
- `test_intelligent_analyzer_integration()`

##### TestUnifiedOrchestratorIntegration

Tests d'intégration pour l'orchestrateur unifié

**Méthodes :**

- `test_orchestrator_availability()`

#### Fonctions

##### main

Exécuter tous les tests

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### create_test_project

Créer un projet de test

##### test_unified_orchestrator_import

Test de l'import de l'orchestrateur unifié

##### test_unified_orchestrator_initialization

Test de l'initialisation de l'orchestrateur unifié

##### test_unified_orchestrator_config

Test de la configuration de l'orchestrateur

##### test_unified_orchestrator_basic_orchestration

Test d'orchestration basique

##### test_unified_orchestrator_insights

Test des insights d'orchestration

##### test_intelligent_analyzer_integration

Test de l'intégration avec l'analyseur intelligent

##### test_orchestrator_availability

Test de la disponibilité de l'orchestrateur unifié

---

### test_ath_audit

#### Fonctions

##### test_ath_audit_runs

---

### test_ath_build

#### Fonctions

##### test_ath_build_runs

---

### test_ath_coverage

#### Fonctions

##### cleanup_coverage_files

##### test_ath_coverage_runs

Test désactivé car il cause une récursivité infinie

---

### test_ath_lint

#### Fonctions

##### test_ath_lint_runs

---

### test_ath_test

#### Fonctions

##### test_ath_test_runs

Test désactivé car il cause une récursivité infinie

---

### test_cli_robustesse

Test d'intégration CLI robuste pour Athalia

#### Fonctions

##### test_cli_robustesse

Test simple de la CLI sans interaction complexe

---

### test_end_to_end

Test d'intégration end-to-end pour la génération de projet Athalia

#### Fonctions

##### test_generation_end_to_end

Génère un projet artistique complet et vérifie tous les artefacts essentiels.
Rend le test plus robuste pour la CI : skip si dépendances manquantes.

**Paramètres :**

- `tmp_path`

---

### test_yaml_validity

Test de validité YAML pour tous les fichiers openapi.yaml du repo

#### Fonctions

##### test_all_openapi_yaml_valid

Vérifie que tous les fichiers openapi*.yaml sont valides.

---

### test_reachy_auditor

Tests pour ReachyAuditor
========================

Tests unitaires et d'intégration pour l'auditeur spécialisé Reachy

#### Classes

##### TestReachyAuditor

Tests pour ReachyAuditor

**Méthodes :**

- `setup_method()`
- `teardown_method()`
- `test_init()`
- `test_audit_empty_project()`
- `test_audit_ros2_workspace()`
- `test_audit_docker_setup()`
- `test_audit_rust_projects()`
- `test_audit_complete_project()`
- `test_generate_report()`
- `test_save_report()`
- `_create_complete_project()`
- `test_audit_docker_parse_error()`
- `test_audit_missing_dependencies()`

##### TestReachyAuditResult

Tests pour ReachyAuditResult

**Méthodes :**

- `test_dataclass_creation()`

#### Fonctions

##### setup_method

Setup pour chaque test

##### teardown_method

Cleanup après chaque test

##### test_init

Test initialisation

##### test_audit_empty_project

Test audit projet vide

##### test_audit_ros2_workspace

Test audit workspace ROS2 valide

##### test_audit_docker_setup

Test audit setup Docker

##### test_audit_rust_projects

Test audit projets Rust

##### test_audit_complete_project

Test audit projet complet

##### test_generate_report

Test génération rapport

##### test_save_report

Test sauvegarde rapport

##### _create_complete_project

Créer un projet complet pour les tests

##### test_audit_docker_parse_error

Test gestion erreur parsing Docker

**Paramètres :**

- `mock_yaml_load`

##### test_audit_missing_dependencies

Test audit dépendances manquantes

##### test_dataclass_creation

Test création dataclass

---

### main

Auto - docstring ajoutée

---

### ath_context_prompt

#### Fonctions

##### score_prompt

**Paramètres :**

- `prompt`
- `filename`
- `content`

##### detect_prompts_scoring

**Paramètres :**

- `filepath`

##### detect_prompt_semantic

**Paramètres :**

- `filepath`

##### show_prompts

**Paramètres :**

- `scored`
- `semantic_prompt`

##### main

---

### main

Module ai_player pour VioletTwistAI.

#### Classes

##### AIPlayerManager

Gestionnaire pour le module ai_player.

**Méthodes :**

- `__init__()`
- `process()`

#### Fonctions

##### main

Test du module ai_player.

##### __init__

##### process

Traite les données.

**Paramètres :**

- `data`

---

### test_booster_ia_VioletTwistAI

#### Fonctions

##### test_prompts_presence

##### test_ath_dev_boost

##### test_ath_context_prompt

##### test_alias_sh

---

### main

Module violette_game pour VioletTwistAI.

#### Classes

##### VioletteGameManager

Gestionnaire pour le module violette_game.

**Méthodes :**

- `__init__()`
- `process()`

#### Fonctions

##### main

Test du module violette_game.

##### __init__

##### process

Traite les données.

**Paramètres :**

- `data`

---

### demo_system_intelligent

🎯 DÉMONSTRATION DU SYSTÈME INTELLIGENT ATHALIA
===============================================
Script de démonstration pour montrer toutes les capacités du système.

#### Fonctions

##### demo_level_1_analysis

Démonstration du niveau 1 - Analyse intelligente

##### demo_level_2_orchestration

Démonstration du niveau 2 - Orchestration

##### demo_level_3_coordination

Démonstration du niveau 3 - Coordination globale

##### demo_integration

Démonstration de l'intégration

##### main

Démonstration complète du système

---

### test_all_orchestrators

🎯 TEST COMPLET DES 3 NIVEAUX D'ORCHESTRATION
=============================================
Test pour vérifier que tous les niveaux d'orchestration fonctionnent.

#### Fonctions

##### test_level_1_analyzer

Test du niveau 1 - Intelligent Analyzer

##### test_level_2_orchestrator

Test du niveau 2 - Intelligent Orchestrator

##### test_level_3_coordinator

Test du niveau 3 - Intelligent Coordinator

##### test_integration

Test d'intégration des 3 niveaux

##### main

Test complet des 3 niveaux d'orchestration

---

### test_final_validation

🎯 TEST FINAL DE VALIDATION DU SYSTÈME INTELLIGENT
==================================================
Test final pour valider que tous les modules fonctionnent correctement.

#### Fonctions

##### test_ast_analyzer

Test de l'analyseur AST

##### test_pattern_detector

Test du détecteur de patterns

##### test_architecture_analyzer

Test de l'analyseur d'architecture

##### test_performance_analyzer

Test de l'analyseur de performance

##### test_intelligent_analyzer

Test de l'analyseur intelligent principal

##### main

Exécuter tous les tests de validation

---

### test_quick_validation

⚡ TEST RAPIDE DE VALIDATION DU SYSTÈME INTELLIGENT
==================================================
Test rapide pour valider que le système d'analyse intelligente fonctionne.

#### Fonctions

##### main

Test rapide du système complet

---

### main

---

### ath_context_prompt

---

### main

Module connectivity pour EmotionSensingRoboticEyes.

#### Classes

##### ConnectivityManager

Gestionnaire pour le module connectivity.

**Méthodes :**

- `__init__()`
- `process()`

#### Fonctions

##### main

Test du module connectivity.

##### __init__

##### process

Traite les données.

**Paramètres :**

- `data`

---

### main

Module emotion_detection pour EmotionSensingRoboticEyes.

#### Classes

##### EmotionDetectionManager

Gestionnaire pour le module emotion_detection.

**Méthodes :**

- `__init__()`
- `process()`

#### Fonctions

##### main

Test du module emotion_detection.

##### __init__

##### process

Traite les données.

**Paramètres :**

- `data`

---

### main

Module motion_control pour EmotionSensingRoboticEyes.

#### Classes

##### MotionControlManager

Gestionnaire pour le module motion_control.

**Méthodes :**

- `__init__()`
- `process()`

#### Fonctions

##### main

Test du module motion_control.

##### __init__

##### process

Traite les données.

**Paramètres :**

- `data`

---

### test_booster_ia_mon-projet

#### Fonctions

##### test_prompts_presence

##### test_ath_dev_boost

##### test_ath_context_prompt

##### test_alias_sh

---

### benchmark_qwen_mistral

Script de benchmark Qwen/Mistral/Mock pour Athalia/Arkalia

Usage :
    python benchmark_qwen_mistral.py

- Compare Qwen, Mistral, Mock sur 10 prompts types
- Mesure temps de réponse, score qualité (heuristique), mémoire
- Résultats exportés en CSV et Markdown

#### Fonctions

##### call_qwen

**Paramètres :**

- `prompt`

##### call_mistral

**Paramètres :**

- `prompt`

##### call_mock

**Paramètres :**

- `prompt`

##### quality_score

**Paramètres :**

- `output`

---

### main

---

### main

#### Classes

##### FlowerAnimation

**Méthodes :**

- `__init__()`

#### Fonctions

##### __init__

---

### voice_assistant

Système d'IA conversationnel multilingue avec reconnaissance vocale et synthèse vocale
Version ultra-performante avec benchmarks automatiques

#### Classes

##### VoiceConfig

Configuration pour la reconnaissance et synthèse vocale

##### ConversationContext

Contexte de conversation

##### MultilingualVoiceAssistant

Assistant vocal multilingue ultra-performant

**Méthodes :**

- `__init__()`
- `_initialize_models()`
- `_update_performance_metrics()`
- `get_performance_report()`
- `cleanup()`

##### VoiceAssistantInterface

Interface principale pour l'assistant vocal

**Méthodes :**

- `__init__()`
- `get_performance_report()`

#### Fonctions

##### __init__

**Paramètres :**

- `config`

##### _initialize_models

Initialise les modèles de langage et moteurs vocaux

##### _update_performance_metrics

Met à jour les métriques de performance

**Paramètres :**

- `response_time`
- `success`

##### get_performance_report

Génère un rapport de performance

##### cleanup

Nettoie les ressources

##### __init__

##### get_performance_report

Obtient le rapport de performance

---

### benchmark_suite

Suite de benchmarks pour l'assistant vocal multilingue
Tests de performance, charge, et robustesse

#### Classes

##### BenchmarkSuite

Suite complète de benchmarks pour l'assistant vocal

**Méthodes :**

- `__init__()`
- `_generate_test_data()`
- `_generate_final_report()`
- `_generate_recommendations()`
- `save_report()`

#### Fonctions

##### __init__

##### _generate_test_data

Génère des données de test

##### _generate_final_report

Génère le rapport final des benchmarks

##### _generate_recommendations

Génère des recommandations basées sur les résultats

##### save_report

Sauvegarde le rapport dans un fichier

**Paramètres :**

- `filename`

---

### test_intelligent_simple

🧪 TEST TRÈS SIMPLE DES MODULES INTELLIGENTS
============================================
Test rapide pour vérifier que les modules de base fonctionnent.

#### Fonctions

##### test_ast_analyzer

Test simple de l'analyseur AST

##### test_pattern_detector

Test simple du détecteur de patterns

##### test_architecture_analyzer

Test simple de l'analyseur d'architecture

##### test_performance_analyzer

Test simple de l'analyseur de performance

##### main

Exécuter tous les tests simples

---

### test_intelligent_system_simple

🧪 TEST SIMPLE DU SYSTÈME D'ANALYSE INTELLIGENTE
================================================
Test simple pour vérifier que tous les modules fonctionnent ensemble.

#### Fonctions

##### test_simple_analysis

Test simple de l'analyse intelligente

---

### test_intelligent_system

🧠 TEST DU SYSTÈME INTELLIGENT ATHALIA
=======================================
Test complet du système intelligent qui :
- Valide l'analyseur intelligent
- Valide la mémoire intelligente
- Valide l'orchestrateur intelligent
- Teste l'intégration complète

#### Fonctions

##### test_intelligent_analyzer

Tester l'analyseur intelligent

##### test_intelligent_memory

Tester la mémoire intelligente

##### test_intelligent_orchestrator

Tester l'orchestrateur intelligent

##### test_integration

Tester l'intégration complète

##### main

Fonction principale de test

---

### audit

Module d'audit intelligent pour analyser la qualité des projets générés.
Analyse le code, détecte la dette technique, et propose des améliorations.

#### Classes

##### ProjectAuditor

Auditeur intelligent de projets générés.

**Méthodes :**

- `__init__()`
- `audit_project()`
- `_analyze_structure()`
- `_analyze_code_quality()`
- `_analyze_python_file()`
- `_analyze_tests()`
- `_analyze_documentation()`
- `_analyze_security()`
- `_analyze_performance()`
- `_calculate_score()`
- `_generate_report()`
- `_find_modules()`

#### Fonctions

##### audit_project_intelligent

Fonction principale pour l'audit intelligent.

**Paramètres :**

- `project_path`

##### generate_audit_report

**Paramètres :**

- `project_path`

##### __init__

**Paramètres :**

- `project_path`

##### audit_project

Audit complet du projet.

##### _analyze_structure

Analyse la structure du projet.

##### _analyze_code_quality

Analyse la qualité du code Python.

##### _analyze_python_file

Analyse un fichier Python avec AST.

**Paramètres :**

- `tree`
- `content`

##### _analyze_tests

Analyse la couverture de tests.

##### _analyze_documentation

Analyse la documentation.

##### _analyze_security

Analyse la sécurité.

##### _analyze_performance

Analyse la performance.

##### _calculate_score

Calcule le score global du projet.

##### _generate_report

Génère le rapport d'audit.

##### _find_modules

Trouve les modules Python dans le projet.

---

### network_agent

#### Classes

##### AuditAgent

**Méthodes :**

- `act()`

##### CorrectionAgent

**Méthodes :**

- `act()`

##### SynthesisAgent

**Méthodes :**

- `act()`

#### Fonctions

##### act

**Paramètres :**

- `prompt`

##### act

**Paramètres :**

- `prompt`

##### act

**Paramètres :**

- `prompt`
- `responses`

---

### qwen_agent

Agent AutoGen pour Qwen 7B (prototype)

#### Classes

##### QwenAgent

**Méthodes :**

- `act()`

#### Fonctions

##### act

**Paramètres :**

- `prompt`

---

### athalia_orchestrator

#### Classes

##### AthaliaOrchestrator

**Méthodes :**

- `__init__()`
- `industrialize_project()`
- `_run_robotics_audit()`
- `_run_audit()`
- `_run_cleanup()`
- `_run_documentation()`
- `_run_testing()`
- `_run_cicd()`
- `_generate_final_report()`
- `_convert_dataclasses_to_dict()`
- `_save_report()`
- `scan_projects()`
- `_is_project()`
- `_detect_project_type()`
- `_get_project_size()`
- `_add_quality_badge()`
- `_add_security_badge()`
- `distill_ia_responses()`
- `distill_audits()`
- `distill_corrections()`
- `distill_adaptive_responses()`
- `distill_genetics()`
- `cache_predictive()`

#### Fonctions

##### main

Point d'entrée du programme

##### __init__

##### industrialize_project

Industrialisation complète d'un projet

**Paramètres :**

- `project_path`
- `config`

##### _run_robotics_audit

Exécute l'audit robotique spécialisé

##### _run_audit

Exécute l'audit intelligent

##### _run_cleanup

Exécute le nettoyage

##### _run_documentation

Exécute la génération de documentation

##### _run_testing

Exécute la génération de tests

##### _run_cicd

Exécute la configuration CI / CD

##### _generate_final_report

Génère le rapport final d'industrialisation Athalia.

**Paramètres :**

- `results`

##### _convert_dataclasses_to_dict

Convertit les dataclasses en dictionnaires pour la sérialisation JSON

**Paramètres :**

- `obj`

##### _save_report

Sauvegarde le fichier de rapport

**Paramètres :**

- `results`

##### scan_projects

Scan les projets et ajoute la clé 'path' à chaque projet.

**Paramètres :**

- `base_dir`

##### _is_project

Détermine si un répertoire est un projet

**Paramètres :**

- `path`

##### _detect_project_type

Détecte le type de projet

**Paramètres :**

- `path`

##### _get_project_size

Calcule la taille du projet

**Paramètres :**

- `path`

##### _add_quality_badge

Ajoute un badge de qualité dans le README du projet

**Paramètres :**

- `score`

##### _add_security_badge

Ajoute un badge de sécurité dans le README du projet

**Paramètres :**

- `score`

##### distill_ia_responses

Interroge Qwen, Mistral, Mock (via RobustAI), distille les réponses et retourne la meilleure.

**Paramètres :**

- `prompt`
- `models`
- `strategy`

##### distill_audits

Fusionne plusieurs audits en un score global distillé.

**Paramètres :**

- `audits`

##### distill_corrections

Sélectionne la meilleure correction parmi plusieurs suggestions IA.

**Paramètres :**

- `corrections`
- `scores`

##### distill_adaptive_responses

Fusionne plusieurs réponses IA de façon adaptative.

**Paramètres :**

- `responses`

##### distill_genetics

**Paramètres :**

- `solutions`

##### cache_predictive

**Paramètres :**

- `key`
- `value`

---

### intelligent_orchestrator

🎯 ORCHESTRATEUR INTELLIGENT ATHALIA
====================================
Orchestrateur qui :
- Intègre l'analyseur intelligent et la mémoire
- Coordonne tous les modules avec apprentissage
- Prédit et prévient les problèmes
- Optimise automatiquement le code
- Apprend de chaque action pour s'améliorer

#### Classes

##### OrchestrationTask

Tâche d'orchestration

##### IntelligentInsight

Insight intelligent

##### IntelligentOrchestrator

Orchestrateur intelligent pour Athalia

**Méthodes :**

- `__init__()`
- `_init_database()`
- `orchestrate_project()`
- `predict_project_issues()`
- `suggest_optimizations()`
- `get_orchestration_insights()`
- `_create_task()`
- `_execute_analysis()`
- `_learn_from_analysis()`
- `_generate_predictions()`
- `_generate_optimizations()`
- `_save_insight()`
- `_save_orchestration_results()`
- `_generate_orchestration_report()`

#### Fonctions

##### main

Test de l'orchestrateur intelligent

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données d'orchestration

##### orchestrate_project

Orchestrer l'analyse complète d'un projet

**Paramètres :**

- `project_path`
- `include_predictions`
- `include_optimizations`

##### predict_project_issues

Prédire les problèmes potentiels d'un projet

**Paramètres :**

- `project_path`

##### suggest_optimizations

Suggérer des optimisations pour un projet

**Paramètres :**

- `project_path`

##### get_orchestration_insights

Obtenir des insights d'orchestration

##### _create_task

Créer une nouvelle tâche d'orchestration

**Paramètres :**

- `task_type`
- `target_path`
- `priority`

##### _execute_analysis

Exécuter l'analyse intelligente

**Paramètres :**

- `project_path`

##### _learn_from_analysis

Apprendre des résultats d'analyse

**Paramètres :**

- `analysis_result`

##### _generate_predictions

Générer des prédictions intelligentes

**Paramètres :**

- `project_path`

##### _generate_optimizations

Générer des optimisations intelligentes

**Paramètres :**

- `project_path`

##### _save_insight

Sauvegarder un insight intelligent

**Paramètres :**

- `insight`

##### _save_orchestration_results

Sauvegarder les résultats d'orchestration

**Paramètres :**

- `results`

##### _generate_orchestration_report

Générer un rapport d'orchestration

**Paramètres :**

- `results`

---

### benchmark_qwen_mistral

Script de benchmark Qwen/Mistral/Mock pour Athalia/Arkalia

Usage :
    python benchmark_qwen_mistral.py

- Compare Qwen, Mistral, Mock sur 10 prompts types
- Mesure temps de réponse, score qualité (heuristique), mémoire
- Résultats exportés en CSV et Markdown

#### Fonctions

##### call_qwen

**Paramètres :**

- `prompt`

##### call_mistral

**Paramètres :**

- `prompt`

##### call_mock

**Paramètres :**

- `prompt`

##### quality_score

**Paramètres :**

- `output`

---

### advanced_analytics

#### Classes

##### AdvancedAnalytics

**Méthodes :**

- `__init__()`
- `run()`
- `_analyze_complexity()`
- `_calculate_complexity()`
- `_analyze_coverage()`
- `_analyze_performance()`
- `_analyze_quality()`
- `_analyze_evolution()`
- `_generate_dashboard()`
- `_generate_summary()`
- `print_report()`

#### Fonctions

##### enrich_genesis_md

**Paramètres :**

- `outdir`
- `infos`
- `perf_log`
- `test_log`

##### __init__

**Paramètres :**

- `project_path`

##### run

Lance l'analyse complète du projet

##### _analyze_complexity

Analyse la complexité du projet

##### _calculate_complexity

Calcule la complexité cyclomatique d'un fichier

**Paramètres :**

- `tree`

##### _analyze_coverage

Analyse la couverture du projet

##### _analyze_performance

Analyse les métriques de performance du projet

##### _analyze_quality

Analyse la qualité du projet

##### _analyze_evolution

Analyse l'évolution du projet

##### _generate_dashboard

Génère un dashboard HTML

##### _generate_summary

Génère un résumé des métriques

##### print_report

Affiche le rapport d'analyse

---

### ai_robust

Module IA robuste pour Athalia
Gestion des modèles IA avec fallback intelligent

#### Classes

##### AIModel

Modèles IA disponibles.

##### PromptContext

Contextes de prompts.

##### RobustAI

Gestionnaire IA robuste avec fallback intelligent.

**Méthodes :**

- `__init__()`
- `generate_blueprint()`
- `review_code()`
- `generate_documentation()`
- `classify_project_complexity()`
- `get_dynamic_prompt()`
- `generate_bluelogger()`
- `generate_blueprint_mock()`
- `save_blueprint()`
- `scan_existing_project()`
- `_detect_available_models()`
- `_build_fallback_chain()`
- `_load_prompt_templates()`
- `generate_response()`
- `_call_model()`
- `_classify_project_complexity()`
- `_get_dynamic_prompt()`
- `_call_ollama()`
- `_mock_response()`

##### _BlueprintProxy

**Méthodes :**

- `__init__()`
- `info()`

#### Fonctions

##### robust_ai

Fonction factory pour créer une instance RobustAI.

##### fallback_ia

Fallback IA multi-modèles (Qwen, Mistral, Ollama, Claude, GPT, Mock...)

**Paramètres :**

- `prompt`
- `models`

##### query_qwen

Appel local à Qwen 7B via Ollama.

**Paramètres :**

- `prompt`

##### query_mistral

Appel local à Mistral Small via Ollama.

**Paramètres :**

- `prompt`

##### __init__

Initialise le gestionnaire IA.

##### generate_blueprint

Génère un blueprint de projet à partir d'une idée.

**Paramètres :**

- `idea`

##### review_code

Fait une revue de code et retourne un rapport mocké.

**Paramètres :**

- `code`
- `filename`
- `project_type`
- `current_score`

##### generate_documentation

Génère une documentation technique mockée.

**Paramètres :**

- `project_name`
- `project_type`
- `modules`

##### classify_project_complexity

Classifie la complexité d'un projet (mock).

**Paramètres :**

- `codebase_path`

##### get_dynamic_prompt

Retourne un prompt dynamique mocké selon le contexte.

**Paramètres :**

- `context`

##### generate_bluelogger

##### generate_blueprint_mock

##### save_blueprint

##### scan_existing_project

##### _detect_available_models

Détecte les modèles IA disponibles.

##### _build_fallback_chain

Construit la chaîne de fallback.

##### _load_prompt_templates

Charge les templates de prompts dynamiques.

##### generate_response

Gère la génération de réponse IA avec fallback ou distillation.
Si distillation=True, interroge tous les modèles et agrège les réponses.
Retourne un dict: {model: réponse, ..., 'distilled': ...}

**Paramètres :**

- `context`
- `distillation`

##### _call_model

**Paramètres :**

- `model`
- `prompt`

##### _classify_project_complexity

Alias privé pour compatibilité avec les tests. Retourne un dict de complexité.

**Paramètres :**

- `codebase_path`

##### _get_dynamic_prompt

Alias privé pour compatibilité avec les tests. Accepte PromptContext ou str et fait un .format sur le template.

**Paramètres :**

- `context`

##### _call_ollama

Appelle Ollama avec un modèle spécifique et timeout paramétrable.

**Paramètres :**

- `model_name`
- `prompt`
- `timeout`

##### _mock_response

Réponse mock pour les tests.

**Paramètres :**

- `prompt`

##### __init__

**Paramètres :**

- `parent`

##### info

---

### analytics

#### Fonctions

##### generate_heatmap_data

Génère les données pour une heatmap des scores d'audit.

**Paramètres :**

- `projects_info`

##### generate_technical_debt_analysis

Analyse la dette technique globale.

**Paramètres :**

- `projects_info`

##### generate_analytics_html

Génère le HTML pour les analytics avancés.

**Paramètres :**

- `projects_info`

##### save_analytics

Sauvegarde les analytics dans un fichier HTML.

**Paramètres :**

- `projects_info`
- `output_file`

##### analyze_project

Analyse un projet et retourne des métriques clés.

**Paramètres :**

- `project_path`

---

### architecture_analyzer

🏗️ ANALYSEUR D'ARCHITECTURE
============================
Module d'analyse d'architecture pour comprendre la structure
du projet, les dépendances et les relations entre modules.

#### Classes

##### ModuleAnalysis

Analyse d'un module

##### PerformanceIssue

Problème de performance

##### ArchitectureMapping

Mapping de l'architecture complète

##### ArchitectureAnalyzer

Analyseur d'architecture pour comprendre la structure du projet

**Méthodes :**

- `__init__()`
- `_init_database()`
- `_load_config()`
- `analyze_entire_architecture()`
- `_analyze_all_modules()`
- `_analyze_single_module()`
- `_extract_dependencies()`
- `_detect_module_issues()`
- `_calculate_performance_score()`
- `_detect_duplicates()`
- `_analyze_performance()`
- `_build_dependency_graph()`
- `_generate_recommendations()`
- `_save_architecture_analysis()`
- `get_optimization_plan()`
- `generate_intelligent_coordination()`

#### Fonctions

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données d'architecture

##### _load_config

Charger la configuration

##### analyze_entire_architecture

Analyser l'architecture complète du projet

##### _analyze_all_modules

Analyser tous les modules du projet

##### _analyze_single_module

Analyser un module individuel

**Paramètres :**

- `file_path`
- `module_type`

##### _extract_dependencies

Extraire les dépendances d'un module

**Paramètres :**

- `imports`
- `module_type`

##### _detect_module_issues

Détecter les problèmes dans un module

**Paramètres :**

- `file_analysis`

##### _calculate_performance_score

Calculer un score de performance pour un module

**Paramètres :**

- `file_analysis`

##### _detect_duplicates

Détecter les doublons entre modules

**Paramètres :**

- `modules`

##### _analyze_performance

Analyser les problèmes de performance

**Paramètres :**

- `modules`

##### _build_dependency_graph

Construire le graphe de dépendances

**Paramètres :**

- `modules`

##### _generate_recommendations

Générer des recommandations d'architecture

**Paramètres :**

- `modules`
- `duplicates`
- `performance_issues`

##### _save_architecture_analysis

Sauvegarder l'analyse d'architecture

**Paramètres :**

- `architecture`

##### get_optimization_plan

Obtenir un plan d'optimisation basé sur l'analyse

##### generate_intelligent_coordination

Générer des recommandations de coordination intelligente

---

### ast_analyzer

🔍 ANALYSEUR AST DE BASE
========================
Module d'analyse AST pour extraire les informations de base
des fichiers Python. Utilisé par les autres modules d'analyse.

#### Classes

##### ASTNodeInfo

Informations extraites d'un nœud AST

##### FileAnalysis

Analyse complète d'un fichier Python

##### ASTAnalyzer

Analyseur AST de base pour extraire les informations structurelles

**Méthodes :**

- `__init__()`
- `analyze_file()`
- `_extract_functions()`
- `_extract_classes()`
- `_extract_conditionals()`
- `_extract_loops()`
- `_extract_imports()`
- `_create_function_signature()`
- `_create_class_signature()`
- `_create_conditional_signature()`
- `_create_loop_signature()`
- `_extract_node_content()`
- `_normalize_code()`
- `_calculate_node_complexity()`
- `_calculate_complexity()`

#### Fonctions

##### __init__

##### analyze_file

Analyser un fichier Python et extraire toutes les informations

**Paramètres :**

- `file_path`

##### _extract_functions

Extraire toutes les fonctions du fichier

**Paramètres :**

- `tree`
- `content`
- `file_path`

##### _extract_classes

Extraire toutes les classes du fichier

**Paramètres :**

- `tree`
- `content`
- `file_path`

##### _extract_conditionals

Extraire toutes les structures conditionnelles

**Paramètres :**

- `tree`
- `content`
- `file_path`

##### _extract_loops

Extraire toutes les boucles

**Paramètres :**

- `tree`
- `content`
- `file_path`

##### _extract_imports

Extraire tous les imports

**Paramètres :**

- `tree`

##### _create_function_signature

Créer une signature unique pour une fonction

**Paramètres :**

- `node`
- `code`

##### _create_class_signature

Créer une signature unique pour une classe

**Paramètres :**

- `node`
- `code`

##### _create_conditional_signature

Créer une signature unique pour une condition

**Paramètres :**

- `node`
- `code`

##### _create_loop_signature

Créer une signature unique pour une boucle

**Paramètres :**

- `node`
- `code`

##### _extract_node_content

Extraire le contenu d'un nœud AST

**Paramètres :**

- `node`
- `code`

##### _normalize_code

Normaliser le code pour la comparaison

**Paramètres :**

- `code`

##### _calculate_node_complexity

Calculer la complexité cyclomatique d'un nœud

**Paramètres :**

- `node`

##### _calculate_complexity

Calculer la complexité globale d'un arbre AST

**Paramètres :**

- `tree`

---

### audit

Fichier de compatibilité pour l'audit
Redirige vers intelligent_auditor.py pour maintenir la compatibilité

#### Classes

##### ProjectAuditor

Alias pour compatibilité avec l'ancien audit.py

**Méthodes :**

- `__init__()`
- `audit_project()`

##### Audit

Alias pour compatibilité avec les tests

**Méthodes :**

- `__init__()`
- `audit_project()`

#### Fonctions

##### audit_project_intelligent

Fonction de compatibilité pour audit_project_intelligent

**Paramètres :**

- `project_path`

##### generate_audit_report

Fonction de compatibilité pour generate_audit_report

**Paramètres :**

- `project_path`

##### __init__

**Paramètres :**

- `project_path`

##### audit_project

Méthode de compatibilité

##### __init__

**Paramètres :**

- `project_path`

##### audit_project

Méthode de compatibilité

---

### auto_cicd

#### Classes

##### AutoCICD

Générateur de CI / CD

**Méthodes :**

- `__init__()`
- `setup_cicd()`
- `_analyze_project()`
- `_detect_project_type()`
- `_detect_languages()`
- `_extract_dependencies()`
- `_find_entry_points()`
- `_has_tests()`
- `_has_documentation()`
- `_generate_github_actions()`
- `_generate_docker_config()`
- `_generate_deployment_config()`
- `_save_cicd_configs()`
- `_get_created_files()`

#### Fonctions

##### generate_github_ci_yaml

**Paramètres :**

- `outdir`

##### __init__

##### setup_cicd

Configuration complète CI / CD pour un projet

**Paramètres :**

- `project_path`

##### _analyze_project

Analyse du projet pour la CI/CD

##### _detect_project_type

Détection du type de projet

##### _detect_languages

Détection des langages du projet

##### _extract_dependencies

Extraction des dépendances du projet

##### _find_entry_points

Trouve les points d'entrée du projet

##### _has_tests

Vérifie si le projet a des tests

##### _has_documentation

Vérifie si le projet a de la documentation

##### _generate_github_actions

Génère les workflows GitHub Actions

##### _generate_docker_config

Génère la configuration Docker

##### _generate_deployment_config

Génère la configuration de déploiement

##### _save_cicd_configs

**Paramètres :**

- `github_actions`
- `docker_config`
- `deployment_config`

##### _get_created_files

---

### auto_cleaner

#### Classes

##### AutoCleaner

Nettoyeur automatique pour Athalia

**Méthodes :**

- `__init__()`
- `clean_project()`
- `run()`
- `_clean_system_files()`
- `_clean_cache_files()`
- `_clean_backup_files()`
- `_clean_temp_files()`
- `_clean_duplicate_files()`
- `_clean_empty_directories()`
- `_clean_old_files()`
- `_clean_large_files()`
- `_safe_remove_file()`
- `_safe_remove_dir()`
- `_is_code_file()`
- `_is_important_file()`
- `_is_empty_directory()`
- `_calculate_file_hash()`
- `_generate_cleanup_report()`
- `_generate_summary()`
- `optimize_project_structure()`
- `_organize_files()`

#### Fonctions

##### main

Point d'entrée du module AutoCleaner

##### __init__

**Paramètres :**

- `project_path`

##### clean_project

Nettoyage complet d'un projet

**Paramètres :**

- `dry_run`

##### run

Méthode run() pour l'orchestrateur - exécute le nettoyage

##### _clean_system_files

Nettoyage des fichiers système

**Paramètres :**

- `project_path`

##### _clean_cache_files

Nettoyage des fichiers de cache

**Paramètres :**

- `project_path`

##### _clean_backup_files

Nettoyage des fichiers de sauvegarde

**Paramètres :**

- `project_path`

##### _clean_temp_files

Nettoyage des fichiers temporaires

**Paramètres :**

- `project_path`

##### _clean_duplicate_files

Nettoyage des fichiers dupliqués

**Paramètres :**

- `project_path`

##### _clean_empty_directories

Nettoyage des répertoires vides

**Paramètres :**

- `project_path`

##### _clean_old_files

Nettoyage des fichiers anciens

**Paramètres :**

- `project_path`

##### _clean_large_files

Nettoyage des fichiers volumineux

**Paramètres :**

- `project_path`

##### _safe_remove_file

Suppression sécurisée d'un fichier

**Paramètres :**

- `file_path`
- `reason`

##### _safe_remove_dir

Suppression sécurisée d'un répertoire

**Paramètres :**

- `dir_path`
- `reason`

##### _is_code_file

Détermine si un fichier est un fichier de code

**Paramètres :**

- `file_path`

##### _is_important_file

Détermine si un fichier est important (ex: config, requirements, etc.)

**Paramètres :**

- `file_path`

##### _is_empty_directory

Vérifie si un répertoire est vide

**Paramètres :**

- `dir_path`

##### _calculate_file_hash

Calcule le hash d'un fichier

**Paramètres :**

- `file_path`

##### _generate_cleanup_report

Génère le rapport de nettoyage

##### _generate_summary

Génère un résumé du nettoyage

##### optimize_project_structure

Optimise la structure du projet

**Paramètres :**

- `project_path`

##### _organize_files

Organise les fichiers dans la structure du projet

**Paramètres :**

- `project_path`
- `optimizations`

---

### auto_documenter

#### Classes

##### AutoDocumenter

Générateur de documentation automatique

**Méthodes :**

- `__init__()`
- `_load_translations()`
- `run()`
- `document_project()`
- `_analyze_project()`
- `_extract_description()`
- `_extract_version()`
- `_extract_author()`
- `_extract_license()`
- `_extract_dependencies()`
- `_find_entry_points()`
- `_analyze_modules()`
- `_analyze_classes()`
- `_analyze_functions()`
- `_generate_readme()`
- `_generate_api_documentation()`
- `_generate_setup_guide()`
- `_generate_usage_guide()`
- `_save_documents()`
- `_get_created_files()`

#### Fonctions

##### main

Point d'entrée du script

##### __init__

**Paramètres :**

- `project_path`
- `lang`

##### _load_translations

**Paramètres :**

- `lang`

##### run

Méthode run() pour l'orchestrateur - exécute la documentation

##### document_project

Documentation complète d'un projet

**Paramètres :**

- `project_path`

##### _analyze_project

Analyse du projet pour la documentation

##### _extract_description

Extrait la description du projet

##### _extract_version

Extrait la version du projet

##### _extract_author

Extrait l'auteur du projet

##### _extract_license

Extrait la licence du projet

##### _extract_dependencies

Extrait les dépendances du projet

##### _find_entry_points

Trouve les points d'entrée du projet

##### _analyze_modules

Analyse les modules du projet

##### _analyze_classes

Analyse les classes du projet

**Paramètres :**

- `modules`

##### _analyze_functions

Analyse les fonctions du projet

**Paramètres :**

- `modules`

##### _generate_readme

Génère le README du projet

##### _generate_api_documentation

Génère la documentation API du projet

##### _generate_setup_guide

Génère le guide d'installation du projet

##### _generate_usage_guide

Génère le guide d'utilisation du projet

##### _save_documents

Sauvegarde les documents générés

**Paramètres :**

- `readme`
- `api_docs`
- `setup_guide`
- `usage_guide`

##### _get_created_files

---

### auto_tester

#### Classes

##### AutoTester

Générateur de tests pour Athalia

**Méthodes :**

- `__init__()`
- `run()`
- `generate_tests()`
- `_analyze_modules()`
- `_generate_unit_tests()`
- `_generate_module_unit_tests()`
- `_generate_integration_tests()`
- `_generate_performance_tests()`
- `_save_tests()`
- `_run_tests()`
- `_get_created_files()`
- `generate_test_report()`

#### Fonctions

##### main

Point dentrée f

##### __init__

**Paramètres :**

- `project_path`

##### run

Méthode run() pour l'orchestrateur - exécute les tests

##### generate_tests

Génération complète de tests pour un projet

**Paramètres :**

- `project_path`

##### _analyze_modules

Analyse les modules Python du projet

##### _generate_unit_tests

Génère les tests f

**Paramètres :**

- `modules`

##### _generate_module_unit_tests

Génère les tests unitaires pour un f

**Paramètres :**

- `module`

##### _generate_integration_tests

Génère les tests df

**Paramètres :**

- `modules`

##### _generate_performance_tests

Génère les tests de f

**Paramètres :**

- `modules`

##### _save_tests

Sauvegarde les tests f

**Paramètres :**

- `unit_tests`
- `integration_tests`
- `performance_tests`

##### _run_tests

Exécute les tests générés et collecte les résultats

##### _get_created_files

Retourne la liste des fichiers créés

##### generate_test_report

Génère un rapport de tests

---

### autocomplete_engine

#### Classes

##### BaseAutocompleteEngine

**Méthodes :**

- `suggest()`

##### SimpleAutocompleteEngine

**Méthodes :**

- `suggest()`

##### OllamaAutocompleteEngine

**Méthodes :**

- `__init__()`
- `suggest()`

#### Fonctions

##### suggest

Retourne une liste de suggestions d'autocomplétion pour un prompt donné.

**Paramètres :**

- `prompt`
- `max_suggestions`

##### suggest

**Paramètres :**

- `prompt`
- `max_suggestions`

##### __init__

**Paramètres :**

- `model_name`
- `host`

##### suggest

**Paramètres :**

- `prompt`
- `max_suggestions`

---

### autocomplete_server

#### Classes

##### AutocompleteRequest

##### AutocompleteResponse

#### Fonctions

##### get_engine

##### autocomplete

**Paramètres :**

- `request`

---

### ci

#### Fonctions

##### generate_github_ci_yaml

**Paramètres :**

- `outdir`

##### add_coverage_badge

**Paramètres :**

- `outdir`

---

### cleanup

#### Fonctions

##### clean_old_tests_and_caches

Supprime les anciens fichiers de test non-suffixés et les caches Python dans le projet cible.
Log chaque suppression pour audit. Retourne la liste des fichiers supprimés.

**Paramètres :**

- `outdir`

##### clean_macos_files

Supprime automatiquement les fichiers macOS parasites (.DS_Store, ._*) dans tout le projet. Retourne la liste des fichiers supprimés.

**Paramètres :**

- `directory`

---

### cli

Interface CLI pour Athalia avec IA robuste.

#### Fonctions

##### cli

Athalia-Générateur de projets IA intelligent.

**Paramètres :**

- `verbose`

##### generate

Génère un projet complet à partir d'une idée.

**Paramètres :**

- `idea`
- `output`
- `dry_run`

##### audit

Audit intelligent d'un projet existant.

**Paramètres :**

- `project_path`

##### ai_status

Affiche le statut de l'IA robuste.

##### test_ai

Teste l'IA robuste avec une idée de projet.

**Paramètres :**

- `idea`

---

### code_linter

#### Classes

##### CodeLinter

Linter de code pour Athalia

**Méthodes :**

- `__init__()`
- `run()`
- `_run_flake8()`
- `_run_black()`
- `_run_isort()`
- `_run_mypy()`
- `_run_bandit()`
- `_calculate_score()`
- `print_report()`

#### Fonctions

##### __init__

**Paramètres :**

- `project_path`
- `auto_fix`

##### run

Lance l'analyse de qualité du projet

##### _run_flake8

Exécution de Flake8

##### _run_black

Exécution de Black

##### _run_isort

Exécution de isort

##### _run_mypy

Exécution de MyPy

##### _run_bandit

Exécution de Bandit pour la sécurité

##### _calculate_score

Calcul du score de qualité

##### print_report

Affichage du rapport de linting

---

### config_manager

#### Classes

##### AthaliaConfig

Configuration centralisée d'f

##### ConfigManager

Gestionnaire de configuration f

**Méthodes :**

- `__init__()`
- `_load_config()`
- `_merge_yaml_config()`
- `_merge_env_config()`
- `_setup_logging()`
- `get()`
- `is_module_enabled()`
- `get_enabled_plugins()`
- `get_available_templates()`
- `get_cleanup_patterns()`
- `to_dict()`

#### Fonctions

##### __init__

**Paramètres :**

- `config_file`

##### _load_config

Charge la configuration depuis le fichier YAML et les variables d'f

##### _merge_yaml_config

Fusionne la configuration YAML avec la config par f

**Paramètres :**

- `config`
- `yaml_data`

##### _merge_env_config

Surcharge la configuration avec les variables d'f

**Paramètres :**

- `config`

##### _setup_logging

Configure le logging selon la f

##### get

Récupère une valeur de f

**Paramètres :**

- `key`
- `default`

##### is_module_enabled

Vérifie si un module est f

**Paramètres :**

- `module_name`

##### get_enabled_plugins

Récupère la liste des plugins f

##### get_available_templates

Récupère la liste des templates f

##### get_cleanup_patterns

Récupère les patterns de f

##### to_dict

Convertit la configuration en f

---

### correction_optimizer

Système d'optimisation de la correction automatique pour Athalia/Arkalia
Améliore le taux de réussite de 80% à 95%+ en utilisant des techniques avancées

#### Classes

##### CorrectionResult

Résultat d'une correction

##### CorrectionOptimizer

Optimiseur de correction automatique avec techniques avancées

**Méthodes :**

- `__init__()`
- `optimize_correction()`
- `_apply_basic_corrections()`
- `_apply_ast_corrections()`
- `_apply_contextual_corrections()`
- `_analyze_syntax_error()`
- `_fix_indentation_error()`
- `_fix_bracket_balance()`
- `_fix_string_issues()`
- `_analyze_context()`
- `_validate_correction()`
- `_learn_from_correction()`
- `_extract_patterns()`
- `get_correction_stats()`

#### Fonctions

##### optimize_correction

Fonction de convenance pour optimiser une correction

**Paramètres :**

- `file_path`
- `content`

##### get_correction_stats

Fonction de convenance pour récupérer les statistiques

##### __init__

##### optimize_correction

Correction optimisée multi-passes avec apprentissage

**Paramètres :**

- `file_path`
- `content`

##### _apply_basic_corrections

Applique les corrections basiques

**Paramètres :**

- `content`

##### _apply_ast_corrections

Corrections basées sur l'analyse AST

**Paramètres :**

- `content`

##### _apply_contextual_corrections

Corrections contextuelles basées sur l'analyse du code

**Paramètres :**

- `content`

##### _analyze_syntax_error

Analyse une erreur de syntaxe pour déterminer le type de correction

**Paramètres :**

- `error`
- `content`

##### _fix_indentation_error

Corrige les erreurs d'indentation

**Paramètres :**

- `content`
- `error_info`

##### _fix_bracket_balance

Corrige les problèmes de parenthèses/accolades

**Paramètres :**

- `content`
- `error_info`

##### _fix_string_issues

Corrige les problèmes de chaînes de caractères

**Paramètres :**

- `content`
- `error_info`

##### _analyze_context

Analyse le contexte du code pour les corrections contextuelles

**Paramètres :**

- `lines`

##### _validate_correction

Valide que la correction a fonctionné

**Paramètres :**

- `content`

##### _learn_from_correction

Apprend des corrections pour améliorer les futures corrections

**Paramètres :**

- `file_path`
- `original`
- `corrected`
- `success`

##### _extract_patterns

Extrait des patterns de correction

**Paramètres :**

- `original`
- `corrected`

##### get_correction_stats

Récupère les statistiques de correction

---

### dashboard

#### Fonctions

##### show_benchmarks

##### main

---

### generation

#### Fonctions

##### generate_blueprint_mock

**Paramètres :**

- `idea`

##### generate_project

**Paramètres :**

- `blueprint`
- `outdir`

##### save_blueprint

**Paramètres :**

- `blueprint`
- `outdir`

##### inject_booster_ia_elements

**Paramètres :**

- `outdir`

##### scan_existing_project

**Paramètres :**

- `outdir`

##### merge_or_suffix_file

**Paramètres :**

- `file_path`
- `content`
- `file_type`
- `section_header`

##### backup_file

**Paramètres :**

- `file_path`

---

### intelligent_analyzer

🧠 ANALYSEUR INTELLIGENT ATHALIA - ORCHESTRATEUR PRINCIPAL
==========================================================
Orchestrateur principal qui coordonne tous les modules d'analyse :
- AST Analyzer (analyse de base)
- Pattern Detector (détection de patterns et doublons)
- Architecture Analyzer (analyse d'architecture)
- Performance Analyzer (analyse de performance)

#### Classes

##### ComprehensiveAnalysis

Analyse complète du projet

##### IntelligentAnalyzer

Orchestrateur principal de l'analyse intelligente

**Méthodes :**

- `__init__()`
- `analyze_project_comprehensive()`
- `_perform_ast_analysis()`
- `_calculate_overall_score()`
- `_generate_comprehensive_recommendations()`
- `_create_optimization_plan()`
- `_save_comprehensive_analysis()`
- `get_learning_insights()`
- `generate_intelligent_coordination()`
- `orchestrate_with_unified()`

#### Fonctions

##### main

Fonction principale pour l'analyse en ligne de commande

##### __init__

**Paramètres :**

- `root_path`

##### analyze_project_comprehensive

Analyser un projet de manière complète avec tous les modules

**Paramètres :**

- `project_path`

##### _perform_ast_analysis

Effectuer l'analyse AST de base

**Paramètres :**

- `project_path`

##### _calculate_overall_score

Calculer le score global basé sur toutes les analyses

**Paramètres :**

- `ast_analysis`
- `pattern_analysis`
- `architecture_analysis`
- `performance_analysis`

##### _generate_comprehensive_recommendations

Générer des recommandations globales

**Paramètres :**

- `pattern_analysis`
- `architecture_analysis`
- `performance_analysis`

##### _create_optimization_plan

Créer un plan d'optimisation global

**Paramètres :**

- `pattern_analysis`
- `architecture_analysis`
- `performance_analysis`

##### _save_comprehensive_analysis

Sauvegarder l'analyse complète

**Paramètres :**

- `analysis`

##### get_learning_insights

Obtenir des insights d'apprentissage de tous les modules

##### generate_intelligent_coordination

Générer une coordination intelligente

##### orchestrate_with_unified

Utiliser l'orchestrateur unifié pour une orchestration complète

**Paramètres :**

- `project_path`
- `config`

---

### intelligent_auditor

#### Classes

##### IntelligentAuditor

Auditeur intelligent pour analyse automatique des projets

**Méthodes :**

- `__init__()`
- `run()`
- `audit_project()`
- `_analyze_project_info()`
- `_detect_project_type()`
- `_calculate_project_size()`
- `_is_code_file()`
- `_detect_languages()`
- `_detect_dependencies()`
- `_get_last_modified()`
- `_analyze_code_quality()`
- `_analyze_complexity()`
- `_calculate_cyclomatic_complexity()`
- `_analyze_style()`
- `_analyze_code_documentation()`
- `_analyze_naming_conventions()`
- `_analyze_security()`
- `_detect_security_vulnerabilities()`
- `_detect_secrets()`
- `_analyze_permissions()`
- `_analyze_performance()`
- `_analyze_file_sizes()`
- `_analyze_imports()`
- `_estimate_memory_usage()`
- `_analyze_documentation()`
- `_check_readme()`
- `_check_api_documentation()`
- `_check_guides()`
- `_analyze_testing()`
- `_analyze_test_coverage()`
- `_find_test_files()`
- `_analyze_test_quality()`
- `_analyze_structure()`
- `_analyze_organization()`
- `_analyze_structure_naming()`
- `_analyze_modularity()`
- `_calculate_score()`
- `_generate_recommendations()`
- `generate_report()`

#### Fonctions

##### main

Point d'entrée

##### __init__

**Paramètres :**

- `project_path`

##### run

Méthode run() pour l'orchestrateur - exécute l'audit

##### audit_project

Audit complet d'un projet

**Paramètres :**

- `project_path`

##### _analyze_project_info

Analyse des informations du projet

##### _detect_project_type

Détection automatique du type de projet

##### _calculate_project_size

Calcul de la taille du projet

##### _is_code_file

Détermine si un fichier est un fichier de code

**Paramètres :**

- `file_path`

##### _detect_languages

Détection des langages du projet

##### _detect_dependencies

Détection des dépendances du projet

##### _get_last_modified

Date de dernière modification

##### _analyze_code_quality

Analyse de la qualité du code

##### _analyze_complexity

Analyse de la complexité du code

##### _calculate_cyclomatic_complexity

Calcul de la complexité cyclomatique d'un fichier

**Paramètres :**

- `tree`

##### _analyze_style

Analyse du style du code

##### _analyze_code_documentation

Analyse de la documentation du code

##### _analyze_naming_conventions

Analyse des conventions de nommage

##### _analyze_security

Analyse de la sécurité

##### _detect_security_vulnerabilities

Détection des vulnérabilités de sécurité

##### _detect_secrets

Détection de secrets

##### _analyze_permissions

Analyse des permissions des fichiers

##### _analyze_performance

Analyse de la performance

##### _analyze_file_sizes

Analyse de la taille des fichiers

##### _analyze_imports

Analyse des imports

##### _estimate_memory_usage

Estimation de la list_datausage

##### _analyze_documentation

Analyse de la documentation

##### _check_readme

Vérification du README

##### _check_api_documentation

Vérification de la documentation API

##### _check_guides

Vérification des guides

##### _analyze_testing

Analyse des tests

##### _analyze_test_coverage

Analyse de la couverture de tests

##### _find_test_files

Trouve les fichiers de tests

##### _analyze_test_quality

Analyse de la qualité des tests

##### _analyze_structure

Analyse de la structure du projet

##### _analyze_organization

Analyse de l'organisation des dossiers

##### _analyze_structure_naming

Analyse du nommage des fichiers et dossiers

##### _analyze_modularity

Analyse de la modularité

##### _calculate_score

Calcul du score global

##### _generate_recommendations

Génération des recommandations

##### generate_report

Génère un rapport d'audit

---

### intelligent_memory

🧠 MÉMOIRE INTELLIGENTE ATHALIA
===============================
Système de mémoire qui :
- Apprend de chaque erreur et correction
- Prédit les problèmes futurs
- Suggère des corrections automatiques
- Maintient un historique d'apprentissage
- Améliore la qualité du code continuellement

#### Classes

##### LearningEvent

Événement d'apprentissage

##### Prediction

Prédiction basée sur l'apprentissage

##### CorrectionSuggestion

Suggestion de correction

##### IntelligentMemory

Système de mémoire intelligente pour Athalia

**Méthodes :**

- `__init__()`
- `_init_database()`
- `learn_from_error()`
- `learn_from_correction()`
- `learn_from_duplicate()`
- `predict_issues()`
- `suggest_corrections()`
- `get_learning_insights()`
- `_record_learning_event()`
- `_analyze_code_pattern()`
- `_normalize_code()`
- `_update_pattern_learning()`
- `_generate_predictions_from_error()`
- `_find_similar_patterns()`
- `_check_antipatterns()`
- `_check_potential_duplicates()`
- `_calculate_code_similarity()`
- `_save_correction_suggestion()`

#### Fonctions

##### main

Test du système de mémoire intelligente

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données de mémoire

##### learn_from_error

Apprendre d'une erreur

**Paramètres :**

- `error_description`
- `code_snippet`
- `location`
- `severity`
- `context`

##### learn_from_correction

Apprendre d'une correction

**Paramètres :**

- `original_code`
- `corrected_code`
- `reason`
- `location`
- `success`
- `context`

##### learn_from_duplicate

Apprendre d'un doublon détecté

**Paramètres :**

- `duplicate_items`
- `locations`
- `similarity_score`
- `context`

##### predict_issues

Prédire les problèmes potentiels

**Paramètres :**

- `code_snippet`
- `context`

##### suggest_corrections

Suggérer des corrections basées sur l'apprentissage

**Paramètres :**

- `problematic_code`
- `issue_description`

##### get_learning_insights

Obtenir des insights d'apprentissage

##### _record_learning_event

Enregistrer un événement d'apprentissage

**Paramètres :**

- `event_type`
- `description`
- `code_snippet`
- `location`
- `severity`
- `success`
- `resolution`
- `context`

##### _analyze_code_pattern

Analyser et créer un hash du pattern de code

**Paramètres :**

- `code`

##### _normalize_code

Normaliser le code pour la comparaison

**Paramètres :**

- `code`

##### _update_pattern_learning

Mettre à jour l'apprentissage d'un pattern

**Paramètres :**

- `pattern_hash`
- `pattern_type`
- `success`

##### _generate_predictions_from_error

Générer des prédictions basées sur une erreur

**Paramètres :**

- `error_description`
- `code_snippet`
- `pattern_hash`

##### _find_similar_patterns

Trouver des patterns similaires

**Paramètres :**

- `pattern_hash`

##### _check_antipatterns

Vérifier les anti-patterns connus

**Paramètres :**

- `code_snippet`

##### _check_potential_duplicates

Vérifier les doublons potentiels

**Paramètres :**

- `code_snippet`

##### _calculate_code_similarity

Calculer la similarité entre deux codes

**Paramètres :**

- `code1`
- `code2`

##### _save_correction_suggestion

Sauvegarder une suggestion de correction

**Paramètres :**

- `original_code`
- `corrected_code`
- `reason`
- `success`

---

### logger_advanced

Système de logging avancé pour Athalia/Arkalia
Logging intelligent avec rotation, compression et analyse automatique

#### Classes

##### AthaliaLogger

Système de logging avancé pour Athalia/Arkalia

**Méthodes :**

- `__init__()`
- `_setup_loggers()`
- `_create_logger()`
- `log_main()`
- `log_validation()`
- `log_correction()`
- `log_performance()`
- `log_error()`
- `get_validation_stats()`
- `get_correction_stats()`
- `get_performance_stats()`
- `get_error_stats()`
- `_cleanup_worker()`
- `_cleanup_old_logs()`
- `_compress_old_logs()`
- `export_metrics()`

#### Fonctions

##### log_main

Log dans le logger principal

**Paramètres :**

- `message`
- `level`

##### log_validation

Log des résultats de validation

**Paramètres :**

- `test_name`
- `result`
- `duration`

##### log_correction

Log des corrections automatiques

**Paramètres :**

- `file_path`
- `correction_type`
- `success`
- `old_content`
- `new_content`
- `duration`

##### log_performance

Log des métriques de performance

**Paramètres :**

- `operation`
- `duration`
- `memory_mb`
- `cpu_percent`

##### log_error

Log des erreurs

**Paramètres :**

- `error`
- `context`

##### __init__

**Paramètres :**

- `log_dir`

##### _setup_loggers

Configure tous les loggers

##### _create_logger

Crée un logger avec rotation et compression

**Paramètres :**

- `name`
- `log_file`
- `level`

##### log_main

Log dans le logger principal

**Paramètres :**

- `message`
- `level`

##### log_validation

Log des résultats de validation

**Paramètres :**

- `test_name`
- `result`
- `duration`

##### log_correction

Log des corrections automatiques

**Paramètres :**

- `file_path`
- `correction_type`
- `success`
- `old_content`
- `new_content`
- `duration`

##### log_performance

Log des métriques de performance

**Paramètres :**

- `operation`
- `duration`
- `memory_mb`
- `cpu_percent`

##### log_error

Log des erreurs

**Paramètres :**

- `error`
- `context`

##### get_validation_stats

Récupère les statistiques de validation

**Paramètres :**

- `hours`

##### get_correction_stats

Récupère les statistiques de correction

**Paramètres :**

- `hours`

##### get_performance_stats

Récupère les statistiques de performance

**Paramètres :**

- `hours`

##### get_error_stats

Récupère les statistiques d'erreurs

**Paramètres :**

- `hours`

##### _cleanup_worker

Thread de nettoyage automatique des logs

##### _cleanup_old_logs

Nettoie les anciens logs

##### _compress_old_logs

Compresse les logs anciens

##### export_metrics

Exporte toutes les métriques

**Paramètres :**

- `output_file`

---

### main

#### Fonctions

##### menu

##### safe_input

Entrée sécurisée avec gestion d'erreurs.

**Paramètres :**

- `prompt`

##### main

**Paramètres :**

- `test_mode`

---

### multi_file_editor

Module d'édition/correction multi-fichiers pour Athalia/Arkalia.
Permet d'appliquer des corrections/refactoring sur plusieurs fichiers en une seule commande, avec logs et rollback.

#### Classes

##### MultiFileEditor

**Méthodes :**

- `__init__()`
- `backup_file()`
- `apply_corrections()`
- `rollback()`

#### Fonctions

##### __init__

**Paramètres :**

- `backup_dir`

##### backup_file

**Paramètres :**

- `file_path`

##### apply_corrections

Applique la fonction de correction à chaque fichier.
:param files: Liste des chemins de fichiers à corriger
:param correction_fn: Fonction qui prend le contenu du fichier et retourne le contenu corrigé
:return: Dictionnaire de résultats (succès, erreurs, logs)

**Paramètres :**

- `files`
- `correction_fn`

##### rollback

Restaure tous les fichiers depuis les backups.

##### dummy_correction

**Paramètres :**

- `content`

---

### onboarding

#### Fonctions

##### generate_onboarding_md

**Paramètres :**

- `blueprint`
- `outdir`

##### generate_onboard_cli

**Paramètres :**

- `blueprint`
- `outdir`

##### generate_onboarding_html_advanced

**Paramètres :**

- `blueprint`
- `outdir`

---

### pattern_detector

🔍 DÉTECTEUR DE PATTERNS ET DOUBLONS
====================================
Module spécialisé dans la détection de patterns de code,
doublons et anti-patterns. Utilise l'analyseur AST de base.

#### Classes

##### CodePattern

Pattern de code détecté

##### DuplicateAnalysis

Analyse de doublons

##### AntiPattern

Anti-pattern détecté

##### PatternDetector

Détecteur de patterns et doublons

**Méthodes :**

- `__init__()`
- `_init_database()`
- `_load_patterns()`
- `analyze_project_patterns()`
- `_extract_patterns_from_file()`
- `_detect_duplicates()`
- `_calculate_similarity()`
- `_detect_antipatterns()`
- `_save_analysis_results()`
- `_generate_recommendations()`
- `get_learning_insights()`

#### Fonctions

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données

##### _load_patterns

Charger les patterns depuis la base de données

##### analyze_project_patterns

Analyser les patterns d'un projet complet

**Paramètres :**

- `project_path`

##### _extract_patterns_from_file

Extraire les patterns d'un fichier analysé

**Paramètres :**

- `file_analysis`

##### _detect_duplicates

Détecter les doublons parmi les patterns

**Paramètres :**

- `patterns`

##### _calculate_similarity

Calculer la similarité entre deux patterns

**Paramètres :**

- `pattern1`
- `pattern2`

##### _detect_antipatterns

Détecter les anti-patterns

**Paramètres :**

- `patterns`

##### _save_analysis_results

Sauvegarder les résultats d'analyse

**Paramètres :**

- `patterns`
- `duplicates`
- `antipatterns`

##### _generate_recommendations

Générer des recommandations basées sur l'analyse

**Paramètres :**

- `duplicates`
- `antipatterns`

##### get_learning_insights

Obtenir des insights d'apprentissage

---

### performance_analyzer

⚡ ANALYSEUR DE PERFORMANCE
===========================
Module spécialisé dans l'analyse des performances du code,
détection des goulots d'étranglement et optimisation.

#### Classes

##### PerformanceMetric

Métrique de performance

##### PerformanceIssue

Problème de performance détecté

##### PerformanceReport

Rapport de performance complet

##### PerformanceAnalyzer

Analyseur de performance pour détecter les goulots d'étranglement

**Méthodes :**

- `__init__()`
- `_init_database()`
- `analyze_project_performance()`
- `_analyze_file_performance()`
- `_detect_performance_issues()`
- `_get_metric_status()`
- `_calculate_overall_score()`
- `_get_metric_weight()`
- `_calculate_metric_score()`
- `_generate_performance_recommendations()`
- `_identify_optimization_opportunities()`
- `_save_performance_report()`
- `profile_function()`
- `get_performance_insights()`

#### Fonctions

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données de performance

##### analyze_project_performance

Analyser les performances d'un projet complet

**Paramètres :**

- `project_path`

##### _analyze_file_performance

Analyser les performances d'un fichier

**Paramètres :**

- `file_analysis`

##### _detect_performance_issues

Détecter les problèmes de performance dans un fichier

**Paramètres :**

- `file_analysis`

##### _get_metric_status

Déterminer le statut d'une métrique

**Paramètres :**

- `value`
- `threshold`
- `reverse`

##### _calculate_overall_score

Calculer le score de performance global

**Paramètres :**

- `metrics`

##### _get_metric_weight

Obtenir le poids d'une métrique

**Paramètres :**

- `metric_type`

##### _calculate_metric_score

Calculer le score d'une métrique

**Paramètres :**

- `metric`

##### _generate_performance_recommendations

Générer des recommandations de performance

**Paramètres :**

- `issues`

##### _identify_optimization_opportunities

Identifier les opportunités d'optimisation

**Paramètres :**

- `issues`

##### _save_performance_report

Sauvegarder le rapport de performance

**Paramètres :**

- `report`

##### profile_function

Profiler une fonction spécifique

**Paramètres :**

- `function_path`
- `function_name`

##### get_performance_insights

Obtenir des insights de performance

---

### plugins_manager

#### Fonctions

##### list_plugins

Liste tous les plugins disponibles.

##### load_plugin

Charge dynamiquement un plugin par nom.

**Paramètres :**

- `name`

##### run_all_plugins

Exécute la fonction run() de tous les plugins et retourne les résultats.

---

### plugins_validator

#### Fonctions

##### validate_plugin

Valide un plugin Python : héritage, méthode run / execute, docstring.

**Paramètres :**

- `path`

---

### project_importer

#### Classes

##### ProjectImporter

**Méthodes :**

- `__init__()`
- `import_project()`
- `_scan_structure()`
- `_detect_project_type()`
- `_analyze_code_quality()`
- `_generate_correction_blueprint()`
- `_suggest_modules()`
- `_suggest_structure()`
- `_suggest_dependencies()`
- `_suggest_prompts()`
- `_suggest_enhancements()`

#### Fonctions

##### __init__

##### import_project

Importe et analyse un projet existant.

**Paramètres :**

- `project_path`

##### _scan_structure

Analyse la structure du projet.

**Paramètres :**

- `project_path`

##### _detect_project_type

Détecte automatiquement le type de projet.

**Paramètres :**

- `project_path`
- `structure`

##### _analyze_code_quality

Analyse la qualité du code.

**Paramètres :**

- `project_path`

##### _generate_correction_blueprint

Génère un blueprint de correction pour le projet.

**Paramètres :**

- `project_path`
- `structure`
- `project_type`
- `quality_analysis`

##### _suggest_modules

Suggère des modules selon le type de projet.

**Paramètres :**

- `project_type`

##### _suggest_structure

Gère une structure améliorée.

**Paramètres :**

- `structure`

##### _suggest_dependencies

Suggère des dépendances selon le type de projet.

**Paramètres :**

- `project_type`

##### _suggest_prompts

Suggère des prompts selon le type de projet.

**Paramètres :**

- `project_type`

##### _suggest_enhancements

Suggère des améliorations spécifiques.

**Paramètres :**

- `project_type`
- `quality_analysis`

---

### ready_check

#### Fonctions

##### open_patch

**Paramètres :**

- `file`
- `mode`

##### check_ready

**Paramètres :**

- `project_path`

---

### security

#### Fonctions

##### security_audit_project

**Paramètres :**

- `project_path`

---

### security_auditor

#### Classes

##### SecurityAuditor

Auditeur de sécurité pour Athalia

**Méthodes :**

- `__init__()`
- `run()`
- `_check_dependencies()`
- `_check_code_vulnerabilities()`
- `_check_secrets()`
- `_check_permissions()`
- `_check_encryption()`
- `_calculate_score()`
- `print_report()`

#### Fonctions

##### __init__

**Paramètres :**

- `project_path`

##### run

Lance l'audit de sécurité

##### _check_dependencies

Vérification des dépendances

##### _check_code_vulnerabilities

Vérification des vulnérabilités dans le code

##### _check_secrets

Vérification des secrets

##### _check_permissions

Vérification des permissions des fichiers

##### _check_encryption

Vérification de l'utilisation du chiffrement

##### _calculate_score

Calcul du score de sécurité

##### print_report

Affichage du rapport de sécurité

---

### unified_orchestrator

🎯 ORCHESTRATEUR UNIFIÉ ATHALIA
================================
Orchestrateur unifié qui combine :
- Industrialisation complète (athalia_orchestrator)
- Intelligence et apprentissage (intelligent_orchestrator)
- Coordination de tous les modules Athalia
- Gestion des tâches et prédictions
- Optimisation automatique du code

#### Classes

##### OrchestrationTask

Tâche d'orchestration unifiée

##### IntelligentInsight

Insight intelligent unifié

##### IndustrializationStep

Étape d'industrialisation

##### UnifiedOrchestrator

Orchestrateur unifié Athalia
Combine industrialisation complète et intelligence avancée

**Méthodes :**

- `__init__()`
- `_init_database()`
- `orchestrate_project_complete()`
- `_run_industrialization()`
- `_run_audit()`
- `_run_linting()`
- `_run_security_audit()`
- `_run_analytics()`
- `_run_cleanup()`
- `_run_documentation()`
- `_run_testing()`
- `_run_cicd()`
- `_run_robotics_audit()`
- `_generate_predictions()`
- `_generate_optimizations()`
- `_learn_from_results()`
- `_generate_unified_report()`
- `_save_unified_results()`
- `get_orchestration_insights()`

#### Fonctions

##### main

Point d'entrée principal

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données unifiée

##### orchestrate_project_complete

Orchestration complète d'un projet
Combine industrialisation et intelligence

**Paramètres :**

- `project_path`
- `config`

##### _run_industrialization

Exécuter l'industrialisation complète

**Paramètres :**

- `project_path`

##### _run_audit

Exécuter l'audit intelligent

**Paramètres :**

- `project_path`

##### _run_linting

Exécuter le linting

**Paramètres :**

- `project_path`

##### _run_security_audit

Exécuter l'audit de sécurité

**Paramètres :**

- `project_path`

##### _run_analytics

Exécuter l'analytics

**Paramètres :**

- `project_path`

##### _run_cleanup

Exécuter le nettoyage

**Paramètres :**

- `project_path`

##### _run_documentation

Exécuter la documentation

**Paramètres :**

- `project_path`

##### _run_testing

Exécuter les tests

**Paramètres :**

- `project_path`

##### _run_cicd

Exécuter le CI/CD

**Paramètres :**

- `project_path`

##### _run_robotics_audit

Exécuter l'audit robotique

**Paramètres :**

- `project_path`

##### _generate_predictions

Générer des prédictions intelligentes

**Paramètres :**

- `project_path`

##### _generate_optimizations

Générer des optimisations intelligentes

**Paramètres :**

- `project_path`

##### _learn_from_results

Apprendre des résultats d'orchestration

**Paramètres :**

- `results`

##### _generate_unified_report

Générer un rapport unifié

**Paramètres :**

- `results`

##### _save_unified_results

Sauvegarder les résultats unifiés

**Paramètres :**

- `results`

##### get_orchestration_insights

Obtenir des insights d'orchestration

---

### auto_correction_advanced

Module d'auto-correction avancée pour Athalia
Correction intelligente de code, suggestions d'amélioration, refactoring automatique

#### Classes

##### AutoCorrectionAvancee

Module d'auto-correction avancée avec correction intelligente

**Méthodes :**

- `__init__()`
- `analyser_et_corriger()`
- `_corriger_syntaxe_avancee()`
- `_corriger_erreur_syntaxe()`
- `_corriger_indentation()`
- `_corriger_parentheses()`
- `_corriger_guillemets()`
- `_corriger_virgules()`
- `_optimiser_code()`
- `_optimiser_list_comprehensions()`
- `_optimiser_imports()`
- `_optimiser_boucles()`
- `_refactoring_automatique()`
- `_extraire_methodes()`
- `_renommer_variables()`
- `_simplifier_conditions()`
- `_corriger_anti_patterns()`
- `_ameliorer_lisibilite()`
- `generer_rapport()`

#### Fonctions

##### main

Fonction principale pour test

##### __init__

**Paramètres :**

- `project_path`

##### analyser_et_corriger

Analyse complète et correction automatique du code

**Paramètres :**

- `dry_run`

##### _corriger_syntaxe_avancee

Correction syntaxique avancée avec analyse AST

**Paramètres :**

- `dry_run`

##### _corriger_erreur_syntaxe

Correction intelligente d'erreur de syntaxe

**Paramètres :**

- `fichier`
- `contenu`
- `erreur`

##### _corriger_indentation

Correction automatique de l'indentation

**Paramètres :**

- `lignes`
- `ligne_erreur`

##### _corriger_parentheses

Correction automatique des parenthèses

**Paramètres :**

- `lignes`
- `ligne_erreur`

##### _corriger_guillemets

Correction automatique des guillemets

**Paramètres :**

- `lignes`
- `ligne_erreur`

##### _corriger_virgules

Correction automatique des virgules manquantes

**Paramètres :**

- `lignes`
- `ligne_erreur`

##### _optimiser_code

Optimisation automatique du code

**Paramètres :**

- `dry_run`

##### _optimiser_list_comprehensions

Optimisation des list comprehensions

**Paramètres :**

- `contenu`

##### _optimiser_imports

Optimisation des imports

**Paramètres :**

- `contenu`

##### _optimiser_boucles

Optimisation des boucles

**Paramètres :**

- `contenu`

##### _refactoring_automatique

Refactoring automatique du code

**Paramètres :**

- `dry_run`

##### _extraire_methodes

Extraction automatique de méthodes

**Paramètres :**

- `contenu`

##### _renommer_variables

Renommage automatique de variables

**Paramètres :**

- `contenu`

##### _simplifier_conditions

Simplification automatique de conditions

**Paramètres :**

- `contenu`

##### _corriger_anti_patterns

Correction des anti-patterns

**Paramètres :**

- `dry_run`

##### _ameliorer_lisibilite

Amélioration de la lisibilité

**Paramètres :**

- `dry_run`

##### generer_rapport

Génération d'un rapport détaillé

**Paramètres :**

- `resultats`

---

### dashboard_unified

#### Classes

##### DashboardUnifieSimple

Dashboard unifié simplifié avec rapports fonctionnels

**Méthodes :**

- `__init__()`
- `_init_database()`
- `enregistrer_metrique()`
- `enregistrer_evenement()`
- `enregistrer_rapport()`
- `obtenir_metriques_temps_reel()`
- `generer_rapport_consolide()`
- `ajouter_section_distillation()`
- `generer_dashboard_html()`
- `ouvrir_dashboard()`

#### Fonctions

##### main

Fonction principale pour test du f

##### __init__

**Paramètres :**

- `db_path`

##### _init_database

Initialisation de la base de données

##### enregistrer_metrique

Enregistrement une métrique

**Paramètres :**

- `type_metrique`
- `valeur`
- `projet`
- `details`

##### enregistrer_evenement

Enregistrement un événement

**Paramètres :**

- `type_evenement`
- `projet`
- `utilisateur`
- `duree`
- `statut`
- `details`

##### enregistrer_rapport

Enregistrement un rapport

**Paramètres :**

- `type_rapport`
- `projet`
- `contenu`
- `score_qualite`
- `score_securite`

##### obtenir_metriques_temps_reel

Obtention des métriques en temps réel

##### generer_rapport_consolide

Génération d'un rapport consolidé

##### ajouter_section_distillation

Ajoute une section Distillation IA au dashboard (exemple statique).

**Paramètres :**

- `file_handle`

##### generer_dashboard_html

Génération d'un dashboard HTML moderne et valide

**Paramètres :**

- `output_file`

##### ouvrir_dashboard

Ouverture du dashboard dans le f

---

### user_profiles_advanced

Module de gestion des profils utilisateur avancés pour Athalia
Gestion des préférences, historique, statistiques et personnalisation

#### Classes

##### ProfilUtilisateur

Profil utilisateur avec préférences et historique

**Méthodes :**

- `__init__()`
- `to_dict()`
- `from_dict()`

##### GestionnaireProfils

Gestionnaire de profils utilisateur avancé

**Méthodes :**

- `__init__()`
- `_init_database()`
- `creer_profil()`
- `obtenir_profil()`
- `mettre_a_jour_profil()`
- `enregistrer_action()`
- `enregistrer_consultation_projet()`
- `obtenir_statistiques()`
- `generer_rapport_profil()`
- `lister_profils()`
- `supprimer_profil()`
- `exporter_profil()`
- `importer_profil()`

#### Fonctions

##### main

Fonction principale pour test

##### __init__

**Paramètres :**

- `nom`
- `email`
- `preferences`

##### to_dict

Conversion en dictionnaire

##### from_dict

Création depuis un dictionnaire

**Paramètres :**

- `cls`
- `data`

##### __init__

**Paramètres :**

- `db_path`

##### _init_database

Initialisation de la base de données

##### creer_profil

Création d'un nouveau profil

**Paramètres :**

- `nom`
- `email`
- `preferences`

##### obtenir_profil

Récupération d'un profil par nom

**Paramètres :**

- `nom`

##### mettre_a_jour_profil

Mise à jour d'un profil

**Paramètres :**

- `profil`

##### enregistrer_action

Enregistrement d'une action utilisateur

**Paramètres :**

- `nom_profil`
- `action`
- `details`

##### enregistrer_consultation_projet

Enregistrement de la consultation d'un projet

**Paramètres :**

- `nom_profil`
- `chemin_projet`
- `duree`

##### obtenir_statistiques

Obtention des statistiques d'un profil

**Paramètres :**

- `nom_profil`

##### generer_rapport_profil

Génération d'un rapport détaillé pour un profil

**Paramètres :**

- `nom_profil`

##### lister_profils

Liste de tous les profils

##### supprimer_profil

Suppression d'un profil

**Paramètres :**

- `nom`

##### exporter_profil

Export d'un profil vers un fichier JSON

**Paramètres :**

- `nom`
- `fichier_destination`

##### importer_profil

Import d'un profil depuis un fichier JSON

**Paramètres :**

- `fichier_source`

---

### audit_agent

#### Classes

##### AuditAgent

**Méthodes :**

- `act()`

#### Fonctions

##### act

**Paramètres :**

- `prompt`

---

### context_prompt

#### Fonctions

##### score_prompt

**Paramètres :**

- `prompt`
- `filename`
- `content`

##### detect_prompts_scoring

**Paramètres :**

- `filepath`

##### detect_prompt_semantic

**Paramètres :**

- `filepath`

##### show_prompts

**Paramètres :**

- `scored`
- `semantic_prompt`

##### main

---

### unified_agent

Agent unifié pour Athalia - Combine les fonctionnalités de network_agent et qwen_agent

#### Classes

##### UnifiedAgent

Agent unifié pour toutes les tâches IA

**Méthodes :**

- `__init__()`
- `act()`
- `_process_prompt()`
- `_synthesize_responses()`

##### AuditAgent

Agent d'audit spécialisé

**Méthodes :**

- `__init__()`

##### CorrectionAgent

Agent de correction spécialisé

**Méthodes :**

- `__init__()`

##### SynthesisAgent

Agent de synthèse spécialisé

**Méthodes :**

- `__init__()`

##### QwenAgent

Agent Qwen spécialisé (compatibilité)

**Méthodes :**

- `__init__()`

#### Fonctions

##### __init__

**Paramètres :**

- `agent_type`

##### act

Action principale de l'agent

**Paramètres :**

- `prompt`
- `responses`

##### _process_prompt

Traite un prompt avec l'IA

**Paramètres :**

- `prompt`

##### _synthesize_responses

Synthétise plusieurs réponses

**Paramètres :**

- `prompt`
- `responses`

##### __init__

##### __init__

##### __init__

##### __init__

---

### project_classifier

#### Fonctions

##### classify_project

Analyse l'idée du projet et retourne le type approprié.

Args:
    idea: Description du projet en une phrase

Returns:
    ProjectType: Type de projet détecté

**Paramètres :**

- `idea`

##### get_project_name

Génère un nom de projet approprié basé sur l'idée et le type.

Args:
    idea: Description du projet
    project_type: Type de projet détecté

Returns:
    str: Nom de projet généré

**Paramètres :**

- `idea`
- `project_type`

---

### project_types

#### Classes

##### ProjectType

Types de projets supportés.

#### Fonctions

##### get_project_config

Retourne la configuration spécialisée pour un type de projet.

**Paramètres :**

- `project_type`

---

### adaptive_distillation

Distillation adaptative pour Athalia/Arkalia
- Pondération dynamique selon préférences et feedback utilisateur
- Historique sauvegardé/chargé en JSON

#### Classes

##### AdaptiveDistiller

**Méthodes :**

- `__init__()`
- `distill_responses()`
- `update_preferences()`
- `apply_learned_weights()`
- `ensemble_fusion()`
- `save_history()`
- `load_history()`

#### Fonctions

##### __init__

Initialise le distillateur adaptatif.
:param history_path: Chemin du fichier JSON pour l'historique (optionnel)

**Paramètres :**

- `history_path`

##### distill_responses

Fusionne les réponses IA en tenant compte des préférences et du feedback utilisateur.
:param responses: Liste de réponses IA
:param context: Contexte optionnel
:return: Réponse distillée

**Paramètres :**

- `responses`
- `context`

##### update_preferences

Met à jour les préférences et le feedback selon la réponse choisie et le succès/échec.
:param chosen_response: Réponse sélectionnée
:param responses: Liste des réponses proposées
:param success: Succès (True) ou échec (False) de la réponse

**Paramètres :**

- `chosen_response`
- `responses`
- `success`

##### apply_learned_weights

Trie les réponses selon leur poids appris et taux de succès.
:param responses: Liste de réponses IA
:return: Liste triée

**Paramètres :**

- `responses`

##### ensemble_fusion

Fusionne les réponses (majority voting par défaut).
:param responses: Liste de réponses pondérées
:param context: Contexte optionnel
:return: Réponse fusionnée

**Paramètres :**

- `responses`
- `context`

##### save_history

Sauvegarde l'historique et les poids en JSON.

##### load_history

Charge l'historique et les poids depuis un JSON si disponible.

##### score

**Paramètres :**

- `r`

---

### audit_distiller

Module de distillation d'audits pour Athalia/Arkalia
Fusionne et pondère plusieurs audits (sécurité, qualité, performance...)

#### Classes

##### AuditDistiller

**Méthodes :**

- `__init__()`
- `distill()`

#### Fonctions

##### __init__

**Paramètres :**

- `weights`

##### distill

Fusionne plusieurs audits en un score global et des recommandations synthétiques.
:param audits: Liste de résultats d'audit (dict)
:return: Audit distillé (dict)

**Paramètres :**

- `audits`

---

### code_genetics

Code Genetics pour Athalia/Arkalia
- Croisement, mutation, sélection, évolution de solutions IA

#### Classes

##### CodeGenetics

**Méthodes :**

- `crossover()`
- `mutate()`
- `select()`
- `evolve()`

#### Fonctions

##### crossover

Croisement de solutions : mélange aléatoire de fragments de chaque solution.
:param solutions: Liste de solutions (str)
:return: Nouvelle solution croisée

**Paramètres :**

- `solutions`

##### mutate

Mutation simple : modifie aléatoirement des mots de la solution.
:param solution: Solution à muter
:param mutation_rate: Taux de mutation (0-1)
:return: Solution mutée

**Paramètres :**

- `solution`
- `mutation_rate`

##### select

Sélectionne les meilleures solutions selon un score.
:param solutions: Liste de solutions
:param scorer: Fonction de scoring (str -> float)
:param top_k: Nombre de solutions à garder
:return: Liste des meilleures solutions

**Paramètres :**

- `solutions`
- `scorer`
- `top_k`

##### evolve

Fait évoluer les solutions sur plusieurs générations (croisement, mutation, sélection).
:param solutions: Liste initiale
:param scorer: Fonction de scoring
:param generations: Nombre de générations
:param mutation_rate: Taux de mutation
:return: Meilleure solution finale

**Paramètres :**

- `solutions`
- `scorer`
- `generations`
- `mutation_rate`

---

### correction_distiller

Module de distillation de corrections IA pour Athalia/Arkalia
Fusionne, score et sélectionne la meilleure correction parmi plusieurs suggestions IA.

#### Classes

##### CorrectionDistiller

**Méthodes :**

- `__init__()`
- `distill()`

#### Fonctions

##### __init__

**Paramètres :**

- `strategy`

##### distill

Sélectionne ou fusionne la meilleure correction IA.
:param corrections: Liste de corrections proposées (str)
:param scores: Scores optionnels pour chaque correction
:param context: Contexte optionnel
:return: Correction distillée (str)

**Paramètres :**

- `corrections`
- `scores`
- `context`

---

### multimodal_distiller

Distillation multimodale pour Athalia/Arkalia
- Fusionne réponses texte et image (LLaVA)
- Appel réel à LLaVA via RobustAI (Ollama)

#### Classes

##### MultimodalDistiller

**Méthodes :**

- `distill()`
- `call_llava()`

#### Fonctions

##### distill

Fusionne les réponses texte et image en utilisant LLaVA (Ollama) et d'autres modèles si besoin.
:param text_prompts: Liste de prompts texte
:param image_paths: Liste de chemins d'images (un par prompt ou global)
:param context: Contexte optionnel
:return: Réponse multimodale fusionnée

**Paramètres :**

- `text_prompts`
- `image_paths`
- `context`

##### call_llava

Appelle LLaVA via Ollama pour une analyse multimodale (texte + image).
:param prompt: Prompt texte
:param image_path: Chemin de l'image à analyser
:return: Réponse de LLaVA (str)

**Paramètres :**

- `prompt`
- `image_path`

---

### predictive_cache

Caching prédictif pour Athalia/Arkalia
- Anticipation contextuelle, pré-génération, invalidation intelligente, stats

#### Classes

##### PredictiveCache

**Méthodes :**

- `__init__()`
- `get()`
- `set()`
- `predict_key()`
- `pre_generate()`
- `invalidate()`
- `get_stats()`

#### Fonctions

##### __init__

:param ttl: Durée de vie (en secondes) d'une entrée (0 = infini)

**Paramètres :**

- `ttl`

##### get

**Paramètres :**

- `key`

##### set

**Paramètres :**

- `key`
- `value`

##### predict_key

**Paramètres :**

- `context`

##### pre_generate

Pré-génère une réponse pour un contexte donné (si non déjà en cache).
:param context: Contexte (dict)
:param generator: Fonction qui génère la valeur à stocker

**Paramètres :**

- `context`
- `generator`

##### invalidate

Supprime une entrée du cache.

**Paramètres :**

- `key`

##### get_stats

Retourne les statistiques d'utilisation du cache.

---

### quality_scorer

Module de scoring de qualité pour Athalia/Arkalia
Évalue la pertinence d'une solution IA ou d'une correction selon plusieurs critères.

#### Classes

##### QualityScorer

**Méthodes :**

- `__init__()`
- `score()`

#### Fonctions

##### __init__

**Paramètres :**

- `weights`

##### score

Évalue la qualité d'une solution IA.
:param solution: Solution à scorer (str, dict, ...)
:param context: Contexte optionnel
:return: Score de qualité (float)

**Paramètres :**

- `solution`
- `context`

---

### response_distiller

Module de distillation de réponses IA pour Athalia/Arkalia
Permet de fusionner plusieurs réponses IA en une solution optimale (voting, stacking, bagging, consensus scoring...)

#### Classes

##### ResponseDistiller

**Méthodes :**

- `__init__()`
- `distill()`
- `majority_voting()`
- `stacking()`
- `bagging()`
- `consensus_scoring()`
- `creative_fusion()`

#### Fonctions

##### distill_responses

Fonction utilitaire pour distiller une liste de réponses IA.

**Paramètres :**

- `responses`
- `strategy`
- `context`

##### __init__

**Paramètres :**

- `strategy`

##### distill

Fusionne plusieurs réponses IA selon la stratégie choisie.
:param responses: Liste de réponses IA (str)
:param context: Contexte optionnel (pour scoring avancé)
:return: Réponse distillée (str)

**Paramètres :**

- `responses`
- `context`

##### majority_voting

Retourne la réponse la plus fréquente (majorité).

**Paramètres :**

- `responses`

##### stacking

Concatène les parties communes, puis les parties uniques.

**Paramètres :**

- `responses`
- `context`

##### bagging

Retourne une réponse aléatoire parmi les plus fréquentes (bagging).

**Paramètres :**

- `responses`

##### consensus_scoring

Retourne la plus longue sous-chaîne commune ET les parties divergentes.

**Paramètres :**

- `responses`

##### creative_fusion

Fusion créative : mélange de fragments, ajout d’un tag IA, et concat unique.

**Paramètres :**

- `responses`

##### lcs

**Paramètres :**

- `a`
- `b`

---

### docker_export_plugin

Plugin d'export Docker pour projet Python.

#### Fonctions

##### export_docker

Génère un Dockerfile optimisé pour le projet donné.

**Paramètres :**

- `project_path`
- `output_path`

##### analyze_dependencies

Affiche les dépendances du projet.

**Paramètres :**

- `project_path`

##### run

Fonction d'entrée standard pour le plugin.

**Paramètres :**

- `project_path`

---

### hello_world_plugin

Plugin exemple : Hello Plugin

#### Fonctions

##### run

---

### en

English translations for Athalia

#### Fonctions

##### get_translation

Returns English translations

**Paramètres :**

- `lang`

---

### fr

Traductions françaises pour Athalia

#### Fonctions

##### get_translation

Retourne les traductions françaises

**Paramètres :**

- `lang`

---

### docker_robotics

Docker Robotics Manager - Gestion Docker pour projets robotiques
===============================================================

Gestion spécialisée Docker pour projets Reachy/ROS2 :
- Configuration Docker Compose
- Variables d'environnement ROS
- Volumes et networking
- Images spécialisées

#### Classes

##### DockerServiceConfig

Configuration d'un service Docker

##### DockerValidationResult

Résultat de validation Docker

##### DockerRoboticsManager

Gestionnaire Docker spécialisé robotique

**Méthodes :**

- `__init__()`
- `validate_docker_setup()`
- `_parse_service_config()`
- `_validate_reachy_service()`
- `create_reachy_compose_template()`
- `create_dockerfile_template()`
- `create_start_script_template()`
- `setup_reachy_environment()`
- `run_docker_compose()`
- `generate_docker_report()`

#### Fonctions

##### __init__

**Paramètres :**

- `project_path`

##### validate_docker_setup

Valider la configuration Docker

##### _parse_service_config

Parser la configuration d'un service

**Paramètres :**

- `name`
- `config`

##### _validate_reachy_service

Valider spécifiquement le service Reachy

**Paramètres :**

- `service`
- `issues`
- `recommendations`

##### create_reachy_compose_template

Créer un template docker-compose.yaml pour Reachy

##### create_dockerfile_template

Créer un template Dockerfile pour Reachy

##### create_start_script_template

Créer un template de script de démarrage

##### setup_reachy_environment

Configurer l'environnement Docker pour Reachy

##### run_docker_compose

Lancer docker-compose

**Paramètres :**

- `service`

##### generate_docker_report

Générer rapport Docker

**Paramètres :**

- `result`

---

### reachy_auditor

Reachy Auditor - Audit spécialisé pour projets Reachy/ROS2
==========================================================

Audit complet des projets robotiques Reachy :
- Validation workspace ROS2
- Contrôle Docker/Containers
- Analyse Rust/Cargo
- Vérification structure projet
- Tests de connectivité

#### Classes

##### ReachyAuditResult

Résultat d'audit Reachy

##### ReachyAuditor

Auditeur spécialisé pour projets Reachy/ROS2

**Méthodes :**

- `__init__()`
- `audit_complete()`
- `_audit_ros2()`
- `_audit_docker()`
- `_audit_rust()`
- `_audit_structure()`
- `generate_report()`
- `save_report()`

#### Fonctions

##### __init__

**Paramètres :**

- `project_path`

##### audit_complete

Audit complet du projet Reachy

##### _audit_ros2

Audit spécifique ROS2

##### _audit_docker

Audit Docker/Containers

##### _audit_rust

Audit Rust/Cargo

##### _audit_structure

Audit structure générale du projet

##### generate_report

Générer rapport d'audit

**Paramètres :**

- `result`

##### save_report

Sauvegarder le rapport

**Paramètres :**

- `result`
- `output_path`

---

### robotics_ci

Robotics CI - CI/CD spécialisé pour projets robotiques
======================================================

Système CI/CD adapté aux projets Reachy/ROS2 :
- Tests ROS2
- Build Docker
- Compilation Rust
- Validation robotique
- Déploiement automatisé

#### Classes

##### CIConfig

Configuration CI/CD

##### CIResult

Résultat d'exécution CI/CD

##### RoboticsCI

Système CI/CD spécialisé robotique

**Méthodes :**

- `__init__()`
- `create_github_workflow()`
- `create_docker_compose_ci()`
- `run_ci_pipeline()`
- `_run_ros2_validation()`
- `_run_docker_build()`
- `_run_rust_build()`
- `_run_tests()`
- `_run_deployment()`
- `_collect_artifacts()`
- `generate_ci_report()`
- `setup_ci_environment()`

#### Fonctions

##### __init__

**Paramètres :**

- `project_path`

##### create_github_workflow

Créer un workflow GitHub Actions pour robotique

##### create_docker_compose_ci

Créer docker-compose pour CI

##### run_ci_pipeline

Exécuter le pipeline CI/CD complet

**Paramètres :**

- `config`

##### _run_ros2_validation

Exécuter validation ROS2

##### _run_docker_build

Exécuter build Docker

##### _run_rust_build

Exécuter build Rust

##### _run_tests

Exécuter tests

##### _run_deployment

Exécuter déploiement

##### _collect_artifacts

Collecter les artifacts

##### generate_ci_report

Générer rapport CI/CD

**Paramètres :**

- `result`

##### setup_ci_environment

Configurer l'environnement CI/CD

---

### ros2_validator

ROS2 Validator - Validation spécialisée ROS2
============================================

Validation complète des workspaces ROS2 :
- Structure workspace
- Packages et dépendances
- Launch files
- URDF/XACRO
- Build system

#### Classes

##### ROS2PackageInfo

Informations sur un package ROS2

##### ROS2ValidationResult

Résultat de validation ROS2

##### ROS2Validator

Validateur spécialisé ROS2

**Méthodes :**

- `__init__()`
- `validate_workspace()`
- `_analyze_package()`
- `_detect_package_type()`
- `_check_build_system()`
- `validate_launch_files()`
- `validate_urdf_files()`
- `generate_validation_report()`

#### Fonctions

##### __init__

**Paramètres :**

- `workspace_path`

##### validate_workspace

Validation complète du workspace ROS2

##### _analyze_package

Analyser un package ROS2

**Paramètres :**

- `package_dir`

##### _detect_package_type

Détecter le type de package ROS2

**Paramètres :**

- `package_dir`

##### _check_build_system

Vérifier si le build system est configuré

##### validate_launch_files

Valider les fichiers launch

##### validate_urdf_files

Valider les fichiers URDF/XACRO

##### generate_validation_report

Générer rapport de validation

**Paramètres :**

- `result`

---

### rust_analyzer

Rust Analyzer - Analyse spécialisée Rust pour robotique
=======================================================

Analyse des projets Rust dans l'écosystème robotique :
- Validation Cargo.toml
- Dépendances ROS2 Rust
- Optimisations de compilation
- Intégration avec Reachy

#### Classes

##### CargoDependency

Dépendance Cargo

##### RustProjectInfo

Informations sur un projet Rust

##### RustAnalysisResult

Résultat d'analyse Rust

##### RustAnalyzer

Analyseur spécialisé Rust pour robotique

**Méthodes :**

- `__init__()`
- `analyze_rust_projects()`
- `_analyze_cargo_project()`
- `_parse_dependencies()`
- `_is_robotics_dependency()`
- `_analyze_build_targets()`
- `_check_rust_build_system()`
- `_calculate_optimization_score()`
- `_check_robotics_integration()`
- `validate_cargo_toml()`
- `generate_rust_report()`
- `create_rust_template()`

#### Fonctions

##### __init__

**Paramètres :**

- `project_path`

##### analyze_rust_projects

Analyser tous les projets Rust du projet

##### _analyze_cargo_project

Analyser un projet Cargo

**Paramètres :**

- `cargo_file`

##### _parse_dependencies

Parser les dépendances Cargo

**Paramètres :**

- `deps_dict`

##### _is_robotics_dependency

Vérifier si c'est une dépendance robotique

**Paramètres :**

- `dep`

##### _analyze_build_targets

Analyser les targets de build

**Paramètres :**

- `project_path`

##### _check_rust_build_system

Vérifier si le build system Rust est configuré

##### _calculate_optimization_score

Calculer le score d'optimisation

**Paramètres :**

- `projects`

##### _check_robotics_integration

Vérifier l'intégration robotique

**Paramètres :**

- `projects`
- `issues`
- `recommendations`

##### validate_cargo_toml

Valider un fichier Cargo.toml

**Paramètres :**

- `cargo_file`

##### generate_rust_report

Générer rapport d'analyse Rust

**Paramètres :**

- `result`

##### create_rust_template

Créer un template Cargo.toml pour robotique

**Paramètres :**

- `project_name`

---

### artistic_templates

#### Fonctions

##### get_artistic_templates

Retourne les templates de code pour projets artistiques.

---

### base_templates

#### Fonctions

##### get_base_templates

Retourne les templates de base pour tous les projets.

---

### ath-audit

#### Fonctions

##### main

---

### ath-build

#### Fonctions

##### main

---

### ath-coverage

#### Fonctions

##### main

---

### ath-lint

#### Fonctions

##### main

---

### ath-test

#### Fonctions

##### main

---

### athalia_unified

Athalia Unified - Pipeline d'industrialisation IA complet
Interface unifiée pour tous les modules Athalia

#### Classes

##### AthaliaOrchestrator

**Méthodes :**

- `industrialize_project()`
- `audit_project()`
- `scan_projects()`

#### Fonctions

##### main

Fonction principale du CLI unifié

##### industrialize_project

**Paramètres :**

- `project_path`
- `config`

##### audit_project

**Paramètres :**

- `project_path`

##### scan_projects

**Paramètres :**

- `project_path`

---

### debug_correction

Script de débogage pour le système de correction

#### Fonctions

##### test_correction

Test simple de correction

---

### athalia_robotics_integration

Intégration Robotique Athalia
=============================

Script simple pour utiliser le module robotique avec Athalia

#### Fonctions

##### main

Fonction principale d'intégration

---

### demo_robotics

Démonstration du module Robotics Athalia
========================================

Script de démonstration pour tester toutes les fonctionnalités robotiques :
- Audit Reachy
- Validation ROS2
- Gestion Docker
- Analyse Rust
- CI/CD robotique

#### Fonctions

##### demo_reachy_auditor

Démonstration de l'auditeur Reachy

##### demo_ros2_validator

Démonstration du validateur ROS2

##### demo_docker_robotics

Démonstration du gestionnaire Docker

##### demo_rust_analyzer

Démonstration de l'analyseur Rust

##### demo_robotics_ci

Démonstration du CI/CD robotique

##### create_sample_project

Créer un projet exemple pour la démonstration

##### main

Fonction principale de démonstration

---

### api_distillation

#### Classes

##### PromptRequest

#### Fonctions

##### distill_ia

**Paramètres :**

- `req`

##### feedback

**Paramètres :**

- `req`

---

### athalia-coordinator

🚀 ATHALIA INTELLIGENT COORDINATOR
==================================
Système de coordination intelligente qui :
- Gère tous les modules Athalia
- Apprend de chaque action
- Coordonne les interactions entre modules
- Met à jour la documentation automatiquement
- Optimise les performances du système

#### Classes

##### ModuleInfo

Informations sur un module

##### ActionRecord

Enregistrement d'une action

##### AthaliaCoordinator

Coordinateur intelligent pour Athalia

**Méthodes :**

- `__init__()`
- `_init_databases()`
- `_discover_modules()`
- `record_action()`
- `get_module_recommendations()`
- `analyze_system_health()`
- `update_documentation()`
- `_update_alias_documentation()`
- `coordinate_action()`
- `get_learning_insights()`
- `_generate_recommendations()`

#### Fonctions

##### main

Fonction principale

##### __init__

**Paramètres :**

- `root_path`

##### _init_databases

Initialiser les bases de données

##### _discover_modules

Découvrir tous les modules disponibles

##### record_action

Enregistrer une action pour l'apprentissage

**Paramètres :**

- `action`
- `module`
- `success`
- `duration`
- `details`
- `context`

##### get_module_recommendations

Obtenir des recommandations de modules basées sur le contexte

**Paramètres :**

- `context`

##### analyze_system_health

Analyser la santé du système

##### update_documentation

Mettre à jour la documentation automatiquement

##### _update_alias_documentation

Mettre à jour la documentation des alias

##### coordinate_action

Coordonner une action entre les modules

**Paramètres :**

- `action`
- `target`
- `context`

##### get_learning_insights

Obtenir des insights d'apprentissage

##### _generate_recommendations

Générer des recommandations basées sur l'apprentissage

**Paramètres :**

- `learning_data`

---

### athalia-doc-generator

📚 ATHALIA DOCUMENTATION GENERATOR
==================================
Générateur automatique de documentation qui :
- Met à jour tous les fichiers de documentation
- Génère des guides d'utilisation
- Crée des index automatiques
- Synchronise la documentation avec le code

#### Classes

##### AthaliaDocGenerator

Générateur de documentation automatique

**Méthodes :**

- `__init__()`
- `generate_main_index()`
- `generate_alias_documentation()`
- `generate_modules_documentation()`
- `generate_usage_guide()`
- `generate_all_documentation()`
- `update_documentation()`

#### Fonctions

##### main

Fonction principale

##### __init__

**Paramètres :**

- `root_path`

##### generate_main_index

Générer l'index principal de la documentation

##### generate_alias_documentation

Générer la documentation des alias

##### generate_modules_documentation

Générer la documentation des modules

##### generate_usage_guide

Générer le guide d'utilisation

##### generate_all_documentation

Générer toute la documentation

##### update_documentation

Mettre à jour la documentation existante

---

### athalia-intelligent-orchestrator

🎯 ATHALIA INTELLIGENT ORCHESTRATOR
===================================
Orchestrateur intelligent qui :
- Utilise les insights du super cerveau
- Coordonne tous les modules de manière optimale
- Apprend des patterns d'exécution
- Optimise les performances en temps réel
- Gère les dépendances intelligemment

#### Classes

##### TaskDefinition

Définition d'une tâche

##### ExecutionResult

Résultat d'exécution d'une tâche

##### OrchestrationPlan

Plan d'orchestration

##### AthaliaIntelligentOrchestrator

Orchestrateur intelligent pour Athalia

**Méthodes :**

- `__init__()`
- `_init_database()`
- `_load_config()`
- `load_super_brain_insights()`
- `create_intelligent_orchestration_plan()`
- `_create_complete_pipeline_tasks()`
- `_create_audit_pipeline_tasks()`
- `_create_test_pipeline_tasks()`
- `_create_default_pipeline_tasks()`
- `_optimize_execution_order()`
- `_create_parallel_groups()`
- `_execute_task()`
- `_save_execution_results()`
- `get_performance_insights()`

#### Fonctions

##### main

Fonction principale

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données d'orchestration

##### _load_config

Charger la configuration

##### load_super_brain_insights

Charger les insights du super cerveau

##### create_intelligent_orchestration_plan

Créer un plan d'orchestration intelligent

**Paramètres :**

- `target_action`

##### _create_complete_pipeline_tasks

Créer les tâches pour le pipeline complet

##### _create_audit_pipeline_tasks

Créer les tâches pour le pipeline d'audit

##### _create_test_pipeline_tasks

Créer les tâches pour le pipeline de tests

##### _create_default_pipeline_tasks

Créer les tâches par défaut

##### _optimize_execution_order

Optimiser l'ordre d'exécution basé sur les insights

**Paramètres :**

- `tasks`
- `insights`

##### _create_parallel_groups

Créer des groupes de tâches parallèles

**Paramètres :**

- `tasks`
- `execution_order`

##### _execute_task

Exécuter une tâche individuelle

**Paramètres :**

- `task`
- `project_path`

##### _save_execution_results

Sauvegarder les résultats d'exécution

**Paramètres :**

- `results`

##### get_performance_insights

Obtenir des insights de performance

##### dfs

**Paramètres :**

- `task_name`

---

### athalia-super-brain

🧠 ATHALIA SUPER BRAIN
======================
Super cerveau intelligent qui :
- Analyse toute l'architecture du projet
- Détecte les doublons et erreurs
- Optimise les performances
- Coordonne tous les modules intelligemment
- Apprend et s'améliore continuellement

#### Classes

##### ModuleAnalysis

Analyse d'un module

##### DuplicateAnalysis

Analyse des doublons

##### PerformanceIssue

Problème de performance

##### ArchitectureMapping

Mapping de l'architecture

##### AthaliaSuperBrain

Super cerveau intelligent pour Athalia

**Méthodes :**

- `__init__()`
- `_init_database()`
- `_load_config()`
- `analyze_entire_architecture()`
- `_analyze_all_modules()`
- `_analyze_single_module()`
- `_calculate_complexity()`
- `_detect_module_issues()`
- `_calculate_performance_score()`
- `_extract_dependencies()`
- `_detect_duplicates()`
- `_analyze_performance()`
- `_build_dependency_graph()`
- `_generate_recommendations()`
- `_save_analysis()`
- `get_optimization_plan()`
- `generate_intelligent_coordination()`

#### Fonctions

##### main

Fonction principale

##### __init__

**Paramètres :**

- `root_path`

##### _init_database

Initialiser la base de données du super cerveau

##### _load_config

Charger la configuration

##### analyze_entire_architecture

Analyser toute l'architecture du projet

##### _analyze_all_modules

Analyser tous les modules du projet

##### _analyze_single_module

Analyser un module individuel

**Paramètres :**

- `file_path`
- `module_type`

##### _calculate_complexity

Calculer la complexité cyclomatique

**Paramètres :**

- `tree`

##### _detect_module_issues

Détecter les problèmes dans un module

**Paramètres :**

- `tree`
- `content`

##### _calculate_performance_score

Calculer un score de performance

**Paramètres :**

- `tree`
- `content`

##### _extract_dependencies

Extraire les dépendances d'un module

**Paramètres :**

- `imports`
- `module_type`

##### _detect_duplicates

Détecter les doublons dans le code

**Paramètres :**

- `modules`

##### _analyze_performance

Analyser les problèmes de performance

**Paramètres :**

- `modules`

##### _build_dependency_graph

Construire le graphe de dépendances

**Paramètres :**

- `modules`

##### _generate_recommendations

Générer des recommandations d'amélioration

**Paramètres :**

- `modules`
- `duplicates`
- `performance_issues`

##### _save_analysis

Sauvegarder l'analyse dans la base de données et le fichier JSON

**Paramètres :**

- `architecture`

##### get_optimization_plan

Générer un plan d'optimisation

##### generate_intelligent_coordination

Générer un plan de coordination intelligente

---

### benchmark_distillation

#### Fonctions

##### main

---

### cleanup_workspace

Script de nettoyage automatique du workspace Athalia
Maintient l'organisation et supprime les fichiers parasites

#### Fonctions

##### load_paths_config

Charge la configuration des f

##### cleanup_macos_files

Supprime les fichiers parasites f

##### cleanup_cache_dirs

Nettoie les dossiers de f

##### organize_files

Organise les fichiers selon la structure f

##### remove_empty_files

Supprime les fichiers f

##### main

Fonction f

---

### identify_problematic_tests

Script pour identifier les tests problématiques qui pourraient faire échouer la CI

#### Fonctions

##### find_problematic_tests

Identifie les tests problématiques

##### suggest_fixes

Suggère des corrections pour les problèmes identifiés

**Paramètres :**

- `problems`

##### generate_ci_safe_test_list

Génère une liste de tests sûrs pour la CI

##### main

Fonction principale

---

### test_prompts_complet

Script de test complet pour tous les types de prompts d'Athalia

#### Fonctions

##### run_prompt_category

Test une catégorie de prompts.

**Paramètres :**

- `category_name`
- `prompts`
- `ai`
- `orch`

##### main

Fonction principale de test.

---

### test_prompts_rapide

Script de test rapide pour les prompts les plus importants d'Athalia

#### Fonctions

##### run_prompt_rapide

Test rapide d'un prompt.

**Paramètres :**

- `prompt`
- `description`
- `ai`
- `orch`

##### main

Test rapide des prompts essentiels.

---

### validation_continue

Validation Continue d'Athalia/Arkalia
Surveillance automatique et détection de régressions

#### Classes

##### ValidationContinue

**Méthodes :**

- `__init__()`
- `test_rapide()`
- `test_demarrage()`
- `test_imports()`
- `test_generation_mini()`
- `test_correction_basique()`
- `detecter_regression()`
- `demarrer_surveillance()`
- `arreter_surveillance()`
- `alerter_regression()`
- `generer_rapport_alerte()`
- `sauvegarder_historique()`
- `charger_historique()`
- `generer_rapport_tendance()`

#### Fonctions

##### __init__

**Paramètres :**

- `intervalle_minutes`

##### test_rapide

Test rapide pour validation continue (5-10 secondes)

##### test_demarrage

Test: Athalia démarre-t-il ?

##### test_imports

Test: Les imports fonctionnent-ils ?

##### test_generation_mini

Test: Génération d'un mini-projet

##### test_correction_basique

Test: Correction basique

##### detecter_regression

Détecte les régressions par rapport à l'historique

**Paramètres :**

- `validation_actuelle`

##### demarrer_surveillance

Démarre la surveillance continue

##### arreter_surveillance

Arrête la surveillance continue

##### alerter_regression

Génère une alerte de régression

**Paramètres :**

- `validation`
- `regression`

##### generer_rapport_alerte

Génère un rapport d'alerte détaillé

**Paramètres :**

- `alerte`

##### sauvegarder_historique

Sauvegarde l'historique des validations

##### charger_historique

Charge l'historique des validations

##### generer_rapport_tendance

Génère un rapport de tendance basé sur l'historique

##### boucle_surveillance

---

### validation_dashboard_simple

Dashboard de Validation Simple - Athalia/Arkalia
Version simplifiée qui fonctionne directement

#### Classes

##### ValidationDashboardHandler

**Méthodes :**

- `do_GET()`
- `do_POST()`
- `send_validation_result()`
- `send_history()`
- `end_headers()`

#### Fonctions

##### run_dashboard

Lance le dashboard de validation

**Paramètres :**

- `port`

##### do_GET

##### do_POST

##### send_validation_result

Envoie le résultat de validation en temps réel

##### send_history

Envoie l'historique des validations

##### end_headers

---

### validation_objective

Validation Objective d'Athalia/Arkalia
Tests qui ne peuvent pas mentir - Mesures concrètes et indépendantes

#### Classes

##### ValidationObjective

**Méthodes :**

- `__init__()`
- `test_generation_et_compilation()`
- `test_correction_reelle()`
- `test_robustesse_cas_limites()`
- `test_performance_benchmark()`
- `test_qualite_code_genere()`
- `validation_complete()`
- `generer_rapport_objectif()`

#### Fonctions

##### __init__

##### test_generation_et_compilation

Test 1: Le code généré compile-t-il vraiment ?

##### test_correction_reelle

Test 2: Athalia corrige-t-il vraiment les erreurs ?

##### test_robustesse_cas_limites

Test 3: Athalia gère-t-il gracieusement les cas d'erreur ?

##### test_performance_benchmark

Test 4: Performance vs solution manuelle

##### test_qualite_code_genere

Test 5: Qualité objective du code généré

##### validation_complete

Validation complète objective

##### generer_rapport_objectif

Génère un rapport objectif et détaillé

**Paramètres :**

- `resultats`
- `temps_total`

---

### demo.launch

#### Fonctions

##### generate_launch_description

---

### analyse_integration_orchestrateur

🔍 ANALYSE D'INTÉGRATION ORCHESTRATEUR
=====================================
Script pour analyser l'intégration actuelle de l'orchestrateur unifié
et identifier les modules manquants.

#### Classes

##### ModuleIntegration

Informations sur l'intégration d'un module

##### IntegrationAnalysis

Analyse d'intégration complète

##### OrchestratorIntegrationAnalyzer

Analyseur d'intégration de l'orchestrateur

**Méthodes :**

- `__init__()`
- `analyze_orchestrator_integration()`
- `_get_all_athalia_modules()`
- `_analyze_orchestrator_file()`
- `_analyze_imports()`
- `_analyze_usage()`
- `_analyze_integration_status()`
- `_create_empty_analysis()`
- `_generate_integration_recommendations()`
- `generate_integration_report()`

#### Fonctions

##### main

Fonction principale

##### __init__

**Paramètres :**

- `root_path`

##### analyze_orchestrator_integration

Analyser l'intégration de l'orchestrateur

##### _get_all_athalia_modules

Obtenir tous les modules athalia_core

##### _analyze_orchestrator_file

Analyser le fichier de l'orchestrateur

##### _analyze_imports

Analyser les imports de l'orchestrateur

**Paramètres :**

- `tree`
- `content`

##### _analyze_usage

Analyser l'utilisation des modules

**Paramètres :**

- `tree`
- `content`

##### _analyze_integration_status

Analyser le statut d'intégration

**Paramètres :**

- `all_modules`

##### _create_empty_analysis

Créer une analyse vide si l'orchestrateur n'existe pas

**Paramètres :**

- `all_modules`

##### _generate_integration_recommendations

Générer des recommandations d'intégration

**Paramètres :**

- `analysis`

##### generate_integration_report

Générer un rapport d'intégration

**Paramètres :**

- `analysis`

---

### analyze_intelligence_usage

🔍 ANALYSE DE L'UTILISATION DE L'INTELLIGENCE ET DÉTECTION DE DOUBLONS
=====================================================================
Script pour analyser tous les modules intelligents et détecter les doublons.

#### Classes

##### ModuleInfo

Informations sur un module

##### DuplicateInfo

Information sur un doublon

##### IntelligenceAnalyzer

Analyseur de l'utilisation de l'intelligence

**Méthodes :**

- `__init__()`
- `discover_intelligent_modules()`
- `_analyze_module()`
- `detect_duplicates()`
- `_calculate_similarity()`
- `_generate_duplicate_recommendation()`
- `analyze_intelligence_usage()`
- `generate_report()`

#### Fonctions

##### main

Analyse complète de l'utilisation de l'intelligence

##### __init__

**Paramètres :**

- `root_path`

##### discover_intelligent_modules

Découvrir tous les modules intelligents

##### _analyze_module

Analyser un module Python

**Paramètres :**

- `file_path`
- `module_type`

##### detect_duplicates

Détecter les doublons entre modules

##### _calculate_similarity

Calculer la similarité entre deux modules

**Paramètres :**

- `module1`
- `module2`

##### _generate_duplicate_recommendation

Générer une recommandation pour un doublon

**Paramètres :**

- `module1`
- `module2`
- `similarity`

##### analyze_intelligence_usage

Analyser l'utilisation de l'intelligence

##### generate_report

Générer un rapport complet

---

### analyze_orchestrators_detailed

🎯 ANALYSE DÉTAILLÉE DES ORCHESTRATEURS
=======================================
Analyse détaillée pour détecter les doublons fonctionnels entre orchestrateurs.

#### Classes

##### OrchestratorInfo

Informations détaillées sur un orchestrateur

##### OrchestratorAnalyzer

Analyseur détaillé des orchestrateurs

**Méthodes :**

- `__init__()`
- `analyze_orchestrators()`
- `_analyze_orchestrator_file()`
- `_extract_responsibilities()`
- `_extract_dependencies()`
- `detect_functional_duplicates()`
- `_calculate_functional_similarity()`
- `_generate_functional_recommendation()`
- `generate_detailed_report()`

#### Fonctions

##### main

Analyse détaillée des orchestrateurs

##### __init__

##### analyze_orchestrators

Analyser tous les orchestrateurs

##### _analyze_orchestrator_file

Analyser un fichier orchestrateur

**Paramètres :**

- `file_path`

##### _extract_responsibilities

Extraire les responsabilités du code

**Paramètres :**

- `content`

##### _extract_dependencies

Extraire les dépendances

**Paramètres :**

- `content`

##### detect_functional_duplicates

Détecter les doublons fonctionnels

##### _calculate_functional_similarity

Calculer la similarité fonctionnelle

**Paramètres :**

- `orch1`
- `orch2`

##### _generate_functional_recommendation

Générer une recommandation fonctionnelle

**Paramètres :**

- `orch1`
- `orch2`
- `common_resp`
- `common_methods`

##### generate_detailed_report

Générer un rapport détaillé

---

### audit_complet_dossiers

🔍 AUDIT COMPLET DOSSIERS ET SOUS-DOSSIERS
==========================================
Script pour analyser chaque dossier et sous-dossier du projet Athalia.
Vérifie : utilité, implémentation, tests, documentation, intégration.

#### Classes

##### DossierInfo

Informations sur un dossier

##### ModuleInfo

Informations sur un module Python

##### AuditResult

Résultat d'audit pour un dossier

##### AuditCompletDossiers

Auditeur complet des dossiers et sous-dossiers

**Méthodes :**

- `__init__()`
- `analyser_tous_dossiers()`
- `_trouver_sous_dossiers_caches()`
- `_analyser_dossier_complet()`
- `_analyser_dossier_info()`
- `_analyser_module()`
- `_chercher_tests_associes()`
- `_chercher_documentation_associee()`
- `_verifier_integration_orchestrateur()`
- `_calculer_score_utilite()`
- `_calculer_score_implementation()`
- `_calculer_score_tests()`
- `_calculer_score_documentation()`
- `_calculer_score_integration()`
- `_generer_recommandations()`
- `_chercher_pepites()`
- `generer_rapport()`

#### Fonctions

##### main

Fonction principale

##### __init__

**Paramètres :**

- `root_path`

##### analyser_tous_dossiers

Analyser tous les dossiers et sous-dossiers

##### _trouver_sous_dossiers_caches

Trouver les sous-dossiers cachés qui pourraient contenir des pépites

##### _analyser_dossier_complet

Analyser un dossier complet

**Paramètres :**

- `dossier_path`
- `nom_dossier`

##### _analyser_dossier_info

Analyser les informations d'un dossier

**Paramètres :**

- `dossier_path`
- `nom_dossier`

##### _analyser_module

Analyser un module Python

**Paramètres :**

- `file_path`

##### _chercher_tests_associes

Chercher les tests associés à un module

**Paramètres :**

- `file_path`

##### _chercher_documentation_associee

Chercher la documentation associée à un module

**Paramètres :**

- `file_path`

##### _verifier_integration_orchestrateur

Vérifier si le module est intégré dans l'orchestrateur

**Paramètres :**

- `content`
- `imports`

##### _calculer_score_utilite

Calculer le score d'utilité

**Paramètres :**

- `dossier_info`
- `modules`

##### _calculer_score_implementation

Calculer le score d'implémentation

**Paramètres :**

- `modules`

##### _calculer_score_tests

Calculer le score des tests

**Paramètres :**

- `dossier_info`
- `modules`

##### _calculer_score_documentation

Calculer le score de documentation

**Paramètres :**

- `dossier_info`
- `modules`

##### _calculer_score_integration

Calculer le score d'intégration

**Paramètres :**

- `modules`

##### _generer_recommandations

Générer des recommandations

**Paramètres :**

- `dossier_info`
- `modules`
- `score_total`

##### _chercher_pepites

Chercher des pépites dans le dossier

**Paramètres :**

- `dossier_info`
- `modules`

##### generer_rapport

Générer un rapport complet

---

### integration_automatique

🔗 INTÉGRATION AUTOMATIQUE DES MODULES
======================================
Script pour intégrer automatiquement les modules manquants dans l'orchestrateur unifié.

#### Fonctions

##### main

Fonction principale

##### analyze_modules_for_classes

Analyser les modules pour déterminer la classe principale

**Paramètres :**

- `modules`

##### select_main_class

Sélectionner la classe principale d'un module

**Paramètres :**

- `classes`
- `module_name`

##### generate_imports

Générer les imports pour les modules

**Paramètres :**

- `module_classes`

##### get_current_imports

Obtenir les imports actuels de l'orchestrateur

##### integrate_imports

Intégrer les nouveaux imports dans le contenu

**Paramètres :**

- `content`
- `new_imports`

##### verify_integration

Vérifier l'intégration après mise à jour

---

### integration_finale_phase4

🔗 INTÉGRATION FINALE PHASE 4
=============================
Script pour intégrer les modules restants et finaliser l'intégration complète.

#### Fonctions

##### main

Fonction principale

##### analyze_modules_for_integration

Analyser les modules pour déterminer les éléments à intégrer

**Paramètres :**

- `modules`

##### select_main_class

Sélectionner la classe principale d'un module

**Paramètres :**

- `classes`
- `module_name`

##### select_main_functions

Sélectionner les fonctions principales d'un module

**Paramètres :**

- `functions`
- `module_name`

##### generate_final_imports

Générer les imports finaux pour les modules

**Paramètres :**

- `module_integrations`

##### get_current_imports

Obtenir les imports actuels de l'orchestrateur

##### integrate_final_imports

Intégrer les nouveaux imports finaux dans le contenu

**Paramètres :**

- `content`
- `new_imports`

##### verify_final_integration

Vérifier l'intégration finale après mise à jour

---

### integration_modules_fonctionnels

🔗 INTÉGRATION MODULES FONCTIONNELS
===================================
Script pour intégrer les modules fonctionnels (sans classes) dans l'orchestrateur unifié.

#### Fonctions

##### main

Fonction principale

##### analyze_modules_for_functions

Analyser les modules pour déterminer les fonctions principales

**Paramètres :**

- `modules`

##### select_main_functions

Sélectionner les fonctions principales d'un module

**Paramètres :**

- `functions`
- `module_name`

##### generate_function_imports

Générer les imports pour les modules fonctionnels

**Paramètres :**

- `module_functions`

##### get_current_imports

Obtenir les imports actuels de l'orchestrateur

##### integrate_function_imports

Intégrer les nouveaux imports de fonctions dans le contenu

**Paramètres :**

- `content`
- `new_imports`

##### verify_integration

Vérifier l'intégration après mise à jour

---

### integration_phase3

🔗 INTÉGRATION PHASE 3 : MODULES PRIORITAIRES
=============================================
Script pour intégrer les modules prioritaires restants dans l'orchestrateur unifié.

#### Fonctions

##### main

Fonction principale

##### analyze_modules_for_classes

Analyser les modules pour déterminer la classe principale

**Paramètres :**

- `modules`

##### select_main_class

Sélectionner la classe principale d'un module

**Paramètres :**

- `classes`
- `module_name`

##### generate_imports

Générer les imports pour les modules

**Paramètres :**

- `module_classes`

##### get_current_imports

Obtenir les imports actuels de l'orchestrateur

##### integrate_imports

Intégrer les nouveaux imports dans le contenu

**Paramètres :**

- `content`
- `new_imports`

##### verify_integration

Vérifier l'intégration après mise à jour

---

### simple_orchestrator_analysis

🎯 ANALYSE SIMPLE DES ORCHESTRATEURS
====================================
Analyse simple pour vérifier l'utilisation de l'intelligence.

#### Fonctions

##### analyze_file_content

Analyser le contenu d'un fichier

**Paramètres :**

- `file_path`

##### main

Analyse simple des orchestrateurs

---

### verification_integration_simple

🔍 VÉRIFICATION SIMPLE D'INTÉGRATION ORCHESTRATEUR
==================================================
Script simple pour vérifier l'intégration actuelle de l'orchestrateur unifié.

#### Fonctions

##### main

Fonction principale

---

