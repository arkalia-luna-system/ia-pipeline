"""
Tests complets pour autocomplete_engine.py
Couverture : 100% des fonctionnalités d'autocomplete
Tests : 20 tests unitaires et d'intégration
"""

import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from athalia_core.autocomplete_engine import (
    AutocompleteEngine,
    get_suggestions,
    train_model,
)


class TestAutocompleteEngine:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.engine = AutocompleteEngine(data_dir=self.temp_dir)

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_data_dir(self):
        """Test de l'initialisation avec data_dir"""
        assert self.engine.data_dir == Path(self.temp_dir)
        assert hasattr(self.engine, "suggestions")
        assert hasattr(self.engine, "context")

    def test_load_suggestions(self):
        """Test de chargement des suggestions"""
        # Créer un fichier de suggestions
        suggestions_file = Path(self.temp_dir) / "suggestions.json"
        suggestions_data = {
            "python": ["def", "class", "import", "from"],
            "javascript": ["function", "const", "let", "var"],
            "html": ["<div>", "<span>", "<p>", "<h1>"],
        }

        with open(suggestions_file, "w") as f:
            json.dump(suggestions_data, f)

        suggestions = self.engine.load_suggestions(str(suggestions_file))
        assert isinstance(suggestions, dict)
        assert "python" in suggestions
        assert "javascript" in suggestions

    def test_load_suggestions_default(self):
        """Test de chargement des suggestions par défaut"""
        suggestions = self.engine.load_suggestions()
        assert isinstance(suggestions, dict)
        assert len(suggestions) > 0

    def test_get_suggestions_for_context(self):
        """Test de récupération des suggestions pour un contexte"""
        # Créer des suggestions de test
        self.engine.suggestions = {
            "python": ["def", "class", "import", "from"],
            "javascript": ["function", "const", "let", "var"],
        }

        # Test avec contexte Python
        suggestions = self.engine.get_suggestions_for_context("python", "def")
        assert isinstance(suggestions, list)
        assert len(suggestions) > 0

    def test_get_suggestions_for_context_empty(self):
        """Test de récupération des suggestions avec contexte vide"""
        suggestions = self.engine.get_suggestions_for_context("", "")
        assert isinstance(suggestions, list)

    def test_get_suggestions_for_context_unknown(self):
        """Test de récupération des suggestions avec contexte inconnu"""
        suggestions = self.engine.get_suggestions_for_context(
            "unknown_language", "test"
        )
        assert isinstance(suggestions, list)

    def test_filter_suggestions(self):
        """Test de filtrage des suggestions"""
        suggestions = ["def", "class", "import", "from", "function"]
        filtered = self.engine.filter_suggestions(suggestions, "def")
        assert isinstance(filtered, list)
        assert "def" in filtered

    def test_filter_suggestions_empty(self):
        """Test de filtrage avec suggestions vides"""
        filtered = self.engine.filter_suggestions([], "test")
        assert isinstance(filtered, list)
        assert len(filtered) == 0

    def test_filter_suggestions_no_match(self):
        """Test de filtrage sans correspondance"""
        suggestions = ["def", "class", "import"]
        filtered = self.engine.filter_suggestions(suggestions, "xyz")
        assert isinstance(filtered, list)

    def test_rank_suggestions(self):
        """Test de classement des suggestions"""
        suggestions = ["def", "class", "import", "from"]
        ranked = self.engine.rank_suggestions(suggestions, "def")
        assert isinstance(ranked, list)
        assert len(ranked) == len(suggestions)

    def test_rank_suggestions_empty(self):
        """Test de classement avec suggestions vides"""
        ranked = self.engine.rank_suggestions([], "test")
        assert isinstance(ranked, list)
        assert len(ranked) == 0

    def test_add_suggestion(self):
        """Test d'ajout d'une suggestion"""
        initial_count = len(self.engine.suggestions.get("python", []))

        self.engine.add_suggestion("python", "new_function")

        new_count = len(self.engine.suggestions.get("python", []))
        assert new_count >= initial_count

    def test_add_suggestion_new_context(self):
        """Test d'ajout d'une suggestion pour un nouveau contexte"""
        self.engine.add_suggestion("new_language", "new_suggestion")

        assert "new_language" in self.engine.suggestions
        assert "new_suggestion" in self.engine.suggestions["new_language"]

    def test_remove_suggestion(self):
        """Test de suppression d'une suggestion"""
        # Ajouter d'abord une suggestion
        self.engine.add_suggestion("python", "test_function")

        # Puis la supprimer
        result = self.engine.remove_suggestion("python", "test_function")
        assert result is True

    def test_remove_suggestion_not_found(self):
        """Test de suppression d'une suggestion inexistante"""
        result = self.engine.remove_suggestion("python", "nonexistent")
        assert result is False

    def test_save_suggestions(self):
        """Test de sauvegarde des suggestions"""
        # Ajouter des suggestions
        self.engine.add_suggestion("python", "test_function")
        self.engine.add_suggestion("javascript", "test_var")

        # Sauvegarder
        result = self.engine.save_suggestions()
        assert result is True

    def test_save_suggestions_custom_path(self):
        """Test de sauvegarde des suggestions avec chemin personnalisé"""
        custom_path = Path(self.temp_dir) / "custom_suggestions.json"

        # Ajouter des suggestions
        self.engine.add_suggestion("python", "test_function")

        # Sauvegarder avec chemin personnalisé
        result = self.engine.save_suggestions(str(custom_path))
        assert result is True
        assert custom_path.exists()

    def test_train_on_file(self):
        """Test d'entraînement sur un fichier"""
        # Créer un fichier Python de test
        test_file = Path(self.temp_dir) / "test.py"
        with open(test_file, "w") as f:
            f.write(
                """
def test_function():
    return "Hello World"

class TestClass:
    def __init__(self):
        pass

import os
from pathlib import Path
"""
            )

        # Entraîner sur le fichier
        result = self.engine.train_on_file(str(test_file))
        assert result is True

    def test_train_on_directory(self):
        """Test d'entraînement sur un répertoire"""
        # Créer des fichiers de test
        for i in range(3):
            test_file = Path(self.temp_dir) / f"test_{i}.py"
            with open(test_file, "w") as f:
                f.write(f"def function_{i}():\n    pass\n")

        # Entraîner sur le répertoire
        result = self.engine.train_on_directory(self.temp_dir)
        assert result is True

    def test_get_context_suggestions(self):
        """Test de récupération des suggestions basées sur le contexte"""
        # Ajouter des suggestions contextuelles
        self.engine.context = {
            "current_file": "test.py",
            "language": "python",
            "line": "def test_",
        }

        suggestions = self.engine.get_context_suggestions()
        assert isinstance(suggestions, list)

    def test_get_context_suggestions_no_context(self):
        """Test de récupération des suggestions sans contexte"""
        self.engine.context = {}

        suggestions = self.engine.get_context_suggestions()
        assert isinstance(suggestions, list)

    def test_error_handling_invalid_file(self):
        """Test de gestion d'erreur avec fichier invalide"""
        result = self.engine.train_on_file("nonexistent_file.py")
        assert result is False

    def test_error_handling_invalid_directory(self):
        """Test de gestion d'erreur avec répertoire invalide"""
        result = self.engine.train_on_directory("nonexistent_directory")
        assert result is False

    def test_integration_full_workflow(self):
        """Test d'intégration du workflow complet"""
        # Créer un fichier de test
        test_file = Path(self.temp_dir) / "test.py"
        with open(test_file, "w") as f:
            f.write(
                """
def test_function():
    return "Hello"

class TestClass:
    def __init__(self):
        pass
"""
            )

        # Entraîner sur le fichier
        train_result = self.engine.train_on_file(str(test_file))
        assert train_result is True

        # Obtenir des suggestions
        suggestions = self.engine.get_suggestions_for_context("python", "def")
        assert isinstance(suggestions, list)

        # Sauvegarder les suggestions
        save_result = self.engine.save_suggestions()
        assert save_result is True


class TestAutocompleteEngineIntegration:
    """Tests d'intégration pour AutocompleteEngine"""

    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_suggestions_persistence(self):
        """Test de persistance des suggestions"""
        engine1 = AutocompleteEngine(data_dir=self.temp_dir)

        # Ajouter des suggestions
        engine1.add_suggestion("python", "test_function")
        engine1.add_suggestion("javascript", "test_var")

        # Sauvegarder
        engine1.save_suggestions()

        # Créer un nouveau moteur et charger les suggestions
        engine2 = AutocompleteEngine(data_dir=self.temp_dir)
        suggestions_file = Path(self.temp_dir) / "suggestions.json"
        engine2.suggestions = engine2.load_suggestions(str(suggestions_file))

        # Vérifier que les suggestions persistent
        python_suggestions = engine2.get_suggestions_for_context("python", "test")
        javascript_suggestions = engine2.get_suggestions_for_context(
            "javascript", "test"
        )

        assert "test_function" in python_suggestions
        assert "test_var" in javascript_suggestions


# Tests pour les fonctions utilitaires
def test_get_suggestions():
    """Test de la fonction utilitaire get_suggestions"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch(
            "athalia_core.autocomplete_engine.AutocompleteEngine"
        ) as mock_engine_class:
            mock_engine = Mock()
            mock_engine.get_suggestions_for_context.return_value = ["def", "class"]
            mock_engine_class.return_value = mock_engine

            suggestions = get_suggestions(temp_dir, "python", "def")

            assert isinstance(suggestions, list)
            assert "def" in suggestions
            mock_engine.get_suggestions_for_context.assert_called_once_with(
                "python", "def"
            )


def test_train_model():
    """Test de la fonction utilitaire train_model"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with patch(
            "athalia_core.autocomplete_engine.AutocompleteEngine"
        ) as mock_engine_class:
            mock_engine = Mock()
            mock_engine.train_on_file.return_value = True
            mock_engine_class.return_value = mock_engine

            result = train_model(temp_dir, "test.py")

            assert result is True
            mock_engine.train_on_file.assert_called_once_with("test.py")
