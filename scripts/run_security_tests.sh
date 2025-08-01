#!/bin/bash
set -e

echo "🧪 Running security tests..."

# Vérifier l'environnement
if [ -z "$CI" ]; then
    echo "🛡️ Protection automatique des tests DÉSACTIVÉE"
    echo "⚠️ Les fichiers de tests ne seront plus supprimés automatiquement"
fi

# Installer pytest-cov si nécessaire
if ! python -c "import pytest_cov" 2>/dev/null; then
    echo "📦 Installation de pytest-cov..."
    pip install pytest-cov>=4.0.0
fi

# Tester si les arguments de couverture fonctionnent
if python -m pytest --help 2>&1 | grep -q "\-\-cov="; then
    echo "✅ Arguments de couverture supportés"
    COVERAGE_ARGS="--cov=athalia_core --cov-report=html:htmlcov --cov-report=term-missing --cov-branch --no-cov-on-fail"
else
    echo "⚠️ Arguments de couverture non supportés, utilisation de coverage standard"
    COVERAGE_ARGS="--no-cov"
fi

# Exécuter les tests
echo "🔍 Exécution des tests de sécurité..."
python -m pytest tests/unit/security/ $COVERAGE_ARGS

echo "✅ Tests de sécurité terminés" 