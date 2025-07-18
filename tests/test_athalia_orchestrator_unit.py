import unittest
from pathlib import Path
from athalia_core.athalia_orchestrator import AthaliaOrchestrator

class TestAthaliaOrchestrator(unittest.TestCase):
    def setUp(self):
        self.project_path = Path('.')
        self.orchestrator = AthaliaOrchestrator()
        self.orchestrator.project_path = self.project_path

    def test_constructor(self):
        self.assertIsInstance(self.orchestrator, AthaliaOrchestrator)
        self.assertEqual(self.orchestrator.project_path, self.project_path)

    def test_run_cleanup(self):
        result = self.orchestrator._run_cleanup()
        self.assertIsInstance(result, dict)

    def test_run_documentation(self):
        result = self.orchestrator._run_documentation()
        self.assertIsInstance(result, dict)

    def test_run_testing(self):
        result = self.orchestrator._run_testing()
        self.assertIsInstance(result, dict)

    def test_run_cicd(self):
        result = self.orchestrator._run_cicd()
        self.assertIsInstance(result, dict)

    def test_generate_final_report(self):
        dummy_results = {'steps': {'cleanup': {'passed': True}, 'docs': {'passed': True}}, 'project_path': str(self.project_path), 'date': '2024-01-01', 'config': {}}
        report = self.orchestrator._generate_final_report(dummy_results)
        self.assertIsInstance(report, str)

    def test_save_report(self):
        dummy_results = {'steps': {'cleanup': {'passed': True}}, 'project_path': str(self.project_path), 'date': '2024-01-01', 'config': {}}
        try:
            self.orchestrator._save_report(dummy_results)
        except Exception as e:
            self.fail(f"_save_report a levé une exception: {e}")

if __name__ == "__main__":
    unittest.main() 