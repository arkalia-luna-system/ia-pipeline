#!/bin/bash
set -e

echo "🔍 Validation CI/CD Athalia"
echo "=========================="

# Vérification de l'environnement
echo "🔧 Vérification de l'environnement..."
if [ ! -d ".venv" ]; then
    echo "❌ Environnement virtuel non trouvé. Création..."
    python3 -m venv .venv
fi

# Activation de l'environnement virtuel
echo "📦 Activation de l'environnement virtuel..."
source .venv/bin/activate

# Installation des dépendances si nécessaire
echo "📥 Vérification des dépendances..."
pip install -q pytest pytest-cov pytest-benchmark

# Tests de base
echo "📋 Tests de base..."
python -m pytest tests/ -v --tb=short

# Couverture de code
echo "📊 Vérification couverture..."
python -m pytest tests/ --cov=athalia_core --cov-report=term-missing --cov-fail-under=75

# Tests de sécurité
echo "🔒 Tests de sécurité..."
python -m pytest tests/ -m security -v

# Tests de performance
echo "⚡ Tests de performance..."
python -m pytest tests/ -m performance -v

# Tests robotiques
echo "🤖 Tests robotiques..."
python -m pytest tests/ -m robotics -v

# Tests d'intégration
echo "🔗 Tests d'intégration..."
python -m pytest tests/integration/ -v

# Validation de la qualité du code
echo "🎯 Validation qualité du code..."
if command -v flake8 &> /dev/null; then
    flake8 athalia_core/ --max-line-length=100 --ignore=E501,W503
    echo "✅ Flake8 validation passed"
else
    echo "⚠️ Flake8 non installé, skip de la validation"
fi

# Validation des imports
echo "📦 Validation des imports..."
python -c "import athalia_core; print('✅ Imports valides')"

# Génération du rapport de couverture HTML
echo "📄 Génération rapport HTML..."
python -m pytest tests/ --cov=athalia_core --cov-report=html --cov-report=term-missing

echo ""
echo "🎉 Validation CI/CD terminée avec succès"
echo "📊 Rapport de couverture disponible dans htmlcov/index.html"
echo "📈 Couverture actuelle : $(python -m pytest tests/ --cov=athalia_core --cov-report=term | grep TOTAL | awk '{print $4}')"
