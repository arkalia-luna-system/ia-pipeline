import os
import unittest

from athalia_core.auto_documenter import AutoDocumenter


class TestAutoDocumenter(unittest.TestCase):
    def setUp(self):
        self.project_path = os.getcwd()
        self.documenter = AutoDocumenter(lang="fr")
        # Initialisation complète et correcte pour toutes les méthodes privées
        self.documenter.project_info = {
            "name": "TestProject",
            "description": "Un projet de test",
            "version": "1.0.0",
            "modules": [
                {
                    "name": "core",
                    "docstring": "Module core",
                    "classes": [
                        {
                            "name": "MainClass",
                            "docstring": "Classe principale",
                            "methods": ["run", "stop"],
                        }
                    ],
                    "functions": [
                        {
                            "name": "run",
                            "docstring": "Lance le module",
                            "args": ["config"],
                        }
                    ],
                },
                {
                    "name": "api",
                    "docstring": "Module api",
                    "classes": [],
                    "functions": [],
                },
            ],
            "dependencies": {"python": ["pytest", "requests"]},
            "classes": [
                {
                    "name": "MainClass",
                    "docstring": "Classe principale",
                    "methods": ["run", "stop"],
                },
                {
                    "name": "HelperClass",
                    "docstring": "Classe utilitaire",
                    "methods": ["help"],
                },
            ],
            "functions": [
                {"name": "main", "docstring": "Fonction principale", "args": []}
            ],
            "entry_points": [],
            "license": "MIT",
        }

    def test_constructor(self):
        self.assertIsInstance(self.documenter, AutoDocumenter)
        self.assertEqual(self.documenter.lang, "fr")

    def test_load_translations(self):
        translations = self.documenter._load_translations("fr")
        self.assertIsInstance(translations, dict)

    def test_document_project(self):
        result = self.documenter.document_project(self.project_path)
        self.assertIsInstance(result, dict)
        self.assertIn("readme", result)
        self.assertIn("api_docs", result)
        self.assertIn("setup_guide", result)
        self.assertIn("usage_guide", result)
        self.assertIn("created_files", result)

    def test_generate_readme(self):
        readme = self.documenter._generate_readme()
        self.assertIsInstance(readme, str)
        self.assertIn("#", readme)

    def test_generate_api_documentation(self):
        api_docs = self.documenter._generate_api_documentation()
        self.assertIsInstance(api_docs, str)

    def test_generate_setup_guide(self):
        setup_guide = self.documenter._generate_setup_guide()
        self.assertIsInstance(setup_guide, str)

    def test_generate_usage_guide(self):
        usage_guide = self.documenter._generate_usage_guide()
        self.assertIsInstance(usage_guide, str)

    def test_get_created_files(self):
        files = self.documenter._get_created_files()
        self.assertIsInstance(files, list)


if __name__ == "__main__":
    unittest.main()
