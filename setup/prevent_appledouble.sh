#!/bin/bash
# 🍎 Script de prévention permanente des fichiers AppleDouble
# Version: 1.0
# Description: Configure macOS pour éviter la création de fichiers AppleDouble

set -euo pipefail

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🍎 PRÉVENTION PERMANENTE DES FICHIERS APPLEDOUBLE${NC}"
echo "========================================================"
echo ""

# Fonction pour afficher les résultats
show_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

show_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

show_error() {
    echo -e "${RED}❌ $1${NC}"
}

show_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Vérifier que nous sommes sur macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    show_error "Ce script est conçu uniquement pour macOS"
    exit 1
fi

echo -e "${YELLOW}🔍 Configuration de la prévention des fichiers AppleDouble...${NC}"

# 1. Désactiver la création de fichiers AppleDouble sur les volumes réseau
if defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true 2>/dev/null; then
    show_success "Création de fichiers AppleDouble désactivée sur les volumes réseau"
else
    show_warning "Impossible de désactiver la création de fichiers AppleDouble sur les volumes réseau (droits insuffisants)"
fi

# 2. Désactiver la création de fichiers AppleDouble sur les volumes USB
if defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true 2>/dev/null; then
    show_success "Création de fichiers AppleDouble désactivée sur les volumes USB"
else
    show_warning "Impossible de désactiver la création de fichiers AppleDouble sur les volumes USB (droits insuffisants)"
fi

# 3. Désactiver la création de fichiers AppleDouble localement
if defaults write com.apple.desktopservices DSDontWriteLocalStores -bool true 2>/dev/null; then
    show_success "Création de fichiers AppleDouble désactivée localement"
else
    show_warning "Impossible de désactiver la création de fichiers AppleDouble localement (droits insuffisants)"
fi

# 4. Désactiver la création de fichiers .DS_Store
if defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true 2>/dev/null; then
    show_success "Création de fichiers .DS_Store désactivée sur les volumes réseau"
else
    show_warning "Impossible de désactiver la création de fichiers .DS_Store sur les volumes réseau"
fi

# 5. Redémarrer Finder pour appliquer les changements
if killall Finder 2>/dev/null; then
    show_info "Finder redémarré pour appliquer les changements"
else
    show_warning "Impossible de redémarrer Finder (peut nécessiter une intervention manuelle)"
fi

# 6. Créer un fichier .gitattributes pour ignorer les fichiers AppleDouble
if [[ ! -f .gitattributes ]]; then
    cat > .gitattributes << 'EOF'
# Ignorer les fichiers AppleDouble et macOS
*._* binary
.DS_Store binary
Thumbs.db binary
desktop.ini binary

# Ignorer les fichiers temporaires
*.tmp binary
*.temp binary
*.swp binary
*.swo binary
*~ binary
*.bak binary
*.backup binary
*.orig binary

# Ignorer les caches
__pycache__/ binary
*.pyc binary
*.pyo binary
.pytest_cache/ binary
.mypy_cache/ binary
.ruff_cache/ binary
.coverage binary
htmlcov/ binary
.tox/ binary
.cache/ binary

# Ignorer les artefacts de build
build/ binary
dist/ binary
*.egg-info/ binary
*.egg binary
EOF
    show_success "Fichier .gitattributes créé pour ignorer les fichiers AppleDouble"
else
    show_info "Fichier .gitattributes existe déjà"
fi

# 7. Vérifier la configuration actuelle
echo ""
echo -e "${BLUE}📊 VÉRIFICATION DE LA CONFIGURATION${NC}"
echo "======================================"

# Vérifier les paramètres réseau
if defaults read com.apple.desktopservices DSDontWriteNetworkStores 2>/dev/null | grep -q "1"; then
    show_success "Désactivation réseau: ACTIVÉE"
else
    show_warning "Désactivation réseau: NON ACTIVÉE"
fi

# Vérifier les paramètres USB
if defaults read com.apple.desktopservices DSDontWriteUSBStores 2>/dev/null | grep -q "1"; then
    show_success "Désactivation USB: ACTIVÉE"
else
    show_warning "Désactivation USB: NON ACTIVÉE"
fi

# Vérifier les paramètres locaux
if defaults read com.apple.desktopservices DSDontWriteLocalStores 2>/dev/null | grep -q "1"; then
    show_success "Désactivation locale: ACTIVÉE"
else
    show_warning "Désactivation locale: NON ACTIVÉE"
fi

echo ""
echo -e "${GREEN}🎉 CONFIGURATION TERMINÉE !${NC}"
echo "======================================"
echo ""
echo -e "${BLUE}📋 RÉSUMÉ DES ACTIONS :${NC}"
echo "   • Désactivation des fichiers AppleDouble sur les volumes réseau"
echo "   • Désactivation des fichiers AppleDouble sur les volumes USB"
echo "   • Désactivation des fichiers AppleDouble localement"
echo "   • Désactivation des fichiers .DS_Store"
echo "   • Redémarrage de Finder"
echo "   • Création du fichier .gitattributes"
echo ""
echo -e "${YELLOW}⚠️  NOTE :${NC}"
echo "   • Les changements sont maintenant permanents"
echo "   • Redémarrez votre Mac pour une application complète"
echo "   • Utilisez 'bin/cleanup/ath-clean' pour le nettoyage régulier"
echo ""
echo -e "${GREEN}✅ Les fichiers AppleDouble ne devraient plus être créés !${NC}"
