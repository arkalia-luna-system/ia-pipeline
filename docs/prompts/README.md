# Documentation des Prompts Athalia

## Vue d'ensemble

Ce répertoire contient la documentation et les templates de prompts utilisés par Athalia pour l'analyse et la génération de code.

## Structure

- `code_refactor.yaml` - Prompts pour le refactoring de code
- `custom_prompts.yaml` - Prompts personnalisés
- `design_review.md` - Prompts pour la revue de design
- `dev_debug.yaml` - Prompts pour le débogage
- `security_audit.md` - Prompts pour l'audit de sécurité
- `test_strategy.md` - Prompts pour la stratégie de tests
- `ux_fun_boost.md` - Prompts pour l'amélioration UX

## Utilisation

Les prompts sont utilisés par les modules suivants :
- `athalia_core.intelligent_auditor`
- `athalia_core.auto_tester`
- `athalia_core.auto_cleaner`
- `athalia_core.advanced_analytics`

## Format

Les prompts sont au format YAML ou Markdown selon leur utilisation :
- YAML pour les prompts structurés avec paramètres
- Markdown pour les prompts textuels longs

## Personnalisation

Les prompts peuvent être personnalisés en modifiant les fichiers correspondants. Assurez-vous de respecter la structure attendue par les modules qui les utilisent. 