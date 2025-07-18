#!/usr / bin/env bash
# Script de lancement des tests pour {self.project_path.name}
# Généré automatiquement par Athalia

echo "🧪 Lancement des tests pour {self.project_path.name}"

# Tests unitaires
echo "📋 Tests unitaires..."
python -m pytest tests / test_unit_*.py -v

# Tests dintégration
echo "🔗 Tests dintégration..."
python -m pytest tests / test_integration_*.py -v

# Tests de performance
echo "⚡ Tests de performance..."
python -m pytest tests / test_performance_*.py -v

# Tests avec couverture
echo "📊 Tests avec couverture..."
python -m pytest tests/ --cov=. --cov - report=html --cov - report=term

echo "✅ Tests terminés !"
