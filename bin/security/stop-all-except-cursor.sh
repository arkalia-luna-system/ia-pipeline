#!/bin/zsh

# =============================================================================
# 🛑 ATHALIA PROCESS MANAGER - STOP ALL EXCEPT CURSOR & VS CODE
# =============================================================================
# Description: Arrête intelligemment les processus Athalia de développement
# Auteur: Athalia Project
# Version: 3.0 - Protection intelligente des éditeurs
# =============================================================================

# Couleurs pour une meilleure lisibilité
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Fonction d'affichage avec style
print_header() {
    echo -e "${BOLD}${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BOLD}${CYAN}║                    🛑 ATHALIA PROCESS MANAGER                ║${NC}"
    echo -e "${BOLD}${CYAN}║              Arrêt intelligent des processus Athalia         ║${NC}"
    echo -e "${BOLD}${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_section() {
    echo -e "${BOLD}${YELLOW}📋 $1${NC}"
    echo -e "${YELLOW}────────────────────────────────────────────────────────────────────${NC}"
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

print_protected() {
    echo -e "${PURPLE}🛡️  $1${NC}"
}

# Configuration des processus à PROTÉGER (ne jamais arrêter)
PROTECTED_PROCESSES=(
    "cursor"
    "Cursor"
    "code"
    "Code"
    "Visual Studio Code"
    "vscode"
    "VS Code"
    "sublime"
    "Sublime"
    "vim"
    "emacs"
    "nano"
    "terminal"
    "Terminal"
    "iTerm"
    "zsh"
    "bash"
    "fish"
    "tmux"
    "screen"
)

# Configuration des processus Athalia à arrêter (plus spécifiques)
ATHALIA_PROCESSES=(
    "athalia_core"
    "athalia_unified"
    "athalia_ai"
    "athalia_showcase"
    "athalia_robotics"
    "athalia_analytics"
    "athalia_audit"
    "athalia_validation"
    "athalia_testing"
    "athalia_performance"
    "athalia_monitoring"
    "athalia_maintenance"
    "athalia_cleanup"
    "athalia_documentation"
    "athalia_ci"
    "athalia_cd"
    "athalia_security"
    "athalia_quality"
    "athalia_automation"
    "athalia_distillation"
    "athalia_classification"
    "athalia_plugins"
    "athalia_templates"
    "athalia_utilities"
    "athalia_core_"
    "athalia_ai_"
    "athalia_robotics_"
    "athalia_analytics_"
    "athalia_audit_"
    "athalia_validation_"
    "athalia_testing_"
    "athalia_performance_"
    "athalia_monitoring_"
    "athalia_maintenance_"
    "athalia_cleanup_"
    "athalia_documentation_"
    "athalia_ci_"
    "athalia_cd_"
    "athalia_security_"
    "athalia_quality_"
    "athalia_automation_"
    "athalia_distillation_"
    "athalia_classification_"
    "athalia_plugins_"
    "athalia_templates_"
    "athalia_utilities_"
)

# Configuration des processus de développement à arrêter (plus spécifiques)
DEV_PROCESSES=(
    "pytest.*athalia"
    "python.*athalia"
    "python.*test.*athalia"
    "python.*script.*athalia"
    "python.*mypy.*athalia"
    "python.*black.*athalia"
    "python.*isort.*athalia"
    "python.*lsp.*athalia"
    "python.*ruff.*athalia"
    "python.*coverage.*athalia"
    "python.*validation.*athalia"
    "python.*correction.*athalia"
    "python.*performance.*athalia"
    "python.*monitoring.*athalia"
    "python.*maintenance.*athalia"
    "python.*cleanup.*athalia"
    "python.*documentation.*athalia"
    "python.*ci.*athalia"
    "python.*cd.*athalia"
    "python.*security.*athalia"
    "python.*quality.*athalia"
    "python.*automation.*athalia"
    "python.*distillation.*athalia"
    "python.*classification.*athalia"
    "python.*plugins.*athalia"
    "python.*templates.*athalia"
    "python.*utilities.*athalia"
)

# Statistiques
TOTAL_PROCESSES=0
KILLED_PROCESSES=0
PROTECTED_PROCESSES_COUNT=0

# Fonction pour vérifier si un processus est protégé
is_protected() {
    local cmd="$1"
    local pid="$2"
    
    # Vérifier les processus protégés
    for protected in "${PROTECTED_PROCESSES[@]}"; do
        if [[ "$cmd" == *"$protected"* ]]; then
            return 0  # Protégé
        fi
    done
    
    # Vérifier si c'est le processus parent ou le shell actuel
    if [ "$pid" = "$$" ] || [ "$pid" = "$PPID" ]; then
        return 0  # Protégé
    fi
    
    # Vérifier si c'est un processus système important
    if [[ "$cmd" == *"launchd"* ]] || [[ "$cmd" == *"kernel"* ]] || [[ "$cmd" == *"System"* ]]; then
        return 0  # Protégé
    fi
    
    return 1  # Pas protégé
}

# Fonction principale d'arrêt des processus
stop_athalia_processes() {
    print_section "PHASE 1: DÉTECTION ET ARRÊT DES PROCESSUS ATHALIA"

    # Arrêter d'abord les processus Athalia spécifiques
    for pattern in "${ATHALIA_PROCESSES[@]}"; do
        print_info "Recherche de processus Athalia: ${BOLD}$pattern${NC}"

        # Trouver les processus correspondants
        local processes=$(ps aux | grep -E "$pattern" | grep -v grep | grep -v "stop-all-except-cursor" 2>/dev/null || true)

        if [ -n "$processes" ]; then
            local process_count=0
            echo "$processes" | while read line; do
                local pid=$(echo "$line" | awk '{print $2}')
                local user=$(echo "$line" | awk '{print $1}')
                local cpu=$(echo "$line" | awk '{print $3}')
                local mem=$(echo "$line" | awk '{print $4}')
                local cmd=$(echo "$line" | awk '{for(i=11;i<=NF;i++) printf "%s ", $i; print ""}')

                process_count=$((process_count + 1))

                # Vérifier que ce n'est pas un processus protégé
                if ! is_protected "$cmd" "$pid"; then
                    if [ -n "$pid" ] && [ "$pid" != "$$" ]; then
                        echo -e "${WHITE}  📊 PID: ${BOLD}$pid${NC} | CPU: ${BOLD}${cpu}%${NC} | MEM: ${BOLD}${mem}%${NC}"
                        echo -e "${WHITE}  📝 Commande: ${cmd:0:80}${NC}"

                        # Tentative d'arrêt propre
                        if kill -TERM "$pid" 2>/dev/null; then
                            print_success "Processus Athalia arrêté proprement: PID $pid"
                            KILLED_PROCESSES=$((KILLED_PROCESSES + 1))
                        else
                            print_error "Impossible d'arrêter: PID $pid"
                        fi
                        echo ""
                    fi
                else
                    print_protected "PROTÉGÉ: PID $pid - $cmd"
                    PROTECTED_PROCESSES_COUNT=$((PROTECTED_PROCESSES_COUNT + 1))
                    echo ""
                fi
            done
            TOTAL_PROCESSES=$((TOTAL_PROCESSES + process_count))
        else
            print_info "Aucun processus Athalia trouvé pour: $pattern"
        fi
    done

    # Ensuite arrêter les processus de développement Athalia
    for pattern in "${DEV_PROCESSES[@]}"; do
        print_info "Recherche de processus de développement: ${BOLD}$pattern${NC}"

        local processes=$(ps aux | grep -E "$pattern" | grep -v grep | grep -v "stop-all-except-cursor" 2>/dev/null || true)

        if [ -n "$processes" ]; then
            local process_count=0
            echo "$processes" | while read line; do
                local pid=$(echo "$line" | awk '{print $2}')
                local user=$(echo "$line" | awk '{print $1}')
                local cpu=$(echo "$line" | awk '{print $3}')
                local mem=$(echo "$line" | awk '{print $4}')
                local cmd=$(echo "$line" | awk '{for(i=11;i<=NF;i++) printf "%s ", $i; print ""}')

                process_count=$((process_count + 1))

                # Vérifier que ce n'est pas un processus protégé
                if ! is_protected "$cmd" "$pid"; then
                    if [ -n "$pid" ] && [ "$pid" != "$$" ]; then
                        echo -e "${WHITE}  📊 PID: ${BOLD}$pid${NC} | CPU: ${BOLD}${cpu}%${NC} | MEM: ${BOLD}${mem}%${NC}"
                        echo -e "${WHITE}  📝 Commande: ${cmd:0:80}${NC}"

                        # Tentative d'arrêt propre
                        if kill -TERM "$pid" 2>/dev/null; then
                            print_success "Processus de développement arrêté: PID $pid"
                            KILLED_PROCESSES=$((KILLED_PROCESSES + 1))
                        else
                            print_error "Impossible d'arrêter: PID $pid"
                        fi
                        echo ""
                    fi
                else
                    print_protected "PROTÉGÉ: PID $pid - $cmd"
                    PROTECTED_PROCESSES_COUNT=$((PROTECTED_PROCESSES_COUNT + 1))
                    echo ""
                fi
            done
            TOTAL_PROCESSES=$((TOTAL_PROCESSES + process_count))
        else
            print_info "Aucun processus de développement trouvé pour: $pattern"
        fi
    done
}

# Fonction d'arrêt forcé des processus Athalia restants
force_kill_remaining_athalia() {
    print_section "PHASE 2: ARRÊT FORCÉ DES PROCESSUS ATHALIA RÉCALCITRANTS"

    local force_patterns=("athalia_core" "python.*athalia" "validation_continue" "correction_finale")

    for pattern in "${force_patterns[@]}"; do
        print_info "Arrêt forcé: $pattern"
        
        # Trouver les PIDs des processus Athalia restants
        local pids=$(ps aux | grep -E "$pattern" | grep -v grep | grep -v "stop-all-except-cursor" | awk '{print $2}' 2>/dev/null || true)
        
        if [ -n "$pids" ]; then
            echo "$pids" | while read pid; do
                local cmd=$(ps -p "$pid" -o command= 2>/dev/null || echo "")
                
                # Vérifier que ce n'est pas un processus protégé
                if ! is_protected "$cmd" "$pid"; then
                    if kill -9 "$pid" 2>/dev/null; then
                        print_success "Processus forcé arrêté: PID $pid"
                        KILLED_PROCESSES=$((KILLED_PROCESSES + 1))
                    else
                        print_warning "Impossible de forcer l'arrêt: PID $pid"
                    fi
                else
                    print_protected "PROTÉGÉ (arrêt forcé ignoré): PID $pid"
                fi
            done
        else
            print_warning "Aucun processus à forcer: $pattern"
        fi
    done
}

# Fonction de rapport final
show_final_report() {
    print_section "RAPPORT FINAL"

    echo -e "${WHITE}📊 ${BOLD}Statistiques:${NC}"
    echo -e "${WHITE}   • Processus détectés: ${BOLD}$TOTAL_PROCESSES${NC}"
    echo -e "${WHITE}   • Processus arrêtés: ${BOLD}${GREEN}$KILLED_PROCESSES${NC}"
    echo -e "${WHITE}   • Processus protégés: ${BOLD}${PURPLE}$PROTECTED_PROCESSES_COUNT${NC}"
    echo ""

    print_info "Vérification des processus Athalia restants:"
    # Filtrer pour exclure les processus protégés
    local remaining=$(ps aux | grep -E "(athalia_core|athalia_unified|python.*athalia|pytest.*athalia|validation_continue)" | grep -v grep | grep -v "stop-all-except-cursor" 2>/dev/null || true)

    if [ -n "$remaining" ]; then
        print_warning "Processus Athalia encore actifs:"
        echo "$remaining" | head -5 | while read line; do
            local pid=$(echo "$line" | awk '{print $2}')
            local cmd=$(echo "$line" | awk '{for(i=11;i<=NF;i++) printf "%s ", $i; print ""}')
            if is_protected "$cmd" "$pid"; then
                echo -e "${PURPLE}   🛡️  PROTÉGÉ: $line${NC}"
            else
                echo -e "${YELLOW}   ⚠️  ACTIF: $line${NC}"
            fi
        done
        
        if [ $(echo "$remaining" | wc -l) -gt 5 ]; then
            echo -e "${YELLOW}   ... et $(($(echo "$remaining" | wc -l) - 5)) autres processus${NC}"
        fi
    else
        print_success "Aucun processus Athalia restant"
    fi

    echo ""
    print_success "🎯 Cursor et VS Code restent actifs et protégés !"
    echo ""
    echo -e "${BOLD}${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BOLD}${GREEN}║                    ✅ OPÉRATION TERMINÉE                     ║${NC}"
    echo -e "${BOLD}${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
}

# =============================================================================
# EXÉCUTION PRINCIPALE
# =============================================================================

# Affichage de l'en-tête
print_header

# Phase 1: Arrêt des processus Athalia
stop_athalia_processes

# Pause pour terminaison propre
print_section "PAUSE DE SÉCURITÉ"
print_info "Attente de 2 secondes pour la terminaison propre..."
sleep 2

# Phase 2: Arrêt forcé des processus Athalia restants
force_kill_remaining_athalia

# Rapport final
show_final_report
