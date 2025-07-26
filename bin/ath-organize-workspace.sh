#!/bin/zsh

echo "🛠️  Organisateur de Workspace Athalia"
echo "======================================"

# Activer l'environnement virtuel
source .venv/bin/activate

# Fonction d'aide
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --dry-run        Mode simulation (par défaut)"
    echo "  --apply          Appliquer les changements"
    echo "  --cleanup        Nettoyer les fichiers temporaires"
    echo "  --validate       Valider l'organisation"
    echo "  --report         Générer un rapport"
    echo "  --help           Afficher cette aide"
    echo ""
    echo "Exemples:"
    echo "  $0 --dry-run --validate    # Simulation avec validation"
    echo "  $0 --apply --cleanup       # Appliquer et nettoyer"
    echo "  $0 --report                # Générer un rapport"
}

# Variables par défaut
DRY_RUN=true
CLEANUP=false
VALIDATE=false
REPORT=false

# Traitement des arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --apply)
            DRY_RUN=false
            shift
            ;;
        --cleanup)
            CLEANUP=true
            shift
            ;;
        --validate)
            VALIDATE=true
            shift
            ;;
        --report)
            REPORT=true
            shift
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            echo "❌ Option inconnue: $1"
            show_help
            exit 1
            ;;
    esac
done

# Construction de la commande
CMD="python tools/maintenance/workspace_organizer.py"

if [[ "$DRY_RUN" == "false" ]]; then
    echo "⚠️  ATTENTION: Mode application activé - les fichiers seront déplacés !"
    read -q "REPLY?Continuer ? (y/N) "
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Opération annulée"
        exit 1
    fi
else
    echo "🔍 Mode simulation activé"
fi

if [[ "$CLEANUP" == "true" ]]; then
    CMD="$CMD --cleanup"
fi

if [[ "$VALIDATE" == "true" ]]; then
    CMD="$CMD --validate"
fi

if [[ "$REPORT" == "true" ]]; then
    CMD="$CMD --report"
fi

# Exécution
echo "🚀 Exécution de la commande: $CMD"
echo ""

eval $CMD

echo ""
echo "✅ Organisation terminée !"
echo ""
echo "📋 Prochaines étapes recommandées:"
echo "  1. Vérifier les changements avec: $0 --validate"
echo "  2. Générer un rapport avec: $0 --report"
echo "  3. Appliquer les changements avec: $0 --apply" 