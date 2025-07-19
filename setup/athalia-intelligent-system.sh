#!/bin/bash

# 🚀 ATHALIA INTELLIGENT SYSTEM
# ==============================
# Système intelligent unifié qui :
# - Centralise tous les alias
# - Met à jour la documentation automatiquement
# - Coordonne tous les modules intelligemment
# - Apprend de chaque action pour améliorer le système

set -e

# === CONFIGURATION GLOBALE ===
ATHALIA_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
export ATHALIA_ROOT

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# === BASE DE DONNÉES D'APPRENTISSAGE ===
LEARNING_DB="$ATHALIA_ROOT/data/athalia_learning.json"
mkdir -p "$(dirname "$LEARNING_DB")"

# Initialisation de la base d'apprentissage
init_learning_db() {
    if [[ ! -f "$LEARNING_DB" ]]; then
        cat > "$LEARNING_DB" << EOF
{
    "actions_history": [],
    "user_preferences": {},
    "module_usage": {},
    "alias_usage": {},
    "error_patterns": {},
    "success_patterns": {},
    "last_update": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF
    fi
}

# === FONCTIONS D'APPRENTISSAGE ===

# Enregistrer une action pour l'apprentissage
record_action() {
    local action="$1"
    local success="$2"
    local details="$3"
    
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    local record="{\"action\":\"$action\",\"success\":$success,\"timestamp\":\"$timestamp\",\"details\":\"$details\"}"
    
    # Ajouter à l'historique
    jq --argjson record "$record" '.actions_history += [$record]' "$LEARNING_DB" > "${LEARNING_DB}.tmp" && mv "${LEARNING_DB}.tmp" "$LEARNING_DB"
    
    # Mettre à jour les statistiques d'usage
    local current_count=$(jq -r ".module_usage[\"$action\"] // 0" "$LEARNING_DB")
    jq --arg action "$action" --argjson count $((current_count + 1)) '.module_usage[$action] = $count' "$LEARNING_DB" > "${LEARNING_DB}.tmp" && mv "${LEARNING_DB}.tmp" "$LEARNING_DB"
    
    echo -e "${GREEN}📊 Action enregistrée pour l'apprentissage : $action${NC}"
}

# Analyser les patterns d'erreur
analyze_error_patterns() {
    echo -e "${YELLOW}🔍 Analyse des patterns d'erreur...${NC}"
    
    local error_count=$(jq -r '.actions_history | map(select(.success == false)) | length' "$LEARNING_DB")
    local total_count=$(jq -r '.actions_history | length' "$LEARNING_DB")
    
    if [[ $total_count -gt 0 ]]; then
        local error_rate=$((error_count * 100 / total_count))
        echo -e "${CYAN}📈 Taux d'erreur global : ${error_rate}%${NC}"
        
        # Actions les plus problématiques
        echo -e "${CYAN}🚨 Actions les plus problématiques :${NC}"
        jq -r '.actions_history | group_by(.action) | map(select(any(.success == false))) | sort_by(length) | reverse | .[0:5] | .[] | "  • \(.[0].action): \(length) erreurs"' "$LEARNING_DB" 2>/dev/null || echo "  Aucune donnée disponible"
    fi
}

# === SYSTÈME DE DOCUMENTATION AUTOMATIQUE ===

# Mettre à jour la documentation des alias
update_alias_documentation() {
    echo -e "${PURPLE}📚 Mise à jour de la documentation des alias...${NC}"
    
    local docs_file="$ATHALIA_ROOT/docs/ALIAS.md"
    local temp_file="${docs_file}.tmp"
    
    # En-tête de la documentation
    cat > "$temp_file" << EOF
# 📚 Guide des Alias Athalia/Arkalia

## 🚀 Vue d'ensemble

Ce document liste tous les alias disponibles dans le système Athalia/Arkalia, généré automatiquement par le système intelligent.

**Dernière mise à jour :** $(date '+%Y-%m-%d %H:%M:%S')

## 📋 Alias par Catégorie

EOF

    # Extraire tous les alias du fichier principal
    local categories=(
        "GIT WORKFLOW:alias-unified.sh"
        "TESTS & QUALITÉ:alias-unified.sh"
        "CORE FEATURES:alias-unified.sh"
        "DÉVELOPPEMENT:alias-unified.sh"
        "DOCUMENTATION:alias-unified.sh"
        "PLUGINS:alias-unified.sh"
        "MODULES AVANCÉS:alias-unified.sh"
        "DOCKER & DÉPLOIEMENT:alias-unified.sh"
        "BENCHMARK & PERFORMANCE:alias-unified.sh"
    )
    
    for category_info in "${categories[@]}"; do
        IFS=':' read -r category file <<< "$category_info"
        echo -e "\n### $category\n" >> "$temp_file"
        
        # Extraire les alias de cette catégorie
        grep -A 20 "=== $category ===" "$ATHALIA_ROOT/setup/$file" 2>/dev/null | \
        grep "^alias ath-" | \
        sed 's/alias //;s/=.*//' | \
        while read -r alias; do
            echo "| \`$alias\` | À documenter |" >> "$temp_file"
        done
    done
    
    # Statistiques d'usage
    echo -e "\n## 📊 Statistiques d'Usage\n" >> "$temp_file"
    echo "| Alias | Utilisations | Dernière utilisation |" >> "$temp_file"
    echo "|-------|--------------|---------------------|" >> "$temp_file"
    
    jq -r '.module_usage | to_entries | sort_by(.value) | reverse | .[0:10] | .[] | "| \(.key) | \(.value) | À calculer |"' "$LEARNING_DB" 2>/dev/null >> "$temp_file" || echo "| Aucune donnée | - | - |" >> "$temp_file"
    
    # Recommandations intelligentes
    echo -e "\n## 💡 Recommandations Intelligentes\n" >> "$temp_file"
    echo "Basées sur l'analyse des patterns d'usage :\n" >> "$temp_file"
    
    # Alias les plus utilisés
    echo "### 🏆 Alias les Plus Utilisés" >> "$temp_file"
    jq -r '.module_usage | to_entries | sort_by(.value) | reverse | .[0:5] | .[] | "- **\(.key)**: \(.value) utilisations"' "$LEARNING_DB" 2>/dev/null >> "$temp_file" || echo "- Aucune donnée disponible" >> "$temp_file"
    
    # Alias à découvrir
    echo -e "\n### 🔍 Alias à Découvrir" >> "$temp_file"
    echo "Alias peu utilisés mais utiles :" >> "$temp_file"
    jq -r '.module_usage | to_entries | sort_by(.value) | .[0:5] | .[] | "- **\(.key)**: \(.value) utilisations"' "$LEARNING_DB" 2>/dev/null >> "$temp_file" || echo "- Aucune donnée disponible" >> "$temp_file"
    
    mv "$temp_file" "$docs_file"
    echo -e "${GREEN}✅ Documentation mise à jour : $docs_file${NC}"
}

# === SYSTÈME DE COORDINATION INTELLIGENTE ===

# Vérifier la cohérence du système
check_system_coherence() {
    echo -e "${YELLOW}🔍 Vérification de la cohérence du système...${NC}"
    
    local issues=0
    
    # Vérifier les fichiers d'alias
    for alias_file in alias.sh alias-unified.sh; do
        if [[ ! -f "$ATHALIA_ROOT/setup/$alias_file" ]]; then
            echo -e "${RED}❌ Fichier d'alias manquant : $alias_file${NC}"
            ((issues++))
        fi
    done
    
    # Vérifier les modules principaux
    local core_modules=("athalia_core" "modules" "agents" "plugins")
    for module in "${core_modules[@]}"; do
        if [[ ! -d "$ATHALIA_ROOT/$module" ]]; then
            echo -e "${RED}❌ Module manquant : $module${NC}"
            ((issues++))
        fi
    done
    
    # Vérifier les scripts essentiels
    local essential_scripts=("ath-generate.sh" "ath-dev-boost.sh")
    for script in "${essential_scripts[@]}"; do
        if [[ ! -f "$ATHALIA_ROOT/setup/$script" ]]; then
            echo -e "${RED}❌ Script manquant : $script${NC}"
            ((issues++))
        fi
    done
    
    if [[ $issues -eq 0 ]]; then
        echo -e "${GREEN}✅ Système cohérent${NC}"
    else
        echo -e "${YELLOW}⚠️  $issues problème(s) détecté(s)${NC}"
    fi
    
    return $issues
}

# === ALIAS INTELLIGENTS UNIFIÉS ===

# Alias de base avec apprentissage
alias ath-clean='record_action "ath-clean" true "Nettoyage du projet" && find . -type f -name "*.pyc" -delete && find . -type d -name "__pycache__" -delete && find . -name ".DS_Store" -delete'

# Alias de génération de projet avec apprentissage
alias ath-generate='record_action "ath-generate" true "Génération de projet" && bash "$ATHALIA_ROOT/setup/ath-generate.sh"'

# Alias de tests avec apprentissage
alias ath-test='record_action "ath-test" true "Exécution des tests" && python3 -m pytest tests/ --cov=athalia_core --cov-report=term'

# Alias de dashboard avec apprentissage
alias ath-dashboard='record_action "ath-dashboard" true "Ouverture du dashboard" && open "$ATHALIA_ROOT/dashboard/dashboard.html"'

# Alias de CLI unifiée avec apprentissage
alias ath-unified='record_action "ath-unified" true "CLI unifiée" && python3 "$ATHALIA_ROOT/athalia_unified.py"'

# Alias de développement avec apprentissage
alias ath-dev-boost='record_action "ath-dev-boost" true "Menu de développement" && bash "$ATHALIA_ROOT/setup/ath-dev-boost.sh"'

# === FONCTIONS INTELLIGENTES ===

# Fonction d'aide intelligente
ath-help-intelligent() {
    echo -e "${BLUE}🚀 ATHALIA INTELLIGENT SYSTEM - Aide Contextuelle${NC}"
    echo -e "${BLUE}================================================${NC}"
    echo ""
    
    # Analyser le contexte actuel
    local current_dir=$(pwd)
    local git_branch=$(git branch --show-current 2>/dev/null || echo "Non initialisé")
    local python_files=$(find . -name "*.py" | wc -l | tr -d ' ')
    
    echo -e "${CYAN}📊 Contexte Actuel :${NC}"
    echo -e "  📁 Répertoire : $current_dir"
    echo -e "  🌿 Branche Git : $git_branch"
    echo -e "  🐍 Fichiers Python : $python_files"
    echo ""
    
    # Recommandations basées sur le contexte
    echo -e "${CYAN}💡 Recommandations Contextuelles :${NC}"
    
    if [[ $python_files -gt 0 ]]; then
        echo -e "  🧪 ath-test : Lancer les tests"
        echo -e "  🔍 ath-smart : Analyser le code avec IA"
    fi
    
    if [[ -f "requirements.txt" ]]; then
        echo -e "  📦 ath-clean : Nettoyer les caches"
    fi
    
    if [[ -d "tests" ]]; then
        echo -e "  📊 ath-coverage : Vérifier la couverture"
    fi
    
    echo ""
    echo -e "${CYAN}🎯 Alias les Plus Utiles :${NC}"
    
    # Alias les plus utilisés (basé sur l'apprentissage)
    jq -r '.module_usage | to_entries | sort_by(.value) | reverse | .[0:5] | .[] | "  \(.key) (\(.value) utilisations)"' "$LEARNING_DB" 2>/dev/null || echo "  ath-generate : Générer un projet"
    echo "  ath-unified : CLI unifiée"
    echo "  ath-dashboard : Dashboard interactif"
    echo "  ath-dev-boost : Menu de développement"
    
    echo ""
    echo -e "${YELLOW}💡 Tapez 'ath-<tab>' pour l'auto-complétion${NC}"
    echo -e "${YELLOW}📖 Consultez docs/ALIAS.md pour la documentation complète${NC}"
}

# Fonction de diagnostic intelligent
ath-diagnostic() {
    echo -e "${BLUE}🔍 DIAGNOSTIC INTELLIGENT ATHALIA${NC}"
    echo -e "${BLUE}================================${NC}"
    echo ""
    
    # Vérification de la cohérence
    check_system_coherence
    
    echo ""
    echo -e "${CYAN}📊 Statistiques d'Usage :${NC}"
    
    # Statistiques globales
    local total_actions=$(jq -r '.actions_history | length' "$LEARNING_DB" 2>/dev/null || echo "0")
    local success_rate=$(jq -r 'if (.actions_history | length) > 0 then ((.actions_history | map(select(.success == true)) | length) * 100 / (.actions_history | length)) else 0 end' "$LEARNING_DB" 2>/dev/null || echo "0")
    
    echo -e "  📈 Actions totales : $total_actions"
    echo -e "  ✅ Taux de succès : ${success_rate}%"
    
    echo ""
    echo -e "${CYAN}🎯 Actions les Plus Populaires :${NC}"
    jq -r '.module_usage | to_entries | sort_by(.value) | reverse | .[0:10] | .[] | "  \(.key): \(.value) utilisations"' "$LEARNING_DB" 2>/dev/null || echo "  Aucune donnée disponible"
    
    echo ""
    echo -e "${CYAN}🚨 Patterns d'Erreur :${NC}"
    analyze_error_patterns
    
    echo ""
    echo -e "${GREEN}✅ Diagnostic terminé${NC}"
}

# Fonction de mise à jour intelligente
ath-update-intelligent() {
    echo -e "${BLUE}🔄 MISE À JOUR INTELLIGENTE ATHALIA${NC}"
    echo -e "${BLUE}==================================${NC}"
    echo ""
    
    # Mettre à jour la documentation
    update_alias_documentation
    
    # Analyser les patterns
    analyze_error_patterns
    
    # Vérifier la cohérence
    check_system_coherence
    
    echo ""
    echo -e "${GREEN}✅ Mise à jour intelligente terminée${NC}"
}

# === AUTO-COMPLÉTION INTELLIGENTE ===

# Auto-complétion basée sur l'apprentissage
if [ -n "$ZSH_VERSION" ]; then
    compctl -K _athalia_intelligent ath-
    _athalia_intelligent() {
        # Alias les plus utilisés en premier
        local popular_aliases=$(jq -r '.module_usage | to_entries | sort_by(.value) | reverse | .[0:10] | .[] | .key' "$LEARNING_DB" 2>/dev/null || echo "")
        local all_aliases=$(grep -E "^alias ath-" "$ATHALIA_ROOT/setup/alias-unified.sh" | sed 's/alias //;s/=.*//' 2>/dev/null || echo "")
        reply=($popular_aliases $all_aliases)
    }
elif [ -n "$BASH_VERSION" ]; then
    complete -W "$(jq -r '.module_usage | to_entries | sort_by(.value) | reverse | .[0:10] | .[] | .key' "$LEARNING_DB" 2>/dev/null || echo "")" ath-
fi

# === INITIALISATION ===

# Initialiser le système au chargement
init_learning_db

# Message de bienvenue intelligent
echo -e "${BLUE}🚀 ATHALIA INTELLIGENT SYSTEM chargé !${NC}"
echo -e "${CYAN}💡 Tapez 'ath-help-intelligent' pour l'aide contextuelle${NC}"
echo -e "${CYAN}🔍 Tapez 'ath-diagnostic' pour le diagnostic complet${NC}"
echo -e "${CYAN}🔄 Tapez 'ath-update-intelligent' pour la mise à jour automatique${NC}"

# Enregistrer le chargement du système
record_action "system_load" true "Chargement du système intelligent" 