import os
import unittest
from pathlib import Path

from athalia_core.analytics.advanced_analytics import AdvancedAnalytics


class TestAdvancedAnalytics(unittest.TestCase):
    def setUp(self) -> None:
        # Utilise le dossier racine du projet comme projet de test
        self.project_path = Path(__file__).parent.parent.parent.parent
        self.analytics = AdvancedAnalytics(str(self.project_path))

        # Crée le dossier dashboard/html s'il n'existe pas
        dashboard_html_dir = self.project_path / "dashboard" / "html"
        dashboard_html_dir.mkdir(parents=True, exist_ok=True)

    def test_constructor(self) -> None:
        self.assertEqual(str(self.analytics.project_path), str(self.project_path))
        self.assertIsInstance(self.analytics.metrics, dict)

    def test_run(self) -> None:
        result = self.analytics.run()
        self.assertIn("metrics", result)
        self.assertIn("dashboard", result)
        self.assertIn("summary", result)

    def test_analyze_coverage(self) -> None:
        self.analytics._analyze_coverage()
        self.assertIn("coverage", self.analytics.metrics)
        self.assertIsInstance(self.analytics.metrics["coverage"], dict)

    def test_analyze_performance(self) -> None:
        self.analytics._analyze_performance()
        self.assertIn("performance", self.analytics.metrics)
        self.assertIsInstance(self.analytics.metrics["performance"], dict)

    def test_generate_dashboard(self) -> None:
        dashboard_path = self.analytics._generate_dashboard()
        self.assertTrue(os.path.exists(dashboard_path))
        self.assertTrue(dashboard_path.endswith("analytics_dashboard.html"))

    def test_generate_summary(self) -> None:
        summary = self.analytics._generate_summary()
        self.assertIsInstance(summary, str)
        self.assertIn("ANALYTICS AVANCÉE", summary)

    def test_print_report(self) -> None:
        # Doit s'exécuter sans lever d'exception
        try:
            self.analytics.print_report()
        except Exception as e:
            self.fail(f"print_report a levé une exception: {e}")


if __name__ == "__main__":
    unittest.main()
