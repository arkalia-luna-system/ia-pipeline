#!/usr/bin/env python3
"""
Tests pour le module dashboard_unified.py
Amélioration de la couverture de code de 9.85% à 80%+
"""

from unittest.mock import MagicMock, mock_open, patch

from athalia_core.advanced_modules.dashboard_unified import DashboardUnifieSimple


class TestDashboardUnifieSimple:
    """Tests pour la classe DashboardUnifieSimple"""

    @patch("sqlite3.connect")
    def test_dashboard_creation(self, mock_connect):
        """Test de création du dashboard unifié"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        assert dashboard.db_path == "test_db.sqlite"
        mock_connect.assert_called()

    @patch("sqlite3.connect")
    def test_enregistrer_metrique(self, mock_connect):
        """Test d'enregistrement d'une métrique"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        # Test d'enregistrement d'une métrique
        dashboard.enregistrer_metrique(
            type_metrique="couverture_tests",
            valeur=85.5,
            projet="test_project",
            details={"tests_passes": 100, "tests_total": 120},
        )

        mock_cursor.execute.assert_called()

    @patch("sqlite3.connect")
    def test_enregistrer_evenement(self, mock_connect):
        """Test d'enregistrement d'un événement"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        # Test d'enregistrement d'un événement
        dashboard.enregistrer_evenement(
            type_evenement="test_execution",
            projet="test_project",
            utilisateur="test_user",
            duree=120,
            statut="succes",
            details={"tests_passes": 95, "tests_echoues": 5},
        )

        mock_cursor.execute.assert_called()

    @patch("sqlite3.connect")
    def test_enregistrer_rapport(self, mock_connect):
        """Test d'enregistrement d'un rapport"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        # Test d'enregistrement d'un rapport
        dashboard.enregistrer_rapport(
            type_rapport="analyse_securite",
            projet="test_project",
            contenu="Rapport de sécurité détaillé",
            score_qualite=85,
            score_securite=90,
        )

        mock_cursor.execute.assert_called()

    @patch("sqlite3.connect")
    def test_obtenir_metriques_temps_reel(self, mock_connect):
        """Test de récupération des métriques en temps réel"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock des données de métriques avec la vraie structure
        mock_cursor.fetchone.side_effect = [
            [5],  # projets_analyses
            [10],  # actions_effectuees
            [85.5],  # score_qualite_moyen
            [90.2],  # score_securite_moyen
        ]

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        metriques = dashboard.obtenir_metriques_temps_reel()

        assert isinstance(metriques, dict)
        assert "projets_analyses" in metriques
        assert "actions_effectuees" in metriques
        assert "score_qualite_moyen" in metriques
        assert "score_securite_moyen" in metriques

    @patch("sqlite3.connect")
    def test_generer_rapport_consolide(self, mock_connect):
        """Test de génération du rapport consolidé"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock des données pour le rapport avec la vraie structure
        mock_cursor.fetchone.side_effect = [
            [5],  # projets_analyses
            [10],  # actions_effectuees
            [85.5],  # score_qualite_moyen
            [90.2],  # score_securite_moyen
        ]
        mock_cursor.fetchall.side_effect = [
            [
                (
                    "couverture_tests",
                    85.5,
                    "test_project",
                    "2023-01-01",
                    '{"tests": 100}',
                )
            ],  # métriques
            [
                (
                    "test_execution",
                    "test_project",
                    "test_user",
                    "2023-01-01",
                    120,
                    "succes",
                    "details",
                )
            ],  # événements
            [
                ("analyse_securite", "test_project", "Rapport", "2023-01-01", 85, 90)
            ],  # rapports
        ]

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        rapport = dashboard.generer_rapport_consolide()

        assert isinstance(rapport, str)
        assert "RAPPORT CONSOLIDÉ" in rapport
        assert "MÉTRIQUES" in rapport
        assert "ÉVÉNEMENTS" in rapport

    @patch("sqlite3.connect")
    @patch("builtins.open", new_callable=mock_open)
    def test_generer_dashboard_html(self, mock_file, mock_connect):
        """Test de génération du dashboard HTML"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock des données pour le dashboard avec la vraie structure
        mock_cursor.fetchone.side_effect = [
            [5],  # projets_analyses
            [10],  # actions_effectuees
            [85.5],  # score_qualite_moyen
            [90.2],  # score_securite_moyen
        ]
        mock_cursor.fetchall.side_effect = [
            [
                (
                    "couverture_tests",
                    85.5,
                    "test_project",
                    "2023-01-01",
                    '{"tests": 100}',
                )
            ],  # métriques
            [
                (
                    "test_execution",
                    "test_project",
                    "test_user",
                    "2023-01-01",
                    120,
                    "succes",
                    "details",
                )
            ],  # événements
            [
                ("analyse_securite", "test_project", "Rapport", "2023-01-01", 85, 90)
            ],  # rapports
        ]

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        result = dashboard.generer_dashboard_html("test_dashboard.html")

        # La fonction retourne le nom du fichier, pas True
        assert result == "test_dashboard.html"
        mock_file.assert_called()

    @patch("sqlite3.connect")
    @patch("webbrowser.open")
    def test_ouvrir_dashboard(self, mock_browser, mock_connect):
        """Test d'ouverture du dashboard"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        with patch.object(dashboard, "generer_dashboard_html") as mock_generate:
            mock_generate.return_value = "dashboard.html"

            dashboard.ouvrir_dashboard()

            mock_generate.assert_called()
            mock_browser.assert_called()


class TestIntegration:
    """Tests d'intégration pour le dashboard unifié"""

    @patch("sqlite3.connect")
    @patch("builtins.open", new_callable=mock_open)
    def test_full_dashboard_workflow(self, mock_file, mock_connect):
        """Test du workflow complet du dashboard"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock des données variées
        mock_cursor.fetchall.side_effect = [
            [
                (
                    "couverture_tests",
                    85.5,
                    "test_project",
                    "2023-01-01",
                    '{"tests": 100}',
                )
            ],
            [
                (
                    "test_execution",
                    "test_project",
                    "test_user",
                    "2023-01-01",
                    120,
                    "succes",
                    "details",
                )
            ],
            [("analyse_securite", "test_project", "Rapport", "2023-01-01", 85, 90)],
        ]

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        # Test du workflow complet
        dashboard.enregistrer_metrique("test_metric", 95.0, "test_project")
        dashboard.enregistrer_evenement("test_event", "test_project", "test_user")
        dashboard.enregistrer_rapport("test_report", "test_project", "Test content")

        metriques = dashboard.obtenir_metriques_temps_reel()
        rapport = dashboard.generer_rapport_consolide()

        assert isinstance(metriques, dict)
        assert isinstance(rapport, str)
        assert len(rapport) > 0

    @patch("sqlite3.connect")
    def test_dashboard_data_consistency(self, mock_connect):
        """Test de cohérence des données du dashboard"""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        dashboard = DashboardUnifieSimple("test_db.sqlite")

        # Test que les données sont cohérentes
        metriques = dashboard.obtenir_metriques_temps_reel()

        assert "projets_analyses" in metriques
        assert "actions_effectuees" in metriques
        assert "score_qualite_moyen" in metriques
        assert "score_securite_moyen" in metriques
        assert "derniere_mise_a_jour" in metriques
