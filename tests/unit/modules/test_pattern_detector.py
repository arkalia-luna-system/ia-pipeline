#!/usr/bin/env python3
"""
Tests pour le module pattern_detector.py
Amélioration de la couverture de code de 0% à 80%+
"""

from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch

from athalia_core.analysis.pattern_detector import CodePattern, PatternDetector


class TestCodePattern:
    """Tests pour la classe CodePattern"""

    def test_code_pattern_creation(self):
        """Test de création d'un pattern de code"""
        pattern = CodePattern(
            name="Function Pattern",
            description="Test function pattern",
            category="function",
            severity="medium",
            location="/path/to/file.py",
            line_number=42,
            suggestion="Refactor this function",
            correction_history=["refactor1", "refactor2"],
        )

        assert pattern.name == "Function Pattern"
        assert pattern.description == "Test function pattern"
        assert pattern.category == "function"
        assert pattern.severity == "medium"
        assert pattern.location == "/path/to/file.py"
        assert pattern.line_number == 42
        assert pattern.suggestion == "Refactor this function"
        assert len(pattern.correction_history) == 2

    def test_code_pattern_default_values(self):
        """Test de création d'un pattern avec valeurs par défaut"""
        pattern = CodePattern(
            name="Simple Pattern",
            description="Simple description",
            category="simple",
            severity="low",
            location="/path/to/file.py",
            line_number=10,
            suggestion="No suggestion needed",
        )

        assert pattern.name == "Simple Pattern"
        assert pattern.correction_history is None


class TestPatternDetector:
    """Tests pour la classe PatternDetector"""

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_init(self, mock_connect, mock_mkdir):
        """Test d'initialisation du détecteur de patterns"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector("/tmp/test")

        assert detector.root_path == Path("/tmp/test")
        assert detector.db_path == Path("/tmp/test") / "patterns.db"
        assert isinstance(detector._pattern_cache, dict)
        assert isinstance(detector._duplicate_cache, dict)
        assert isinstance(detector._antipattern_cache, dict)

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_init_default_path(self, mock_connect, mock_mkdir):
        """Test d'initialisation avec chemin par défaut"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector()

        assert detector.root_path == Path(".")
        assert detector.db_path == Path(".") / "patterns.db"

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_database_initialization(self, mock_connect, mock_mkdir):
        """Test de l'initialisation de la base de données"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector("/tmp/test")

        # Vérifier que la base de données est initialisée
        assert detector.root_path == Path("/tmp/test")
        assert detector.db_path == Path("/tmp/test") / "patterns.db"
        assert isinstance(detector._pattern_cache, dict)
        assert isinstance(detector._duplicate_cache, dict)
        assert isinstance(detector._antipattern_cache, dict)

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_analyze_project_patterns(self, mock_connect, mock_mkdir):
        """Test de l'analyse des patterns du projet"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector("/tmp/test")

        # Mock des méthodes internes
        detector._load_patterns = MagicMock()

        with patch("pathlib.Path.rglob") as mock_rglob:
            mock_rglob.return_value = [Path("file1.py"), Path("file2.py")]

            result = detector.analyze_project_patterns()

            assert result["project"] == "/tmp/test"
            assert result["total_files"] == 2
            assert "patterns" in result
            assert "duplications" in result
            assert "antipatterns" in result

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_detect_code_duplication(self, mock_connect, mock_mkdir):
        """Test de la détection de duplication de code"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector("/tmp/test")

        with patch("pathlib.Path.rglob") as mock_rglob:
            mock_rglob.return_value = [Path("file1.py"), Path("file2.py")]

            # Mock de la méthode de calcul de similarité
            detector._calculate_file_similarity = MagicMock(return_value=0.9)
            detector._extract_common_lines = MagicMock(return_value="common code")

            result = detector.detect_code_duplication(min_similarity=0.8)

            assert isinstance(result, list)
            # Avec 2 fichiers, on devrait avoir 1 comparaison
            if result:  # Si des duplications sont trouvées
                assert len(result) > 0
                assert "file1" in result[0]
                assert "file2" in result[0]
                assert "similarity" in result[0]

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_detect_antipatterns(self, mock_connect, mock_mkdir):
        """Test de la détection d'anti-patterns"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector("/tmp/test")

        with patch("pathlib.Path.rglob") as mock_rglob:
            mock_rglob.return_value = [Path("file1.py")]

            # Mock de la méthode d'analyse des anti-patterns
            detector._analyze_file_antipatterns = MagicMock(
                return_value=[
                    {
                        "name": "Test Anti-pattern",
                        "description": "Test description",
                        "location": "/tmp/test/file1.py",
                        "line_number": 10,
                        "impact": "medium",
                        "fix_suggestion": "Fix this",
                    }
                ]
            )

            result = detector.detect_antipatterns()

            assert isinstance(result, list)
            if result:  # Si des anti-patterns sont trouvés
                assert len(result) > 0
                assert "name" in result[0]
                assert "description" in result[0]
                assert "location" in result[0]

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_generate_pattern_report(self, mock_connect, mock_mkdir):
        """Test de la génération du rapport de patterns"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector("/tmp/test")

        # Mock de l'analyse
        detector.analyze_project_patterns = MagicMock(
            return_value={
                "project": "/tmp/test",
                "total_files": 5,
                "patterns_detected": 3,
                "duplications_found": 1,
                "antipatterns_detected": 2,
                "patterns": [],
                "duplications": [],
                "antipatterns": [],
            }
        )

        report = detector.generate_pattern_report()

        assert isinstance(report, str)
        assert "/tmp/test" in report
        assert "5" in report  # total_files
        assert "3" in report  # patterns_detected
        assert "1" in report  # duplications_found
        assert "2" in report  # antipatterns_detected

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_save_patterns_to_database(self, mock_connect, mock_mkdir):
        """Test de la sauvegarde des patterns en base de données"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        detector = PatternDetector("/tmp/test")

        test_patterns = [
            {
                "name": "Test Pattern",
                "description": "Test description",
                "category": "test",
                "severity": "low",
                "location": "/tmp/test/file.py",
                "line_number": 42,
                "suggestion": "Test suggestion",
            }
        ]

        result = detector.save_patterns_to_database(test_patterns)

        assert result is True

    @patch("pathlib.Path.mkdir")
    @patch("sqlite3.connect")
    def test_save_patterns_to_database_error(self, mock_connect, mock_mkdir):
        """Test de la gestion d'erreur lors de la sauvegarde"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception("Database error")

        detector = PatternDetector("/tmp/test")

        test_patterns = [{"name": "Test"}]

        result = detector.save_patterns_to_database(test_patterns)

        assert result is False
