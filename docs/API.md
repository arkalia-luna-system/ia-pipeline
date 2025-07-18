# API Documentation - athalia-dev-setup

## Vue d'ensemble

Cette documentation décrit l'API de athalia-dev-setup.

## Modules

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

### hello_plugin

Plugin exemple : Hello Plugin

#### Fonctions

##### run

---

### export_docker_plugin

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

### test_ath_context_prompt_semantic

Test d'intégration sémantique pour ath_context_prompt

#### Fonctions

##### test_ath_context_prompt_semantic

Teste que le prompt sécurité est détecté par l'analyse sémantique/custom.

---

### test_ath_dev_boost

Tests pour ath-dev-boost

#### Fonctions

##### test_ath_dev_boost_script_exists

Test que le script ath-dev-boost existe

##### test_ath_dev_boost_executable

Test que le script est exécutable

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

### test_ath_dev_boost_menu

Test du menu interactif ath-dev-boost

#### Fonctions

##### test_ath_dev_boost_menu

Teste le menu interactif ath-dev-boost pour chaque choix.

**Paramètres :**

- `user_input`
- `expected`

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

### test_ready_check

Tests pour ready_check.py

#### Fonctions

##### test_check_ready_ok

Test que le projet est prêt

##### test_check_ready_missing

Test avec un projet manquant

---

### test_plugins

Tests pour le système de plugins dynamiques Athalia

#### Fonctions

##### test_list_plugins

##### test_load_plugin

##### test_run_all_plugins

##### test_export_docker_plugin

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

### test_continue_models

Test de présence des modèles dans la config Continue

#### Fonctions

##### test_models_presence

Vérifie la présence des modèles Claude et Mistral dans la config Continue.

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

### test_onboarding

#### Fonctions

##### test_onboarding

**Paramètres :**

- `tmp_path`

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

### test_security

#### Fonctions

##### test_security_audit_project

**Paramètres :**

- `tmp_path`

---

### test_plugins_validator

#### Fonctions

##### test_validate_plugin_ok

##### test_validate_plugin_fail

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

### test_aliases

#### Fonctions

##### test_alias_presence

Vérifie que chaque alias défini dans setup/alias.sh est bien présent et correctement écrit.
Prépare la structure pour tester leur exécution réelle à l’avenir.

**Paramètres :**

- `alias_name`

---

### test_project_importer

#### Fonctions

##### test_project_import_concept

---

### test_ci_manual

---

### test_complet_athalia

Script de test complet pour Athalia - Détection et correction automatique d'erreurs

#### Classes

##### TestCompletAthalia

Classe pour tester et corriger automatiquement le projet f

**Méthodes :**

- `__init__()`
- `safe_read_file()`
- `safe_write_file()`
- `run_complete_test()`
- `test_syntax_python()`
- `test_imports()`
- `test_fstrings()`
- `test_encoding()`
- `test_indentation()`
- `test_undefined_variables()`
- `test_logic_errors()`
- `clean_parasite_files()`
- `test_execution()`
- `fix_syntax_error()`
- `module_exists()`
- `is_defined_variable()`
- `generate_report()`

#### Fonctions

##### main

Fonction f

##### __init__

**Paramètres :**

- `project_root`

##### safe_read_file

Lit un fichier en gérant différents f

**Paramètres :**

- `file_path`

##### safe_write_file

Écrit un fichier en UTF-f

**Paramètres :**

- `file_path`
- `content`

##### run_complete_test

Exécute tous les tests et f

##### test_syntax_python

Test de syntaxe Python sur tous les fichiers .f

##### test_imports

Test des f

##### test_fstrings

Test et correction des f-strings f

##### test_encoding

Test et correction de l'f

##### test_indentation

Test et correction de l'f

##### test_undefined_variables

Test des variables non f

##### test_logic_errors

Test des erreurs de logique

##### clean_parasite_files

Nettoyage des fichiers parasites

##### test_execution

Test d'exécution des modules

##### fix_syntax_error

Tentative de correction automatique d'erreur de syntaxe

**Paramètres :**

- `file_path`
- `error_msg`

##### module_exists

Vérifie si un module existe

**Paramètres :**

- `module_name`

##### is_defined_variable

Vérifie si une variable est définie dans le contenu

**Paramètres :**

- `var_name`
- `content`

##### generate_report

Génère un rapport de test complet Athalia.

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

### test_athalia_orchestrator

#### Classes

##### TestAthaliaOrchestrator

Tests pour l'orchestrateur principal

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

Test que l'orchestrateur peut être importé

##### test_distill_ia_responses

**Paramètres :**

- `monkeypatch`

##### test_distill_audits

##### test_distill_corrections

##### test_distill_adaptive_responses

##### test_distill_genetics

##### test_cache_predictive

##### test_distillation_multi_ia_reelle

Test d'intégration : distillation réelle multi-IA (Qwen, Mistral, Mock) via l'orchestrateur.

**Paramètres :**

- `monkeypatch`

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

Test le scan de projets

##### test_invalid_project_path

Test avec un chemin de projet invalide

##### test_empty_project

Test avec un projet vide

##### fake_call_model

**Paramètres :**

- `model`
- `prompt`

##### fake_call_model

**Paramètres :**

- `model`
- `prompt`

---

### test_auto_correction_avancee

#### Classes

##### TestAutoCorrectionAvancee

Tests pour l'auto-correction avancée

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_initialisation()`
- `test_analyse_dry_run()`
- `test_generation_rapport()`

#### Fonctions

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### test_initialisation

Test de l'initialisation du module

##### test_analyse_dry_run

Test de l'analyse en mode dry-run

##### test_generation_rapport

Test de génération de rapport

---

### test_profils_utilisateur_avances

#### Classes

##### TestProfilsUtilisateurAvances

Tests pour la gestion des profils utilisateur avancés

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_initialisation()`
- `test_creation_profil()`
- `test_obtention_profil()`
- `test_enregistrement_action()`
- `test_generation_rapport()`

#### Fonctions

##### setUp

Configuration des tests

##### tearDown

Nettoyage après les tests

##### test_initialisation

Test de l'initialisation du gestionnaire

##### test_creation_profil

Test de création d'un profil utilisateur

##### test_obtention_profil

Test de récupération d'un profil utilisateur

##### test_enregistrement_action

Test de l'enregistrement d'une action utilisateur

##### test_generation_rapport

Test de génération de rapport utilisateur

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

### test_distillation

#### Classes

##### TestResponseDistiller

**Méthodes :**

- `test_majority_voting()`
- `test_empty()`
- `test_stacking()`
- `test_consensus()`
- `test_consensus_divergents()`

##### TestAuditDistiller

**Méthodes :**

- `test_weighted_average()`
- `test_empty()`

##### TestCorrectionDistiller

**Méthodes :**

- `test_best_score()`
- `test_empty()`

##### TestQualityScorer

**Méthodes :**

- `test_score_default()`

#### Fonctions

##### test_majority_voting

##### test_empty

##### test_stacking

##### test_consensus

##### test_consensus_divergents

##### test_weighted_average

##### test_empty

##### test_best_score

##### test_empty

##### test_score_default

---

### test_dashboard_unifie_simple

#### Classes

##### TestDashboardUnifieSimple

Tests pour le dashboard unifié simple

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

Test de l'initialisation du dashboard simple

##### test_enregistrement_metrique

Test de l'enregistrement d'une métrique

##### test_enregistrement_evenement

Test de l'enregistrement d'un événement

##### test_generation_rapport

Test de génération de rapport consolidé

##### test_generation_html

Test de génération du dashboard HTML

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

### test_unit_1

Tests unitaires pour setup
Généré automatiquement par Athalia

#### Classes

##### TestSetup

Tests unitaires pour setup

**Méthodes :**

- `test_read_readme_exists()`
- `test_read_readme_content()`
- `test_requirements_exists()`
- `test_requirements_content()`
- `test_setup_files_structure()`
- `test_setup_imports()`

#### Fonctions

##### test_read_readme_exists

Test que le fichier README.md existe

##### test_read_readme_content

Test que le README.md contient du contenu

##### test_requirements_exists

Test que le fichier requirements.txt existe

##### test_requirements_content

Test que requirements.txt contient des dépendances

##### test_setup_files_structure

Test de la structure des fichiers de setup

##### test_setup_imports

Test des imports de setup (skip en CI)

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

### test_unit_2

Tests unitaires pour athalia_new
Généré automatiquement par Athalia

#### Classes

##### TestAthaliaNew

Tests unitaires pour athalia_new

**Méthodes :**

- `test_project_structure_exists()`
- `test_core_modules_exist()`
- `test_config_files_exist()`
- `test_documentation_exists()`
- `test_athalia_new_imports()`
- `test_project_initialization_files()`

#### Fonctions

##### test_project_structure_exists

Test que la structure du projet existe

##### test_core_modules_exist

Test que les modules core existent

##### test_config_files_exist

Test que les fichiers de configuration existent

##### test_documentation_exists

Test que la documentation existe

##### test_athalia_new_imports

Test des imports athalia_new (skip en CI)

##### test_project_initialization_files

Test des fichiers d'initialisation du projet

---

### test_unit_3

Tests unitaires pour athalia_unified
Généré automatiquement par Athalia

#### Classes

##### TestAthaliaUnified

Tests unitaires pour athalia_unified

**Méthodes :**

- `test_athalia_unified_file_exists()`
- `test_athalia_unified_content()`
- `test_athalia_unified_enhanced_exists()`
- `test_orchestrator_structure()`
- `test_project_management_functions()`
- `test_audit_functions()`
- `test_athalia_unified_imports()`
- `test_unified_interface_consistency()`

#### Fonctions

##### test_athalia_unified_file_exists

Test que le fichier athalia_unified.py existe

##### test_athalia_unified_content

Test que athalia_unified.py contient du contenu

##### test_athalia_unified_enhanced_exists

Test que le fichier athalia_unified_enhanced.py existe

##### test_orchestrator_structure

Test de la structure de l'orchestrator

##### test_project_management_functions

Test des fonctions de gestion de projet

##### test_audit_functions

Test des fonctions d'audit

##### test_athalia_unified_imports

Test des imports athalia_unified (skip en CI)

##### test_unified_interface_consistency

Test de la cohérence de l'interface unifiée

---

### test_lint_flake8

Tests pour le linting flake8

#### Fonctions

##### test_flake8_clean

Test que le code passe flake8 sans erreurs

---

### test_unit_4

Tests unitaires pour demo_athalia
Généré automatiquement par Athalia

#### Classes

##### TestDemoAthalia

Tests unitaires pour demo_athalia

**Méthodes :**

- `test_demo_structure_exists()`
- `test_project_examples_exist()`
- `test_module_examples_exist()`
- `test_plugin_examples_exist()`
- `test_demo_documentation_exists()`
- `test_demo_configuration_exists()`
- `test_demo_imports()`
- `test_demo_functionality_structure()`

#### Fonctions

##### test_demo_structure_exists

Test que la structure de démonstration existe

##### test_project_examples_exist

Test que les exemples de projets existent

##### test_module_examples_exist

Test que les exemples de modules existent

##### test_plugin_examples_exist

Test que les exemples de plugins existent

##### test_demo_documentation_exists

Test que la documentation de démonstration existe

##### test_demo_configuration_exists

Test que la configuration de démonstration existe

##### test_demo_imports

Test des imports de démonstration (skip en CI)

##### test_demo_functionality_structure

Test de la structure fonctionnelle de démonstration

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

### test_unit_5

Tests unitaires pour athalia_quick_start
Généré automatiquement par Athalia

#### Classes

##### TestAthaliaQuickStart

Tests unitaires pour athalia_quick_start

**Méthodes :**

- `test_quick_start_structure_exists()`
- `test_quick_start_scripts_exist()`
- `test_quick_start_prompts_exist()`
- `test_quick_start_cli_exists()`
- `test_quick_start_configuration_exists()`
- `test_quick_start_documentation_exists()`
- `test_quick_start_imports()`
- `test_quick_start_functionality_structure()`
- `test_quick_start_menu_structure()`

#### Fonctions

##### test_quick_start_structure_exists

Test que la structure de quick start existe

##### test_quick_start_scripts_exist

Test que les scripts de quick start existent

##### test_quick_start_prompts_exist

Test que les prompts de quick start existent

##### test_quick_start_cli_exists

Test que l'interface CLI de quick start existe

##### test_quick_start_configuration_exists

Test que la configuration de quick start existe

##### test_quick_start_documentation_exists

Test que la documentation de quick start existe

##### test_quick_start_imports

Test des imports de quick start (skip en CI)

##### test_quick_start_functionality_structure

Test de la structure fonctionnelle de quick start

##### test_quick_start_menu_structure

Test de la structure du menu de quick start

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

### test_unit_6

#### Classes

##### TestHelloPlugin

Tests unitaires pour hello_plugin

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_run()`

#### Fonctions

##### setUp

##### tearDown

##### test_run

---

### test_unit_7

#### Classes

##### TestExportDockerPlugin

Tests unitaires pour export_docker_plugin

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_export_docker()`
- `test_analyze_dependencies()`
- `test_run()`

#### Fonctions

##### setUp

##### tearDown

##### test_export_docker

##### test_analyze_dependencies

##### test_run

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

### test_unit_9

#### Classes

##### TestMain

Tests unitaires pour main

**Méthodes :**

- `setUp()`
- `tearDown()`

#### Fonctions

##### setUp

##### tearDown

---

### test_unit_10

#### Classes

##### TestMain

Tests unitaires pour main

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_Violette_gameManager_creation()`
- `test_Violette_gameManager_process()`
- `test_main()`

#### Fonctions

##### setUp

##### tearDown

##### test_Violette_gameManager_creation

##### test_Violette_gameManager_process

##### test_main

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

### test_unit_11

#### Classes

##### TestMain

Tests unitaires pour main

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_Ai_playerManager_creation()`
- `test_Ai_playerManager_process()`
- `test_main()`

#### Fonctions

##### setUp

##### tearDown

##### test_Ai_playerManager_creation

##### test_Ai_playerManager_process

##### test_main

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

### test_unit_12

#### Classes

##### TestCi

Tests unitaires pour ci

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_generate_github_ci_yaml()`
- `test_add_coverage_badge()`

#### Fonctions

##### setUp

##### tearDown

##### test_generate_github_ci_yaml

##### test_add_coverage_badge

---

### test_agent_audit

---

### test_unit_13

#### Classes

##### TestCleanup

Tests unitaires pour cleanup

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_clean_old_tests_and_caches()`
- `test_clean_macos_files()`

#### Fonctions

##### setUp

Configuration avant chaque test

##### tearDown

Nettoyage après chaque test

##### test_clean_old_tests_and_caches

Test de la fonction clean_old_tests_and_caches

##### test_clean_macos_files

Test de la fonction clean_macos_files

---

### test_unit_14

#### Classes

##### TestMain

Tests unitaires pour main

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_menu()`
- `test_safe_input()`
- `test_main()`

#### Fonctions

##### setUp

Configuration avant chaque test

##### tearDown

Nettoyage après chaque test

##### test_menu

Test de la fonction menu

##### test_safe_input

Test de la fonction safe_input

##### test_main

Test de la fonction main (skip en CI car input interactif)

##### fake_input

---

### test_agent_network

#### Classes

##### TestAgentNetwork

**Méthodes :**

- `test_agent_network()`

#### Fonctions

##### test_agent_network

**Paramètres :**

- `mock_qwen`

---

### test_unit_15

#### Classes

##### TestOnboarding

Tests unitaires pour onboarding

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_generate_onboarding_md()`
- `test_generate_onboard_cli()`
- `test_generate_onboarding_html_advanced()`

#### Fonctions

##### setUp

Configuration avant chaque test

##### tearDown

Nettoyage après chaque test

##### test_generate_onboarding_md

Test de la fonction generate_onboarding_md

##### test_generate_onboard_cli

Test de la fonction generate_onboard_cli

##### test_generate_onboarding_html_advanced

Test de la fonction generate_onboarding_html_advanced

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

### test_unit_16

#### Classes

##### TestAudit

Tests unitaires pour audit

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_ProjectAuditor_creation()`
- `test_ProjectAuditor_audit_project()`
- `test_ProjectAuditor__analyze_structure()`
- `test_ProjectAuditor__analyze_code_quality()`
- `test_ProjectAuditor__analyze_python_file()`
- `test_ProjectAuditor__analyze_tests()`
- `test_ProjectAuditor__analyze_documentation()`
- `test_ProjectAuditor__analyze_security()`
- `test_ProjectAuditor__analyze_performance()`
- `test_ProjectAuditor__calculate_score()`
- `test_ProjectAuditor__generate_report()`
- `test_ProjectAuditor__generate_summary()`
- `test_ProjectAuditor__find_modules()`
- `test_ProjectAuditor__find_python_files()`
- `test_calculate_base_score()`
- `test_analyze_code_issues()`
- `test_generate_basic_suggestions()`
- `test_audit_code_quality()`
- `test_audit_project_intelligent()`

#### Fonctions

##### setUp

Configuration avant chaque test

##### tearDown

Nettoyage après chaque test

##### test_ProjectAuditor_creation

Test de création de ProjectAuditor

##### test_ProjectAuditor_audit_project

Test de la méthode audit_project

##### test_ProjectAuditor__analyze_structure

Test de la méthode _analyze_structure

##### test_ProjectAuditor__analyze_code_quality

Test de la méthode _analyze_code_quality

##### test_ProjectAuditor__analyze_python_file

Test de la méthode _analyze_python_file

##### test_ProjectAuditor__analyze_tests

Test de la méthode _analyze_tests

##### test_ProjectAuditor__analyze_documentation

Test de la méthode _analyze_documentation

##### test_ProjectAuditor__analyze_security

Test de la méthode _analyze_security

##### test_ProjectAuditor__analyze_performance

Test de la méthode _analyze_performance

##### test_ProjectAuditor__calculate_score

Test de la méthode _calculate_score

##### test_ProjectAuditor__generate_report

Test de la méthode _generate_report

##### test_ProjectAuditor__generate_summary

Test de la méthode _generate_summary

##### test_ProjectAuditor__find_modules

Test de la méthode _find_modules

##### test_ProjectAuditor__find_python_files

Test de la méthode _find_python_files

##### test_calculate_base_score

Test de la fonction calculate_base_score

##### test_analyze_code_issues

Test de la fonction analyze_code_issues

##### test_generate_basic_suggestions

Test de la fonction generate_basic_suggestions

##### test_audit_code_quality

Test de la fonction audit_code_quality

##### test_audit_project_intelligent

Test de la fonction audit_project_intelligent

---

### test_api_distillation

#### Fonctions

##### test_feedback

---

### test_unit_17

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestSecurity

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_security_audit_project()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_security_audit_project

Test de la fonction f

---

### test_unit_18

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestPlugins_Manager

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_list_plugins()`
- `test_load_plugin()`
- `test_run_all_plugins()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_list_plugins

Test de la fonction f

##### test_load_plugin

Test de la fonction f

##### test_run_all_plugins

Test de la fonction f

---

### test_integration_multimodal

#### Classes

##### TestIntegrationMultimodal

**Méthodes :**

- `test_multimodal_distillation()`

#### Fonctions

##### test_multimodal_distillation

---

### test_unit_19

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestPlugins_Validator

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_validate_plugin()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_validate_plugin

Test de la fonction f

---

### test_integration_autogen

#### Classes

##### TestIntegrationAutoGen

**Méthodes :**

- `test_autogen_orchestration()`

#### Fonctions

##### test_autogen_orchestration

---

### test_unit_20

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

#### Fonctions

##### test_placeholder

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

### test_unit_21

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestReady_Check

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_check_ready()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_check_ready

Test de la fonction f

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

### test_unit_22

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestProject_Importer

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_ProjectImporter_creation()`
- `test_ProjectImporter_import_project()`
- `test_ProjectImporter__scan_structure()`
- `test_ProjectImporter__detect_project_type()`
- `test_ProjectImporter__analyze_code_quality()`
- `test_ProjectImporter__generate_correction_blueprint()`
- `test_ProjectImporter__suggest_modules()`
- `test_ProjectImporter__suggest_structure()`
- `test_ProjectImporter__suggest_dependencies()`
- `test_ProjectImporter__suggest_prompts()`
- `test_ProjectImporter__suggest_enhancements()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_ProjectImporter_creation

Test de création de f

##### test_ProjectImporter_import_project

Test de la méthode f

##### test_ProjectImporter__scan_structure

Test de la méthode f

##### test_ProjectImporter__detect_project_type

Test de la méthode f

##### test_ProjectImporter__analyze_code_quality

Test de la méthode f

##### test_ProjectImporter__generate_correction_blueprint

Test de la méthode f

##### test_ProjectImporter__suggest_modules

Test de la méthode f

##### test_ProjectImporter__suggest_structure

Test de la méthode f

##### test_ProjectImporter__suggest_dependencies

Test de la méthode f

##### test_ProjectImporter__suggest_prompts

Test de la méthode f

##### test_ProjectImporter__suggest_enhancements

Test de la méthode f

---

### test_unit_23

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestProfiles

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_get_user_profile()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_get_user_profile

Test de la fonction f

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

### test_unit_26

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestCode_Linter

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_CodeLinter_creation()`
- `test_CodeLinter_run()`
- `test_CodeLinter__run_flake8()`
- `test_CodeLinter__run_black()`
- `test_CodeLinter__run_isort()`
- `test_CodeLinter__run_mypy()`
- `test_CodeLinter__run_bandit()`
- `test_CodeLinter__compute_score()`
- `test_CodeLinter_print_report()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_CodeLinter_creation

Test de création de f

##### test_CodeLinter_run

Test de la méthode f

##### test_CodeLinter__run_flake8

Test de la méthode f

##### test_CodeLinter__run_black

Test de la méthode f

##### test_CodeLinter__run_isort

Test de la méthode f

##### test_CodeLinter__run_mypy

Test de la méthode f

##### test_CodeLinter__run_bandit

Test de la méthode f

##### test_CodeLinter__compute_score

Test de la méthode f

##### test_CodeLinter_print_report

Test de la méthode f

---

### test_dashboard

#### Fonctions

##### test_benchmarks_section_present

Vérifie que la section Benchmarks et les éléments clés existent dans le dashboard.

---

### test_unit_27

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestSecurity_Auditor

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_SecurityAuditor_creation()`
- `test_SecurityAuditor_run()`
- `test_SecurityAuditor__run_bandit()`
- `test_SecurityAuditor__run_safety()`
- `test_SecurityAuditor__detect_secrets()`
- `test_SecurityAuditor__compute_score()`
- `test_SecurityAuditor__generate_recommendations()`
- `test_SecurityAuditor_print_report()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_SecurityAuditor_creation

Test de création de f

##### test_SecurityAuditor_run

Test de la méthode f

##### test_SecurityAuditor__run_bandit

Test de la méthode f

##### test_SecurityAuditor__run_safety

Test de la méthode f

##### test_SecurityAuditor__detect_secrets

Test de la méthode f

##### test_SecurityAuditor__compute_score

Test de la méthode f

##### test_SecurityAuditor__generate_recommendations

Test de la méthode f

##### test_SecurityAuditor_print_report

Test de la méthode f

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

### test_unit_28

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestAdvanced_Analytics

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_AdvancedAnalytics_creation()`
- `test_AdvancedAnalytics_run()`
- `test_AdvancedAnalytics__analyze_complexity()`
- `test_AdvancedAnalytics__calculate_complexity()`
- `test_AdvancedAnalytics__analyze_coverage()`
- `test_AdvancedAnalytics__analyze_performance()`
- `test_AdvancedAnalytics__analyze_quality()`
- `test_AdvancedAnalytics__analyze_evolution()`
- `test_AdvancedAnalytics__generate_dashboard()`
- `test_AdvancedAnalytics__generate_summary()`
- `test_AdvancedAnalytics_print_report()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_AdvancedAnalytics_creation

Test de création de f

##### test_AdvancedAnalytics_run

Test de la méthode f

##### test_AdvancedAnalytics__analyze_complexity

Test de la méthode f

##### test_AdvancedAnalytics__calculate_complexity

Test de la méthode f

##### test_AdvancedAnalytics__analyze_coverage

Test de la méthode f

##### test_AdvancedAnalytics__analyze_performance

Test de la méthode f

##### test_AdvancedAnalytics__analyze_quality

Test de la méthode f

##### test_AdvancedAnalytics__analyze_evolution

Test de la méthode f

##### test_AdvancedAnalytics__generate_dashboard

Test de la méthode f

##### test_AdvancedAnalytics__generate_summary

Test de la méthode f

##### test_AdvancedAnalytics_print_report

Test de la méthode f

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

### test_unit_30

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestProject_Types

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_ProjectType_creation()`
- `test_get_project_config()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_ProjectType_creation

Test de création de f

##### test_get_project_config

Test de la fonction f

---

### test_unit_31

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestProject_Classifier

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_classify_project()`
- `test_get_project_name()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_classify_project

Test de la fonction f

##### test_get_project_name

Test de la fonction f

---

### test_ci_ultra_fast

Tests CI ultra-rapides - Vérifications essentielles uniquement
Exécution: < 10 secondes

#### Classes

##### TestCIUltraFast

Tests CI ultra-rapides pour validation essentielle

**Méthodes :**

- `test_python_version()`
- `test_essential_imports()`
- `test_config_files_exist()`
- `test_syntax_check_core()`
- `test_no_critical_errors()`
- `test_requirements_parseable()`
- `test_git_clean()`
- `test_essential_structure()`

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

##### test_git_clean

Test que le projet est propre (pas de fichiers temporaires)

##### test_essential_structure

Vérifie la structure essentielle du projet

---

### test_unit_32

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

##### TestArtistic_Templates

Tests unitaires pour f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_get_artistic_templates()`

#### Fonctions

##### test_placeholder

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_get_artistic_templates

Test de la fonction f

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

### test_unit_33

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

#### Fonctions

##### test_placeholder

---

### test_unit_34

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

#### Fonctions

##### test_placeholder

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

### test_unit_35

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

#### Fonctions

##### test_placeholder

---

### test_unit_36

#### Classes

##### TestPlaceholder

**Méthodes :**

- `test_placeholder()`

#### Fonctions

##### test_placeholder

---

### test_integration_1

#### Classes

##### TestIntegration

Tests dict_data'f

**Méthodes :**

- `setUp()`
- `tearDown()`
- `test_project_import()`
- `test_basic_functionality()`
- `test_error_handling()`

#### Fonctions

##### setUp

Configuration avant chaque f

##### tearDown

Nettoyage après chaque f

##### test_project_import

Test dict_data'import du f

##### test_basic_functionality

Test de fonctionnalité de f

##### test_error_handling

Test de gestion dict_data'f

---

### test_performance_1

#### Classes

##### TestPerformance

Tests de performance Athalia

**Méthodes :**

- `setUp()`
- `test_import_performance()`
- `test_memory_usage()`
- `test_execution_time()`

#### Fonctions

##### setUp

##### test_import_performance

##### test_memory_usage

##### test_execution_time

---

### test_aliases_execution

#### Fonctions

##### test_alias_execution

Teste l'exécution de chaque alias non interactif dans un sous-shell interactif.
Vérifie que l'exit code est 0 (pas d'erreur fatale).

**Paramètres :**

- `alias_name`

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

### test_aliases_unified

#### Classes

##### TestAliasesUnified

Tests complets pour le système d'alias unifié Athalia

**Méthodes :**

- `test_alias_file_exists()`
- `test_alias_file_readable()`
- `test_all_aliases_defined()`
- `test_git_aliases_present()`
- `test_athalia_core_aliases_present()`
- `test_athalia_functions_present()`
- `test_workflow_aliases_present()`
- `test_functions_present()`
- `test_autocompletion_configured()`
- `test_athalia_root_exported()`
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
- `test_syntax_validity()`
- `test_help_function_content()`
- `test_status_function_content()`
- `test_initialization_message()`

#### Fonctions

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

##### test_functions_present

Vérifie la présence des fonctions d'aide

##### test_autocompletion_configured

Vérifie que l'auto-complétion est configurée

##### test_athalia_root_exported

Vérifie que ATHALIA_ROOT est exporté

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

##### test_syntax_validity

Vérifie la validité syntaxique du fichier bash

##### test_help_function_content

Vérifie le contenu de la fonction d'aide

##### test_status_function_content

Vérifie le contenu de la fonction de statut

##### test_initialization_message

Vérifie le message d'initialisation

---

### test_ci_robust

Tests CI robustes - Vérifications essentielles pour la CI
Exécution: < 5 secondes

#### Classes

##### TestCIRobust

Tests CI robustes pour validation essentielle

**Méthodes :**

- `test_imports_core_modules()`
- `test_syntax_check()`
- `test_requirements_installable()`
- `test_config_files_exist()`
- `test_test_discovery()`
- `test_core_functionality()`
- `test_no_hardcoded_paths()`
- `test_encoding_consistency()`

#### Fonctions

##### test_imports_core_modules

Vérifie les imports des modules core

##### test_syntax_check

Vérifie la syntaxe des fichiers Python essentiels

##### test_requirements_installable

Vérifie que requirements.txt est installable

##### test_config_files_exist

Vérifie l'existence des fichiers de configuration

##### test_test_discovery

Vérifie que les tests peuvent être découverts

##### test_core_functionality

Test de fonctionnalités core essentielles

##### test_no_hardcoded_paths

Vérifie qu'il n'y a pas de chemins hardcodés problématiques

##### test_encoding_consistency

Test que tous les fichiers Python sont encodés en UTF-8

---

### test_ci_final

Test CI Final - Vérifications complètes pour la CI
Exécution: < 30 secondes

#### Classes

##### TestCIFinal

Tests CI finaux pour validation complète

**Méthodes :**

- `test_environment_setup()`
- `test_core_imports()`
- `test_configuration_files()`
- `test_syntax_validation()`
- `test_no_corrupted_files()`
- `test_requirements_quality()`
- `test_project_structure()`
- `test_test_discovery()`
- `test_core_functionality()`
- `test_performance_ci()`
- `test_no_hardcoded_paths()`

#### Fonctions

##### test_environment_setup

Vérifie l'environnement CI

##### test_core_imports

Vérifie tous les imports core

##### test_configuration_files

Vérifie tous les fichiers de configuration

##### test_syntax_validation

Vérifie la syntaxe de tous les fichiers Python

##### test_no_corrupted_files

Vérifie qu'il n'y a pas de fichiers corrompus

##### test_requirements_quality

Vérifie la qualité du fichier requirements.txt

##### test_project_structure

Vérifie la structure du projet

##### test_test_discovery

Vérifie que les tests peuvent être découverts

##### test_core_functionality

Test de fonctionnalités core essentielles

##### test_performance_ci

Test de performance pour la CI

##### test_no_hardcoded_paths

Vérifie qu'il n'y a pas de chemins hardcodés problématiques

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

### test_cli_robustesse

Test d'intégration CLI robuste pour Athalia

#### Fonctions

##### test_cli_robustesse

Test simple de la CLI sans interaction complexe

---

### test_yaml_validity

Test de validité YAML pour tous les fichiers openapi.yaml du repo

#### Fonctions

##### test_all_openapi_yaml_valid

Vérifie que tous les fichiers openapi*.yaml sont valides.

---

### test_ath_test

#### Fonctions

##### test_ath_test_runs

Test désactivé car il cause une récursivité infinie

---

### test_ath_lint

#### Fonctions

##### test_ath_lint_runs

---

### test_ath_build

#### Fonctions

##### test_ath_build_runs

---

### test_ath_audit

#### Fonctions

##### test_ath_audit_runs

---

### test_ath_coverage

#### Fonctions

##### cleanup_coverage_files

##### test_ath_coverage_runs

Test désactivé car il cause une récursivité infinie

---

### main

Auto - docstring ajoutée

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

### auto_correction_avancee

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

### profils_utilisateur_avances

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

### dashboard_unifie_simple

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

### main

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

### test_booster_ia_mon-projet

#### Fonctions

##### test_prompts_presence

##### test_ath_dev_boost

##### test_ath_context_prompt

##### test_alias_sh

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

### ath_context_prompt

---

### agent_qwen

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

### agent_audit

#### Classes

##### AuditAgent

**Méthodes :**

- `act()`

#### Fonctions

##### act

**Paramètres :**

- `prompt`

---

### agent_network

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

### benchmark_distillation

#### Fonctions

##### main

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

### security

#### Fonctions

##### security_audit_project

**Paramètres :**

- `project_path`

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

### dashboard

#### Fonctions

##### show_benchmarks

##### main

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

### intelligent_auditor

#### Classes

##### IntelligentAuditor

Auditeur intelligent pour analyse automatique des projets

**Méthodes :**

- `__init__()`
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

### auto_cleaner

#### Classes

##### AutoCleaner

Nettoyeur automatique pour Athalia

**Méthodes :**

- `__init__()`
- `clean_project()`
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

### auto_documenter

#### Classes

##### AutoDocumenter

Générateur de documentation automatique

**Méthodes :**

- `__init__()`
- `_load_translations()`
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

- `lang`

##### _load_translations

**Paramètres :**

- `lang`

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

##### generate_tests

Génération complète de tests pour un projet

**Paramètres :**

- `project_path`

##### _analyze_modules

Analyse les modules pour générer les f

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

Exécute les tests générés et collecte les f

##### _get_created_files

Retourne la liste des fichiers f

##### generate_test_report

Génère un rapport de tests

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

### athalia_orchestrator

#### Classes

##### AthaliaOrchestrator

**Méthodes :**

- `__init__()`
- `industrialize_project()`
- `_run_audit()`
- `_run_cleanup()`
- `_run_documentation()`
- `_run_testing()`
- `_run_cicd()`
- `_generate_final_report()`
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

### fr

Traductions françaises pour Athalia

#### Fonctions

##### get_translation

Retourne les traductions françaises

**Paramètres :**

- `lang`

---

### en

English translations for Athalia

#### Fonctions

##### get_translation

Returns English translations

**Paramètres :**

- `lang`

---

### ath-test

#### Fonctions

##### main

---

### ath-lint

#### Fonctions

##### main

---

### ath-build

#### Fonctions

##### main

---

### ath-audit

#### Fonctions

##### main

---

### ath-coverage

#### Fonctions

##### main

---

