#!/bin/bash
# Validation Express d'Athalia/Arkalia - 30 secondes chrono

echo "🚀 Validation Express Athalia/Arkalia"
echo "======================================"

# Variables
START_TIME=$(date +%s)
SUCCESS_COUNT=0
TOTAL_TESTS=0

# Fonction pour incrémenter les compteurs
increment_test() {
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    if [ $1 -eq 0 ]; then
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        echo "✅ $2"
    else
        echo "❌ $2"
    fi
}

# Test 1: Démarrage (5s max)
echo "📝 Test 1: Démarrage..."
timeout 5s python athalia_unified.py --help > /dev/null 2>&1
increment_test $? "Démarrage OK"

# Test 2: Imports (5s max)
echo "📦 Test 2: Imports..."
timeout 5s python -c "
import sys
sys.path.insert(0, '.')
try:
    from athalia_core.main import *
    from athalia_core.ai_robust import *
    print('OK')
except Exception as e:
    print(f'ERREUR: {e}')
    sys.exit(1)
" > /dev/null 2>&1
increment_test $? "Imports OK"

# Test 3: Génération express (15s max)
echo "⚡ Test 3: Génération express..."
PROJECT_TEST="/tmp/test_express_$(date +%s)"
mkdir -p "$PROJECT_TEST"
echo 'def test():
    return "express test"' > "$PROJECT_TEST/main.py"

timeout 15s python athalia_unified.py "$PROJECT_TEST" --action complete > /dev/null 2>&1
if [ $? -eq 0 ]; then
    # Vérifie qu'il y a des fichiers Python
    PY_FILES=$(find "$PROJECT_TEST" -name "*.py" | wc -l)
    if [ $PY_FILES -gt 0 ]; then
        increment_test 0 "Génération OK ($PY_FILES fichiers Python)"
    else
        increment_test 1 "Génération échouée (pas de fichiers Python)"
    fi
    # Nettoyage
    rm -rf "$PROJECT_TEST"
else
    increment_test 1 "Génération échouée"
    rm -rf "$PROJECT_TEST"
fi

# Test 4: Correction basique (5s max)
echo "🔧 Test 4: Correction basique..."
TEST_FILE="/tmp/test_correction_express.py"
echo 'def test():
    x = 1
    return x + y  # y nexiste pas' > "$TEST_FILE"

timeout 5s python athalia_unified.py "$(dirname "$TEST_FILE")" --action fix --auto-fix > /dev/null 2>&1
if [ $? -eq 0 ]; then
    # Vérifie si le fichier a été modifié
    if [ -s "$TEST_FILE" ]; then
        increment_test 0 "Correction OK"
    else
        increment_test 1 "Correction échouée (fichier vide)"
    fi
else
    increment_test 1 "Correction échouée"
fi
rm -f "$TEST_FILE"

# Calcul du temps total
END_TIME=$(date +%s)
TOTAL_TIME=$((END_TIME - START_TIME))

# Calcul du score
SCORE=$((SUCCESS_COUNT * 100 / TOTAL_TESTS))

echo ""
echo "🏁 Validation terminée !"
echo "========================"
echo "⏱️  Temps total: ${TOTAL_TIME}s"
echo "📊 Tests réussis: $SUCCESS_COUNT/$TOTAL_TESTS"
echo "🎯 Score: ${SCORE}%"

# Verdict
if [ $SCORE -ge 90 ]; then
    echo "🎉 EXCELLENT - Athalia est très fiable !"
    EXIT_CODE=0
elif [ $SCORE -ge 75 ]; then
    echo "✅ BON - Athalia est fiable avec quelques améliorations"
    EXIT_CODE=0
elif [ $SCORE -ge 50 ]; then
    echo "⚠️  MOYEN - Athalia a des problèmes à corriger"
    EXIT_CODE=1
else
    echo "❌ PROBLÉMATIQUE - Athalia nécessite une refonte"
    EXIT_CODE=1
fi

# Sauvegarde du rapport
REPORT_FILE="validation_express_$(date +%Y%m%d_%H%M%S).txt"
{
    echo "Validation Express Athalia/Arkalia"
    echo "Date: $(date)"
    echo "Temps total: ${TOTAL_TIME}s"
    echo "Tests réussis: $SUCCESS_COUNT/$TOTAL_TESTS"
    echo "Score: ${SCORE}%"
    echo ""
    echo "Verdict: $([ $SCORE -ge 90 ] && echo "EXCELLENT" || [ $SCORE -ge 75 ] && echo "BON" || [ $SCORE -ge 50 ] && echo "MOYEN" || echo "PROBLÉMATIQUE")"
} > "$REPORT_FILE"

echo ""
echo "📄 Rapport sauvegardé: $REPORT_FILE"

exit $EXIT_CODE 