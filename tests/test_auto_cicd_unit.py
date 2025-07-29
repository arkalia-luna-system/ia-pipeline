import os
import tempfile
import unittest
from pathlib import Path

from athalia_core.auto_cicd import AutoCICD, generate_github_ci_yaml


class TestAutoCICD(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.cicd = AutoCICD()

    def tearDown(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_constructor(self):
        self.assertIsInstance(self.cicd, AutoCICD)
        self.assertIsNone(self.cicd.project_path)
        self.assertEqual(self.cicd.project_info, {})
        self.assertEqual(self.cicd.cicd_config, {})

    def test_setup_cicd(self):
        # Créer un projet Python de test
        project_dir = Path(self.temp_dir) / "test_project"
        project_dir.mkdir()
        (project_dir / "requirements.txt").write_text("pytest\nrequests")
        (project_dir / "main.py").write_text("print('Hello')")
        (project_dir / "tests").mkdir()
        (project_dir / "tests" / "test_main.py").write_text("def test_hello(): pass")

        result = self.cicd.setup_cicd(str(project_dir))
        self.assertIn("github_actions", result)
        self.assertIn("docker_config", result)
        self.assertIn("deployment_config", result)
        self.assertIn("created_files", result)

    def test_detect_project_type_python(self):
        project_dir = Path(self.temp_dir) / "python_project"
        project_dir.mkdir()
        (project_dir / "requirements.txt").write_text("pytest")

        self.cicd.project_path = project_dir
        project_type = self.cicd._detect_project_type()
        self.assertEqual(project_type, "python")

    def test_detect_project_type_nodejs(self):
        project_dir = Path(self.temp_dir) / "nodejs_project"
        project_dir.mkdir()
        (project_dir / "package.json").write_text('{"name": "test"}')

        self.cicd.project_path = project_dir
        project_type = self.cicd._detect_project_type()
        self.assertEqual(project_type, "nodejs")

    def test_detect_languages(self):
        project_dir = Path(self.temp_dir) / "multi_lang_project"
        project_dir.mkdir()
        (project_dir / "main.py").write_text("print('Python')")
        (project_dir / "app.js").write_text("console.log('JS')")

        self.cicd.project_path = project_dir
        languages = self.cicd._detect_languages()
        self.assertIn("python", languages)
        self.assertIn("javascript", languages)

    def test_extract_dependencies_python(self):
        project_dir = Path(self.temp_dir) / "python_deps"
        project_dir.mkdir()
        (project_dir / "requirements.txt").write_text(
            "pytest\nrequests\n# comment\n\nflask"
        )

        self.cicd.project_path = project_dir
        deps = self.cicd._extract_dependencies()
        self.assertIn("python", deps)
        self.assertIn("pytest", deps["python"])
        self.assertIn("requests", deps["python"])
        self.assertIn("flask", deps["python"])

    def test_find_entry_points(self):
        project_dir = Path(self.temp_dir) / "entry_points"
        project_dir.mkdir()
        (project_dir / "main.py").write_text("print('main')")
        (project_dir / "app.py").write_text("print('app')")

        self.cicd.project_path = project_dir
        entry_points = self.cicd._find_entry_points()
        self.assertIn(str(project_dir / "main.py"), entry_points)
        self.assertIn(str(project_dir / "app.py"), entry_points)

    def test_has_tests(self):
        project_dir = Path(self.temp_dir) / "test_project"
        project_dir.mkdir()
        (project_dir / "tests").mkdir()
        (project_dir / "tests" / "test_main.py").write_text("def test(): pass")

        self.cicd.project_path = project_dir
        has_tests = self.cicd._has_tests()
        self.assertTrue(has_tests)

    def test_has_documentation(self):
        project_dir = Path(self.temp_dir) / "doc_project"
        project_dir.mkdir()
        (project_dir / "README.md").write_text("# Documentation")

        self.cicd.project_path = project_dir
        has_docs = self.cicd._has_documentation()
        self.assertTrue(has_docs)

    def test_generate_github_actions(self):
        self.cicd.project_info = {"has_tests": True}
        workflows = self.cicd._generate_github_actions()
        self.assertIn("main", workflows)
        self.assertIn("deploy", workflows)
        self.assertIn("test", workflows)

    def test_generate_docker_config(self):
        configs = self.cicd._generate_docker_config()
        self.assertIn("Dockerfile", configs)
        self.assertIn("docker-compose.yml", configs)
        self.assertIn(".dockerignore", configs)

    def test_generate_deployment_config(self):
        configs = self.cicd._generate_deployment_config()
        self.assertIn("k8s-deployment.yaml", configs)
        self.assertIn("k8s-service.yaml", configs)

    def test_get_created_files(self):
        project_dir = Path(self.temp_dir) / "created_files"
        project_dir.mkdir()
        self.cicd.project_path = project_dir

        # Créer le fichier ci.f(f
        ci_dir = project_dir / ".f" / "f"
        ci_dir.mkdir(parents=True, exist_ok=True)
        (ci_dir / "ci.f(f").write_text("# CI/CD config")

        files = self.cicd._get_created_files()
        self.assertIn(str(ci_dir / "ci.f(f"), files)


def test_generate_github_ci_yaml():
    with tempfile.TemporaryDirectory() as temp_dir:
        generate_github_ci_yaml(temp_dir)
        ci_file = Path(temp_dir) / ".f" / "f" / "ci.f(f"
        assert ci_file.exists()
        assert ci_file.read_text() == "# CI/CD config"


if __name__ == "__main__":
    unittest.main()
