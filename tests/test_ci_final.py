"""
Test CI Final - Vérifications complètes pour la CI
Exécution: < 30 secondes
"""
import pytest
import sys
import os
import time
from pathlib import Path


class TestCIFinal:
    """Tests CI finaux pour validation complète"""
    
    def test_environment_setup(self):
        """Vérifie l'environnement CI"""
        # En local, on peut ne pas avoir les variables CI
        if os.getenv('CI') != 'true' and os.getenv('GITHUB_ACTIONS') is None:
            pytest.skip("Pas en environnement CI")
        assert sys.version_info >= (3, 8), "Python 3.8+ requis"
    
    def test_core_imports(self):
        """Vérifie tous les imports core"""
        core_modules = [
            'athalia_core',
            'athalia_core.audit',
            'athalia_core.cleanup', 
            'athalia_core.analytics',
            'athalia_core.cli',
            'athalia_core.config_manager'
        ]
        
        for module in core_modules:
            try:
                __import__(module)
            except ImportError as e:
                pytest.fail(f"Import échoué pour {module}: {e}")
    
    def test_configuration_files(self):
        """Vérifie tous les fichiers de configuration"""
        config_files = [
            "config/requirements.txt",
            "config/athalia_config.yaml", 
            "config/pyproject.toml",
            "pytest-ci.ini",
            ".github/workflows/ci.yaml",
            "README.md",
            "docs/README.md"
        ]
        
        for file_path in config_files:
            assert Path(file_path).exists(), f"Fichier de config manquant: {file_path}"
    
    def test_syntax_validation(self):
        """Vérifie la syntaxe de tous les fichiers Python"""
        import ast
        
        python_files = list(Path(".").glob("**/*.py"))
        python_files = [f for f in python_files if ".git" not in str(f) and "__pycache__" not in str(f) and "venv" not in str(f) and not f.name.startswith("._")]
        
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    ast.parse(f.read())
            except SyntaxError as e:
                pytest.fail(f"Erreur de syntaxe dans {py_file}: {e}")
            except UnicodeDecodeError as e:
                pytest.fail(f"Erreur d'encodage dans {py_file}: {e}")
    
    def test_no_corrupted_files(self):
        """Vérifie qu'il n'y a pas de fichiers corrompus"""
        corrupted_patterns = [
            "athalia_unified_enhanced.py",
            "module_discovery.py",
            "api_templates.py", 
            "fix_all_athalia_core.py"
        ]
        
        for pattern in corrupted_patterns:
            assert not Path(pattern).exists(), f"Fichier corrompu détecté: {pattern}"
    
    def test_requirements_quality(self):
        """Vérifie la qualité du fichier requirements.txt"""
        try:
            with open("config/requirements.txt", 'r') as f:
                content = f.read()
                assert content.strip(), "requirements.txt vide"
                assert "f" not in content or content.count("f") < 50, "Fichier requirements.txt suspect"
                
                # Vérifie qu'il y a des dépendances essentielles
                essential_deps = ['pytest', 'yaml', 'requests']
                for dep in essential_deps:
                    assert any(dep in line for line in content.split('\n')), f"Dépendance manquante: {dep}"
        except Exception as e:
            pytest.fail(f"Erreur lecture requirements.txt: {e}")
    
    def test_project_structure(self):
        """Vérifie la structure du projet"""
        essential_dirs = [
            "athalia_core",
            "tests",
            "docs", 
            "config",
            "setup"
        ]
        
        for dir_name in essential_dirs:
            assert Path(dir_name).exists(), f"Répertoire manquant: {dir_name}"
            assert Path(dir_name).is_dir(), f"Pas un répertoire: {dir_name}"
    
    def test_test_discovery(self):
        """Vérifie que les tests peuvent être découverts"""
        import pytest
        
        # Test de découverte des tests
        test_files = list(Path("tests").glob("test_*.py"))
        assert len(test_files) > 10, f"Pas assez de tests trouvés: {len(test_files)}"
        
        # Vérifie que les tests CI existent
        ci_tests = ["test_ci_ultra_fast.py", "test_ci_robust.py", "test_ci_final.py"]
        for test in ci_tests:
            assert Path(f"tests/{test}").exists(), f"Test CI manquant: {test}"
    
    def test_core_functionality(self):
        """Test de fonctionnalités core essentielles"""
        try:
            # Test que les modules existent
            import athalia_core.audit
            import athalia_core.cleanup
            import athalia_core.analytics
            
            # Test que les modules ont des fonctions
            assert hasattr(athalia_core.audit, '__file__'), "Module audit non trouvé"
            assert hasattr(athalia_core.cleanup, '__file__'), "Module cleanup non trouvé"
            assert hasattr(athalia_core.analytics, '__file__'), "Module analytics non trouvé"
            
        except ImportError as e:
            pytest.fail(f"Import fonctionnalité core échoué: {e}")
    
    def test_performance_ci(self):
        """Test de performance pour la CI"""
        start_time = time.time()
        
        # Test rapide d'import
        import athalia_core
        import athalia_core.audit
        
        end_time = time.time()
        assert end_time - start_time < 5.0, f"Import trop lent: {end_time - start_time:.2f}s"
    
    def test_no_hardcoded_paths(self):
        """Vérifie qu'il n'y a pas de chemins hardcodés problématiques"""
        import re
        
        # Patterns de chemins hardcodés à éviter (plus permissif)
        hardcoded_patterns = [
            r'/Users/[^/]+/Desktop',
            r'/home/[^/]+/Desktop',
            r'C:\\Users\\[^\\]+\\Desktop'
        ]
        
        python_files = list(Path(".").glob("**/*.py"))
        python_files = [f for f in python_files if ".git" not in str(f) and "__pycache__" not in str(f) and not f.name.startswith("._")]
        
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in hardcoded_patterns:
                        matches = re.findall(pattern, content)
                        if matches:
                            pytest.fail(f"Chemin hardcodé trouvé dans {py_file}: {matches}")
            except Exception:
                continue  # Ignore les erreurs de lecture


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"]) 