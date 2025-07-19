# API Documentation - athalia_core

## Vue d'ensemble

Cette documentation décrit l'API de athalia_core.

## Modules

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

