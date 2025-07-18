import unittest
import os
from athalia_core.advanced_analytics import AdvancedAnalytics

class TestAdvancedAnalytics(unittest.TestCase):
    def setUp(self):
        # Utilise le dossier courant comme projet de test
        self.project_path = os.getcwd()
        self.analytics = AdvancedAnalytics(self.project_path)

    def test_constructor(self):
        self.assertEqual(str(self.analytics.project_path), self.project_path)
        self.assertIsInstance(self.analytics.metrics, dict)

    def test_run(self):
        result = self.analytics.run()
        self.assertIn("metrics", result)
        self.assertIn("dashboard", result)
        self.assertIn("summary", result)

    def test_analyze_coverage(self):
        self.analytics._analyze_coverage()
        self.assertIn("coverage", self.analytics.metrics)
        self.assertIsInstance(self.analytics.metrics["coverage"], dict)

    def test_analyze_performance(self):
        self.analytics._analyze_performance()
        self.assertIn("performance", self.analytics.metrics)
        self.assertIsInstance(self.analytics.metrics["performance"], dict)

    def test_generate_dashboard(self):
        dashboard_path = self.analytics._generate_dashboard()
        self.assertTrue(os.path.exists(dashboard_path))
        self.assertTrue(dashboard_path.endswith("analytics_dashboard.html"))

    def test_generate_summary(self):
        summary = self.analytics._generate_summary()
        self.assertIsInstance(summary, str)
        self.assertIn("ANALYTICS AVANCÉE", summary)

    def test_print_report(self):
        # Doit s'exécuter sans lever d'exception
        try:
            self.analytics.print_report()
        except Exception as e:
            self.fail(f"print_report a levé une exception: {e}")

if __name__ == "__main__":
    unittest.main() 