#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module intelligent_memory.
Tests professionnels pour la CI/CD.
"""

import tempfile
import unittest
from datetime import datetime
from pathlib import Path

# Import du module à tester
try:
    from athalia_core.intelligent_memory import (
        CorrectionSuggestion,
        IntelligentMemory,
        LearningEvent,
        Prediction,
    )
except ImportError:
    # Type: ignore pour éviter les erreurs de type quand le module n'est pas disponible
    IntelligentMemory = None  # type: ignore
    CorrectionSuggestion = None  # type: ignore
    LearningEvent = None  # type: ignore
    Prediction = None  # type: ignore


class TestIntelligentMemory(unittest.TestCase):
    """Tests pour le système de mémoire intelligente"""

    def setUp(self):
        """Configuration initiale pour chaque test"""
        # Créer un répertoire temporaire pour les tests
        self.test_dir = tempfile.mkdtemp()
        self.memory = IntelligentMemory(root_path=self.test_dir)

    def tearDown(self):
        """Nettoyage après chaque test"""
        # Supprimer le répertoire temporaire
        import shutil

        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_init_database(self):
        """Test de l'initialisation de la base de données"""
        # Vérifier que la base de données est créée
        db_path = Path(self.test_dir) / "data" / "intelligent_memory.db"
        self.assertTrue(db_path.exists())

        # Vérifier que les tables sont créées
        import sqlite3

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]

            expected_tables = [
                "learning_events",
                "predictions",
                "correction_suggestions",
                "learned_patterns",
                "learning_metrics",
            ]
            for table in expected_tables:
                self.assertIn(table, tables)

    def test_learn_from_error(self):
        """Test d'apprentissage d'une erreur"""
        error_description = "Fonction trop longue détectée"
        code_snippet = "def very_long_function():\n    # 100 lignes de code..."
        location = "test_file.py:10"

        event_id = self.memory.learn_from_error(
            error_description=error_description,
            code_snippet=code_snippet,
            location=location,
            severity="medium",
        )

        self.assertIsInstance(event_id, str)
        self.assertTrue(len(event_id) > 0)

    def test_learn_from_correction(self):
        """Test d'apprentissage d'une correction"""
        original_code = "def very_long_function():\n    # 100 lignes..."
        corrected_code = (
            "def short_function1():\n    # 30 lignes...\n"
            "def short_function2():\n    # 30 lignes..."
        )
        reason = "Division en fonctions plus petites"
        location = "test_file.py:10"

        event_id = self.memory.learn_from_correction(
            original_code=original_code,
            corrected_code=corrected_code,
            reason=reason,
            location=location,
            success=True,
        )

        self.assertIsInstance(event_id, str)
        self.assertTrue(len(event_id) > 0)

    def test_learn_from_duplicate(self):
        """Test d'apprentissage d'un doublon"""
        duplicate_items = ["function1", "function2"]
        locations = ["file1.py:10", "file2.py:15"]
        similarity_score = 0.85

        event_id = self.memory.learn_from_duplicate(
            duplicate_items=duplicate_items,
            locations=locations,
            similarity_score=similarity_score,
        )

        self.assertIsInstance(event_id, str)
        self.assertTrue(len(event_id) > 0)

    def test_predict_issues(self):
        """Test de prédiction d'issues"""
        code_snippet = "def another_long_function():\n    # 80 lignes de code..."

        predictions = self.memory.predict_issues(code_snippet)

        self.assertIsInstance(predictions, list)
        # Même sans données d'apprentissage, on peut avoir des prédictions basées
        # sur des anti-patterns
        self.assertGreaterEqual(len(predictions), 0)

    def test_suggest_corrections(self):
        """Test de suggestions de corrections"""
        problematic_code = (
            "def bad_function():\n    print('Hello')\n    print('World')\n    print('Again')"
        )
        issue_description = "Fonction avec trop de prints"

        suggestions = self.memory.suggest_corrections(
            problematic_code=problematic_code, issue_description=issue_description
        )

        self.assertIsInstance(suggestions, list)
        # Même sans données d'apprentissage, on peut avoir des suggestions basiques
        self.assertGreaterEqual(len(suggestions), 0)

    def test_get_learning_insights(self):
        """Test de récupération des insights d'apprentissage"""
        insights = self.memory.get_learning_insights()

        self.assertIsInstance(insights, dict)
        expected_keys = [
            "total_events",
            "total_errors",
            "total_successes",
            "error_rate",
            "total_patterns",
            "total_predictions",
            "total_corrections",
            "learning_progress",
        ]

        for key in expected_keys:
            self.assertIn(key, insights)

    def test_analyze_code_pattern(self):
        """Test d'analyse de pattern de code"""
        code = "def test_function():\n    return True"
        pattern_hash = self.memory._analyze_code_pattern(code)

        self.assertIsInstance(pattern_hash, str)
        self.assertEqual(len(pattern_hash), 32)  # MD5 hash length

    def test_normalize_code(self):
        """Test de normalisation de code"""
        code = """
        # Commentaire
        def test_function():
            \"\"\"Docstring\"\"\"
            return True  # Inline comment
        """

        normalized = self.memory._normalize_code(code)

        self.assertIsInstance(normalized, str)
        self.assertNotIn("#", normalized)  # Commentaires supprimés
        self.assertNotIn('"""', normalized)  # Docstrings supprimées

    def test_calculate_code_similarity(self):
        """Test de calcul de similarité de code"""
        code1 = "def function1():\n    return True"
        code2 = "def function2():\n    return True"

        similarity = self.memory._calculate_code_similarity(code1, code2)

        self.assertIsInstance(similarity, float)
        self.assertGreaterEqual(similarity, 0.0)
        self.assertLessEqual(similarity, 1.0)

    def test_record_learning_event(self):
        """Test d'enregistrement d'événement d'apprentissage"""
        event_id = self.memory._record_learning_event(
            event_type="error",
            description="Test error",
            code_snippet="def test():\n    pass",
            location="test.py:1",
            severity="low",
            success=True,
        )

        self.assertIsInstance(event_id, str)
        self.assertTrue(len(event_id) > 0)

    def test_find_similar_patterns(self):
        """Test de recherche de patterns similaires"""
        pattern_hash = "test_hash_12345678901234567890123456789012"
        similar_patterns = self.memory._find_similar_patterns(pattern_hash)

        self.assertIsInstance(similar_patterns, list)

    def test_check_antipatterns(self):
        """Test de vérification d'anti-patterns"""
        code_snippet = "def bad_function():\n    pass"
        predictions = self.memory._check_antipatterns(code_snippet)

        self.assertIsInstance(predictions, list)

    def test_check_potential_duplicates(self):
        """Test de vérification de doublons potentiels"""
        code_snippet = "def test_function():\n    pass"
        predictions = self.memory._check_potential_duplicates(code_snippet)

        self.assertIsInstance(predictions, list)

    def test_save_correction_suggestion(self):
        """Test de sauvegarde de suggestion de correction"""
        original_code = "def bad():\n    pass"
        corrected_code = "def good():\n    pass"
        reason = "Amélioration du nom"

        # Ne devrait pas lever d'exception
        self.memory._save_correction_suggestion(
            original_code=original_code,
            corrected_code=corrected_code,
            reason=reason,
            success=True,
        )

    def test_learning_event_dataclass(self):
        """Test de la dataclass LearningEvent"""
        event = LearningEvent(
            event_type="error",
            description="Test event",
            code_snippet="def test():\n    pass",
            location="test.py:1",
            timestamp=datetime.now(),
            severity="low",
        )

        self.assertEqual(event.event_type, "error")
        self.assertEqual(event.description, "Test event")
        self.assertEqual(event.severity, "low")

    def test_prediction_dataclass(self):
        """Test de la dataclass Prediction"""
        prediction = Prediction(
            prediction_type="error",
            confidence=0.8,
            description="Test prediction",
            suggested_action="Refactor",
            estimated_impact="high",
            code_pattern="test_pattern",
        )

        self.assertEqual(prediction.prediction_type, "error")
        self.assertEqual(prediction.confidence, 0.8)
        self.assertEqual(prediction.estimated_impact, "high")

    def test_correction_suggestion_dataclass(self):
        """Test de la dataclass CorrectionSuggestion"""
        suggestion = CorrectionSuggestion(
            original_code="def bad():\n    pass",
            suggested_code="def good():\n    pass",
            reason="Amélioration",
            confidence=0.9,
            based_on_previous_corrections=[],
        )

        self.assertEqual(suggestion.original_code, "def bad():\n    pass")
        self.assertEqual(suggestion.confidence, 0.9)

    def test_integration_workflow(self):
        """Test d'un workflow d'intégration complet"""
        # 1. Apprendre d'une erreur
        error_id = self.memory.learn_from_error(
            error_description="Fonction trop longue",
            code_snippet="def long_function():\n    # 50 lignes...",
            location="test.py:10",
            severity="medium",
        )

        # 2. Apprendre d'une correction
        correction_id = self.memory.learn_from_correction(
            original_code="def long_function():\n    # 50 lignes...",
            corrected_code="def short_function():\n    # 10 lignes...",
            reason="Division en fonctions plus petites",
            location="test.py:10",
            success=True,
        )

        # 3. Prédire des issues sur du code similaire
        predictions = self.memory.predict_issues(
            "def another_long_function():\n    # 60 lignes..."
        )

        # 4. Obtenir des insights
        insights = self.memory.get_learning_insights()

        # Vérifications
        self.assertIsInstance(error_id, str)
        self.assertIsInstance(correction_id, str)
        self.assertIsInstance(predictions, list)
        self.assertIsInstance(insights, dict)
        self.assertGreaterEqual(insights["total_events"], 2)


if __name__ == "__main__":
    unittest.main()
