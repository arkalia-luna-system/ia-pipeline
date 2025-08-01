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

# Configuration pour pytest (maintenant dans pyproject.toml)
if [ ! -f pyproject.toml ]; then
    echo "❌ pyproject.toml manquant - configuration pytest non trouvée"
    exit 1
else
    echo "✅ Configuration pytest trouvée dans pyproject.toml"
fi

echo "✅ Configuration terminée ! Les fichiers .pyc ne seront plus générés."
echo "💡 Redémarrez votre terminal ou exécutez 'source ~/.zshrc' pour appliquer les changements."
