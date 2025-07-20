#!/bin/bash

# 🚀 Alias Athalia/Arkalia Unifiés - Version Professionnelle
# ============================================================
# Ce fichier combine tous les alias du projet en une interface unifiée
# Sourcez ce fichier dans votre .bashrc ou .zshrc pour l'activer

# === CONFIGURATION ===
ATHALIA_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
export ATHALIA_ROOT

# === ALIAS GIT PROFESSIONNELS ===
# Workflow Git sécurisé et professionnel

# Branches
alias gb='git branch'
alias gba='git branch -a'
alias gbd='git branch -d'
alias gbD='git branch -D'
alias gco='git checkout'
alias gcob='git checkout -b'
alias gcom='git checkout main'
alias gcod='git checkout develop'

# Status et Logs
alias gs='git status'
alias gl='git log --oneline'
alias gla='git log --oneline --all --graph'
alias gl10='git log --oneline -10'
alias gl20='git log --oneline -20'

# Workflow quotidien
alias gstart='git checkout develop && git pull origin develop'
alias gfeature='git checkout -b feature/'
alias ghotfix='git checkout -b hotfix/'
alias grelease='git checkout -b release/'

# Commits
alias ga='git add .'
alias gc='git commit -m'
alias gca='git commit --amend'
alias gcan='git commit --amend --no-edit'

# Push/Pull
alias gp='git push'
alias gpu='git push -u origin'
alias gpl='git pull'
alias gplo='git pull origin'

# Merge et Rebase
alias gm='git merge'
alias grb='git rebase'
alias grbi='git rebase -i'

# Nettoyage
alias gclean='git branch --merged | grep -v "\*" | xargs -n 1 git branch -d'
alias gclean-remote='git remote prune origin'

# Utilitaires
alias gdiff='git diff'
alias gstash='git stash'
alias gstashp='git stash pop'
alias greset='git reset --hard HEAD'

# === ALIAS ATHALIA CORE ===
# Fonctionnalités principales du pipeline IA

# Tests et Qualité
alias ath-test='python3 -m pytest tests/ --cov=athalia_core --cov-report=term'
alias ath-test-unit='python3 -m pytest tests/test_*_unit.py --cov=athalia_core --cov-report=term'
alias ath-test-integration='python3 -m pytest tests/test_integration_*.py --cov=athalia_core --cov-report=term'
alias ath-test-performance='python3 -m pytest tests/test_performance_*.py --cov=athalia_core --cov-report=term'
alias ath-lint='python3 -m flake8 athalia_core/ tests/ --max-line-length=120'
alias ath-coverage='python3 -m coverage run -m pytest tests/ && python3 -m coverage report'
alias ath-coverage-html='python3 -m coverage run -m pytest tests/ && python3 -m coverage html && open htmlcov/index.html'

# Nettoyage et Maintenance
alias ath-clean='find . -type f -name "*.pyc" -delete && find . -type d -name "__pycache__" -delete && find . -name ".DS_Store" -delete'
alias ath-clean-all='ath-clean && find . -name "*.log" -delete && find . -name "*.tmp" -delete'

# Dashboard et Interface
alias ath-dashboard='open "$ATHALIA_ROOT/dashboard/dashboard.html"'
alias ath-dashboard-py='python3 "$ATHALIA_ROOT/athalia_core/dashboard.py"'
alias ath-dashboard-full='open "$ATHALIA_ROOT/dashboard/analytics_dashboard.html"'

# CLI et Outils
alias ath-cli='python3 -m athalia_core.cli'
alias ath-cli-main='python3 -m athalia_core.cli'
alias ath-unified='python3 "$ATHALIA_ROOT/athalia_unified.py"'
alias ath-smart='python3 "$ATHALIA_ROOT/agents/ath_context_prompt.py"'

# Audit et Sécurité
alias ath-audit='python3 "$ATHALIA_ROOT/bin/ath-audit.py"'
alias ath-audit-intelligent='python3 "$ATHALIA_ROOT/athalia_core/intelligent_auditor.py"'
alias ath-security='python3 "$ATHALIA_ROOT/athalia_core/security_auditor.py"'

# Documentation
alias ath-doc='python3 "$ATHALIA_ROOT/athalia_core/auto_documenter.py"'
alias ath-doc-open='open "$ATHALIA_ROOT/docs/README.md"'
alias ath-doc-api='open "$ATHALIA_ROOT/docs/API_REFERENCE.md"'
alias ath-doc-guide='open "$ATHALIA_ROOT/docs/USER_GUIDE.md"'

# === ALIAS WORKFLOW ATHALIA ===
# Workflow automatisé pour le développement quotidien

alias ath-start='echo "🚀 Démarrage journée Athalia" && git checkout develop && git pull origin develop && echo "✅ Prêt pour le développement"'
alias ath-feature='echo "🎯 Création feature branch" && git checkout -b feature/'
alias ath-commit='echo "💾 Commit avec message conventionnel" && git add . && git commit -m'
alias ath-push='echo "📤 Push feature branch" && git push -u origin'
alias ath-merge='echo "🔄 Retour develop et merge" && git checkout develop && git pull origin develop'

# === ALIAS MODULES AVANCÉS ===
# Modules spécialisés du pipeline

alias ath-auto-correct='python3 "$ATHALIA_ROOT/modules/auto_correction_avancee.py"'
alias ath-dashboard-unified='python3 "$ATHALIA_ROOT/modules/dashboard_unifie_simple.py"'
alias ath-profile-advanced='python3 "$ATHALIA_ROOT/modules/profils_utilisateur_avances.py"'

# === ALIAS PLUGINS ===
# Système de plugins extensible

alias ath-plugin-docker='python3 "$ATHALIA_ROOT/plugins/export_docker_plugin.py"'
alias ath-plugin-hello='python3 "$ATHALIA_ROOT/plugins/hello_plugin.py"'
alias ath-plugins-list='ls "$ATHALIA_ROOT/plugins/" | grep -E "^.*_plugin\\.py$" | sed "s/\\.py$//;s/_plugin$//"'

# === ALIAS DÉVELOPPEMENT ===
# Outils de développement et debugging

alias ath-dev-boost='bash "$ATHALIA_ROOT/setup/ath-dev-boost.sh"'
alias ath-perplex='open https://www.perplexity.ai/'
alias ath-jupyter='jupyter notebook'
alias ath-notebook='jupyter notebook'
alias ath-profile='python3 -m cProfile -o profile.out'

# === ALIAS CONFIGURATION ===
# Gestion de la configuration

alias ath-config='open "$ATHALIA_ROOT/config/athalia_config.yaml"'
alias ath-prompts='open "$ATHALIA_ROOT/prompts/"'
alias ath-final-report='open "$ATHALIA_ROOT/FINAL_SUMMARY.md"'

# === ALIAS DOCKER ET DÉPLOIEMENT ===
# Gestion des conteneurs et déploiement

alias ath-docker='docker compose up'
alias ath-docker-build='docker compose build'
alias ath-docker-down='docker compose down'

# === ALIAS BENCHMARK ET PERFORMANCE ===
# Tests de performance et benchmarks

alias ath-benchmark='python3 "$ATHALIA_ROOT/setup/benchmark_distillation.py"'
alias ath-benchmark-full='python3 "$ATHALIA_ROOT/setup/benchmark_distillation.py"'
alias ath-test-ci='python3 "$ATHALIA_ROOT/test_ci_manual.py"'
alias ath-test-final='python3 "$ATHALIA_ROOT/test_final_athalia.py"'
alias ath-test-dashboard='python3 "$ATHALIA_ROOT/test_dashboard_unifie.py"'

# === ALIAS SYSTÈME INTELLIGENT ===
# Système de coordination et d'apprentissage intelligent

alias ath-coordinator='python3 "$ATHALIA_ROOT/setup/athalia-coordinator.py"'
alias ath-coordinator-analyze='python3 "$ATHALIA_ROOT/setup/athalia-coordinator.py" --action analyze'
alias ath-coordinator-insights='python3 "$ATHALIA_ROOT/setup/athalia-coordinator.py" --action insights'
alias ath-coordinator-update-docs='python3 "$ATHALIA_ROOT/setup/athalia-coordinator.py" --action update-docs'

# Système intelligent unifié
alias ath-intelligent='source "$ATHALIA_ROOT/setup/athalia-intelligent-system.sh"'
alias ath-help-intelligent='ath-help-intelligent'
alias ath-diagnostic='ath-diagnostic'
alias ath-update-intelligent='ath-update-intelligent'

# === ALIAS À IMPLÉMENTER ===
# Placeholders pour les fonctionnalités futures

alias ath-generate='bash "$ATHALIA_ROOT/setup/ath-generate.sh"'
alias ath-correct='echo "🚧 Fonctionnalité à implémenter : ath-correct"'
alias ath-profile='echo "🚧 Fonctionnalité à implémenter : ath-profile"'
alias ath-scan='echo "🚧 Fonctionnalité à implémenter : ath-scan"'
alias ath-test-prompts='echo "🚧 Fonctionnalité à implémenter : ath-test-prompts"'
alias ath-export='echo "🚧 Fonctionnalité à implémenter : ath-export"'
alias ath-mkdocs='echo "🚧 Fonctionnalité à implémenter : ath-mkdocs"'

# === AUTO-COMPLÉTION INTELLIGENTE ===
# Auto-complétion pour tous les alias ath-

if [ -n "$ZSH_VERSION" ]; then
    compctl -K _athalia_aliases ath-
    _athalia_aliases() { 
        reply=($(compgen -A function -A command -A alias -- "${words[1]}"))
    }
elif [ -n "$BASH_VERSION" ]; then
    complete -A alias ath-
fi

# Auto-complétion pour les plugins ath-plugin-*
if [ -n "$ZSH_VERSION" ]; then
    compctl -K _athalia_plugins ath-plugin-
    _athalia_plugins() { 
        reply=($(ls "$ATHALIA_ROOT/plugins/" | grep -E '^.*_plugin\\.py$' | sed 's/\\.py$//;s/_plugin$//;s/^/ath-plugin-/'))
    }
elif [ -n "$BASH_VERSION" ]; then
    complete -W "$(ls "$ATHALIA_ROOT/plugins/" | grep -E '^.*_plugin\\.py$' | sed 's/\\.py$//;s/_plugin$//;s/^/ath-plugin-/')" ath-plugin-
fi

# === FONCTIONS D'AIDE ===
# Aide contextuelle et informations

function ath-help() {
    echo "🚀 Athalia/Arkalia - Alias Disponibles"
    echo "======================================"
    echo ""
    echo "📋 GIT WORKFLOW :"
    echo "  ath-start     : Démarrage journée (develop + pull)"
    echo "  ath-feature   : Nouvelle feature branch"
    echo "  ath-commit    : Commit conventionnel"
    echo "  ath-push      : Push feature branch"
    echo "  ath-merge     : Retour develop"
    echo ""
    echo "🧪 TESTS & QUALITÉ :"
    echo "  ath-test      : Tests complets"
    echo "  ath-test-unit : Tests unitaires uniquement"
    echo "  ath-lint      : Lint du code"
    echo "  ath-coverage  : Couverture de tests"
    echo ""
    echo "🎯 CORE FEATURES :"
    echo "  ath-cli       : CLI principale"
    echo "  ath-dashboard : Dashboard interactif"
    echo "  ath-smart     : Prompt contextuel IA"
    echo "  ath-audit     : Audit intelligent"
    echo ""
    echo "🔧 DÉVELOPPEMENT :"
    echo "  ath-clean     : Nettoyage projet"
    echo "  ath-dev-boost : Menu prompts IA"
    echo "  ath-jupyter   : Notebook Jupyter"
    echo ""
    echo "📚 DOCUMENTATION :"
    echo "  ath-doc       : Générer documentation"
    echo "  ath-doc-open  : Ouvrir documentation"
    echo ""
    echo "🔌 PLUGINS :"
    echo "  ath-plugin-*  : Plugins disponibles"
    echo "  ath-plugins-list : Lister plugins"
    echo ""
    echo "💡 Tapez 'ath-<tab>' pour l'auto-complétion"
    echo "📖 Consultez docs/ALIAS.md pour plus de détails"
}

function ath-status() {
    echo "🔍 État du projet Athalia :"
    echo "=========================="
    echo "📁 Répertoire racine : $ATHALIA_ROOT"
    echo "🌿 Branche actuelle  : $(git branch --show-current 2>/dev/null || echo 'Non initialisé')"
    echo "📊 Tests disponibles : $(find tests/ -name "test_*.py" | wc -l | tr -d ' ') fichiers"
    echo "🔌 Plugins installés : $(ls plugins/*_plugin.py 2>/dev/null | wc -l | tr -d ' ') plugins"
    echo "📚 Documentation    : $(find docs/ -name "*.md" | wc -l | tr -d ' ') fichiers"
}

function ath-user-context() {
    case "$USER" in
        admin*) echo "👑 Bienvenue, administrateur ! Alias spéciaux activés." ;;
        dev*) echo "👨‍💻 Bienvenue, développeur ! Voici vos outils favoris." ;;
        *) echo "👤 Bienvenue, utilisateur standard !" ;;
    esac
}

# === SUPER CERVEAU ET ORCHESTRATEUR ===
# Système de super cerveau et orchestration intelligente

alias ath-super-brain='python3 "$ATHALIA_ROOT/setup/athalia-super-brain.py"'
alias ath-brain-analyze='python3 "$ATHALIA_ROOT/setup/athalia-super-brain.py" --action analyze'
alias ath-brain-optimize='python3 "$ATHALIA_ROOT/setup/athalia-super-brain.py" --action optimize'
alias ath-brain-coordinate='python3 "$ATHALIA_ROOT/setup/athalia-super-brain.py" --action coordinate'
alias ath-brain-report='python3 "$ATHALIA_ROOT/setup/athalia-super-brain.py" --action report --output data/super_brain_report.json'

alias ath-orchestrator='python3 "$ATHALIA_ROOT/setup/athalia-intelligent-orchestrator.py"'
alias ath-orchestrate-plan='python3 "$ATHALIA_ROOT/setup/athalia-intelligent-orchestrator.py" --action plan'
alias ath-orchestrate-complete='python3 "$ATHALIA_ROOT/setup/athalia-intelligent-orchestrator.py" --action orchestrate --pipeline complete'
alias ath-orchestrate-audit='python3 "$ATHALIA_ROOT/setup/athalia-intelligent-orchestrator.py" --action orchestrate --pipeline audit'
alias ath-orchestrate-test='python3 "$ATHALIA_ROOT/setup/athalia-intelligent-orchestrator.py" --action orchestrate --pipeline test'
alias ath-orchestrate-insights='python3 "$ATHALIA_ROOT/setup/athalia-intelligent-orchestrator.py" --action insights'

# === INITIALISATION ===
# Définir le chemin racine
export ATHALIA_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

# Message de bienvenue et vérifications
echo "🚀 Alias Athalia/Arkalia unifiés chargés !"
echo "💡 Tapez 'ath-help' pour voir toutes les commandes"
echo "🔍 Tapez 'ath-status' pour l'état du projet"
echo "🧠 Tapez 'ath-brain-analyze' pour analyser l'architecture"
echo "🎯 Tapez 'ath-orchestrate-plan' pour voir les plans d'orchestration" 