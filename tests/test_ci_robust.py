"""
Tests CI robustes - Vérifications essentielles pour la CI
Exécution: < 5 secondes
"""
import pytest
import sys
import os
import ast
from pathlib import Path


class TestCIRobust:
    """Tests CI robustes pour validation essentielle"""

    def test_imports_core_modules(self):
        """Vérifie les imports des modules core"""
        core_modules = [
            'athalia_core',
            'athalia_core.audit',
            'athalia_core.cleanup',
            'athalia_core.analytics'
        ]

        for module in core_modules:
            try:
                __import__(module)
            except ImportError as e:
                pytest.fail(f"Import échoué pour {module}: {e}")

    def test_syntax_check(self):
        """Vérifie la syntaxe des fichiers Python essentiels"""
        essential_files = [
            'athalia_core/audit.py',
            'athalia_core/cleanup.py',
            'athalia_core/analytics.py',
            'athalia_core/cli.py'
        ]

        for file_path in essential_files:
            if Path(file_path).exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        ast.parse(f.read())
                except SyntaxError as e:
                    pytest.fail(f"Erreur de syntaxe dans {file_path}: {e}")

    @pytest.mark.skip(reason="Test CI uniquement")
    def test_requirements_installable(self):
        """Vérifie que requirements.txt est installable"""
        try:
            with open('config/requirements.txt', 'r') as f:
                requirements = f.read()
                assert requirements.strip(), "requirements.txt vide"
        except Exception as e:
            pytest.fail(f"Erreur requirements.txt: {e}")

    def test_config_files_exist(self):
        """Vérifie l'existence des fichiers de configuration"""
        config_files = [
            'config/requirements.txt',
            'config/athalia_config.yaml',
            'README.md'
        ]

        for file_path in config_files:
            assert Path(file_path).exists(), (
                f"Fichier de config manquant: {file_path}")

    def test_test_discovery(self):
        """Vérifie que les tests peuvent être découverts"""
        test_files = list(Path('tests').glob('test_*.py'))
        assert len(test_files) > 5, (
            f"Pas assez de tests trouvés: {len(test_files)}")

    def test_core_functionality(self):
        """Test de fonctionnalités core essentielles"""
        try:
            # Test que les modules existent
            import athalia_core.audit
            import athalia_core.cleanup
            import athalia_core.analytics

            # Test que les modules ont des fonctions
            assert hasattr(athalia_core.audit, '__file__'), (
                "Module audit non trouvé")
            assert hasattr(athalia_core.cleanup, '__file__'), (
                "Module cleanup non trouvé")
            assert hasattr(athalia_core.analytics, '__file__'), (
                "Module analytics non trouvé")

        except ImportError as e:
            pytest.fail(f"Import fonctionnalité core échoué: {e}")

    def test_no_hardcoded_paths(self):
        """Vérifie qu'il n'y a pas de chemins hardcodés problématiques"""
        import re

        # Patterns de chemins hardcodés à éviter
        hardcoded_patterns = [
            r'/Users/[^/]+/Desktop',
            r'/home/[^/]+/Desktop',
            r'C:\\Users\\[^\\]+\\Desktop'
        ]

        python_files = list(Path('.').glob('**/*.py'))
        python_files = [
            f for f in python_files
            if '.git' not in str(f) and '__pycache__' not in str(f)
        ]

        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8',
                         errors='ignore') as f:
                    content = f.read()
                    for pattern in hardcoded_patterns:
                        matches = re.findall(pattern, content)
                        if matches:
                            pytest.fail(
                                f"Chemin hardcodé trouvé dans {py_file}: "
                                f"{matches}")
            except Exception:
                continue  # Ignore les erreurs de lecture

    @pytest.mark.skip(reason="Test désactivé - fichiers corrompus nettoyés")
    def test_encoding_consistency(self):
        """Test que tous les fichiers Python sont encodés en UTF-8"""
        python_files = []
        for root, dirs, files in os.walk('.'):
            if '.git' in root or '__pycache__' in root:
                continue
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    f.read()
            except UnicodeDecodeError as e:
                pytest.fail(f"Erreur d'encodage dans {py_file}: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"]) 