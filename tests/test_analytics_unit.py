import unittest

from athalia_core import analytics


class TestAnalytics(unittest.TestCase):
    def setUp(self):
        # Exemple de données de projet
        self.projects_info = [{"name": "ProjetA"}, {"name": "ProjetB"}]

    def test_generate_heatmap_data(self):
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            # Créer des fichiers de test
            open(os.path.join(tmpdir, "main.py"), "w").close()
            open(os.path.join(tmpdir, "test_module.py"), "w").close()
            data = analytics.generate_heatmap_data(tmpdir)
            self.assertIn("heatmap_data", data)
            self.assertIn("total_files", data)
            self.assertIn("max_complexity", data)

    def test_generate_technical_debt_analysis(self):
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            # Créer des fichiers de test
            with open(os.path.join(tmpdir, "main.py"), "w") as f:
                f.write(
                    "# Test comment for technical debt analysis\n# Bug comment for testing\n"
                )
            data = analytics.generate_technical_debt_analysis(tmpdir)
            self.assertIn("technical_debt_score", data)
            self.assertIn("debt_indicators", data)
            self.assertIn("recommendations", data)

    def test_generate_analytics_html(self):
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            # Créer des fichiers de test
            open(os.path.join(tmpdir, "main.py"), "w").close()
            open(os.path.join(tmpdir, "README.md"), "w").close()
            html = analytics.generate_analytics_html(tmpdir)
            self.assertIn("<html", html)
            self.assertIn("Analytics", html)

    def test_analyze_project(self):
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            # Créer des fichiers de test
            open(os.path.join(tmpdir, "main.py"), "w").close()
            open(os.path.join(tmpdir, "test_module.py"), "w").close()
            open(os.path.join(tmpdir, "README.md"), "w").close()
            os.mkdir(os.path.join(tmpdir, "subdir"))
            report = analytics.analyze_project(tmpdir)
            self.assertIn("structure", report)
            self.assertIn("complexity", report["structure"])
            self.assertIn("coverage", report["structure"])
            self.assertIn("dependencies", report["structure"])
            self.assertIn("score", report)


if __name__ == "__main__":
    unittest.main()
