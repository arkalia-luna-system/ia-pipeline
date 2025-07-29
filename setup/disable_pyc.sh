#!/bin/bash
# Script pour désactiver la génération de fichiers .pyc en développement

echo "🔧 Configuration pour éviter les fichiers .pyc..."

# Variable d'environnement pour désactiver les .pyc
export PYTHONDONTWRITEBYTECODE=1

# Ajouter à .bashrc/.zshrc si pas déjà présent
if ! grep -q "PYTHONDONTWRITEBYTECODE=1" ~/.zshrc 2>/dev/null; then
    echo "export PYTHONDONTWRITEBYTECODE=1" >> ~/.zshrc
    echo "✅ Variable PYTHONDONTWRITEBYTECODE ajoutée à ~/.zshrc"
fi

# Créer un fichier .env dans le projet
if [ ! -f .env ]; then
    echo "PYTHONDONTWRITEBYTECODE=1" > .env
    echo "✅ Fichier .env créé avec PYTHONDONTWRITEBYTECODE=1"
fi

# Configuration pour pytest
if [ ! -f pytest.ini ]; then
    cat > pytest.ini << EOF
[pytest]
addopts = --cache-clear
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
EOF
    echo "✅ Configuration pytest créée avec --cache-clear"
fi

echo "✅ Configuration terminée ! Les fichiers .pyc ne seront plus générés."
echo "💡 Redémarrez votre terminal ou exécutez 'source ~/.zshrc' pour appliquer les changements." 