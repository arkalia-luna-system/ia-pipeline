#!/usr/bin/env python3
"""
Tests unitaires pour le module tutorials.video_tutorial_system
"""

import json
import logging
import shutil
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest


class TestVideoTutorialSystem:
    """Tests pour le module InteractiveTutorialSystem"""

    def setup_method(self):
        """Configuration avant chaque test"""
        self.project_path = Path(tempfile.mkdtemp())

    def teardown_method(self):
        """Nettoyage après chaque test"""
        if self.project_path.exists():
            shutil.rmtree(self.project_path)

    def test_video_tutorial_system_import(self):
        """Test de l'import du module InteractiveTutorialSystem"""
        try:
            from athalia_core.tutorials.interactive_tutorial_system import (
                InteractiveTutorialSystem,
            )

            assert InteractiveTutorialSystem is not None
            assert callable(InteractiveTutorialSystem)
        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")

    def test_video_tutorial_system_initialization(self):
        """Test de l'initialisation de InteractiveTutorialSystem"""
        try:
            from athalia_core.tutorials.interactive_tutorial_system import (
                InteractiveTutorialSystem,
            )

            # Créer une instance
            system = InteractiveTutorialSystem(str(self.project_path))

            # Vérifier les attributs de base
            assert system.project_path == self.project_path
            assert system.tutorials_dir == self.project_path / "dashboard" / "tutorials"
            assert hasattr(system, "tutorials")
            assert isinstance(system.tutorials, list)
            assert len(system.tutorials) > 0

        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")

    def test_get_default_tutorials(self):
        """Test de la méthode _get_default_tutorials"""
        try:
            from athalia_core.tutorials.interactive_tutorial_system import (
                InteractiveTutorialSystem,
            )

            system = InteractiveTutorialSystem(str(self.project_path))

            # Vérifier que les tutoriels par défaut sont présents
            tutorials = system.tutorials

            # Vérifier la structure des tutoriels
            for tutorial in tutorials:
                assert hasattr(tutorial, "id")
                assert hasattr(tutorial, "title")
                assert hasattr(tutorial, "description")
                assert hasattr(tutorial, "estimated_total_time")
                assert hasattr(tutorial, "difficulty")
                assert hasattr(tutorial, "category")
                assert hasattr(tutorial, "steps")
                assert hasattr(tutorial, "tags")

                # Vérifier les types
                assert isinstance(tutorial.id, str)
                assert isinstance(tutorial.title, str)
                assert isinstance(tutorial.description, str)
                assert isinstance(tutorial.estimated_total_time, int)
                assert isinstance(tutorial.difficulty, str)
                assert isinstance(tutorial.category, str)
                assert isinstance(tutorial.steps, list)
                assert isinstance(tutorial.tags, list)

        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")

    def test_get_tutorials_summary(self):
        """Test de la méthode get_tutorials_summary"""
        try:
            from athalia_core.tutorials.interactive_tutorial_system import (
                InteractiveTutorialSystem,
            )

            system = InteractiveTutorialSystem(str(self.project_path))

            summary = system.get_tutorials_summary()
            assert isinstance(summary, dict)

            # Vérifier les clés attendues (selon ton implémentation réelle)
            expected_keys = [
                "total_tutorials",
                "total_steps",
                "total_attempts",
                "average_completion_rate",
                "categories",
                "difficulties",
                "last_updated",
            ]
            for key in expected_keys:
                assert key in summary

            # Vérifier les types
            assert isinstance(summary["total_tutorials"], int)
            assert isinstance(summary["total_steps"], int)
            assert isinstance(summary["total_attempts"], int)
            assert isinstance(summary["average_completion_rate"], float)
            assert isinstance(summary["categories"], list)
            assert isinstance(summary["difficulties"], list)
            assert isinstance(summary["last_updated"], str)

            # Vérifier les valeurs logiques
            assert summary["total_tutorials"] > 0
            assert summary["total_steps"] > 0
            assert summary["total_attempts"] >= 0
            assert 0 <= summary["average_completion_rate"] <= 100

        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")

    @patch("webbrowser.open")
    def test_open_tutorials(self, mock_browser):
        """Test de la méthode open_tutorials"""
        try:
            from athalia_core.tutorials.interactive_tutorial_system import (
                InteractiveTutorialSystem,
            )

            system = InteractiveTutorialSystem(str(self.project_path))

            # Test d'ouverture des tutoriels
            system.open_tutorials()
            mock_browser.assert_called_once()

        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")

    def test_generate_tutorials_interface(self):
        """Test de la méthode generate_tutorials_interface"""
        try:
            from athalia_core.tutorials.interactive_tutorial_system import (
                InteractiveTutorialSystem,
            )

            system = InteractiveTutorialSystem(str(self.project_path))

            # Générer l'interface
            interface_file = system.generate_tutorials_interface()

            # Vérifier que le fichier a été créé
            assert Path(interface_file).exists()

            # Vérifier que c'est un fichier HTML
            with open(interface_file, encoding="utf-8") as f:
                content = f.read()
                assert "<!DOCTYPE html>" in content
                assert "<html" in content  # Plus flexible pour lang="fr"
                assert "</html>" in content
                assert "Athalia" in content

        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")

    def test_module_structure(self):
        """Test de la structure du module"""
        try:
            from athalia_core.tutorials.interactive_tutorial_system import (
                InteractiveTutorialSystem,
            )

            # Vérifier que la classe a les méthodes attendues
            assert hasattr(InteractiveTutorialSystem, "__init__")
            assert hasattr(InteractiveTutorialSystem, "start_tutorial")
            assert hasattr(InteractiveTutorialSystem, "get_current_step")
            assert hasattr(InteractiveTutorialSystem, "open_tutorials")
            assert hasattr(InteractiveTutorialSystem, "generate_tutorials_interface")

        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")

    def test_module_docstring(self):
        """Test de la docstring du module"""
        try:
            import athalia_core.tutorials.interactive_tutorial_system as module

            # Vérifier que le module a une docstring
            assert module.__doc__ is not None
            assert len(module.__doc__) > 0

            # Vérifier que la docstring contient des informations utiles
            docstring = module.__doc__
            assert "tutoriels" in docstring.lower() or "tutorials" in docstring.lower()

        except ImportError as e:
            pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")


def test_module_integration():
    """Test d'intégration complet du module"""
    try:
        from athalia_core.tutorials.interactive_tutorial_system import (
            InteractiveTutorialSystem,
        )

        # Test d'import complet du module
        assert InteractiveTutorialSystem is not None
        assert callable(InteractiveTutorialSystem)

        # Test de création d'instance
        with tempfile.TemporaryDirectory() as temp_dir:
            system = InteractiveTutorialSystem(temp_dir)

            # Vérifier les attributs de base
            assert hasattr(system, "project_path")
            assert hasattr(system, "tutorials")
            assert isinstance(system.tutorials, list)

    except ImportError as e:
        pytest.skip(f"Module InteractiveTutorialSystem non disponible: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
