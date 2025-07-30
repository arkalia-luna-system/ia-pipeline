#!/bin/bash
# Script wrapper pour les tests Athalia avec nettoyage automatique
# Usage: ./bin/ath-test-wrapper.sh [options]

set -e

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction pour afficher les messages
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
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

# Fonction de nettoyage d'urgence
cleanup_emergency() {
    print_warning "Nettoyage d'urgence en cours..."
    
    # Arrêter les processus Athalia
    pkill -f "athalia_core.main" 2>/dev/null || true
    pkill -f "athalia_core.cli" 2>/dev/null || true
    pkill -f "ath-audit" 2>/dev/null || true
    
    # Nettoyer les fichiers temporaires
    find . -name "athalia_*.tmp" -delete 2>/dev/null || true
    find . -name "athalia_*.log" -delete 2>/dev/null || true
    
    print_success "Nettoyage d'urgence terminé"
}

# Gestionnaire de signal pour le nettoyage d'urgence
trap cleanup_emergency SIGINT SIGTERM

# Vérifier que nous sommes dans le bon répertoire
if [ ! -f "pytest.ini" ]; then
    print_error "Ce script doit être exécuté depuis la racine du projet Athalia"
    exit 1
fi

print_info "🧪 Démarrage des tests Athalia avec nettoyage automatique"
echo "============================================================"

# Configuration de l'environnement
export ATHALIA_TEST_RUNNING=1
export ATHALIA_TEST_MODE=1
export ATHALIA_VERBOSE=0
export ATHALIA_LOG_LEVEL=ERROR

# Nettoyage initial
print_info "🧹 Nettoyage initial..."
python3 bin/ath-test-clean.py >/dev/null 2>&1 || true

# Exécution des tests
print_info "🚀 Exécution des tests..."
if [ $# -eq 0 ]; then
    # Mode normal
    python3 -m pytest tests/ -v --tb=short
else
    # Mode avec arguments
    python3 -m pytest tests/ "$@"
fi

TEST_EXIT_CODE=$?

echo ""
echo "============================================================"
print_info "🧹 NETTOYAGE AUTOMATIQUE APRÈS LES TESTS"
echo "============================================================"

# Nettoyage final
if python3 bin/ath-test-clean.py; then
    print_success "Nettoyage automatique réussi"
else
    print_warning "Nettoyage automatique avec avertissements"
fi

echo "============================================================"
if [ $TEST_EXIT_CODE -eq 0 ]; then
    print_success "🎉 Tests terminés avec succès et nettoyage automatique"
else
    print_error "💥 Tests échoués mais nettoyage effectué"
fi
echo "============================================================"

exit $TEST_EXIT_CODE 