import os
import tempfile
import unittest
from pathlib import Path

from athalia_core.auto_cleaner import AutoCleaner


class TestAutoCleaner(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.cleaner = AutoCleaner(self.temp_dir)
        # Forcer le mode dry_run pour éviter la suppression réelle
        self.cleaner.dry_run = True

    def tearDown(self):
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_constructor(self):
        self.assertIsInstance(self.cleaner, AutoCleaner)
        self.assertEqual(str(self.cleaner.project_path), self.temp_dir)
        self.assertTrue(self.cleaner.dry_run)  # Forcé à True
        self.assertEqual(self.cleaner.cleaned_files, [])
        self.assertEqual(self.cleaner.cleaned_dirs, [])
        self.assertEqual(self.cleaner.errors, [])

    def test_clean_project_dry_run(self):
        # Créer des fichiers de test
        test_file = Path(self.temp_dir) / "test.pyc"
        test_file.write_text("test")

        result = self.cleaner.clean_project(dry_run=True)
        self.assertIn("stats", result)
        self.assertIn("files_removed", result["stats"])
        self.assertIn("dirs_removed", result["stats"])
        self.assertIn("space_freed_mb", result["stats"])
        self.assertIn("errors", result["stats"])

    def test_clean_system_files(self):
        # Créer un fichier système
        ds_store = Path(self.temp_dir) / ".DS_Store"
        ds_store.write_text("system file")

        self.cleaner._clean_system_files(Path(self.temp_dir))
        # En mode dry_run=True, le fichier ne devrait pas être supprimé
        self.assertTrue(ds_store.exists())

    def test_clean_cache_files(self):
        # Créer des fichiers de cache
        pycache_dir = Path(self.temp_dir) / "__pycache__"
        pycache_dir.mkdir()
        (pycache_dir / "test.pyc").write_text("cache")

        self.cleaner._clean_cache_files(Path(self.temp_dir))
        # En mode dry_run=True, les fichiers ne devraient pas être supprimés
        self.assertTrue(pycache_dir.exists())

    def test_clean_backup_files(self):
        # Créer un fichier de backup
        backup_file = Path(self.temp_dir) / "test.bak"
        backup_file.write_text("backup")

        self.cleaner._clean_backup_files(Path(self.temp_dir))
        # En mode dry_run=True, le fichier ne devrait pas être supprimé
        self.assertTrue(backup_file.exists())

    def test_clean_temp_files(self):
        # Créer un fichier temporaire
        temp_file = Path(self.temp_dir) / "temp.tmp"
        temp_file.write_text("temp")

        self.cleaner._clean_temp_files(Path(self.temp_dir))
        # En mode dry_run=True, le fichier ne devrait pas être supprimé
        self.assertTrue(temp_file.exists())

    def test_clean_duplicate_files(self):
        # Créer des fichiers identiques
        file1 = Path(self.temp_dir) / "test1.py"
        file2 = Path(self.temp_dir) / "test2.py"
        content = "print('Hello')"
        file1.write_text(content)
        file2.write_text(content)

        self.cleaner._clean_duplicate_files(Path(self.temp_dir))
        # En mode dry_run=True, les fichiers ne devraient pas être supprimés
        self.assertTrue(file1.exists())
        self.assertTrue(file2.exists())

    def test_clean_empty_directories(self):
        # Créer un répertoire vide
        empty_dir = Path(self.temp_dir) / "empty_dir"
        empty_dir.mkdir()

        self.cleaner._clean_empty_directories(Path(self.temp_dir))
        # En mode dry_run=True, le répertoire ne devrait pas être supprimé
        self.assertTrue(empty_dir.exists())

    def test_is_code_file(self):
        code_file = Path(self.temp_dir) / "test.py"
        code_file.write_text("print('test')")

        self.assertTrue(self.cleaner._is_code_file(code_file))

        non_code_file = Path(self.temp_dir) / "test.txt"
        non_code_file.write_text("text")
        self.assertFalse(self.cleaner._is_code_file(non_code_file))

    def test_is_important_file(self):
        # Tester avec des fichiers réels du projet
        important_files = ["README.md", "requirements.txt", "setup.py", "main.py"]
        for filename in important_files:
            file_path = Path(self.temp_dir) / filename
            file_path.write_text("content")
            # Vérifier si le fichier est considéré comme important
            is_important = self.cleaner._is_important_file(file_path)
            # Au moins certains fichiers devraient être importants
            if filename in ["README.md", "requirements.txt"]:
                self.assertTrue(is_important, f"{filename} devrait être important")

        # Fichier non important
        non_important = Path(self.temp_dir) / "temp.txt"
        non_important.write_text("temp")
        self.assertFalse(self.cleaner._is_important_file(non_important))

    def test_is_empty_directory(self):
        # Répertoire vide
        empty_dir = Path(self.temp_dir) / "empty"
        empty_dir.mkdir()
        self.assertTrue(self.cleaner._is_empty_directory(empty_dir))

        # Répertoire avec fichier
        non_empty_dir = Path(self.temp_dir) / "non_empty"
        non_empty_dir.mkdir()
        (non_empty_dir / "test.txt").write_text("content")
        self.assertFalse(self.cleaner._is_empty_directory(non_empty_dir))

    def test_calculate_file_hash(self):
        test_file = Path(self.temp_dir) / "hash_test.txt"
        test_file.write_text("Hello World")

        hash1 = self.cleaner._calculate_file_hash(test_file)
        hash2 = self.cleaner._calculate_file_hash(test_file)

        self.assertEqual(hash1, hash2)
        self.assertIsInstance(hash1, str)

    def test_generate_cleanup_report(self):
        # Simuler des nettoyages
        self.cleaner.cleaned_files = [{"path": "test.pyc", "reason": "Cache"}]
        self.cleaner.cleaned_dirs = [{"path": "empty_dir", "reason": "Empty"}]
        self.cleaner.stats["files_removed"] = 1
        self.cleaner.stats["dirs_removed"] = 1

        report = self.cleaner._generate_cleanup_report()
        self.assertIn("stats", report)
        self.assertIn("files", report)  # Clé réelle utilisée
        self.assertIn("dirs", report)  # Clé réelle utilisée
        self.assertIn("summary", report)

    def test_optimize_project_structure(self):
        result = self.cleaner.optimize_project_structure(self.temp_dir)
        self.assertIn("optimizations", result)
        # Vérifier les clés réellement retournées
        self.assertIn("dry_run", result)


if __name__ == "__main__":
    unittest.main()
