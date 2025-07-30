#!/bin/bash
# Script d'installation des alias de workflow Athalia
# Active les nouveaux outils de workflow intelligent

set -e

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Fonctions d'affichage
print_header() {
    echo -e "${PURPLE}🚀 Installation des alias de workflow Athalia${NC}"
    echo -e "${BLUE}📋 Activation des nouveaux outils de développement${NC}"
    echo
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Vérification de l'environnement
check_environment() {
    print_info "Vérification de l'environnement..."
    
    # Vérifier si on est dans le projet Athalia
    if [ ! -f "setup/alias.sh" ]; then
        print_error "Ce script doit être exécuté depuis la racine du projet Athalia"
        exit 1
    fi
    
    # Vérifier les nouveaux scripts
    for script in bin/ath-prepare-commit bin/ath-push bin/ath-workflow; do
        if [ ! -f "$script" ]; then
            print_error "Script manquant: $script"
            exit 1
        fi
    done
    
    print_success "Environnement vérifié"
}

# Détection du shell
detect_shell() {
    print_info "Détection du shell..."
    
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_RC="$HOME/.zshrc"
        SHELL_NAME="Zsh"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_RC="$HOME/.bashrc"
        SHELL_NAME="Bash"
    else
        print_warning "Shell non reconnu, utilisation de .bashrc par défaut"
        SHELL_RC="$HOME/.bashrc"
        SHELL_NAME="Bash"
    fi
    
    print_success "Shell détecté: $SHELL_NAME ($SHELL_RC)"
}

# Installation des alias
install_aliases() {
    print_info "Installation des alias..."
    
    # Chemin absolu du projet
    PROJECT_ROOT="$(pwd)"
    
    # Créer le fichier de configuration des alias
    ALIAS_FILE="$PROJECT_ROOT/setup/athalia-workflow-aliases.sh"
    
    cat > "$ALIAS_FILE" << EOF
# Alias de workflow Athalia - Généré automatiquement
# Sourcez ce fichier dans votre .bashrc ou .zshrc

export ATHALIA_ROOT="$PROJECT_ROOT"

# === ALIAS DE WORKFLOW INTELLIGENT ===
# Préparation automatique au commit
alias ath-prepare='$PROJECT_ROOT/bin/ath-prepare-commit'

# Préparation avec correction automatique
alias ath-prepare-fix='$PROJECT_ROOT/bin/ath-prepare-commit --auto-fix'

# Préparation en mode simulation
alias ath-prepare-dry='$PROJECT_ROOT/bin/ath-prepare-commit --dry-run'

# Push intelligent avec vérifications
alias ath-push-smart='$PROJECT_ROOT/bin/ath-push'

# Push en mode simulation
alias ath-push-dry='$PROJECT_ROOT/bin/ath-push --dry-run'

# Push forcé (ignorer les erreurs)
alias ath-push-force='$PROJECT_ROOT/bin/ath-push --force'

# Workflow complet orchestré
alias ath-workflow='$PROJECT_ROOT/bin/ath-workflow'

# Workflow de développement
alias ath-dev='$PROJECT_ROOT/bin/ath-workflow --mode develop'

# Workflow de feature
alias ath-feature='$PROJECT_ROOT/bin/ath-workflow --mode feature'

# Workflow de hotfix
alias ath-hotfix='$PROJECT_ROOT/bin/ath-workflow --mode hotfix'

# Workflow de release
alias ath-release='$PROJECT_ROOT/bin/ath-workflow --mode release'

# Workflow avec commit automatique
alias ath-dev-auto='$PROJECT_ROOT/bin/ath-workflow --mode develop --auto-commit'

# Workflow avec push automatique
alias ath-dev-push='$PROJECT_ROOT/bin/ath-workflow --mode develop --auto-commit --auto-push'

# Workflow rapide (développement quotidien)
alias ath-quick='$PROJECT_ROOT/bin/ath-workflow --mode develop --auto-commit --auto-push --skip-checks'

# Workflow de feature complet
alias ath-feature-full='$PROJECT_ROOT/bin/ath-workflow --mode feature --auto-commit --auto-push'

# Workflow de release complet
alias ath-release-full='$PROJECT_ROOT/bin/ath-workflow --mode release --auto-commit --auto-push'

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
    echo "📖 Documentation : $PROJECT_ROOT/docs/DEVELOPER/WORKFLOW_AMELIORATIONS.md"
}

echo "🚀 Alias de workflow Athalia chargés !"
echo "💡 Tapez 'ath-workflow-help' pour voir toutes les commandes"
EOF
    
    print_success "Fichier d'alias créé: $ALIAS_FILE"
    
    # Ajouter la source au fichier RC si pas déjà présent
    if ! grep -q "athalia-workflow-aliases.sh" "$SHELL_RC"; then
        echo "" >> "$SHELL_RC"
        echo "# Alias de workflow Athalia" >> "$SHELL_RC"
        echo "source \"$ALIAS_FILE\"" >> "$SHELL_RC"
        print_success "Alias ajoutés à $SHELL_RC"
    else
        print_warning "Alias déjà présents dans $SHELL_RC"
    fi
}

# Test des alias
test_aliases() {
    print_info "Test des nouveaux alias..."
    
    # Source temporaire des alias
    source "$PROJECT_ROOT/setup/athalia-workflow-aliases.sh"
    
    # Test de la fonction d'aide
    if command -v ath-workflow-help > /dev/null 2>&1; then
        print_success "Fonction d'aide installée"
    else
        print_warning "Fonction d'aide non disponible"
    fi
    
    # Test d'un alias
    if command -v ath-prepare > /dev/null 2>&1; then
        print_success "Alias ath-prepare installé"
    else
        print_warning "Alias ath-prepare non disponible"
    fi
}

# Instructions post-installation
post_install_instructions() {
    echo
    print_success "🎉 Installation terminée avec succès !"
    echo
    print_info "📋 Prochaines étapes :"
    print_info "1. Redémarrez votre terminal ou exécutez :"
    print_info "   source $SHELL_RC"
    echo
    print_info "2. Testez les nouveaux alias :"
    print_info "   ath-workflow-help"
    echo
    print_info "3. Essayez un workflow rapide :"
    print_info "   ath-quick"
    echo
    print_info "4. Consultez la documentation :"
    print_info "   open docs/DEVELOPER/WORKFLOW_AMELIORATIONS.md"
    echo
    print_info "💡 Alias disponibles :"
    print_info "   ath-prepare, ath-push-smart, ath-dev, ath-quick, etc."
    echo
}

# Fonction principale
main() {
    print_header
    
    check_environment
    detect_shell
    install_aliases
    test_aliases
    post_install_instructions
}

# Exécution
main "$@" 