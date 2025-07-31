#!/bin/zsh

# =============================================================================
# 🛑 ATHALIA PROCESS MANAGER - STOP ALL EXCEPT CURSOR
# =============================================================================
# Description: Arrête tous les processus de développement sauf Cursor
# Auteur: Athalia Project
# Version: 2.0 - Interface améliorée
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
    echo -e "${BOLD}${CYAN}║              Arrêt sécurisé des processus de développement   ║${NC}"
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

# Configuration des processus à arrêter
PROCESS_PATTERNS=(
    "athalia_core"
    "athalia_unified"
    "python.*athalia"
    "pytest.*athalia"
    "validation_continue"
    "ollama"
    "docker"
    "node"
    "npm"
    "yarn"
    "python.*test"
    "python.*script"
    "python.*mypy"
    "python.*black"
    "python.*isort"
    "python.*lsp"
)

# Statistiques
TOTAL_PROCESSES=0
KILLED_PROCESSES=0
PROTECTED_PROCESSES=0

# Fonction principale d'arrêt des processus
stop_processes_except_cursor() {
    print_section "PHASE 1: DÉTECTION ET ARRÊT DES PROCESSUS"

    for pattern in "${PROCESS_PATTERNS[@]}"; do
        print_info "Recherche de processus: ${BOLD}$pattern${NC}"

        # Trouver les processus correspondants
        local processes=$(ps aux | grep -E "$pattern" | grep -v grep | grep -v "stop-all-except-cursor" | grep -v "cursor" 2>/dev/null || true)

        if [ -n "$processes" ]; then
            local process_count=0
            echo "$processes" | while read line; do
                local pid=$(echo "$line" | awk '{print $2}')
                local user=$(echo "$line" | awk '{print $1}')
                local cpu=$(echo "$line" | awk '{print $3}')
                local mem=$(echo "$line" | awk '{print $4}')
                local cmd=$(echo "$line" | awk '{for(i=11;i<=NF;i++) printf "%s ", $i; print ""}')

                process_count=$((process_count + 1))

                # Vérifier que ce n'est pas Cursor
                if [[ "$cmd" != *"cursor"* ]] && [[ "$cmd" != *"Cursor"* ]]; then
                    if [ -n "$pid" ] && [ "$pid" != "$$" ]; then
                        echo -e "${WHITE}  📊 PID: ${BOLD}$pid${NC} | CPU: ${BOLD}${cpu}%${NC} | MEM: ${BOLD}${mem}%${NC}"
                        echo -e "${WHITE}  📝 Commande: ${cmd:0:80}${NC}"

                        # Tentative d'arrêt propre
                        if kill -TERM "$pid" 2>/dev/null; then
                            print_success "Processus arrêté proprement: PID $pid"
                            KILLED_PROCESSES=$((KILLED_PROCESSES + 1))
                        else
                            print_error "Impossible d'arrêter: PID $pid"
                        fi
                        echo ""
                    fi
                else
                    print_protected "PROTÉGÉ (Cursor): PID $pid - $cmd"
                    PROTECTED_PROCESSES=$((PROTECTED_PROCESSES + 1))
                    echo ""
                fi
            done
            TOTAL_PROCESSES=$((TOTAL_PROCESSES + process_count))
        else
            print_info "Aucun processus trouvé pour: $pattern"
        fi
    done
}

# Fonction d'arrêt forcé
force_kill_remaining() {
    print_section "PHASE 2: ARRÊT FORCÉ DES PROCESSUS RÉCALCITRANTS"

    local force_patterns=("athalia_core" "python.*athalia" "validation_continue")

    for pattern in "${force_patterns[@]}"; do
        print_info "Arrêt forcé: $pattern"
        if pkill -f "$pattern" 2>/dev/null; then
            print_success "Processus forcés arrêtés: $pattern"
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
    echo -e "${WHITE}   • Processus protégés: ${BOLD}${PURPLE}$PROTECTED_PROCESSES${NC}"
    echo ""

    print_info "Vérification des processus restants:"
    # Filtrer pour exclure les processus Cursor
    local remaining=$(ps aux | grep -E "(athalia_core|athalia_unified|python.*athalia|pytest.*athalia|validation_continue)" | grep -v grep | grep -v "stop-all-except-cursor" | grep -v "cursor" | grep -v "Cursor" 2>/dev/null || true)

    if [ -n "$remaining" ]; then
        print_warning "Processus Athalia encore actifs:"
        echo "$remaining" | head -3
        if [ $(echo "$remaining" | wc -l) -gt 3 ]; then
            echo -e "${YELLOW}   ... et $(($(echo "$remaining" | wc -l) - 3)) autres processus${NC}"
        fi
    else
        print_success "Aucun processus Athalia restant"
    fi

    echo ""
    print_success "🎯 Cursor reste actif et protégé !"
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

# Phase 1: Arrêt des processus
stop_processes_except_cursor

# Pause pour terminaison propre
print_section "PAUSE DE SÉCURITÉ"
print_info "Attente de 3 secondes pour la terminaison propre..."
sleep 3

# Phase 2: Arrêt forcé
force_kill_remaining

# Rapport final
show_final_report
