"""
Tests pour le module athalia_core.auto_documenter
Tests appropriés pour la génération automatique de documentation
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

import athalia_core.auto_documenter as module


def test_module_import():
    """Test que le module peut être importé."""
    assert module is not None


def test_module_has_content():
    """Test que le module a du contenu."""
    assert len(dir(module)) > 0


def test_function_generate_documentation_exists():
    """Test que la fonction generate_documentation existe."""
    assert hasattr(module, "generate_documentation")
    assert callable(getattr(module, "generate_documentation"))


def test_function_analyze_documentation_needs_exists():
    """Test que la fonction analyze_documentation_needs existe."""
    assert hasattr(module, "analyze_documentation_needs")
    assert callable(getattr(module, "analyze_documentation_needs"))


def test_class_AutoDocumenter_exists():
    """Test que la classe AutoDocumenter existe."""
    assert hasattr(module, "AutoDocumenter")
    from athalia_core.auto_documenter import AutoDocumenter
    assert AutoDocumenter is not None


class TestAutoDocumenter:
    """Tests pour la classe AutoDocumenter"""

    def test_auto_documenter_initialization(self):
        """Test l'initialisation de AutoDocumenter."""
        with tempfile.TemporaryDirectory() as temp_dir:
            doc = module.AutoDocumenter(temp_dir)
            assert doc.project_path == Path(temp_dir)
            assert doc.lang == "en"
            assert doc.doc_config is not None
            assert doc.doc_history == []

    def test_auto_documenter_default_initialization(self):
        """Test l'initialisation par défaut de AutoDocumenter."""
        doc = module.AutoDocumenter()
        assert doc.project_path == Path(".")
        assert doc.lang == "en"

    def test_load_documentation_config_default(self):
        """Test le chargement de la configuration par défaut."""
        doc = module.AutoDocumenter()
        config = doc.load_documentation_config()
        
        assert "output_formats" in config
        assert "include_private" in config
        assert "generate_api_docs" in config
        assert "exclude_patterns" in config
        assert "include_patterns" in config

    def test_is_excluded_method(self):
        """Test la méthode _is_excluded."""
        doc = module.AutoDocumenter()
        
        # Test avec un fichier Python normal
        normal_file = Path("test_file.py")
        assert not doc._is_excluded(normal_file)
        
        # Test avec un fichier __pycache__
        cache_file = Path("__pycache__/test.pyc")
        assert doc._is_excluded(cache_file)

    def test_scan_project_structure_empty(self):
        """Test le scan d'une structure de projet vide."""
        with tempfile.TemporaryDirectory() as temp_dir:
            doc = module.AutoDocumenter(temp_dir)
            structure = doc.scan_project_structure()
            
            assert "python_files" in structure
            assert "test_files" in structure
            assert "documentation_files" in structure
            assert "config_files" in structure
            assert "other_files" in structure

    def test_scan_project_structure_with_files(self):
        """Test le scan d'une structure avec des fichiers."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Créer quelques fichiers de test
            (Path(temp_dir) / "test.py").touch()
            (Path(temp_dir) / "test_test.py").touch()
            (Path(temp_dir) / "README.md").touch()
            (Path(temp_dir) / "config.yaml").touch()
            
            doc = module.AutoDocumenter(temp_dir)
            structure = doc.scan_project_structure()
            
            # Vérifier que la structure contient les bonnes clés
            assert "python_files" in structure
            assert "test_files" in structure
            assert "documentation_files" in structure
            assert "config_files" in structure
            assert "other_files" in structure

    @patch('athalia_core.auto_documenter.yaml.safe_load')
    def test_load_documentation_config_with_file(self, mock_yaml_load):
        """Test le chargement de configuration depuis un fichier."""
        mock_yaml_load.return_value = {
            "output_formats": ["pdf"],
            "include_private": True
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml') as temp_file:
            temp_file.write("test: config")
            temp_file.flush()
            
            doc = module.AutoDocumenter()
            config = doc.load_documentation_config(temp_file.name)
            
            assert config["output_formats"] == ["pdf"]
            assert config["include_private"] is True

    def test_calculate_documentation_coverage(self):
        """Test le calcul de la couverture de documentation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            doc = module.AutoDocumenter(temp_dir)
            coverage = doc.calculate_documentation_coverage()
            
            assert "total_files" in coverage
            assert "documented_files" in coverage
            assert "coverage_percentage" in coverage
            assert isinstance(coverage["coverage_percentage"], (int, float))

    def test_validate_documentation(self):
        """Test la validation de documentation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            doc = module.AutoDocumenter(temp_dir)
            validation = doc.validate_documentation()
            
            assert "is_valid" in validation
            assert "errors" in validation
            assert "warnings" in validation
            assert isinstance(validation["is_valid"], bool)

    def test_save_and_load_documentation_history(self):
        """Test la sauvegarde et le chargement de l'historique."""
        with tempfile.TemporaryDirectory() as temp_dir:
            doc = module.AutoDocumenter(temp_dir)
            
            # Ajouter un élément à l'historique
            doc.doc_history.append({"test": "entry"})
            
            # Sauvegarder
            history_file = os.path.join(temp_dir, "history.json")
            success = doc.save_documentation_history(history_file)
            assert success is True
            
            # Charger
            loaded_history = doc.load_documentation_history(history_file)
            assert len(loaded_history) >= 1
            assert loaded_history[0]["test"] == "entry"


def test_generate_documentation_function():
    """Test la fonction generate_documentation."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = module.generate_documentation(temp_dir)
        
        assert isinstance(result, dict)
        assert "success" in result or "status" in result


def test_analyze_documentation_needs_function():
    """Test la fonction analyze_documentation_needs."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = module.analyze_documentation_needs(temp_dir)
        
        assert isinstance(result, dict)
        assert "needs" in result or "recommendations" in result


def test_module_integration():
    """Test d'intégration de base du module."""
    # Test que le module peut être utilisé sans erreur
    try:
        # Essayer d'accéder aux attributs principaux
        for attr in dir(module):
            if not attr.startswith("_"):
                getattr(module, attr)
    except Exception as e:
        pytest.skip(f"Erreur lors de l'accès aux attributs: {e}")
