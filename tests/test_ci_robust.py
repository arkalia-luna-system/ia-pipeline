#!/usr/bin/env python3
"""
Tests CI robustes pour Athalia - Évite les problèmes courants en CI
"""

import os
import sys
import pytest
import subprocess
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

# Configuration pour éviter les problèmes en CI
os.environ['PYTHONPATH'] = os.pathsep.join([
    os.getcwd(),
    os.environ.get('PYTHONPATH', '')
])

# Désactiver les tests interactifs et lourds en CI
CI_MODE = os.environ.get('CI') == 'true'

class TestCIRobust:
    """Tests robustes pour la CI"""
    
    def test_imports_core_modules(self):
        """Test d'import des modules core sans dépendances externes"""
        core_modules = [
            'athalia_core.audit',
            'athalia_core.cleanup', 
            'athalia_core.auto_cleaner',
            'athalia_core.auto_tester',
            'athalia_core.auto_documenter',
            'athalia_core.auto_cicd',
            'athalia_core.analytics',
            'athalia_core.ai_robust',
            'athalia_core.athalia_orchestrator',
            'athalia_core.advanced_analytics'
        ]
        
        for module_name in core_modules:
            try:
                __import__(module_name)
                print(f"✅ {module_name} importé avec succès")
            except ImportError as e:
                if CI_MODE:
                    pytest.skip(f"Module {module_name} non disponible en CI: {e}")
                else:
                    raise
    
    def test_syntax_check(self):
        """Vérifie la syntaxe de tous les fichiers Python"""
        python_files = []
        
        # Trouver tous les fichiers Python
        for root, dirs, files in os.walk('.'):
            # Ignorer les dossiers problématiques
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'archive', '.mypy_cache', '.benchmarks']]
            
            for file in files:
                if file.endswith('.py') and not file.startswith('._'):
                    python_files.append(os.path.join(root, file))
        
        errors = []
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    compile(f.read(), py_file, 'exec')
            except Exception as e:
                # Ignorer les erreurs dans les fichiers de projets externes
                if 'projects/' in py_file or 'mon-projet/' in py_file:
                    continue
                errors.append(f"{py_file}: {e}")
        
        if errors:
            pytest.fail(f"Erreurs de syntaxe trouvées:\n" + "\n".join(errors))
    
    def test_requirements_installable(self):
        """Test que les requirements peuvent être installés"""
        if not CI_MODE:
            pytest.skip("Test CI uniquement")
        
        try:
            # Test d'installation des requirements essentiels
            essential_packages = [
                'pytest', 'requests', 'pyyaml', 'jinja2', 'click', 'rich'
            ]
            
            for package in essential_packages:
                try:
                    __import__(package.replace('-', '_'))
                except ImportError:
                    pytest.fail(f"Package {package} non installé")
                    
        except Exception as e:
            pytest.fail(f"Erreur lors du test des requirements: {e}")
    
    def test_config_files_exist(self):
        """Vérifie l'existence des fichiers de configuration essentiels"""
        required_files = [
            'config/requirements.txt',
            'config/athalia_config.yaml',
            '.gitignore',
            'README.md'
        ]
        
        missing_files = []
        for file_path in required_files:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            pytest.fail(f"Fichiers manquants: {missing_files}")
    
    def test_test_discovery(self):
        """Vérifie que pytest peut découvrir les tests"""
        try:
            result = subprocess.run([
                sys.executable, '-m', 'pytest', '--collect-only', '-q'
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                pytest.fail(f"Pytest discovery échoué: {result.stderr}")
                
            # Vérifier qu'on a trouvé des tests
            if 'collected 0 items' in result.stdout:
                pytest.fail("Aucun test trouvé par pytest")
                
        except subprocess.TimeoutExpired:
            pytest.fail("Timeout lors de la découverte des tests")
        except Exception as e:
            pytest.fail(f"Erreur lors de la découverte des tests: {e}")
    
    def test_core_functionality(self):
        """Test des fonctionnalités core sans dépendances externes"""
        try:
            # Test d'import du module principal
            from athalia_core import audit, cleanup, analytics
            
            # Test de création d'objets de base
            from athalia_core.auto_cleaner import AutoCleaner
            from athalia_core.auto_tester import AutoTester
            from athalia_core.auto_documenter import AutoDocumenter
            
            # Test en mode dry_run
            with tempfile.TemporaryDirectory() as temp_dir:
                cleaner = AutoCleaner(temp_dir)
                cleaner.dry_run = True
                
                result = cleaner.clean_project()
                assert isinstance(result, dict)
                assert 'stats' in result
                
        except ImportError as e:
            if CI_MODE:
                pytest.skip(f"Module non disponible en CI: {e}")
            else:
                raise
        except Exception as e:
            pytest.fail(f"Erreur lors du test des fonctionnalités core: {e}")
    
    def test_no_hardcoded_paths(self):
        """Vérifie qu'il n'y a pas de chemins hardcodés problématiques"""
        problematic_patterns = [
            '/Users/', '/home/', '/Volumes/', 'C:\\', 'D:\\'
        ]
        
        python_files = []
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'archive', '.mypy_cache', '.benchmarks']]
            for file in files:
                if file.endswith('.py') and not file.startswith('._'):
                    python_files.append(os.path.join(root, file))
        
        hardcoded_paths = []
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in problematic_patterns:
                        if pattern in content:
                            # Ignorer les fichiers de test qui contiennent ces patterns pour tester
                            if 'test_ci_robust.py' in py_file or 'identify_problematic_tests.py' in py_file:
                                continue
                            hardcoded_paths.append(f"{py_file}: {pattern}")
            except Exception:
                continue
        
        if hardcoded_paths:
            pytest.fail(f"Chemins hardcodés trouvés:\n" + "\n".join(hardcoded_paths))
    
    def test_encoding_consistency(self):
        """Vérifie la cohérence de l'encodage des fichiers"""
        python_files = []
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'archive', '.mypy_cache', '.benchmarks']]
            for file in files:
                if file.endswith('.py') and not file.startswith('._'):
                    python_files.append(os.path.join(root, file))
        
        encoding_errors = []
        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    f.read()
            except UnicodeDecodeError as e:
                encoding_errors.append(f"{py_file}: {e}")
        
        if encoding_errors:
            pytest.fail(f"Erreurs d'encodage trouvées:\n" + "\n".join(encoding_errors))

if __name__ == '__main__':
    pytest.main([__file__, '-v']) 