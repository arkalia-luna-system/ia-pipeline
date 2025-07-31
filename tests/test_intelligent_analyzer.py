#!/usr/bin/env python3
"""
Tests pour le module intelligent_analyzer.py
Amélioration de la couverture de code de 0% à 80%+
"""

from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

from athalia_core.intelligent_analyzer import ComprehensiveAnalysis, IntelligentAnalyzer


class TestComprehensiveAnalysis:
    """Tests pour la classe ComprehensiveAnalysis"""

    def test_comprehensive_analysis_creation(self):
        """Test de création d'une analyse complète"""
        analysis = ComprehensiveAnalysis(
            project_name="test_project",
            analysis_date=datetime.now(),
            ast_analysis={"files_analyzed": 10},
            pattern_analysis={"patterns_found": 5},
            architecture_analysis={"modules": 3},
            performance_analysis={"execution_time": 1.2},
            overall_score=85.5,
            recommendations=["Optimiser les imports"],
            optimization_plan={"priority": "high"},
        )

        assert analysis.project_name == "test_project"
        assert analysis.overall_score == 85.5
        assert len(analysis.recommendations) == 1
        assert "Optimiser les imports" in analysis.recommendations

    def test_comprehensive_analysis_to_dict(self):
        """Test de conversion en dictionnaire"""
        analysis = ComprehensiveAnalysis(
            project_name="test_project",
            analysis_date=datetime.now(),
            ast_analysis={"files_analyzed": 10, "summary": {"average_complexity": 5.2}},
            pattern_analysis={"patterns": [], "summary": {"total_duplicates": 1}},
            architecture_analysis={"modules": 3},
            performance_analysis={"execution_time": 1.2},
            overall_score=85.5,
            recommendations=["Test recommendation"],
            optimization_plan={"priority": "high"},
        )

        analysis_dict = asdict(analysis)

        assert isinstance(analysis_dict, dict)
        assert analysis_dict["project_name"] == "test_project"
        assert analysis_dict["overall_score"] == 85.5


class TestIntelligentAnalyzer:
    """Tests pour la classe IntelligentAnalyzer"""

    @patch("pathlib.Path.cwd")
    def test_intelligent_analyzer_creation_default(self, mock_cwd):
        """Test de création de l'analyseur intelligent avec chemin par défaut"""
        mock_cwd.return_value = Path("/tmp/test_project")

        analyzer = IntelligentAnalyzer()

        assert analyzer.root_path == Path("/tmp/test_project")
        assert analyzer.ast_analyzer is not None
        assert analyzer.pattern_detector is not None
        assert analyzer.architecture_analyzer is not None
        assert analyzer.performance_analyzer is not None

    def test_intelligent_analyzer_creation_with_path(self):
        """Test de création de l'analyseur intelligent avec chemin spécifique"""
        test_path = "/tmp/custom_project"

        analyzer = IntelligentAnalyzer(test_path)

        assert analyzer.root_path == Path(test_path)
        assert analyzer.ast_analyzer is not None
        assert analyzer.pattern_detector is not None
        assert analyzer.architecture_analyzer is not None
        assert analyzer.performance_analyzer is not None

    @patch.object(IntelligentAnalyzer, "_perform_ast_analysis")
    @patch.object(IntelligentAnalyzer, "_calculate_overall_score")
    @patch.object(IntelligentAnalyzer, "_generate_comprehensive_recommendations")
    @patch.object(IntelligentAnalyzer, "_create_optimization_plan")
    def test_analyze_project_comprehensive(
        self, mock_optimization, mock_recommendations, mock_score, mock_ast
    ):
        """Test d'analyse complète de projet"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        # Mock des résultats d'analyse
        mock_ast.return_value = {
            "files_analyzed": 10,
            "summary": {"average_complexity": 5.2, "total_functions": 15},
        }
        mock_score.return_value = 85.5
        mock_recommendations.return_value = [
            "Optimiser les imports",
            "Réduire la complexité",
        ]
        mock_optimization.return_value = {"priority": "high", "estimated_time": "2h"}

        # Mock des analyseurs spécialisés
        with patch.object(
            analyzer.pattern_detector, "analyze_project_patterns"
        ) as mock_pattern:
            with patch.object(
                analyzer.architecture_analyzer, "analyze_entire_architecture"
            ) as mock_arch:
                with patch.object(
                    analyzer.performance_analyzer, "analyze_project_performance"
                ) as mock_perf:
                    mock_pattern.return_value = {
                        "patterns": [],
                        "duplicates": [{"file1": "test1.py", "file2": "test2.py"}],
                        "antipatterns": [],
                        "recommendations": [],
                        "summary": {"total_duplicates": 1, "total_antipatterns": 0},
                    }
                    mock_arch.return_value = {"modules": 3, "dependencies": 10}
                    mock_perf.return_value = {
                        "execution_time": 1.2,
                        "memory_usage": 50.5,
                    }

                    result = analyzer.analyze_project_comprehensive("/tmp/test_project")

                    assert isinstance(result, ComprehensiveAnalysis)
                    assert result.project_name == "test_project"
                    assert result.overall_score == 85.5
                    assert len(result.recommendations) == 2
                    assert "Optimiser les imports" in result.recommendations

    @patch("pathlib.Path.rglob")
    def test_perform_ast_analysis(self, mock_rglob):
        """Test d'analyse AST"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        # Mock des fichiers Python
        mock_files = [
            Path("/tmp/test_project/file1.py"),
            Path("/tmp/test_project/file2.py"),
        ]
        mock_rglob.return_value = mock_files

        # Mock de l'analyseur AST
        with patch.object(analyzer.ast_analyzer, "analyze_file") as mock_analyze:
            mock_analyze.side_effect = [
                {"complexity": 3.5, "functions": 5},
                {"complexity": 4.2, "functions": 8},
            ]

            result = analyzer._perform_ast_analysis(Path("/tmp/test_project"))

            assert isinstance(result, dict)
            assert "files_analyzed" in result
            assert "summary" in result
            assert "total_functions" in result

    def test_calculate_overall_score(self):
        """Test de calcul du score global"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        # Données de test
        ast_analysis = {"files_analyzed": 10, "summary": {"average_complexity": 5.2}}
        pattern_analysis = {
            "patterns": [],
            "duplicates": [{"file1": "test1.py"}],
            "antipatterns": [],
            "summary": {"total_duplicates": 1, "total_antipatterns": 0},
        }
        architecture_analysis = {
            "modules": 3,
            "dependencies": 10,
            "performance_issues": [],
        }
        performance_analysis = {
            "execution_time": 1.2,
            "memory_usage": 50.5,
            "overall_score": 85.0,
            "issues": [],
        }

        score = analyzer._calculate_overall_score(
            ast_analysis, pattern_analysis, architecture_analysis, performance_analysis
        )

        assert isinstance(score, float)
        assert 0 <= score <= 100

    def test_generate_comprehensive_recommendations(self):
        """Test de génération de recommandations complètes"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        # Données de test
        pattern_analysis = {
            "patterns": [],
            "duplicates": [{"file1": "test1.py"}],
            "antipatterns": [],
            "summary": {"total_duplicates": 1, "total_antipatterns": 0},
        }
        architecture_analysis = {
            "modules": 3,
            "dependencies": 10,
            "performance_issues": [],
        }
        performance_analysis = {
            "execution_time": 1.2,
            "memory_usage": 50.5,
            "overall_score": 85.0,
            "issues": [],
        }

        recommendations = analyzer._generate_comprehensive_recommendations(
            pattern_analysis, architecture_analysis, performance_analysis
        )

        assert isinstance(recommendations, list)
        assert all(isinstance(rec, str) for rec in recommendations)

    def test_create_optimization_plan(self):
        """Test de création du plan d'optimisation"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        # Données de test
        pattern_analysis = {
            "patterns": [],
            "duplicates": [{"file1": "test1.py"}],
            "antipatterns": [],
            "summary": {"total_duplicates": 1, "total_antipatterns": 0},
        }
        architecture_analysis = {
            "modules": 3,
            "dependencies": 10,
            "performance_issues": [],
        }
        performance_analysis = {
            "execution_time": 1.2,
            "memory_usage": 50.5,
            "overall_score": 85.0,
            "issues": [],
        }

        plan = analyzer._create_optimization_plan(
            pattern_analysis, architecture_analysis, performance_analysis
        )

        assert isinstance(plan, dict)
        assert "priority_tasks" in plan
        assert "estimated_effort" in plan
        assert "expected_improvement" in plan

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save_comprehensive_analysis(self, mock_json_dump, mock_file):
        """Test de sauvegarde de l'analyse complète"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        analysis = ComprehensiveAnalysis(
            project_name="test_project",
            analysis_date=datetime.now(),
            ast_analysis={"files_analyzed": 10, "summary": {"average_complexity": 5.2}},
            pattern_analysis={
                "patterns": [],
                "duplicates": [],
                "antipatterns": [],
                "recommendations": [],
                "summary": {"total_duplicates": 1, "total_antipatterns": 0},
            },
            architecture_analysis={"modules": 3},
            performance_analysis={"execution_time": 1.2},
            overall_score=85.5,
            recommendations=["Test recommendation"],
            optimization_plan={"priority": "high"},
        )

        analyzer._save_comprehensive_analysis(analysis)

        mock_file.assert_called()
        mock_json_dump.assert_called()

    def test_get_learning_insights(self):
        """Test de récupération des insights d'apprentissage"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        insights = analyzer.get_learning_insights()

        assert isinstance(insights, dict)
        assert "ast_insights" in insights
        assert "pattern_insights" in insights
        assert "architecture_insights" in insights
        assert "performance_insights" in insights

    def test_generate_intelligent_coordination(self):
        """Test de génération de coordination intelligente"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        coordination = analyzer.generate_intelligent_coordination()

        assert isinstance(coordination, dict)
        assert "timestamp" in coordination
        assert "modules_available" in coordination
        assert "recommendations" in coordination

    @patch("athalia_core.intelligent_analyzer.UNIFIED_ORCHESTRATOR_AVAILABLE", True)
    @patch("athalia_core.intelligent_analyzer.UnifiedOrchestrator")
    def test_orchestrate_with_unified_available(self, mock_unified_class):
        """Test d'orchestration avec l'orchestrateur unifié disponible"""
        mock_unified = MagicMock()
        mock_unified_class.return_value = mock_unified
        mock_unified.orchestrate_project_complete.return_value = {
            "status": "success",
            "score": 90,
        }

        analyzer = IntelligentAnalyzer("/tmp/test_project")

        result = analyzer.orchestrate_with_unified("/tmp/test_project")

        assert isinstance(result, dict)
        assert result["status"] == "success"
        assert result["score"] == 90

    @patch("athalia_core.intelligent_analyzer.UNIFIED_ORCHESTRATOR_AVAILABLE", False)
    def test_orchestrate_with_unified_unavailable(self):
        """Test d'orchestration avec l'orchestrateur unifié non disponible"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        result = analyzer.orchestrate_with_unified("/tmp/test_project")

        assert isinstance(result, ComprehensiveAnalysis)
        assert result.project_name == "test_project"


class TestIntegration:
    """Tests d'intégration pour l'analyseur intelligent"""

    @patch.object(IntelligentAnalyzer, "_perform_ast_analysis")
    @patch.object(IntelligentAnalyzer, "_calculate_overall_score")
    @patch.object(IntelligentAnalyzer, "_generate_comprehensive_recommendations")
    @patch.object(IntelligentAnalyzer, "_create_optimization_plan")
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_full_analysis_workflow(
        self,
        mock_json_dump,
        mock_file,
        mock_optimization,
        mock_recommendations,
        mock_score,
        mock_ast,
    ):
        """Test du workflow complet d'analyse"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        # Mock des résultats d'analyse
        mock_ast.return_value = {
            "files_analyzed": 10,
            "summary": {"average_complexity": 5.2, "total_functions": 15},
        }
        mock_score.return_value = 85.5
        mock_recommendations.return_value = ["Optimiser les imports"]
        mock_optimization.return_value = {"priority": "high", "estimated_time": "2h"}

        # Mock des analyseurs spécialisés
        with patch.object(
            analyzer.pattern_detector, "analyze_project_patterns"
        ) as mock_pattern:
            with patch.object(
                analyzer.architecture_analyzer, "analyze_entire_architecture"
            ) as mock_arch:
                with patch.object(
                    analyzer.performance_analyzer, "analyze_project_performance"
                ) as mock_perf:
                    mock_pattern.return_value = {
                        "patterns": [],
                        "duplicates": [{"file1": "test1.py", "file2": "test2.py"}],
                        "antipatterns": [],
                        "recommendations": [],
                        "summary": {"total_duplicates": 1, "total_antipatterns": 0},
                    }
                    mock_arch.return_value = {"modules": 3, "dependencies": 10}
                    mock_perf.return_value = {
                        "execution_time": 1.2,
                        "memory_usage": 50.5,
                    }

                    # Test d'analyse complète
                    result = analyzer.analyze_project_comprehensive("/tmp/test_project")

                    assert isinstance(result, ComprehensiveAnalysis)
                    assert result.project_name == "test_project"
                    assert result.overall_score == 85.5

                    # Test de sauvegarde
                    analyzer._save_comprehensive_analysis(result)
                    mock_file.assert_called()
                    mock_json_dump.assert_called()

    def test_analyzer_components_integration(self):
        """Test d'intégration des composants de l'analyseur"""
        analyzer = IntelligentAnalyzer("/tmp/test_project")

        # Vérifier que tous les composants sont initialisés
        assert analyzer.ast_analyzer is not None
        assert analyzer.pattern_detector is not None
        assert analyzer.architecture_analyzer is not None
        assert analyzer.performance_analyzer is not None

        # Vérifier que les méthodes sont disponibles
        assert hasattr(analyzer, "analyze_project_comprehensive")
        assert hasattr(analyzer, "get_learning_insights")
        assert hasattr(analyzer, "generate_intelligent_coordination")
        assert hasattr(analyzer, "orchestrate_with_unified")

    def test_comprehensive_analysis_serialization(self):
        """Test de sérialisation de l'analyse complète"""
        analysis = ComprehensiveAnalysis(
            project_name="test_project",
            analysis_date=datetime.now(),
            ast_analysis={"files_analyzed": 10},
            pattern_analysis={"patterns_found": 5},
            architecture_analysis={"modules": 3},
            performance_analysis={"execution_time": 1.2},
            overall_score=85.5,
            recommendations=["Test recommendation"],
            optimization_plan={"priority": "high"},
        )

        # Test de conversion en dictionnaire
        analysis_dict = asdict(analysis)

        assert isinstance(analysis_dict, dict)
        assert analysis_dict["project_name"] == "test_project"
        assert analysis_dict["overall_score"] == 85.5
        assert "recommendations" in analysis_dict
        assert "optimization_plan" in analysis_dict
