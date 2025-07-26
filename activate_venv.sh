#!/bin/bash

# Script d'activation rapide du venv Athalia
# Usage: source activate_venv.sh

echo "🐍 Activation du venv Athalia..."

# Vérifier si le venv existe
if [ ! -d ".venv" ]; then
    echo "❌ Erreur: Le venv .venv n'existe pas."
    echo "💡 Créez-le avec: python3 -m venv .venv"
    return 1
fi

# Activer le venv
source .venv/bin/activate

# Vérifier l'activation
if [ "$VIRTUAL_ENV" = "$(pwd)/.venv" ]; then
    echo "✅ Venv activé: $VIRTUAL_ENV"
    echo "🐍 Python: $(which python)"
    echo "📦 Pip: $(which pip)"
    echo ""
    echo "🚀 Vous pouvez maintenant utiliser Athalia !"
    echo "💡 Pour désactiver: deactivate"
else
    echo "❌ Erreur lors de l'activation du venv"
    return 1
fi 