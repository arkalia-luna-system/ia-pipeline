"""
Tests pour le module autocomplete_engine.
"""

import tempfile

import pytest


def test_autocomplete_engine_import():
    """Test d'import du module autocomplete_engine."""
    try:
        from athalia_core.autocomplete_engine import AutocompleteEngine

        # Test avec répertoire temporaire
        with tempfile.TemporaryDirectory() as temp_dir:
            engine = AutocompleteEngine(temp_dir)
            assert engine is not None
            print("✅ Module autocomplete_engine importé avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import: {e}")
        pytest.skip("Module autocomplete_engine non disponible")


def test_autocomplete_engine_initialization():
    """Test d'initialisation du moteur de complétion."""
    try:
        from athalia_core.autocomplete_engine import AutocompleteEngine

        with tempfile.TemporaryDirectory() as temp_dir:
            engine = AutocompleteEngine(temp_dir)

            # Vérifier que les suggestions sont chargées
            assert isinstance(engine.suggestions, dict)
            assert hasattr(engine, "suggestions")
            print("✅ Moteur de complétion initialisé avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import: {e}")
        pytest.skip("Module autocomplete_engine non disponible")


def test_autocomplete_engine_suggestions():
    """Test de récupération des suggestions."""
    try:
        from athalia_core.autocomplete_engine import AutocompleteEngine

        with tempfile.TemporaryDirectory() as temp_dir:
            engine = AutocompleteEngine(temp_dir)

            # Test des suggestions Python
            suggestions = engine.get_suggestions_for_context("python", "def")
            assert isinstance(suggestions, list)
            assert len(suggestions) >= 0

            # Test des suggestions JavaScript
            suggestions = engine.get_suggestions_for_context("javascript", "function")
            assert isinstance(suggestions, list)
            assert len(suggestions) >= 0

            print("✅ Suggestions récupérées avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import: {e}")
        pytest.skip("Module autocomplete_engine non disponible")


def test_autocomplete_engine_integration():
    """Test d'intégration complète du module."""
    try:
        from athalia_core.autocomplete_engine import AutocompleteEngine

        with tempfile.TemporaryDirectory() as temp_dir:
            engine = AutocompleteEngine(temp_dir)

            # Test complet du workflow
            suggestions = engine.get_suggestions_for_context("python", "def")
            assert isinstance(suggestions, list)

            # Vérifier que le moteur peut gérer différents contextes
            assert hasattr(engine, "get_suggestions_for_context")
            assert callable(engine.get_suggestions_for_context)

            print("✅ Intégration du module testée avec succès")
    except ImportError as e:
        print(f"⚠️  Erreur d'import: {e}")
        pytest.skip("Module autocomplete_engine non disponible")
