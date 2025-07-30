# Alias de workflow Athalia - Généré automatiquement
# Sourcez ce fichier dans votre .bashrc ou .zshrc

export ATHALIA_ROOT="/Volumes/T7/athalia-dev-setup"

# === ALIAS DE WORKFLOW INTELLIGENT ===
# Préparation automatique au commit
alias ath-prepare='/Volumes/T7/athalia-dev-setup/bin/ath-prepare-commit'

# Préparation avec correction automatique
alias ath-prepare-fix='/Volumes/T7/athalia-dev-setup/bin/ath-prepare-commit --auto-fix'

# Préparation en mode simulation
alias ath-prepare-dry='/Volumes/T7/athalia-dev-setup/bin/ath-prepare-commit --dry-run'

# Push intelligent avec vérifications
alias ath-push-smart='/Volumes/T7/athalia-dev-setup/bin/ath-push'

# Push en mode simulation
alias ath-push-dry='/Volumes/T7/athalia-dev-setup/bin/ath-push --dry-run'

# Push forcé (ignorer les erreurs)
alias ath-push-force='/Volumes/T7/athalia-dev-setup/bin/ath-push --force'

# Workflow complet orchestré
alias ath-workflow='/Volumes/T7/athalia-dev-setup/bin/ath-workflow'

# Workflow de développement
alias ath-dev='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode develop'

# Workflow de feature
alias ath-feature='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode feature'

# Workflow de hotfix
alias ath-hotfix='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode hotfix'

# Workflow de release
alias ath-release='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode release'

# Workflow avec commit automatique
alias ath-dev-auto='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode develop --auto-commit'

# Workflow avec push automatique
alias ath-dev-push='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode develop --auto-commit --auto-push'

# Workflow rapide (développement quotidien)
alias ath-quick='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode develop --auto-commit --auto-push'

# Workflow de feature complet
alias ath-feature-full='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode feature --auto-commit --auto-push'

# Workflow de release complet
alias ath-release-full='/Volumes/T7/athalia-dev-setup/bin/ath-workflow --mode release --auto-commit --auto-push'

# === FONCTION D'AIDE ===
function ath-workflow-help() {
    echo "🔄 Alias de workflow Athalia disponibles :"
    echo "========================================"
    echo ""
    echo "📋 PRÉPARATION :"
    echo "  ath-prepare     : Préparation automatique au commit"
    echo "  ath-prepare-fix : Préparation avec correction auto"
    echo "  ath-prepare-dry : Préparation en mode simulation"
    echo ""
    echo "📤 PUSH INTELLIGENT :"
    echo "  ath-push-smart  : Push avec vérifications"
    echo "  ath-push-dry    : Push en mode simulation"
    echo "  ath-push-force  : Push forcé"
    echo ""
    echo "🎯 WORKFLOW COMPLET :"
    echo "  ath-dev         : Workflow de développement"
    echo "  ath-feature     : Workflow de feature"
    echo "  ath-hotfix      : Workflow de hotfix"
    echo "  ath-release     : Workflow de release"
    echo ""
    echo "⚡ WORKFLOW RAPIDE :"
    echo "  ath-quick       : Développement quotidien rapide"
    echo "  ath-dev-auto    : Développement avec commit auto"
    echo "  ath-dev-push    : Développement complet auto"
    echo "  ath-feature-full: Feature complète"
    echo "  ath-release-full: Release complète"
    echo ""
    echo "💡 Exemples d'utilisation :"
    echo "  ath-quick       # Développement quotidien"
    echo "  ath-feature-full # Nouvelle feature"
    echo "  ath-release-full # Nouvelle release"
    echo ""
    echo "📖 Documentation : /Volumes/T7/athalia-dev-setup/docs/DEVELOPER/WORKFLOW_AMELIORATIONS.md"
}

echo "🚀 Alias de workflow Athalia chargés !"
echo "💡 Tapez 'ath-workflow-help' pour voir toutes les commandes"
