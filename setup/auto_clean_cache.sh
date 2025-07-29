#!/bin/bash
# Script de nettoyage automatique des fichiers cache et AppleDouble

echo "🧹 Nettoyage automatique des fichiers cache..."

# Nettoyer les fichiers AppleDouble
echo "🔍 Suppression des fichiers AppleDouble (._*)..."
find . -name "._*" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -delete 2>/dev/null

# Nettoyer les fichiers .pyc et __pycache__
echo "🔍 Suppression des fichiers .pyc et __pycache__..."
find . -name "*.pyc" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -delete 2>/dev/null
find . -name "__pycache__" -type d -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -exec rm -rf {} + 2>/dev/null

# Nettoyer les caches de tests
echo "🔍 Suppression des caches de tests..."
rm -rf .pytest_cache 2>/dev/null
rm -rf .mypy_cache 2>/dev/null
rm -rf htmlcov 2>/dev/null

# Nettoyer les caractères null des fichiers Python
echo "🔍 Nettoyage des caractères null..."
find . -name "*.py" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -exec grep -l $'\x00' {} \; | while read file; do
    if [ -f "$file" ]; then
        tr -d '\000' < "$file" > "$file.tmp" && mv "$file.tmp" "$file"
        echo "   ✅ Nettoyé: $file"
    fi
done

echo "✅ Nettoyage automatique terminé !" 