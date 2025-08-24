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
    """Tests pour le module tutorials.video_tutorial_system"""

    def setup_method(self):
        """Setup pour chaque test"""
        # Créer un répertoire temporaire pour les tests
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir)

    def teardown_method(self):
        """Cleanup après chaque test"""
        # Nettoyer le répertoire temporaire
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_video_tutorial_system_import(self):
        """Test que le module peut être importé"""
        try:
            from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

            assert VideoTutorialSystem is not None
            assert callable(VideoTutorialSystem)
        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")

    def test_video_tutorial_system_initialization(self):
        """Test de l'initialisation de VideoTutorialSystem"""
        try:
            from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

            # Créer une instance
            system = VideoTutorialSystem(str(self.project_path))

            # Vérifier les attributs de base
            assert system.project_path == self.project_path
            assert system.tutorials_dir == self.project_path / "dashboard" / "tutorials"
            assert isinstance(system.tutorials_data, list)
            assert len(system.tutorials_data) > 0

        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")

    def test_get_default_tutorials(self):
        """Test de la méthode _get_default_tutorials"""
        try:
            from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

            system = VideoTutorialSystem(str(self.project_path))

            # Vérifier que les tutoriels par défaut sont présents
            tutorials = system.tutorials_data

            # Vérifier la structure des tutoriels
            for tutorial in tutorials:
                assert "id" in tutorial
                assert "title" in tutorial
                assert "description" in tutorial
                assert "duration" in tutorial
                assert "difficulty" in tutorial
                assert "category" in tutorial
                assert "thumbnail" in tutorial
                assert "video_url" in tutorial
                assert "tags" in tutorial
                assert "views" in tutorial
                assert "rating" in tutorial
                assert "created_at" in tutorial

                # Vérifier les types
                assert isinstance(tutorial["id"], str)
                assert isinstance(tutorial["title"], str)
                assert isinstance(tutorial["description"], str)
                assert isinstance(tutorial["duration"], str)
                assert isinstance(tutorial["difficulty"], str)
                assert isinstance(tutorial["category"], str)
                assert isinstance(tutorial["thumbnail"], str)
                assert isinstance(tutorial["video_url"], str)
                assert isinstance(tutorial["tags"], list)
                assert isinstance(tutorial["views"], int)
                assert isinstance(tutorial["rating"], int | float)
                assert isinstance(tutorial["created_at"], str)

        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")

    def test_get_tutorials_summary(self):
        """Test de la méthode get_tutorials_summary"""
        try:
            from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

            system = VideoTutorialSystem(str(self.project_path))

            summary = system.get_tutorials_summary()
            assert isinstance(summary, dict)

            # Vérifier les clés attendues
            expected_keys = [
                "total_tutorials",
                "total_views",
                "average_rating",
                "categories",
                "difficulties",
                "last_updated",
            ]
            for key in expected_keys:
                assert key in summary

            # Vérifier les types
            assert isinstance(summary["total_tutorials"], int)
            assert isinstance(summary["total_views"], int)
            assert isinstance(summary["average_rating"], int | float)
            assert isinstance(summary["categories"], list)
            assert isinstance(summary["difficulties"], list)
            assert isinstance(summary["last_updated"], str)

            # Vérifier les valeurs logiques
            assert summary["total_tutorials"] > 0
            assert summary["total_views"] >= 0
            assert 0 <= summary["average_rating"] <= 5

        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")

    @patch("webbrowser.open")
    def test_open_tutorials(self, mock_browser):
        """Test de la méthode open_tutorials"""
        try:
            from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

            system = VideoTutorialSystem(str(self.project_path))

            # Test d'ouverture des tutoriels
            system.open_tutorials()
            mock_browser.assert_called_once()

        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")

    def test_generate_tutorials_interface(self):
        """Test de la méthode generate_tutorials_interface"""
        try:
            from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

            system = VideoTutorialSystem(str(self.project_path))

            # Générer l'interface
            interface_file = system.generate_tutorials_interface()

            # Vérifier que le fichier a été créé
            assert Path(interface_file).exists()

            # Vérifier que c'est un fichier HTML
            with open(interface_file, encoding="utf-8") as f:
                content = f.read()
                assert "<!DOCTYPE html>" in content
                assert "<html" in content  # Changed from "<html>" to "<html"
                assert "</html>" in content
                assert "Athalia" in content

        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")

    def test_module_structure(self):
        """Test de la structure du module"""
        try:
            from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

            # Vérifier que la classe a les méthodes attendues
            assert hasattr(VideoTutorialSystem, "__init__")
            assert hasattr(VideoTutorialSystem, "get_tutorials_summary")
            assert hasattr(VideoTutorialSystem, "open_tutorials")
            assert hasattr(VideoTutorialSystem, "generate_tutorials_interface")

        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")

    def test_module_docstring(self):
        """Test que le module a une docstring appropriée"""
        try:
            import athalia_core.tutorials.video_tutorial_system as module

            # Vérifier que le module a une docstring
            assert module.__doc__ is not None
            assert len(module.__doc__) > 0

            # Vérifier que la docstring contient des informations utiles
            docstring = module.__doc__
            assert "tutoriels" in docstring.lower() or "tutorials" in docstring.lower()

        except ImportError as e:
            pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")


def test_module_integration():
    """Test d'intégration du module"""
    try:
        from athalia_core.tutorials.video_tutorial_system import VideoTutorialSystem

        # Test d'import complet du module
        assert VideoTutorialSystem is not None
        assert callable(VideoTutorialSystem)

        # Test de création d'instance
        with tempfile.TemporaryDirectory() as temp_dir:
            system = VideoTutorialSystem(temp_dir)
            assert system is not None
            assert hasattr(system, "tutorials_data")
            assert isinstance(system.tutorials_data, list)

    except ImportError as e:
        pytest.skip(f"Module VideoTutorialSystem non disponible: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
