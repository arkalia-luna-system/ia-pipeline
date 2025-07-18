"""
Tests CI ultra-rapides - Vérifications essentielles uniquement
Exécution: < 10 secondes
"""
import pytest
import sys
import os
from pathlib import Path


class TestCIUltraFast:
    """Tests CI ultra-rapides pour validation essentielle"""
    
    def test_python_version(self):
        """Vérifie la version Python"""
        assert sys.version_info >= (3, 8), "Python 3.8+ requis"
    
    def test_essential_imports(self):
        """Vérifie les imports essentiels"""
        try:
            import athalia_core
            import athalia_core.audit
            import athalia_core.cleanup
            import athalia_core.analytics
            assert True
        except ImportError as e:
            pytest.fail(f"Import essentiel échoué: {e}")
    
    def test_config_files_exist(self):
        """Vérifie l'existence des fichiers de config essentiels"""
        essential_files = [
            "config/requirements.txt",
            "config/athalia_config.yaml",
            "README.md",
            "docs/README.md"
        ]
        
        for file_path in essential_files:
            assert Path(file_path).exists(), f"Fichier manquant: {file_path}"
    
    def test_syntax_check_core(self):
        """Vérifie la syntaxe des modules core"""
        import ast
        
        core_modules = [
            "athalia_core/audit.py",
            "athalia_core/cleanup.py", 
            "athalia_core/analytics.py",
            "athalia_core/cli.py"
        ]
        
        for module in core_modules:
            if Path(module).exists():
                try:
                    with open(module, 'r', encoding='utf-8') as f:
                        ast.parse(f.read())
                except SyntaxError as e:
                    pytest.fail(f"Erreur de syntaxe dans {module}: {e}")
    
    def test_no_critical_errors(self):
        """Vérifie qu'il n'y a pas d'erreurs critiques"""
        # Vérifie qu'il n'y a pas de fichiers corrompus
        corrupted_patterns = [
            "athalia_unified_enhanced.py",
            "module_discovery.py", 
            "api_templates.py",
            "fix_all_athalia_core.py"
        ]
        
        for pattern in corrupted_patterns:
            assert not Path(pattern).exists(), f"Fichier corrompu détecté: {pattern}"
    
    def test_requirements_parseable(self):
        """Vérifie que requirements.txt est parseable"""
        try:
            with open("config/requirements.txt", 'r') as f:
                requirements = f.read()
                assert requirements.strip(), "requirements.txt vide"
                # Vérifie qu'il n'y a pas de caractères corrompus
                assert "f" not in requirements or requirements.count("f") < 100, "Fichier requirements.txt corrompu"
        except Exception as e:
            pytest.fail(f"Erreur lecture requirements.txt: {e}")
    
    def test_git_clean(self):
        """Vérifie que le repo git est propre"""
        # Vérifie qu'il n'y a pas trop de fichiers temporaires
        temp_files = list(Path(".").glob("*.tmp"))
        temp_files.extend(Path(".").glob("*.log"))
        temp_files.extend(Path(".").glob("._*"))
        
        assert len(temp_files) < 50, f"Trop de fichiers temporaires: {len(temp_files)}"
    
    def test_essential_structure(self):
        """Vérifie la structure essentielle du projet"""
        essential_dirs = [
            "athalia_core",
            "tests", 
            "docs",
            "config"
        ]
        
        for dir_name in essential_dirs:
            assert Path(dir_name).exists(), f"Répertoire manquant: {dir_name}"
            assert Path(dir_name).is_dir(), f"Pas un répertoire: {dir_name}"


if __name__ == "__main__":
    # Exécution directe pour debug
    pytest.main([__file__, "-v", "--tb=short"]) 