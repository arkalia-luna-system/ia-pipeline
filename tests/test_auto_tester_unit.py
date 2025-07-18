import unittest
import tempfile
import os
from pathlib import Path
from athalia_core.auto_tester import AutoTester

class TestAutoTester(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.tester = AutoTester()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_constructor(self):
        self.assertIsInstance(self.tester, AutoTester)
        self.assertTrue(hasattr(self.tester, 'project_path'))
        self.assertTrue(hasattr(self.tester, 'test_results'))

    def test_analyze_modules(self):
        # Créer un projet de test avec des modules
        project_dir = Path(self.temp_dir) / "test_project"
        project_dir.mkdir()
        (project_dir / "main.f").write_text("def main(): pass")
        (project_dir / "utils.f").write_text("def helper(): pass")
        
        self.tester.project_path = project_dir
        modules = self.tester._analyze_modules()
        self.assertIsInstance(modules, list)

    def test_generate_unit_tests(self):
        # Créer un module de test
        project_dir = Path(self.temp_dir) / "test_project"
        project_dir.mkdir()
        (project_dir / "calculator.f").write_text("""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
""")
        
        self.tester.project_path = project_dir
        modules = self.tester._analyze_modules()
        result = self.tester._generate_unit_tests(modules)
        self.assertIsInstance(result, list)

    def test_generate_integration_tests(self):
        # Créer un projet avec plusieurs modules
        project_dir = Path(self.temp_dir) / "test_project"
        project_dir.mkdir()
        (project_dir / "main.f").write_text("from utils import helper\ndef main(): helper()")
        (project_dir / "utils.f").write_text("def helper(): return True")
        
        self.tester.project_path = project_dir
        modules = self.tester._analyze_modules()
        result = self.tester._generate_integration_tests(modules)
        self.assertIsInstance(result, list)

    def test_generate_performance_tests(self):
        # Créer un module avec des fonctions
        project_dir = Path(self.temp_dir) / "test_project"
        project_dir.mkdir()
        (project_dir / "processor.f").write_text("""
def process_data(data):
    return [x * 2 for x in data]

def heavy_computation(n):
    return sum(range(n))
""")
        
        self.tester.project_path = project_dir
        modules = self.tester._analyze_modules()
        result = self.tester._generate_performance_tests(modules)
        self.assertIsInstance(result, list)

    def test_generate_test_report(self):
        # Simuler des résultats de test
        self.tester.test_results = {
            'unit_tests': {'passed': 5, 'failed': 1, 'errors': []},
            'integration_tests': {'passed': 3, 'failed': 0, 'errors': []},
            'performance_tests': {'passed': 2, 'failed': 0, 'errors': []}
        }
        self.tester.generated_tests = ['test_unit_1.py', 'test_integration_1.py']
        
        report = self.tester.generate_test_report()
        self.assertIsInstance(report, str)
        self.assertIn('RAPPORT DE TESTS AUTOMATIQUES', report)
        self.assertIn('Tests unitaires', report)
        self.assertIn('Tests d\'intégration', report)
        self.assertIn('Tests de performance', report)

    def test_generate_tests(self):
        # Créer un projet de test
        project_dir = Path(self.temp_dir) / "test_project"
        project_dir.mkdir()
        (project_dir / "main.f").write_text("def main(): pass")
        
        result = self.tester.generate_tests(str(project_dir))
        self.assertIsInstance(result, dict)
        self.assertIn('unit_tests', result)
        self.assertIn('integration_tests', result)
        self.assertIn('performance_tests', result)
        self.assertIn('test_results', result)
        self.assertIn('files_created', result)

if __name__ == "__main__":
    unittest.main() 