#!/bin/bash

# Script de correction de linting utilisant la configuration config/autopep8.cfg
# Usage: ./config/lint-fix.sh [dossier]

set -e

# Dossier par défaut
TARGET_DIR="${1:-athalia_core}"

# Chemin vers la configuration
CONFIG_FILE="$(dirname "$0")/autopep8.cfg"

echo "🔧 Correction de linting pour: $TARGET_DIR"
echo "📁 Configuration: $CONFIG_FILE"

# Vérifier que la configuration existe
if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Configuration non trouvée: $CONFIG_FILE"
    exit 1
fi

# Vérifier l'état avant correction
echo "📊 État avant correction:"
flake8 "$TARGET_DIR" --select=W293,E302,E305,E501,F841 --count || true

# Correction avec la configuration
echo "🛠️  Application des corrections..."
autopep8 --in-place --aggressive --aggressive --max-line-length=79 --recursive "$TARGET_DIR"

# Vérifier l'état après correction
echo "📊 État après correction:"
flake8 "$TARGET_DIR" --select=W293,E302,E305,E501,F841 --count || true

echo "✅ Correction terminée !"
