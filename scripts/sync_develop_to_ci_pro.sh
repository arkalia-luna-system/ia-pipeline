#!/bin/bash

# 🔄 Script de synchronisation Develop vers CI Professional
# Usage: ./scripts/sync_develop_to_ci_pro.sh

set -e

echo "🔄 SYNCHRONISATION DEVELOP → CI-CD-PROFESSIONAL"
echo "================================================"

# Vérifier qu'on est sur develop
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "develop" ]; then
    echo "❌ Erreur: Tu dois être sur la branche 'develop'"
    echo "   Branche actuelle: $CURRENT_BRANCH"
    echo "   Commande: git checkout develop"
    exit 1
fi

echo "✅ Branche actuelle: $CURRENT_BRANCH"

# Mettre à jour develop
echo "📥 Mise à jour de develop..."
git pull origin develop

# Vérifier si ci-cd-professional existe
if git ls-remote --heads origin ci-cd-professional | grep -q ci-cd-professional; then
    echo "✅ Branche ci-cd-professional existe"
    
    # Basculer sur ci-cd-professional
    echo "🔄 Basculement vers ci-cd-professional..."
    git checkout ci-cd-professional
    
    # Mettre à jour la branche
    echo "📥 Mise à jour de ci-cd-professional..."
    git pull origin ci-cd-professional
    
    # Fusionner develop
    echo "🔀 Fusion de develop dans ci-cd-professional..."
    git merge develop --no-edit
    
else
    echo "🆕 Création de la branche ci-cd-professional..."
    git checkout -b ci-cd-professional
fi

# Pousser les changements
echo "📤 Poussée vers origin/ci-cd-professional..."
git push origin ci-cd-professional

# Retourner sur develop
echo "🔄 Retour sur develop..."
git checkout develop

echo ""
echo "✅ SYNCHRONISATION TERMINÉE !"
echo "============================="
echo "📊 Impact:"
echo "   - Branche ci-cd-professional mise à jour"
echo "   - Workflows CI/CD pro déclenchés automatiquement"
echo "   - Tests et rapports générés"
echo ""
echo "🔍 Vérifications:"
echo "   - GitHub Actions: https://github.com/arkalia-luna-system/ia-pipeline/actions"
echo "   - Progression: python scripts/ci_progress_tracker.py report"
echo ""
echo "🚀 Prochaines étapes:"
echo "   1. Vérifier les résultats des workflows CI/CD pro"
echo "   2. Analyser les rapports de progression"
echo "   3. Valider les améliorations" 