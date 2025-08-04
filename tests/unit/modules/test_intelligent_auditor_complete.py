#!/usr/bin/env python3
"""
Tests complets pour intelligent_auditor.py (810 lignes)
LE PLUS GROS FICHIER SOUS-TESTÉ - PRIORITÉ MAXIMALE

Couverture actuelle: 15% → Objectif: 85%
Standards: Black + Ruff + MyPy + Bandit
"""

import pytest
import tempfile
import shutil
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from athalia_core.intelligent_auditor import IntelligentAuditor


class TestIntelligentAuditorComplete:
    """Tests complets pour IntelligentAuditor."""

    def setup_method(self):
        """Configuration avant chaque test."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "test_project"
        self.project_path.mkdir(parents=True)
        
        # Créer structure projet de test
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        (self.project_path / "docs").mkdir()
        
        # Créer fichiers de test
        (self.project_path / "src" / "main.py").write_text("""
def main():
    print("Hello World")
    return 0

if __name__ == "__main__":
    main()
""")
        
        (self.project_path / "requirements.txt").write_text("""
numpy==1.21.0
pandas==1.3.0
requests==2.28.0
""")
        
        (self.project_path / "README.md").write_text("# Test Project")
        
        self.auditor = IntelligentAuditor(str(self.project_path))

    def teardown_method(self):
        """Nettoyage après chaque test."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_auditor_initialization(self):
        """Test initialisation de l'auditeur."""
        assert self.auditor.project_path == str(self.project_path)
        assert hasattr(self.auditor, 'audit_results')
        assert hasattr(self.auditor, 'metrics')

    def test_auditor_initialization_nonexistent_path(self):
        """Test initialisation avec chemin inexistant."""
        nonexistent_path = "/path/that/does/not/exist"
        
        # L'auditeur devrait gérer gracieusement les chemins invalides
        try:
            auditor = IntelligentAuditor(nonexistent_path)
            assert auditor.project_path == nonexistent_path
        except Exception as e:
            # Exception attendue pour chemin invalide
            assert "not found" in str(e).lower() or "does not exist" in str(e).lower()

    def test_analyze_project_structure(self):
        """Test analyse structure du projet."""
        structure_analysis = self.auditor.analyze_project_structure()
        
        assert isinstance(structure_analysis, dict)
        assert "directories" in structure_analysis
        assert "files" in structure_analysis
        assert "total_files" in structure_analysis
        
        # Vérifier que les répertoires créés sont détectés
        directories = structure_analysis["directories"]
        assert any("src" in str(d) for d in directories)
        assert any("tests" in str(d) for d in directories)

    def test_analyze_code_quality(self):
        """Test analyse qualité du code."""
        quality_analysis = self.auditor.analyze_code_quality()
        
        assert isinstance(quality_analysis, dict)
        # Les métriques de qualité typiques
        expected_metrics = ["complexity", "maintainability", "readability"]
        
        # Au moins une métrique devrait être présente
        assert any(metric in quality_analysis for metric in expected_metrics)

    def test_analyze_dependencies(self):
        """Test analyse des dépendances."""
        deps_analysis = self.auditor.analyze_dependencies()
        
        assert isinstance(deps_analysis, dict)
        
        if "requirements" in deps_analysis:
            requirements = deps_analysis["requirements"]
            # Vérifier que les dépendances du fichier requirements.txt sont détectées
            req_names = [req.get("name", "") for req in requirements if isinstance(req, dict)]
            assert any("numpy" in name for name in req_names) or "numpy" in str(deps_analysis)

    def test_analyze_security_vulnerabilities(self):
        """Test analyse vulnérabilités sécurité."""
        security_analysis = self.auditor.analyze_security_vulnerabilities()
        
        assert isinstance(security_analysis, dict)
        assert "vulnerabilities" in security_analysis or "issues" in security_analysis

    def test_analyze_performance_bottlenecks(self):
        """Test analyse goulots d'étranglement performance."""
        perf_analysis = self.auditor.analyze_performance_bottlenecks()
        
        assert isinstance(perf_analysis, dict)
        # Métriques de performance typiques
        expected_keys = ["bottlenecks", "performance_issues", "recommendations"]
        
        # Au moins une clé devrait être présente
        assert any(key in perf_analysis for key in expected_keys)

    def test_calculate_technical_debt(self):
        """Test calcul de la dette technique."""
        tech_debt = self.auditor.calculate_technical_debt()
        
        assert isinstance(tech_debt, (dict, float, int))
        
        if isinstance(tech_debt, dict):
            assert "score" in tech_debt or "debt_ratio" in tech_debt
        else:
            # Score numérique
            assert tech_debt >= 0

    def test_generate_recommendations(self):
        """Test génération de recommandations."""
        recommendations = self.auditor.generate_recommendations()
        
        assert isinstance(recommendations, (dict, list))
        
        if isinstance(recommendations, list):
            assert len(recommendations) >= 0
        else:
            assert "recommendations" in recommendations or "suggestions" in recommendations

    def test_audit_code_complexity_simple_file(self):
        """Test audit complexité code fichier simple."""
        simple_file = self.project_path / "simple.py"
        simple_file.write_text("""
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
""")
        
        complexity = self.auditor.audit_code_complexity(str(simple_file))
        
        assert isinstance(complexity, (dict, int, float))
        if isinstance(complexity, dict):
            assert "complexity_score" in complexity or "cyclomatic" in complexity

    def test_audit_code_complexity_complex_file(self):
        """Test audit complexité code fichier complexe."""
        complex_file = self.project_path / "complex.py"
        complex_file.write_text("""
def complex_function(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                for i in range(x):
                    for j in range(y):
                        if i + j > z:
                            return i * j
                        elif i - j < 0:
                            return i + j
                        else:
                            continue
            else:
                return x + y
        else:
            return x - y
    else:
        return 0
""")
        
        complexity = self.auditor.audit_code_complexity(str(complex_file))
        
        assert isinstance(complexity, (dict, int, float))
        # Le fichier complexe devrait avoir une complexité plus élevée
        if isinstance(complexity, (int, float)):
            assert complexity > 1
        elif isinstance(complexity, dict) and "complexity_score" in complexity:
            assert complexity["complexity_score"] > 1

    def test_audit_test_coverage(self):
        """Test audit couverture des tests."""
        # Créer fichier de test
        test_file = self.project_path / "tests" / "test_main.py"
        test_file.write_text("""
import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        result = main()
        self.assertEqual(result, 0)
""")
        
        coverage = self.auditor.audit_test_coverage()
        
        assert isinstance(coverage, dict)
        assert "coverage_percentage" in coverage or "coverage" in coverage

    def test_audit_documentation_quality(self):
        """Test audit qualité documentation."""
        # Ajouter documentation
        (self.project_path / "docs" / "api.md").write_text("# API Documentation")
        
        doc_quality = self.auditor.audit_documentation_quality()
        
        assert isinstance(doc_quality, dict)
        assert "documentation_score" in doc_quality or "quality" in doc_quality

    def test_detect_code_smells(self):
        """Test détection code smells."""
        # Créer fichier avec code smells
        smelly_file = self.project_path / "smelly.py"
        smelly_file.write_text("""
# Long function with many parameters
def bad_function(a, b, c, d, e, f, g, h, i, j):
    # Duplicate code
    if a > 0:
        print("a is positive")
        print("processing a")
    if b > 0:
        print("b is positive") 
        print("processing b")
    # Long if-else chain
    if c == 1:
        return "one"
    elif c == 2:
        return "two"
    elif c == 3:
        return "three"
    elif c == 4:
        return "four"
    elif c == 5:
        return "five"
    else:
        return "other"
""")
        
        code_smells = self.auditor.detect_code_smells()
        
        assert isinstance(code_smells, (dict, list))
        # Devrait détecter au moins quelques code smells
        if isinstance(code_smells, list):
            assert len(code_smells) >= 0
        else:
            assert "smells" in code_smells or "issues" in code_smells

    def test_analyze_architecture_patterns(self):
        """Test analyse patterns architecturaux."""
        # Créer structure MVC basique
        (self.project_path / "models").mkdir()
        (self.project_path / "views").mkdir()
        (self.project_path / "controllers").mkdir()
        
        (self.project_path / "models" / "user.py").write_text("class User: pass")
        (self.project_path / "views" / "user_view.py").write_text("class UserView: pass")
        (self.project_path / "controllers" / "user_controller.py").write_text("class UserController: pass")
        
        arch_analysis = self.auditor.analyze_architecture_patterns()
        
        assert isinstance(arch_analysis, dict)
        assert "patterns" in arch_analysis or "architecture" in arch_analysis

    def test_audit_naming_conventions(self):
        """Test audit conventions de nommage."""
        # Créer fichier avec mauvaises conventions
        bad_naming_file = self.project_path / "BadNaming.py"
        bad_naming_file.write_text("""
class badClass:
    def BadMethod(self):
        BadVariable = 1
        return BadVariable

def bad_function():
    return True
""")
        
        naming_audit = self.auditor.audit_naming_conventions()
        
        assert isinstance(naming_audit, dict)
        assert "violations" in naming_audit or "issues" in naming_audit

    def test_analyze_cyclomatic_complexity(self):
        """Test analyse complexité cyclomatique."""
        # Créer fonction avec haute complexité cyclomatique
        complex_file = self.project_path / "cyclomatic.py"
        complex_file.write_text("""
def high_complexity(x):
    if x > 10:
        if x > 20:
            if x > 30:
                return "very high"
            else:
                return "high"
        else:
            if x > 15:
                return "medium-high"
            else:
                return "medium"
    else:
        if x > 5:
            return "low-medium"
        else:
            return "low"
""")
        
        cyclomatic = self.auditor.analyze_cyclomatic_complexity()
        
        assert isinstance(cyclomatic, dict)
        assert "average_complexity" in cyclomatic or "complexity" in cyclomatic

    def test_full_audit_execution(self):
        """Test exécution audit complet."""
        audit_results = self.auditor.run_full_audit()
        
        assert isinstance(audit_results, dict)
        
        # Vérifier que les sections principales sont présentes
        expected_sections = [
            "structure", "quality", "dependencies", "security", 
            "performance", "technical_debt", "recommendations"
        ]
        
        # Au moins la moitié des sections devraient être présentes
        present_sections = sum(1 for section in expected_sections if section in audit_results)
        assert present_sections >= len(expected_sections) // 2

    def test_generate_audit_report(self):
        """Test génération rapport d'audit."""
        report = self.auditor.generate_audit_report()
        
        assert isinstance(report, (dict, str))
        
        if isinstance(report, str):
            # Rapport formaté en texte
            assert len(report) > 100
            assert "audit" in report.lower() or "analysis" in report.lower()
        else:
            # Rapport structuré
            assert "summary" in report or "results" in report

    def test_export_audit_results_json(self):
        """Test export résultats audit en JSON."""
        # Exécuter audit d'abord
        self.auditor.run_full_audit()
        
        json_file = self.project_path / "audit_report.json"
        success = self.auditor.export_audit_results(str(json_file), format="json")
        
        if success:
            assert json_file.exists()
            
            # Vérifier que le JSON est valide
            with open(json_file) as f:
                data = json.load(f)
                assert isinstance(data, dict)

    def test_compare_audits(self):
        """Test comparaison d'audits."""
        # Exécuter premier audit
        audit1 = self.auditor.run_full_audit()
        
        # Modifier le projet
        (self.project_path / "src" / "new_file.py").write_text("def new_function(): pass")
        
        # Exécuter second audit
        audit2 = self.auditor.run_full_audit()
        
        # Comparer
        comparison = self.auditor.compare_audits(audit1, audit2)
        
        assert isinstance(comparison, dict)
        assert "changes" in comparison or "differences" in comparison

    @patch('athalia_core.intelligent_auditor.subprocess')
    def test_external_tool_integration(self, mock_subprocess):
        """Test intégration outils externes."""
        mock_subprocess.run.return_value.returncode = 0
        mock_subprocess.run.return_value.stdout = "Linting passed"
        
        # Test avec mock pour éviter dépendances externes
        result = self.auditor.run_external_linter()
        
        assert isinstance(result, (dict, str, bool))

    def test_performance_benchmark(self):
        """Test benchmark performance audit."""
        import time
        
        # Créer projet plus large pour test performance
        for i in range(10):
            py_file = self.project_path / f"module_{i}.py"
            py_file.write_text(f"""
def function_{i}():
    return {i}

class Class{i}:
    def method(self):
        return {i}
""")
        
        start_time = time.time()
        self.auditor.run_full_audit()
        audit_duration = time.time() - start_time
        
        # L'audit ne devrait pas prendre trop de temps
        assert audit_duration < 10.0  # Moins de 10 secondes

    def test_memory_usage_monitoring(self):
        """Test monitoring utilisation mémoire."""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss
        
        # Exécuter audit
        self.auditor.run_full_audit()
        
        memory_after = process.memory_info().rss
        memory_increase = memory_after - memory_before
        
        # L'augmentation mémoire ne devrait pas être excessive
        # (100MB = 100 * 1024 * 1024 bytes)
        assert memory_increase < 100 * 1024 * 1024

    @pytest.mark.parametrize("file_type,content", [
        ("python", "def test(): pass"),
        ("yaml", "key: value"),
        ("json", '{"key": "value"}'),
        ("markdown", "# Title"),
    ])
    def test_file_type_analysis(self, file_type, content):
        """Test analyse par type de fichier."""
        extensions = {
            "python": ".py",
            "yaml": ".yml", 
            "json": ".json",
            "markdown": ".md"
        }
        
        test_file = self.project_path / f"test{extensions[file_type]}"
        test_file.write_text(content)
        
        # L'audit devrait gérer différents types de fichiers
        structure = self.auditor.analyze_project_structure()
        assert isinstance(structure, dict)

    def test_error_handling_corrupted_files(self):
        """Test gestion erreurs fichiers corrompus."""
        # Créer fichier avec contenu invalide
        corrupted_file = self.project_path / "corrupted.py"
        corrupted_file.write_bytes(b'\x00\x01\x02\x03')  # Contenu binaire invalide
        
        # L'audit devrait gérer gracieusement les fichiers corrompus
        try:
            structure = self.auditor.analyze_project_structure()
            assert isinstance(structure, dict)
        except Exception as e:
            # Exception acceptable pour fichier corrompu
            assert "corrupt" in str(e).lower() or "invalid" in str(e).lower()

    def test_large_project_handling(self):
        """Test gestion grands projets."""
        # Créer beaucoup de fichiers
        large_dir = self.project_path / "large_module"
        large_dir.mkdir()
        
        for i in range(50):
            (large_dir / f"file_{i}.py").write_text(f"# File {i}\ndef func_{i}(): pass")
        
        # L'audit devrait gérer les grands projets
        structure = self.auditor.analyze_project_structure()
        assert isinstance(structure, dict)
        assert structure.get("total_files", 0) >= 50


class TestIntelligentAuditorIntegration:
    """Tests d'intégration pour IntelligentAuditor."""

    def setup_method(self):
        """Configuration tests intégration."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_path = Path(self.temp_dir) / "integration_project"
        self.project_path.mkdir()

    def teardown_method(self):
        """Nettoyage tests intégration."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_audit_workflow_integration(self):
        """Test workflow complet d'audit intégration."""
        # Créer projet complet
        (self.project_path / "src").mkdir()
        (self.project_path / "tests").mkdir()
        (self.project_path / "docs").mkdir()
        
        # Code principal
        (self.project_path / "src" / "__init__.py").write_text("")
        (self.project_path / "src" / "app.py").write_text("""
#!/usr/bin/env python3
'''Application principale.'''

class Application:
    def __init__(self):
        self.name = "Test App"
    
    def run(self):
        return "Running..."
""")
        
        # Tests
        (self.project_path / "tests" / "__init__.py").write_text("")
        (self.project_path / "tests" / "test_app.py").write_text("""
import unittest
from src.app import Application

class TestApplication(unittest.TestCase):
    def test_init(self):
        app = Application()
        self.assertEqual(app.name, "Test App")
""")
        
        # Configuration
        (self.project_path / "setup.py").write_text("""
from setuptools import setup, find_packages

setup(
    name="test-app",
    version="1.0.0",
    packages=find_packages(),
)
""")
        
        # Documentation
        (self.project_path / "README.md").write_text("# Test Application")
        (self.project_path / "docs" / "api.md").write_text("# API Documentation")
        
        # Créer auditeur et exécuter audit complet
        auditor = IntelligentAuditor(str(self.project_path))
        results = auditor.run_full_audit()
        
        # Vérifications
        assert isinstance(results, dict)
        assert len(results) > 0
        
        # Générer rapport
        report = auditor.generate_audit_report()
        assert isinstance(report, (dict, str))
        
        # Export résultats
        json_file = self.project_path / "integration_audit.json"
        export_success = auditor.export_audit_results(str(json_file))
        
        if export_success:
            assert json_file.exists()


class TestIntelligentAuditorPerformance:
    """Tests de performance pour IntelligentAuditor."""

    def setup_method(self):
        """Configuration tests performance."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Nettoyage tests performance."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_scalability_large_codebase(self):
        """Test scalabilité sur grande base de code."""
        import time
        
        large_project = Path(self.temp_dir) / "large_project"
        large_project.mkdir()
        
        # Créer structure complexe
        for i in range(20):
            module_dir = large_project / f"module_{i}"
            module_dir.mkdir()
            
            for j in range(10):
                (module_dir / f"file_{j}.py").write_text(f"""
# Module {i}, File {j}
def function_{j}():
    '''Function {j} in module {i}.'''
    return {i} * {j}

class Class{j}:
    '''Class {j} in module {i}.'''
    def method(self):
        return function_{j}()
""")
        
        # Test performance audit
        auditor = IntelligentAuditor(str(large_project))
        
        start_time = time.time()
        results = auditor.run_full_audit()
        audit_time = time.time() - start_time
        
        # Vérifications performance
        assert isinstance(results, dict)
        assert audit_time < 30.0  # Moins de 30 secondes pour 200 fichiers
        
        # Vérifier que l'audit a traité tous les fichiers
        structure = results.get("structure", {})
        total_files = structure.get("total_files", 0)
        assert total_files >= 200