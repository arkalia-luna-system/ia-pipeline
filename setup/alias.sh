# Alias Athalia/Arkalia Dev - à sourcer dans votre .bashrc ou .zshrc

# (Désactivé) Ouvre un shell IA (commande 'continue' non reconnue)
# alias ath-chat='continue'

# Nettoie le projet (cache Python, fichiers temporaires, logs)
alias ath-clean='$(git rev-parse --show-toplevel)/bin/ath-clean'

# Nettoie les fichiers AppleDouble et configure la prévention
alias ath-clean-appledouble='$(git rev-parse --show-toplevel)/bin/ath-clean-appledouble'

# Menu interactif de prompts IA (debug, UX, audit, test, refactor)
alias ath-dev-boost='bash $(git rev-parse --show-toplevel)/setup/ath-dev-boost.sh'

# Ouvre Perplexity.ai dans le navigateur
alias ath-perplex='open https://www.perplexity.ai/'

# Lance les tests via script Python dédié
alias ath-test='$(git rev-parse --show-toplevel)/bin/ath-test.py'

# === NOUVEAUX OUTILS DE WORKFLOW ===
# Scripts de workflow intelligent créés pour faciliter le développement

# Préparation automatique au commit
alias ath-prepare='$(git rev-parse --show-toplevel)/bin/ath-prepare-commit'

# Préparation avec correction automatique
alias ath-prepare-fix='$(git rev-parse --show-toplevel)/bin/ath-prepare-commit --auto-fix'

# Préparation en mode simulation
alias ath-prepare-dry='$(git rev-parse --show-toplevel)/bin/ath-prepare-commit --dry-run'

# Push intelligent avec vérifications
alias ath-push-smart='$(git rev-parse --show-toplevel)/bin/ath-push'

# Push en mode simulation
alias ath-push-dry='$(git rev-parse --show-toplevel)/bin/ath-push --dry-run'

# Push forcé (ignorer les erreurs)
alias ath-push-force='$(git rev-parse --show-toplevel)/bin/ath-push --force'

# Workflow complet orchestré
alias ath-workflow='$(git rev-parse --show-toplevel)/bin/ath-workflow'

# Workflow de développement
alias ath-dev='$(git rev-parse --show-toplevel)/bin/ath-workflow --mode develop'

# Workflow de feature
alias ath-feature='$(git rev-parse --show-toplevel)/bin/ath-workflow --mode feature'

# Workflow de hotfix
alias ath-hotfix='$(git rev-parse --show-toplevel)/bin/ath-workflow --mode hotfix'

# Workflow de release
alias ath-release='$(git rev-parse --show-toplevel)/bin/ath-workflow --mode release'

# Workflow avec commit automatique
alias ath-dev-auto='$(git rev-parse --show-toplevel)/bin/ath-workflow --mode develop --auto-commit'

# Workflow avec push automatique
alias ath-dev-push='$(git rev-parse --show-toplevel)/bin/ath-workflow --mode develop --auto-commit --auto-push'

# Test des outils de workflow
alias ath-test-workflow='$(git rev-parse --show-toplevel)/bin/ath-test-workflow'

# Tests unitaires spécifiques
alias ath-test-unit='python3 -m pytest tests/ -m "unit" -v'

# Tests d'intégration
alias ath-test-integration='python3 -m pytest tests/integration/ -v'

# Tests de performance
alias ath-test-performance='python3 -m pytest tests/ -m "performance" -v'

# Lint le code via script Python dédié
alias ath-lint='$(git rev-parse --show-toplevel)/bin/ath-lint.py'

# Build le projet via script Python dédié
alias ath-build='$(git rev-parse --show-toplevel)/bin/ath-build.py'

# (À implémenter) Génération rapide de projet/module (script manquant)
# alias ath-new='bash setup/ath-new.sh'

# Lance le prompt contextuel IA (athalia_core/agents/context_prompt.py)
alias ath-smart='python3 $(git rev-parse --show-toplevel)/athalia_core/agents/context_prompt.py'

# Ouvre le dashboard interactif dans le navigateur
alias ath-dashboard='open $(git rev-parse --show-toplevel)/dashboard/dashboard.html'

# Dashboard web (script Python)
alias ath-dashboard-py='python3 $(git rev-parse --show-toplevel)/athalia_core/dashboard.py'

# Dashboard de validation temps réel
alias ath-dashboard-validation='python3 $(git rev-parse --show-toplevel)/validation_dashboard_simple.py & sleep 2 && open http://localhost:5001/dashboard_validation.html'

# Test CI local (utilise les tests existants)
alias ath-ci-test='python3 -m pytest tests/test_ci_ultra_fast.py -v && python3 -m pytest tests/test_ci_robust.py -v'

# CLI principal
alias ath-cli-main='python3 -m athalia_core.cli'

# CLI unifiée
alias ath-unified='python3 $(git rev-parse --show-toplevel)/athalia_unified.py'

# Audit intelligent via script Python dédié
alias ath-audit='$(git rev-parse --show-toplevel)/bin/ath-audit.py'

# Audit intelligent avancé
alias ath-audit-intelligent='python3 $(git rev-parse --show-toplevel)/athalia_core/audit_intelligent.py'

# Génération rapide de projet/module (script manquant)
alias ath-generate='bash $(git rev-parse --show-toplevel)/setup/ath-generate.sh'

# Correction de code (script manquant)
alias ath-correct='bash $(git rev-parse --show-toplevel)/setup/ath-correct.sh'

# Création de profils (script manquant)
alias ath-profile='bash $(git rev-parse --show-toplevel)/setup/ath-profile.sh'

# Scan de sécurité (script manquant)
alias ath-scan='bash $(git rev-parse --show-toplevel)/setup/ath-scan.sh'

# Tests prompts (script manquant)
alias ath-test-prompts='bash $(git rev-parse --show-toplevel)/setup/ath-test-prompts.sh'

# Benchmark (script manquant)
alias ath-benchmark='bash $(git rev-parse --show-toplevel)/setup/ath-benchmark.sh'

# Export (script manquant)
alias ath-export='bash $(git rev-parse --show-toplevel)/setup/ath-export.sh'

# Mkdocs (script manquant)
alias ath-mkdocs='bash $(git rev-parse --show-toplevel)/setup/ath-mkdocs.sh'

# Lancement du serveur Docker (docker compose up)
alias ath-docker='docker compose up'

# Docker build
alias ath-docker-build='docker build -t athalia .'

# Docker run
alias ath-docker-run='docker run -it athalia'

# Docker down
alias ath-docker-down='docker compose down'

# Couverture de tests via script Python dédié
alias ath-coverage='$(git rev-parse --show-toplevel)/bin/ath-coverage.py'

# Lance un notebook Jupyter
alias ath-jupyter='jupyter notebook'

# Documentation
alias ath-doc='open $(git rev-parse --show-toplevel)/docs/README.md'

# Documentation API
alias ath-doc-api='open $(git rev-parse --show-toplevel)/docs/API.md'

# Sécurité
alias ath-security='python3 $(git rev-parse --show-toplevel)/athalia_core/security_auditor.py'

# === Alias avancés / modules / plugins / outils ===

# Modules avancés (maintenant dans athalia_core/advanced_modules/)
alias ath-auto-correct='python3 $(git rev-parse --show-toplevel)/athalia_core/advanced_modules/auto_correction_advanced.py'
alias ath-dashboard-unified='python3 $(git rev-parse --show-toplevel)/athalia_core/advanced_modules/dashboard_unified.py'
alias ath-profile-advanced='python3 $(git rev-parse --show-toplevel)/athalia_core/advanced_modules/user_profiles_advanced.py'

# Plugins (maintenant dans athalia_core/external_plugins/)
alias ath-plugin-docker='python3 $(git rev-parse --show-toplevel)/athalia_core/external_plugins/docker_export_plugin.py'
alias ath-plugin-hello='python3 $(git rev-parse --show-toplevel)/athalia_core/external_plugins/hello_world_plugin.py'

# Tests et benchmarks
alias ath-test-ci='python3 $(git rev-parse --show-toplevel)/test_ci_manual.py'
alias ath-test-final='python3 $(git rev-parse --show-toplevel)/test_final_athalia.py'
alias ath-test-dashboard='python3 $(git rev-parse --show-toplevel)/test_dashboard_unifie.py'
alias ath-benchmark-full='python3 $(git rev-parse --show-toplevel)/setup/benchmark_distillation.py'

# Ouverture de la doc locale
alias ath-doc-open='open $(git rev-parse --show-toplevel)/docs/README.md'

# Ouverture des prompts
alias ath-prompts='open $(git rev-parse --show-toplevel)/prompts/'

# Ouverture de la config
alias ath-config='open $(git rev-parse --show-toplevel)/config/athalia_config.yaml'

# Lister les plugins
alias ath-plugins-list='ls $(git rev-parse --show-toplevel)/athalia_core/external_plugins/'

# Lancer un notebook Jupyter
alias ath-notebook='jupyter notebook'

# Ouvrir le rapport de couverture
alias ath-coverage-html='open $(git rev-parse --show-toplevel)/htmlcov/index.html'

# Ouvrir le rapport final
alias ath-final-report='open $(git rev-parse --show-toplevel)/FINAL_SUMMARY.md'

# Ouvrir le dashboard complet
alias ath-dashboard-full='open $(git rev-parse --show-toplevel)/dashboard/analytics_dashboard.html'

# === Auto-complétion intelligente pour tous les alias ath- ===
# (Zsh)
if [ -n "$ZSH_VERSION" ]; then
  # Auto-complétion pour les alias ath- spécifiques
  compctl -K _athalia_aliases ath-audit ath-build ath-clean ath-coverage ath-lint ath-test ath-kill
  _athalia_aliases() { reply=($(compgen -A function -A command -A alias -- "${words[1]}")); }
fi
# (Bash)
if [ -n "$BASH_VERSION" ]; then
  complete -A alias ath-
fi

# === Auto-complétion intelligente pour les plugins ath-plugin-* ===
if [ -n "$ZSH_VERSION" ]; then
  # Auto-complétion pour les plugins spécifiques
  compctl -K _athalia_plugins ath-plugin-docker ath-plugin-hello
  _athalia_plugins() { reply=($(ls $(git rev-parse --show-toplevel)/athalia_core/external_plugins/ | grep -E '^.*_plugin\\.py$' | sed 's/\\.py$//;s/_plugin$//;s/^/ath-plugin-/')); }
fi
if [ -n "$BASH_VERSION" ]; then
  complete -W "$(ls $(git rev-parse --show-toplevel)/athalia_core/external_plugins/ | grep -E '^.*_plugin\\.py$' | sed 's/\\.py$//;s/_plugin$//;s/^/ath-plugin-/')" ath-plugin-
fi

# === Alias magique : aide dynamique sur tous les alias ===
function ath-help() {
  echo "\nAlias disponibles :"
  grep -E "^alias ath-" "$(git rev-parse --show-toplevel)/setup/alias.sh" | sed "s/alias //;s/=.*//" | while read a; do
    desc=$(grep "| \`${a}\`" "$(git rev-parse --show-toplevel)/docs/ALIAS.md" | head -1 | cut -d'|' -f3 | sed 's/^ *//')
    printf "  %-22s : %s\n" "$a" "$desc"
  done
  echo "\nTapez 'ath-<tab>' pour l'auto-complétion.\nConsultez docs/ALIAS.md pour plus de détails."
}

# === Alias dynamique selon l'utilisateur courant ===
function ath-user-context() {
  case "$USER" in
    admin*) echo "Bienvenue, administrateur ! Alias spéciaux activés." ;;
    dev*) echo "Bienvenue, développeur ! Voici vos outils favoris." ;;
    *) echo "Bienvenue, utilisateur standard !" ;;
  esac
}

# === (Préparation) Alias contextuels (exemple de base) ===
# function ath-context() {
#   if [ -f "athalia_unified.py" ]; then
#     echo "Projet principal Athalia détecté"
#     # Proposer des alias spécifiques ici
#   fi
# }# Docker down
alias ath-docker-down='docker compose down'
# Documentation API
alias ath-doc-api='open $(git rev-parse --show-toplevel)/docs/API.md'
# Sécurité
alias ath-security='python3 $(git rev-parse --show-toplevel)/athalia_core/security_auditor.py'
# Documentation Guide
alias ath-doc-guide='open $(git rev-parse --show-toplevel)/docs/GUIDE.md'

# Arrêt des processus Athalia
alias ath-kill='$(git rev-parse --show-toplevel)/bin/ath-clean --kill-processes'
alias ath-stop-all='$(git rev-parse --show-toplevel)/bin/stop-all-except-cursor.sh'
alias ath-maintenance='python $(git rev-parse --show-toplevel)/tools/maintenance/phase3_maintenance.py'
alias ath-maintenance-execute='python $(git rev-parse --show-toplevel)/tools/maintenance/phase3_maintenance.py --execute'
