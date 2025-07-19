#!/bin/bash

# Athalia Project Generator
# Script pour générer des projets avec Athalia

set -e

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Fonction d'aide
show_help() {
    echo -e "${BLUE}🚀 ATHALIA PROJECT GENERATOR${NC}"
    echo ""
    echo "Usage: ath-generate [OPTIONS] <IDÉE_PROJET>"
    echo ""
    echo "Options:"
    echo "  -o, --output DIR     Dossier de sortie (défaut: ./generated_project)"
    echo "  -d, --dry-run        Mode simulation (pas de fichiers créés)"
    echo "  -i, --industrialize  Industrialiser automatiquement après génération"
    echo "  -h, --help           Afficher cette aide"
    echo ""
    echo "Exemples:"
    echo "  ath-generate 'calculatrice simple'"
    echo "  ath-generate 'API REST pour gestion de tâches' -o mon-projet"
    echo "  ath-generate 'dashboard web interactif' -d"
    echo "  ath-generate 'bot Discord' -i"
    echo ""
    echo "Types de projets supportés:"
    echo "  • API REST"
    echo "  • Application web"
    echo "  • Bot Discord/Telegram"
    echo "  • Script d'automatisation"
    echo "  • Dashboard/Visualisation"
    echo "  • Jeu simple"
    echo "  • Outil CLI"
    echo "  • Et plus encore..."
}

# Variables par défaut
OUTPUT_DIR="./generated_project"
DRY_RUN=false
INDUSTRIALIZE=false
PROJECT_IDEA=""

# Parsing des arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -d|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -i|--industrialize)
            INDUSTRIALIZE=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}❌ Option inconnue: $1${NC}"
            show_help
            exit 1
            ;;
        *)
            PROJECT_IDEA="$1"
            shift
            ;;
    esac
done

# Vérification des arguments
if [[ -z "$PROJECT_IDEA" ]]; then
    echo -e "${RED}❌ Erreur: Vous devez spécifier une idée de projet${NC}"
    echo ""
    show_help
    exit 1
fi

# Affichage du header
echo -e "${BLUE}🚀============================================================🚀${NC}"
echo -e "${BLUE}🌟 ATHALIA PROJECT GENERATOR - Création de projets IA${NC}"
echo -e "${BLUE}🌟 Génération intelligente avec pipeline complet${NC}"
echo -e "${BLUE}🚀============================================================🚀${NC}"
echo ""

echo -e "${CYAN}📋 Idée de projet:${NC} $PROJECT_IDEA"
echo -e "${CYAN}📁 Dossier de sortie:${NC} $OUTPUT_DIR"
echo -e "${CYAN}🔍 Mode simulation:${NC} $([ "$DRY_RUN" = true ] && echo "Oui" || echo "Non")"
echo -e "${CYAN}🏭 Industrialisation:${NC} $([ "$INDUSTRIALIZE" = true ] && echo "Oui" || echo "Non")"
echo ""

# Vérification de l'environnement
echo -e "${YELLOW}🔍 Vérification de l'environnement...${NC}"

# Vérifier que Python est disponible
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 n'est pas installé${NC}"
    exit 1
fi

# Vérifier que le module athalia_core est disponible
if ! python3 -c "import athalia_core" &> /dev/null; then
    echo -e "${RED}❌ Module athalia_core non disponible${NC}"
    echo -e "${YELLOW}💡 Assurez-vous d'être dans le répertoire racine d'Athalia${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Environnement vérifié${NC}"
echo ""

# Génération du projet
echo -e "${PURPLE}🤖 Génération du projet avec IA robuste...${NC}"

# Construire la commande
CMD="python3 -m athalia_core.cli generate \"$PROJECT_IDEA\" --output \"$OUTPUT_DIR\""

if [[ "$DRY_RUN" = true ]]; then
    CMD="$CMD --dry-run"
fi

# Exécuter la génération
if eval "$CMD"; then
    echo -e "${GREEN}✅ Projet généré avec succès !${NC}"
else
    echo -e "${RED}❌ Erreur lors de la génération${NC}"
    exit 1
fi

echo ""

# Industrialisation automatique si demandée
if [[ "$INDUSTRIALIZE" = true && "$DRY_RUN" = false ]]; then
    echo -e "${PURPLE}🏭 Lancement de l'industrialisation automatique...${NC}"
    
    if python3 athalia_unified.py "$OUTPUT_DIR" --action complete; then
        echo -e "${GREEN}✅ Industrialisation terminée !${NC}"
    else
        echo -e "${YELLOW}⚠️  Industrialisation terminée avec des avertissements${NC}"
    fi
    
    echo ""
fi

# Affichage des résultats
echo -e "${BLUE}📊 RÉSULTATS DE LA GÉNÉRATION${NC}"
echo -e "${BLUE}================================${NC}"

if [[ "$DRY_RUN" = false ]]; then
    if [[ -d "$OUTPUT_DIR" ]]; then
        echo -e "${GREEN}📁 Projet créé dans: $OUTPUT_DIR${NC}"
        
        # Lister les fichiers créés
        echo -e "${CYAN}📄 Fichiers générés:${NC}"
        find "$OUTPUT_DIR" -type f -name "*.py" -o -name "*.md" -o -name "*.yaml" -o -name "*.txt" | while read -r file; do
            echo -e "  • ${file#$OUTPUT_DIR/}"
        done
        
        # Afficher le contenu du README si il existe
        if [[ -f "$OUTPUT_DIR/README.md" ]]; then
            echo ""
            echo -e "${CYAN}📖 README généré:${NC}"
            echo -e "${YELLOW}$(cat "$OUTPUT_DIR/README.md")${NC}"
        fi
        
        echo ""
        echo -e "${GREEN}🎉 Votre projet est prêt !${NC}"
        echo ""
        echo -e "${BLUE}🚀 PROCHAINES ÉTAPES:${NC}"
        echo -e "  cd $OUTPUT_DIR"
        echo -e "  python3 main.py"
        echo ""
        
        if [[ "$INDUSTRIALIZE" = false ]]; then
            echo -e "${YELLOW}💡 Pour industrialiser le projet:${NC}"
            echo -e "  python3 athalia_unified.py $OUTPUT_DIR --action complete"
        fi
        
    else
        echo -e "${RED}❌ Erreur: Le dossier de sortie n'a pas été créé${NC}"
    fi
else
    echo -e "${GREEN}✅ Simulation terminée avec succès${NC}"
    echo -e "${YELLOW}💡 Pour créer le projet réel, relancez sans --dry-run${NC}"
fi

echo ""
echo -e "${BLUE}🚀============================================================🚀${NC}"
echo -e "${BLUE}🌟 ATHALIA - Votre assistant IA pour le développement${NC}"
echo -e "${BLUE}🚀============================================================🚀${NC}" 