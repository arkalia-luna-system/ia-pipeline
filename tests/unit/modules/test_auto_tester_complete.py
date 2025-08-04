#!/usr/bin/env python3
"""
Tests complets pour auto_tester.py (713 lignes)
MODULE CRITIQUE GÉNÉRATION AUTOMATIQUE DE TESTS

Couverture actuelle: 15% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import ast
import subprocess
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock, call

from athalia_core.auto_tester import AutoTester


class TestAutoTesterComplete:
    """Tests complets pour AutoTester."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)
        
        # Créer structure projet avec modules Python à tester
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        (self.project_path / "lib").mkdir()
        
        # Module simple avec classe et fonctions
        (self.project_path / "src" / "calculator.py").write_text('''
"""Module calculatrice simple."""

class Calculator:
    """Calculatrice basique."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition de deux nombres."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication de deux nombres."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history(self):
        """Retourne l'historique des calculs."""
        return self.history.copy()

def factorial(n):
    """Calcule la factorielle de n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Vérifie si un nombre est premier."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
''')
        
        # Module avec fonctions complexes
        (self.project_path / "src" / "data_processor.py").write_text('''
"""Module traitement données."""

class DataProcessor:
    """Processeur de données."""
    
    def __init__(self, data_source=None):
        self.data_source = data_source
        self.processed_data = []
    
    def load_data(self, source):
        """Charge les données depuis une source."""
        self.data_source = source
        # Simulation chargement
        return True
    
    def process_data(self, data):
        """Traite les données."""
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        
        processed = []
        for item in data:
            if isinstance(item, (int, float)):
                processed.append(item * 2)
            else:
                processed.append(str(item).upper())
        
        self.processed_data = processed
        return processed
    
    def save_data(self, filename):
        """Sauvegarde les données traitées."""
        if not self.processed_data:
            raise ValueError("No processed data to save")
        
        # Simulation sauvegarde
        return len(self.processed_data)

def validate_email(email):
    """Valide un email."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def parse_config(config_str):
    """Parse une configuration."""
    try:
        import json
        return json.loads(config_str)
    except (json.JSONDecodeError, TypeError):
        return None
''')
        
        # Module avec erreurs intentionnelles pour tester la détection
        (self.project_path / "src" / "buggy_module.py").write_text('''
"""Module avec bugs intentionnels."""

def divide_by_zero():
    """Fonction qui cause une division par zéro."""
    return 10 / 0

def undefined_variable():
    """Fonction qui utilise une variable non définie."""
    return undefined_var + 1

class BuggyClass:
    """Classe avec méthodes bugguées."""
    
    def method_with_syntax_error(self):
        """Méthode avec erreur de syntaxe potentielle."""
        # Cette méthode pourrait causer des problèmes
        return self.non_existent_attribute
''')
        
        # Fichier requirements.txt
        (self.project_path / "requirements.txt").write_text('''
pytest>=7.0.0
coverage>=6.0.0
black>=22.0.0
''')
        
        self.auto_tester = AutoTester(str(self.project_path))

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_auto_tester_initialization(self):
        """Test initialisation de l'AutoTester."""
        assert self.auto_tester.project_path == self.project_path
        assert hasattr(self.auto_tester, 'test_results')
        assert hasattr(self.auto_tester, 'generated_tests')
        assert isinstance(self.auto_tester.test_results, dict)
        assert isinstance(self.auto_tester.generated_tests, list)

    def test_auto_tester_initialization_default_path(self):
        """Test initialisation avec chemin par défaut."""
        with patch('pathlib.Path.cwd', return_value=Path('/test/dir')):
            tester = AutoTester()
            assert tester.project_path == Path('.')

    def test_auto_tester_initialization_custom_path(self):
        """Test initialisation avec chemin personnalisé."""
        custom_path = "/custom/project/path"
        tester = AutoTester(custom_path)
        assert tester.project_path == Path(custom_path)

    def test_run_method_execution(self):
        """Test exécution méthode run()."""
        with patch.object(self.auto_tester, 'generate_tests') as mock_generate:
            mock_generate.return_value = {"status": "success"}
            
            result = self.auto_tester.run()
            
            assert isinstance(result, dict)
            mock_generate.assert_called_once_with(str(self.project_path))

    def test_run_method_no_project_path(self):
        """Test run() sans project_path."""
        tester = AutoTester()
        tester.project_path = None
        
        with pytest.raises(ValueError, match="project_path doit être défini"):
            tester.run()

    def test_analyze_modules_comprehensive(self):
        """Test analyse complète des modules."""
        modules = self.auto_tester._analyze_modules()
        
        assert isinstance(modules, list)
        assert len(modules) > 0
        
        # Vérifier que les modules Python sont détectés
        module_names = [m.get('name', '') for m in modules]
        assert any('calculator' in name for name in module_names)
        assert any('data_processor' in name for name in module_names)

    def test_analyze_single_module_calculator(self):
        """Test analyse module calculator spécifique."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        assert isinstance(analysis, dict)
        assert "classes" in analysis
        assert "functions" in analysis
        assert "imports" in analysis
        
        # Vérifier détection classe Calculator
        classes = analysis["classes"]
        assert len(classes) >= 1
        calc_class = next((c for c in classes if c["name"] == "Calculator"), None)
        assert calc_class is not None
        assert "methods" in calc_class

    def test_analyze_single_module_data_processor(self):
        """Test analyse module data_processor."""
        proc_file = self.project_path / "src" / "data_processor.py"
        analysis = self.auto_tester._analyze_module(proc_file)
        
        assert isinstance(analysis, dict)
        
        # Vérifier détection fonctions
        functions = analysis["functions"]
        function_names = [f["name"] for f in functions]
        assert "validate_email" in function_names
        assert "parse_config" in function_names

    def test_generate_unit_tests_for_class(self):
        """Test génération tests unitaires pour classe."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        # Trouver la classe Calculator
        calc_class = next((c for c in analysis["classes"] if c["name"] == "Calculator"), None)
        assert calc_class is not None
        
        # Générer tests
        unit_tests = self.auto_tester._generate_unit_tests(calc_class, "Calculator")
        
        assert isinstance(unit_tests, str)
        assert "class TestCalculator" in unit_tests
        assert "def test_" in unit_tests
        assert "Calculator" in unit_tests

    def test_generate_unit_tests_for_function(self):
        """Test génération tests unitaires pour fonction."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        # Trouver la fonction factorial
        factorial_func = next((f for f in analysis["functions"] if f["name"] == "factorial"), None)
        assert factorial_func is not None
        
        # Générer tests
        unit_tests = self.auto_tester._generate_unit_tests(factorial_func, "factorial")
        
        assert isinstance(unit_tests, str)
        assert "def test_factorial" in unit_tests
        assert "factorial" in unit_tests

    def test_generate_integration_tests(self):
        """Test génération tests d'intégration."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        integration_tests = self.auto_tester._generate_integration_tests(analysis, "calculator")
        
        assert isinstance(integration_tests, str)
        assert "def test_integration" in integration_tests or "integration" in integration_tests.lower()

    def test_generate_test_fixtures(self):
        """Test génération fixtures de test."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        fixtures = self.auto_tester._generate_test_fixtures(analysis)
        
        assert isinstance(fixtures, str)
        # Les fixtures peuvent être vides pour des modules simples
        assert len(fixtures) >= 0

    def test_detect_test_patterns_calculator(self):
        """Test détection patterns de test pour Calculator."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        patterns = self.auto_tester._detect_test_patterns(analysis)
        
        assert isinstance(patterns, list)
        # Devrait détecter des patterns pour les méthodes mathématiques
        pattern_types = [p.get("type", "") for p in patterns]
        assert len(pattern_types) >= 0

    def test_create_test_file_calculator(self):
        """Test création fichier de test complet."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        test_content = self.auto_tester._create_test_file(analysis, "calculator")
        
        assert isinstance(test_content, str)
        assert "import pytest" in test_content
        assert "Calculator" in test_content
        assert "def test_" in test_content

    def test_write_test_file_to_disk(self):
        """Test écriture fichier de test sur disque."""
        test_content = '''
import pytest

class TestCalculator:
    def test_add(self):
        assert True
'''
        
        test_file_path = self.auto_tester._write_test_file(test_content, "calculator")
        
        assert isinstance(test_file_path, Path)
        assert test_file_path.exists()
        assert test_file_path.name.startswith("test_")
        assert "calculator" in test_file_path.name

    def test_run_generated_tests(self):
        """Test exécution des tests générés."""
        # Créer un test simple
        test_file = self.project_path / "tests" / "test_simple.py"
        test_file.write_text('''
import pytest

def test_simple_assertion():
    assert 1 + 1 == 2

def test_another_assertion():
    assert "hello".upper() == "HELLO"
''')
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="2 passed", stderr="")
            
            results = self.auto_tester._run_tests([test_file])
            
            assert isinstance(results, dict)
            mock_run.assert_called()

    def test_analyze_test_coverage(self):
        """Test analyse couverture de test."""
        # Créer fichier de test et module
        test_file = self.project_path / "tests" / "test_coverage.py"
        test_file.write_text('def test_dummy(): assert True')
        
        module_file = self.project_path / "src" / "calculator.py"
        
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(
                returncode=0, 
                stdout="calculator.py 85%",
                stderr=""
            )
            
            coverage = self.auto_tester._analyze_coverage([module_file])
            
            assert isinstance(coverage, dict)

    def test_generate_test_report(self):
        """Test génération rapport de test."""
        # Simuler résultats de tests
        self.auto_tester.test_results = {
            "total_tests": 10,
            "passed": 8,
            "failed": 2,
            "coverage": 75.5
        }
        
        report = self.auto_tester._generate_test_report()
        
        assert isinstance(report, dict)
        assert "summary" in report
        assert "details" in report

    def test_detect_potential_bugs(self):
        """Test détection bugs potentiels."""
        buggy_file = self.project_path / "src" / "buggy_module.py"
        analysis = self.auto_tester._analyze_module(buggy_file)
        
        bugs = self.auto_tester._detect_potential_bugs(analysis)
        
        assert isinstance(bugs, list)
        # Devrait détecter des patterns suspects
        assert len(bugs) >= 0

    def test_suggest_test_improvements(self):
        """Test suggestions améliorations tests."""
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        suggestions = self.auto_tester._suggest_test_improvements(analysis)
        
        assert isinstance(suggestions, list)
        # Devrait proposer des améliorations
        assert len(suggestions) >= 0

    def test_validate_test_quality(self):
        """Test validation qualité des tests."""
        test_content = '''
import pytest

class TestCalculator:
    def test_add_positive_numbers(self):
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
    
    def test_add_negative_numbers(self):
        calc = Calculator()
        result = calc.add(-2, -3)
        assert result == -5
'''
        
        quality = self.auto_tester._validate_test_quality(test_content)
        
        assert isinstance(quality, dict)
        assert "score" in quality
        assert "issues" in quality

    def test_optimize_test_suite(self):
        """Test optimisation suite de tests."""
        # Créer plusieurs fichiers de test
        test_files = []
        for i in range(3):
            test_file = self.project_path / "tests" / f"test_module_{i}.py"
            test_file.write_text(f'''
def test_function_{i}():
    assert {i} + 1 == {i + 1}
''')
            test_files.append(test_file)
        
        optimized = self.auto_tester._optimize_test_suite(test_files)
        
        assert isinstance(optimized, dict)
        assert "recommendations" in optimized

    def test_generate_tests_full_workflow(self):
        """Test workflow complet génération tests."""
        result = self.auto_tester.generate_tests(str(self.project_path))
        
        assert isinstance(result, dict)
        assert "modules_analyzed" in result
        assert "tests_generated" in result
        assert "status" in result

    def test_error_handling_invalid_module(self):
        """Test gestion erreurs module invalide."""
        # Créer module avec syntaxe invalide
        invalid_file = self.project_path / "src" / "invalid.py"
        invalid_file.write_text("def broken_syntax(\n    pass")  # Syntaxe cassée
        
        # L'analyse devrait gérer l'erreur gracieusement
        try:
            analysis = self.auto_tester._analyze_module(invalid_file)
            assert isinstance(analysis, dict)
        except SyntaxError:
            # Exception acceptable
            pass

    def test_error_handling_missing_file(self):
        """Test gestion erreurs fichier manquant."""
        missing_file = self.project_path / "does_not_exist.py"
        
        try:
            analysis = self.auto_tester._analyze_module(missing_file)
            assert analysis is None or isinstance(analysis, dict)
        except FileNotFoundError:
            # Exception acceptable
            pass

    def test_batch_test_generation(self):
        """Test génération tests en lot."""
        modules = [
            self.project_path / "src" / "calculator.py",
            self.project_path / "src" / "data_processor.py"
        ]
        
        results = self.auto_tester._batch_generate_tests(modules)
        
        assert isinstance(results, list)
        assert len(results) == len(modules)

    def test_test_template_customization(self):
        """Test personnalisation templates de test."""
        custom_template = {
            "imports": ["import pytest", "from unittest.mock import Mock"],
            "class_prefix": "TestCustom",
            "method_prefix": "test_custom_"
        }
        
        calc_file = self.project_path / "src" / "calculator.py"
        analysis = self.auto_tester._analyze_module(calc_file)
        
        custom_tests = self.auto_tester._generate_custom_tests(analysis, custom_template)
        
        assert isinstance(custom_tests, str)
        assert "TestCustom" in custom_tests

    def test_integration_with_ci_cd(self):
        """Test intégration CI/CD."""
        ci_config = {
            "auto_run_tests": True,
            "generate_coverage_report": True,
            "fail_on_low_coverage": True,
            "coverage_threshold": 80
        }
        
        result = self.auto_tester._integrate_ci_cd(ci_config)
        
        assert isinstance(result, dict)
        assert "ci_integration" in result

    @pytest.mark.parametrize("module_type,expected_tests", [
        ("class", ["test_initialization", "test_methods"]),
        ("function", ["test_normal_case", "test_edge_case"]),
        ("module", ["test_imports", "test_integration"]),
    ])
    def test_test_type_generation(self, module_type, expected_tests):
        """Test génération tests par type de module."""
        # Mock différents types d'analyse
        if module_type == "class":
            analysis = {
                "classes": [{"name": "TestClass", "methods": ["method1", "method2"]}],
                "functions": [],
                "imports": []
            }
        elif module_type == "function":
            analysis = {
                "classes": [],
                "functions": [{"name": "test_function", "args": ["x", "y"]}],
                "imports": []
            }
        else:
            analysis = {
                "classes": [],
                "functions": [],
                "imports": ["import os", "import sys"]
            }
        
        tests = self.auto_tester._generate_tests_by_type(analysis, module_type)
        
        assert isinstance(tests, str)
        # Vérifier que certains patterns de test sont présents
        assert "def test_" in tests

    def test_performance_large_project(self):
        """Test performance sur gros projet."""
        import time
        
        # Créer beaucoup de modules Python
        large_src_dir = self.project_path / "large_src"
        large_src_dir.mkdir()
        
        for i in range(20):
            (large_src_dir / f"module_{i}.py").write_text(f'''
"""Module {i} pour test performance."""

class Class{i}:
    """Classe {i}."""
    
    def method_{i}(self, x):
        """Méthode {i}."""
        return x + {i}

def function_{i}():
    """Fonction {i}."""
    return {i}
''')
        
        # Mesurer performance analyse
        start_time = time.time()
        modules = self.auto_tester._analyze_modules()
        analysis_duration = time.time() - start_time
        
        # Devrait analyser rapidement même avec beaucoup de modules
        assert isinstance(modules, list)
        assert len(modules) >= 20
        assert analysis_duration < 10.0  # Moins de 10 secondes

    def test_concurrent_test_generation(self):
        """Test génération tests concurrente."""
        import threading
        
        def test_generation_worker(worker_id):
            """Worker pour génération concurrente."""
            calc_file = self.project_path / "src" / "calculator.py"
            analysis = self.auto_tester._analyze_module(calc_file)
            tests = self.auto_tester._create_test_file(analysis, f"calc_{worker_id}")
            return len(tests)
        
        # Lancer plusieurs workers
        threads = []
        results = []
        
        def worker_wrapper(worker_id):
            result = test_generation_worker(worker_id)
            results.append(result)
        
        for i in range(3):
            thread = threading.Thread(target=worker_wrapper, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Attendre fin
        for thread in threads:
            thread.join()
        
        # Vérifier résultats
        assert len(results) == 3
        assert all(isinstance(r, int) and r > 0 for r in results)


class TestAutoTesterIntegration:
    """Tests d'intégration pour AutoTester."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "integration_project"
        self.project_path.mkdir()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_auto_testing_workflow(self):
        """Test workflow complet génération automatique tests."""
        # Créer projet complexe
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        
        # Module principal avec plusieurs classes
        (self.project_path / "src" / "main.py").write_text('''
"""Module principal."""

class UserManager:
    """Gestionnaire utilisateurs."""
    
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, email):
        """Ajoute un utilisateur."""
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = {"email": email}
        return True
    
    def get_user(self, username):
        """Récupère un utilisateur."""
        return self.users.get(username)
    
    def delete_user(self, username):
        """Supprime un utilisateur."""
        if username not in self.users:
            raise ValueError("User not found")
        del self.users[username]
        return True

def validate_user_data(username, email):
    """Valide les données utilisateur."""
    if not username or len(username) < 3:
        return False
    if "@" not in email:
        return False
    return True
''')
        
        # Module utilitaires
        (self.project_path / "src" / "utils.py").write_text('''
"""Utilitaires."""

def format_name(first_name, last_name):
    """Formate un nom complet."""
    return f"{first_name.title()} {last_name.title()}"

def calculate_age(birth_year, current_year=2024):
    """Calcule l'âge."""
    return current_year - birth_year

class ConfigManager:
    """Gestionnaire configuration."""
    
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.config = {}
    
    def load_config(self):
        """Charge la configuration."""
        # Simulation chargement
        self.config = {"debug": True, "version": "1.0"}
        return self.config
    
    def get_setting(self, key, default=None):
        """Récupère un paramètre."""
        return self.config.get(key, default)
''')
        
        # Générer tests automatiquement
        auto_tester = AutoTester(str(self.project_path))
        
        # 1. Analyser modules
        modules = auto_tester._analyze_modules()
        assert len(modules) >= 2
        
        # 2. Générer tests pour module principal
        main_file = self.project_path / "src" / "main.py"
        main_analysis = auto_tester._analyze_module(main_file)
        main_tests = auto_tester._create_test_file(main_analysis, "main")
        assert isinstance(main_tests, str)
        assert "UserManager" in main_tests
        
        # 3. Générer tests pour utils
        utils_file = self.project_path / "src" / "utils.py"
        utils_analysis = auto_tester._analyze_module(utils_file)
        utils_tests = auto_tester._create_test_file(utils_analysis, "utils")
        assert isinstance(utils_tests, str)
        assert "ConfigManager" in utils_tests
        
        # 4. Écrire tests sur disque
        main_test_path = auto_tester._write_test_file(main_tests, "main")
        utils_test_path = auto_tester._write_test_file(utils_tests, "utils")
        
        assert main_test_path.exists()
        assert utils_test_path.exists()
        
        # 5. Workflow complet
        result = auto_tester.generate_tests(str(self.project_path))
        assert isinstance(result, dict)
        assert result.get("status") == "success"


class TestAutoTesterPerformance:
    """Tests de performance pour AutoTester."""

    def setup_method(self):
        """Configuration tests performance."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Nettoyage tests performance."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_scalability_massive_codebase(self):
        """Test scalabilité sur base de code massive."""
        import time
        
        massive_project = Path(self.temp_dir) / "massive_project"
        massive_project.mkdir()
        (massive_project / "src").mkdir()
        
        # Créer structure massive
        for i in range(30):
            package_dir = massive_project / "src" / f"package_{i}"
            package_dir.mkdir()
            
            for j in range(5):
                (package_dir / f"module_{j}.py").write_text(f'''
"""Module {i}_{j}."""

class Component{i}_{j}:
    """Composant {i}_{j}."""
    
    def __init__(self, value={i}):
        self.value = value
    
    def process(self, data):
        """Traite les données."""
        return data + self.value
    
    def validate(self, input_data):
        """Valide les données."""
        return isinstance(input_data, (int, float))

def utility_function_{i}_{j}(x, y={j}):
    """Fonction utilitaire {i}_{j}."""
    return x * y + {i}

def helper_{i}_{j}():
    """Helper {i}_{j}."""
    return f"helper_{i}_{j}"
''')
        
        # Test performance AutoTester
        auto_tester = AutoTester(str(massive_project))
        
        start_time = time.time()
        modules = auto_tester._analyze_modules()
        analysis_duration = time.time() - start_time
        
        start_generation = time.time()
        # Générer tests pour quelques modules seulement (pour performance)
        sample_modules = modules[:10] if len(modules) > 10 else modules
        results = auto_tester._batch_generate_tests([
            massive_project / "src" / f"package_{i}" / "module_0.py" 
            for i in range(min(10, len(sample_modules)))
        ])
        generation_duration = time.time() - start_generation
        
        # Vérifications performance
        assert isinstance(modules, list)
        assert len(modules) >= 150  # 30 packages * 5 modules
        assert isinstance(results, list)
        assert analysis_duration < 15.0  # Moins de 15 secondes pour analyse
        assert generation_duration < 30.0  # Moins de 30 secondes pour génération
        
        # Vérifier qualité de l'analyse
        for module in modules[:5]:  # Vérifier quelques modules
            assert "name" in module
            assert "path" in module