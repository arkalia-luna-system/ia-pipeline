#!/bin/bash

# Script de nettoyage RAM pour Athalia
# Usage: ./ath-cleanup-ram.sh

echo "🧹 Nettoyage RAM Athalia - $(date)"
echo "=================================="

# Nettoyage des caches Python
echo "📦 Nettoyage cache pip..."
pip cache purge 2>/dev/null || echo "Pip non disponible"

# Nettoyage Homebrew
echo "🍺 Nettoyage cache Homebrew..."
brew cleanup 2>/dev/null || echo "Homebrew non disponible"

# Nettoyage des caches système
echo "🗂️ Nettoyage caches système..."
rm -rf ~/Library/Caches/pip/* 2>/dev/null || true
rm -rf ~/Library/Caches/ms-playwright/* 2>/dev/null || true
rm -rf ~/Library/Caches/Google/* 2>/dev/null || true

# Nettoyage fichiers temporaires
echo "📁 Nettoyage fichiers temporaires..."
rm -rf /tmp/* 2>/dev/null || true
rm -rf ~/Library/Caches/TemporaryItems/* 2>/dev/null || true

# Purge mémoire système
echo "🧠 Purge mémoire système..."
sudo purge 2>/dev/null || echo "Purge nécessite sudo"

# Affichage état final
echo ""
echo "📊 État final :"
df -h / | tail -1
echo ""
echo "✅ Nettoyage terminé !" 