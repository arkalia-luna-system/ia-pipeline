#!/bin/bash
# Script de nettoyage continu ultra-agressif pour Athalia

# Variables d'environnement
export COPYFILE_DISABLE=1
export PYTHONDONTWRITEBYTECODE=1

# Fonction de nettoyage ultra-agressif
clean_aggressively() {
    echo "🧹 Nettoyage en cours..."
    
    # 1. Supprimer TOUS les fichiers AppleDouble (.DS_Store, ._*)
    find . -name "._*" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -not -path "./archive/*" -delete 2>/dev/null
    find . -name ".DS_Store" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -not -path "./archive/*" -delete 2>/dev/null
    
    # 2. Nettoyer les caractères null des fichiers Python de manière FORCÉE
    find . -name "*.py" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -not -path "./archive/*" -exec sh -c '
        for file do
            if grep -q $'\''\x00'\'' "$file" 2>/dev/null; then
                echo "Nettoyage: $file"
                tr -d '\''\000'\'' < "$file" > "$file.tmp" && mv "$file.tmp" "$file"
            fi
        done
    ' sh {} + 2>/dev/null
    
    # 3. Supprimer les fichiers cache Python
    find . -name "*.pyc" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -not -path "./archive/*" -delete 2>/dev/null
    find . -name "__pycache__" -type d -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -not -path "./archive/*" -exec rm -rf {} + 2>/dev/null
    
    # 4. Supprimer les caches de tests
    rm -rf .pytest_cache 2>/dev/null
    rm -rf .mypy_cache 2>/dev/null
    rm -rf htmlcov 2>/dev/null
    
    # 5. Supprimer les fichiers temporaires
    find . -name ".!*" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -not -path "./archive/*" -delete 2>/dev/null
    
    # 6. Supprimer les fichiers .noindex
    find . -name "*.noindex" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./venv/*" -not -path "./archive/*" -delete 2>/dev/null
    
    # 7. PROTECTION DES TESTS - Supprimer les fichiers de tests automatiques
    find tests/ -name "test_unit_*.py" -delete 2>/dev/null || true
    find tests/ -name "test_integration_*.py" -delete 2>/dev/null || true
    find tests/ -name "test_performance_*.py" -delete 2>/dev/null || true
    
    echo "✅ Nettoyage terminé"
}

# Nettoyage initial
clean_aggressively

# Boucle de surveillance ultra-agressive
while true; do
    sleep 3  # Nettoyage toutes les 3 secondes
    clean_aggressively
done 