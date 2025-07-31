#!/usr/bin/env python3
"""
Tests pour le module architecture_analyzer.py
Amélioration de la couverture de code de 0% à 80%+
"""

from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

from athalia_core.architecture_analyzer import (
    ArchitectureAnalyzer,
    ArchitectureMapping,
    ModuleAnalysis,
    PerformanceIssue,
)


class TestModuleAnalysis:
    """Tests pour la classe ModuleAnalysis"""

    def test_module_analysis_creation(self):
        """Test de création d'une analyse de module"""
        module = ModuleAnalysis(
            name="test_module",
            path="/path/to/test_module.py",
            type="core",
            size=1000,
            functions=["func1", "func2"],
            classes=["Class1", "Class2"],
            imports=["import1", "import2"],
            dependencies=["dep1", "dep2"],
            complexity=2.5,
            issues=["issue1"],
            performance_score=85.0,
            last_modified=datetime.now(),
        )

        assert module.name == "test_module"
        assert module.path == "/path/to/test_module.py"
        assert module.type == "core"
        assert module.size == 1000
        assert len(module.functions) == 2
        assert len(module.classes) == 2
        assert len(module.imports) == 2
        assert len(module.dependencies) == 2
        assert module.complexity == 2.5
        assert len(module.issues) == 1
        assert module.performance_score == 85.0


class TestPerformanceIssue:
    """Tests pour la classe PerformanceIssue"""

    def test_performance_issue_creation(self):
        """Test de création d'un problème de performance"""
        issue = PerformanceIssue(
            type="memory_leak",
            location="module.py:42",
            description="Memory leak detected",
            impact="high",
            suggestion="Use context managers",
        )

        assert issue.type == "memory_leak"
        assert issue.location == "module.py:42"
        assert issue.description == "Memory leak detected"
        assert issue.impact == "high"
        assert issue.suggestion == "Use context managers"


class TestArchitectureMapping:
    """Tests pour la classe ArchitectureMapping"""

    def test_architecture_mapping_creation(self):
        """Test de création d'un mapping d'architecture"""
        mapping = ArchitectureMapping(
            modules={},
            dependencies={},
            duplicates=[],
            performance_issues=[],
            recommendations=[],
        )

        assert isinstance(mapping.modules, dict)
        assert isinstance(mapping.dependencies, dict)
        assert isinstance(mapping.duplicates, list)
        assert isinstance(mapping.performance_issues, list)
        assert isinstance(mapping.recommendations, list)


class TestArchitectureAnalyzer:
    """Tests pour la classe ArchitectureAnalyzer"""

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_init(self, mock_connect, mock_mkdir):
        """Test d'initialisation de l'analyseur d'architecture"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            assert analyzer.root_path == Path("/tmp/test")
            assert analyzer.db_path == Path("/tmp/test/data/architecture_analysis.db")
            assert analyzer.config_path == Path("/tmp/test/config/athalia_config.yaml")

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_init_default_path(self, mock_connect, mock_mkdir):
        """Test d'initialisation avec chemin par défaut"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            with patch("pathlib.Path.cwd", return_value=Path("/current/dir")):
                analyzer = ArchitectureAnalyzer()

                assert analyzer.root_path == Path("/current/dir")

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_load_config(self, mock_connect, mock_mkdir):
        """Test de chargement de configuration"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        config_data = """
        architecture:
          analysis_enabled: true
          performance_threshold: 80
        """

        with patch("builtins.open", mock_open(read_data=config_data)):
            analyzer = ArchitectureAnalyzer("/tmp/test")
            config = analyzer._load_config()

            assert config is not None

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_load_config_file_not_found(self, mock_connect, mock_mkdir):
        """Test de chargement de configuration avec fichier inexistant"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", side_effect=FileNotFoundError):
            analyzer = ArchitectureAnalyzer("/tmp/test")
            config = analyzer._load_config()

            assert config == {}

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_analyze_entire_architecture(self, mock_connect, mock_mkdir):
        """Test d'analyse complète de l'architecture"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            with patch.object(analyzer, "_analyze_all_modules") as mock_analyze_modules:
                with patch.object(
                    analyzer, "_detect_duplicates"
                ) as mock_detect_duplicates:
                    with patch.object(
                        analyzer, "_analyze_performance"
                    ) as mock_analyze_performance:
                        with patch.object(
                            analyzer, "_build_dependency_graph"
                        ) as mock_build_graph:
                            with patch.object(
                                analyzer, "_generate_recommendations"
                            ) as mock_generate_recs:
                                with patch.object(
                                    analyzer, "_save_architecture_analysis"
                                ) as mock_save:
                                    mock_analyze_modules.return_value = {}
                                    mock_detect_duplicates.return_value = []
                                    mock_analyze_performance.return_value = []
                                    mock_build_graph.return_value = {}
                                    mock_generate_recs.return_value = []

                                    result = analyzer.analyze_entire_architecture()

                                    assert isinstance(result, ArchitectureMapping)
                                    mock_analyze_modules.assert_called_once()
                                    mock_detect_duplicates.assert_called_once()
                                    mock_analyze_performance.assert_called_once()
                                    mock_build_graph.assert_called_once()
                                    mock_generate_recs.assert_called_once()
                                    mock_save.assert_called_once()

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_analyze_single_module(self, mock_connect, mock_mkdir):
        """Test d'analyse d'un module unique"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            with patch.object(
                analyzer.ast_analyzer, "analyze_file"
            ) as mock_analyze_file:
                mock_file_analysis = MagicMock()
                mock_file_analysis.functions = ["func1", "func2"]
                mock_file_analysis.classes = ["Class1"]
                mock_file_analysis.imports = ["import1"]
                mock_file_analysis.complexity = 2.5
                mock_file_analysis.issues = []
                mock_analyze_file.return_value = mock_file_analysis

                with patch("pathlib.Path.stat") as mock_stat:
                    mock_stat.return_value.st_size = 1000
                    mock_stat.return_value.st_mtime = 1234567890

                    analyzer._analyze_single_module(Path("/tmp/test.py"), "core")

                    # Test que la fonction s'exécute sans erreur
                    assert True

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_extract_dependencies(self, mock_connect, mock_mkdir):
        """Test d'extraction des dépendances"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            imports = ["numpy", "pandas", "matplotlib.pyplot"]
            dependencies = analyzer._extract_dependencies(imports, "core")

            # Test que la fonction s'exécute sans erreur
            assert isinstance(dependencies, list)

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_detect_module_issues(self, mock_connect, mock_mkdir):
        """Test de détection des problèmes de module"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            mock_file_analysis = MagicMock()
            # Configuration correcte des attributs
            mock_file_analysis.complexity_score = 15.0
            mock_file_analysis.total_lines = 600
            mock_file_analysis.functions = ["func1"] * 50
            mock_file_analysis.classes = ["Class1"] * 20

            issues = analyzer._detect_module_issues(mock_file_analysis)

            assert isinstance(issues, list)

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_calculate_performance_score(self, mock_connect, mock_mkdir):
        """Test de calcul du score de performance"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            mock_file_analysis = MagicMock()
            # Configuration correcte des attributs
            mock_file_analysis.complexity_score = 2.0
            mock_file_analysis.total_lines = 150
            mock_file_analysis.functions = ["func1", "func2"]
            mock_file_analysis.classes = ["Class1"]
            mock_file_analysis.issues = []

            score = analyzer._calculate_performance_score(mock_file_analysis)

            assert 0 <= score <= 100
            assert isinstance(score, float)

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_detect_duplicates(self, mock_connect, mock_mkdir):
        """Test de détection des duplications"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            modules = {
                "module1": ModuleAnalysis(
                    name="module1",
                    path="/path1",
                    type="core",
                    size=100,
                    functions=["func1", "func2"],
                    classes=["Class1"],
                    imports=["import1"],
                    dependencies=["dep1"],
                    complexity=2.0,
                    issues=[],
                    performance_score=85.0,
                    last_modified=datetime.now(),
                ),
                "module2": ModuleAnalysis(
                    name="module2",
                    path="/path2",
                    type="core",
                    size=100,
                    functions=["func1", "func2"],  # Duplication
                    classes=["Class1"],  # Duplication
                    imports=["import1"],
                    dependencies=["dep1"],
                    complexity=2.0,
                    issues=[],
                    performance_score=85.0,
                    last_modified=datetime.now(),
                ),
            }

            duplicates = analyzer._detect_duplicates(modules)

            assert isinstance(duplicates, list)

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_analyze_performance(self, mock_connect, mock_mkdir):
        """Test d'analyse des performances"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            modules = {
                "module1": ModuleAnalysis(
                    name="module1",
                    path="/path1",
                    type="core",
                    size=1000,
                    functions=["func1"] * 50,  # Trop de fonctions
                    classes=["Class1"] * 20,  # Trop de classes
                    imports=["import1"],
                    dependencies=["dep1"],
                    complexity=15.0,  # Complexité élevée
                    issues=[],
                    performance_score=30.0,  # Score faible
                    last_modified=datetime.now(),
                ),
            }

            performance_issues = analyzer._analyze_performance(modules)

            assert isinstance(performance_issues, list)
            assert all(
                isinstance(issue, PerformanceIssue) for issue in performance_issues
            )

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_build_dependency_graph(self, mock_connect, mock_mkdir):
        """Test de construction du graphe de dépendances"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            modules = {
                "module1": ModuleAnalysis(
                    name="module1",
                    path="/path1",
                    type="core",
                    size=100,
                    functions=["func1"],
                    classes=["Class1"],
                    imports=["import1"],
                    dependencies=["module2"],
                    complexity=2.0,
                    issues=[],
                    performance_score=85.0,
                    last_modified=datetime.now(),
                ),
                "module2": ModuleAnalysis(
                    name="module2",
                    path="/path2",
                    type="core",
                    size=100,
                    functions=["func2"],
                    classes=["Class2"],
                    imports=["import2"],
                    dependencies=[],
                    complexity=2.0,
                    issues=[],
                    performance_score=85.0,
                    last_modified=datetime.now(),
                ),
            }

            dependency_graph = analyzer._build_dependency_graph(modules)

            assert isinstance(dependency_graph, dict)
            assert "module1" in dependency_graph
            assert "module2" in dependency_graph

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_generate_recommendations(self, mock_connect, mock_mkdir):
        """Test de génération de recommandations"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            modules = {
                "module1": ModuleAnalysis(
                    name="module1",
                    path="/path1",
                    type="core",
                    size=100,
                    functions=["func1"],
                    classes=["Class1"],
                    imports=["import1"],
                    dependencies=["dep1"],
                    complexity=2.0,
                    issues=[],
                    performance_score=85.0,
                    last_modified=datetime.now(),
                ),
            }

            duplicates = []
            performance_issues = [
                PerformanceIssue(
                    type="complexity",
                    location="module1.py:10",
                    description="High complexity",
                    impact="medium",
                    suggestion="Refactor code",
                )
            ]

            recommendations = analyzer._generate_recommendations(
                modules, duplicates, performance_issues
            )

            assert isinstance(recommendations, list)
            assert len(recommendations) > 0

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_get_optimization_plan(self, mock_connect, mock_mkdir):
        """Test de génération du plan d'optimisation"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            with patch.object(analyzer, "analyze_entire_architecture") as mock_analyze:
                mock_architecture = ArchitectureMapping(
                    modules={},
                    dependencies={},
                    duplicates=[],
                    performance_issues=[],
                    recommendations=["Refactor module1"],
                )
                mock_analyze.return_value = mock_architecture

                # Mock les valeurs de retour de la base de données
                mock_cursor.fetchone.return_value = [
                    10,
                    5.0,
                    85.0,
                ]  # total_modules, avg_complexity, avg_performance
                mock_cursor.fetchall.return_value = [["module1", "high"]]

                plan = analyzer.get_optimization_plan()

                assert isinstance(plan, dict)
                assert "total_modules" in plan
                assert "average_complexity" in plan
                assert "average_performance" in plan
                assert "problematic_modules" in plan
                assert "optimization_score" in plan

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_generate_intelligent_coordination(self, mock_connect, mock_mkdir):
        """Test de génération de coordination intelligente"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        with patch("builtins.open", mock_open(read_data="config: test")):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            with patch.object(analyzer, "analyze_entire_architecture") as mock_analyze:
                mock_architecture = ArchitectureMapping(
                    modules={},
                    dependencies={},
                    duplicates=[],
                    performance_issues=[],
                    recommendations=[],
                )
                mock_analyze.return_value = mock_architecture

                # Mock les valeurs de retour de la base de données
                mock_cursor.fetchone.return_value = [
                    10,
                    5.0,
                    85.0,
                ]  # total_modules, avg_complexity, avg_performance
                mock_cursor.fetchall.return_value = [["module1", "high"]]

                coordination = analyzer.generate_intelligent_coordination()

                assert isinstance(coordination, dict)
                assert "priority_tasks" in coordination
                assert "parallel_tasks" in coordination
                assert "dependencies" in coordination
                assert "estimated_time" in coordination


class TestIntegration:
    """Tests d'intégration"""

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_full_architecture_analysis_workflow(self, mock_connect, mock_mkdir):
        """Test du workflow complet d'analyse d'architecture"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        config_data = """
        architecture:
          analysis_enabled: true
          performance_threshold: 80
        """

        with patch("builtins.open", mock_open(read_data=config_data)):
            analyzer = ArchitectureAnalyzer("/tmp/test")

            # Test du workflow complet
            with patch.object(analyzer, "_analyze_all_modules") as mock_analyze_modules:
                with patch.object(
                    analyzer, "_detect_duplicates"
                ) as mock_detect_duplicates:
                    with patch.object(
                        analyzer, "_analyze_performance"
                    ) as mock_analyze_performance:
                        with patch.object(
                            analyzer, "_build_dependency_graph"
                        ) as mock_build_graph:
                            with patch.object(
                                analyzer, "_generate_recommendations"
                            ) as mock_generate_recs:
                                mock_analyze_modules.return_value = {}
                                mock_detect_duplicates.return_value = []
                                mock_analyze_performance.return_value = []
                                mock_build_graph.return_value = {}
                                mock_generate_recs.return_value = []

                                # Test analyse complète
                                architecture = analyzer.analyze_entire_architecture()
                                assert isinstance(architecture, ArchitectureMapping)

                                # Test plan d'optimisation
                                mock_cursor.fetchone.return_value = [10, 5.0, 85.0]
                                mock_cursor.fetchall.return_value = [
                                    ["module1", "high"]
                                ]
                                plan = analyzer.get_optimization_plan()
                                assert isinstance(plan, dict)

                                # Test coordination intelligente
                                coordination = (
                                    analyzer.generate_intelligent_coordination()
                                )
                                assert isinstance(coordination, dict)
                                assert "priority_tasks" in coordination
                                assert "parallel_tasks" in coordination
                                assert "dependencies" in coordination
                                assert "estimated_time" in coordination

                                # Vérifier que toutes les méthodes ont été appelées
                                mock_analyze_modules.assert_called()
                                mock_detect_duplicates.assert_called()
                                mock_analyze_performance.assert_called()
                                mock_build_graph.assert_called()
                                mock_generate_recs.assert_called()
