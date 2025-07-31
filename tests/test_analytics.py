#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour le module analytics
"""
from pathlib import Path
import tempfile

import pytest

# Import conditionnel du module analytics
try:
    from athalia_core.analytics import (
        analyze_project,
        generate_analytics_html,
        generate_heatmap_data,
        generate_technical_debt_analysis,
    )

    ANALYTICS_AVAILABLE = True
except ImportError:
    ANALYTICS_AVAILABLE = False


class TestAnalyticsModule:
    """Tests pour le module analytics d'Athalia"""

    def setup_method(self):
        """Configuration avant chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.project_dir = Path(self.temp_dir) / "test_project"
        self.project_dir.mkdir(exist_ok=True)

        # Créer un projet de test
        self.create_test_project()

    def teardown_method(self):
        """Nettoyage après chaque test"""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def create_test_project(self):
        """Créer un projet de test pour les analyses"""
        # Structure de projet
        (self.project_dir / "src").mkdir(exist_ok=True)
        (self.project_dir / "tests").mkdir(exist_ok=True)
        (self.project_dir / "docs").mkdir(exist_ok=True)

        # Fichiers Python
        (self.project_dir / "main.py").write_text(
            """
def main():
    print("Hello World")
    return True

if __name__ == "__main__":
    main()
"""
        )

        (self.project_dir / "src" / "module.py").write_text(
            """
class TestClass:
    def __init__(self):
        self.value = 42

    def get_value(self):
        return self.value

def helper_function():
    return "helper"
"""
        )

        # Tests
        (self.project_dir / "tests" / "test_main.py").write_text(
            """
import pytest

def test_main():
    assert True

def test_another():
    assert 1 + 1 == 2
"""
        )

        # Documentation
        (self.project_dir / "README.md").write_text(
            "# Test Project\n\nA test project for analytics."
        )
        (self.project_dir / "requirements.txt").write_text("pytest\nrequests")

    def test_analytics_module_import(self):
        """Test d'import du module analytics"""
        if not ANALYTICS_AVAILABLE:
            pytest.skip("Module analytics non disponible")
        assert ANALYTICS_AVAILABLE
        assert analyze_project is not None
        assert generate_heatmap_data is not None
        assert generate_technical_debt_analysis is not None

    def test_analyze_project(self):
        """Test d'analyse de projet"""
        try:
            result = analyze_project(str(self.project_dir))
            assert isinstance(result, dict)

            # Vérifier la nouvelle structure de base
            assert "project_name" in result
            assert "structure" in result
            assert "score" in result
            assert "metrics" in result
        except Exception as e:
            # Test échoue si la fonction ne fonctionne pas
            assert False, f"analyze_project non fonctionnel: {e}"

    def test_generate_heatmap_data(self):
        """Test de génération de données pour heatmap"""
        try:
            # Générer les données heatmap directement
            heatmap_data = generate_heatmap_data(str(self.project_dir))
            assert isinstance(heatmap_data, dict)
            assert "heatmap_data" in heatmap_data
            assert "total_files" in heatmap_data
        except Exception as e:
            # Test échoue si la fonction ne fonctionne pas
            assert False, f"generate_heatmap_data non fonctionnel: {e}"

    def test_generate_technical_debt_analysis(self):
        """Test d'analyse de dette technique"""
        try:
            # Générer l'analyse de dette technique directement
            debt_analysis = generate_technical_debt_analysis(str(self.project_dir))
            assert isinstance(debt_analysis, dict)

            # Vérifier la nouvelle structure de base
            assert "technical_debt_score" in debt_analysis
            assert "debt_indicators" in debt_analysis
            assert "recommendations" in debt_analysis
        except Exception as e:
            # Test échoue si la fonction ne fonctionne pas
            assert False, f"generate_technical_debt_analysis non fonctionnel: {e}"

    def test_generate_analytics_html(self):
        """Test de génération de rapport HTML"""
        try:
            # Générer le HTML directement
            html_report = generate_analytics_html(str(self.project_dir))
            assert isinstance(html_report, str)
            assert len(html_report) > 0
            assert "<html" in html_report.lower() or "<!DOCTYPE" in html_report
        except Exception as e:
            # Test échoue si la fonction ne fonctionne pas
            assert False, f"generate_analytics_html non fonctionnel: {e}"

    def test_analytics_with_empty_project(self):
        """Test d'analyse avec un projet vide"""
        empty_dir = Path(self.temp_dir) / "empty_project"
        empty_dir.mkdir(exist_ok=True)

        try:
            result = analyze_project(str(empty_dir))
            assert isinstance(result, dict)
        except Exception as e:
            # Test échoue si la fonction ne fonctionne pas
            assert False, f"analyze_project avec projet vide non fonctionnel: {e}"

    def test_analytics_with_nonexistent_project(self):
        """Test d'analyse avec un projet inexistant"""
        nonexistent_dir = "/tmp/nonexistent_project_12345"

        try:
            result = analyze_project(nonexistent_dir)
            # Peut retourner un résultat d'erreur ou lever une exception
            assert isinstance(result, dict) or isinstance(result, str)
        except Exception as e:
            # C'est acceptable qu'une exception soit levée
            assert "not found" in str(e).lower() or "does not exist" in str(e).lower()


def test_analytics_integration():
    """Test d'intégration du module analytics"""
    # Test que le module peut être importé
    try:
        from athalia_core import analytics

        assert analytics is not None
    except ImportError:
        pytest.skip("Module analytics non disponible")

    # Test de cycle complet
    with tempfile.TemporaryDirectory() as temp_dir:
        project_dir = Path(temp_dir) / "test_project"
        project_dir.mkdir(exist_ok=True)

        # Créer un fichier simple
        (project_dir / "main.py").write_text("print('test')")

        try:
            # Analyser le projet
            analysis = analyze_project(str(project_dir))
            assert isinstance(analysis, dict)

            # Générer un rapport HTML directement
            html = generate_analytics_html(str(project_dir))
            assert isinstance(html, str)
            assert len(html) > 0
        except Exception as e:
            # Test échoue si l'intégration ne fonctionne pas
            assert False, f"Test d'intégration non fonctionnel: {e}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
