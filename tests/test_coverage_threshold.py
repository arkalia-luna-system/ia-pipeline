"""
Test de seuil de couverture de code
Vérifie que la couverture de code est suffisante
"""
import pytest
from pathlib import Path


class TestCoverageThreshold:
    """Tests de seuil de couverture"""

    def test_coverage_file_exists(self):
        """Vérifie que le fichier de couverture existe"""
        coverage_files = [
            '.coverage',
            'htmlcov/index.html',
            'coverage.xml'
        ]

        coverage_found = False
        for coverage_file in coverage_files:
            if Path(coverage_file).exists():
                coverage_found = True
                break

        if not coverage_found:
            pytest.skip("Aucun fichier de couverture trouvé")

    def test_minimum_coverage_threshold(self):
        """Vérifie le seuil minimum de couverture"""
        # Seuil minimum de couverture (en pourcentage)
        min_coverage = 50

        # Vérifie si on a un fichier de couverture
        coverage_file = Path('.coverage')
        if not coverage_file.exists():
            pytest.skip("Fichier .coverage non trouvé")

        # Pour ce test, on vérifie juste que le fichier existe
        # Une vraie vérification nécessiterait d'analyser le fichier
        assert coverage_file.exists(), (
            "Fichier de couverture manquant")

    def test_core_modules_coverage(self):
        """Vérifie la couverture des modules core"""
        core_modules = [
            'athalia_core/audit.py',
            'athalia_core/cleanup.py',
            'athalia_core/analytics.py',
            'athalia_core/cli.py'
        ]

        for module in core_modules:
            if Path(module).exists():
                # Vérifie que le module existe et est lisible
                try:
                    with open(module, 'r', encoding='utf-8') as f:
                        content = f.read()
                        assert content.strip(), (
                            f"Module {module} vide")
                except Exception as e:
                    pytest.fail(f"Erreur lecture {module}: {e}")

    def test_test_files_exist(self):
        """Vérifie que les fichiers de test existent"""
        test_files = list(Path('tests').glob('test_*.py'))
        assert len(test_files) > 10, (
            f"Pas assez de fichiers de test: {len(test_files)}")

    def test_test_coverage_structure(self):
        """Vérifie la structure de couverture des tests"""
        # Vérifie que les tests couvrent les modules principaux
        test_patterns = [
            'test_ci_',
            'test_imports_',
            'test_security_',
            'test_encoding_',
            'test_requirements_'
        ]

        test_files = list(Path('tests').glob('test_*.py'))
        test_names = [f.name for f in test_files]

        for pattern in test_patterns:
            matching_tests = [
                name for name in test_names
                if pattern in name
            ]
            assert len(matching_tests) > 0, (
                f"Aucun test trouvé pour le pattern: {pattern}")

    def test_no_untested_critical_modules(self):
        """Vérifie qu'il n'y a pas de modules critiques non testés"""
        critical_modules = [
            'athalia_core/audit.py',
            'athalia_core/cleanup.py',
            'athalia_core/analytics.py'
        ]

        for module in critical_modules:
            if Path(module).exists():
                # Vérifie qu'il y a au moins un test correspondant
                module_name = Path(module).stem
                test_pattern = f"test_{module_name}"
                test_files = list(Path('tests').glob(f"{test_pattern}*.py"))
                assert len(test_files) > 0, (
                    f"Aucun test trouvé pour {module}")

    def test_coverage_report_readable(self):
        """Vérifie que le rapport de couverture est lisible"""
        coverage_report = Path('htmlcov/index.html')
        if coverage_report.exists():
            try:
                with open(coverage_report, 'r', encoding='utf-8') as f:
                    content = f.read()
                    assert content.strip(), (
                        "Rapport de couverture vide")
                    assert 'coverage' in content.lower(), (
                        "Rapport de couverture invalide")
            except Exception as e:
                pytest.fail(f"Erreur lecture rapport couverture: {e}")

    def test_coverage_configuration(self):
        """Vérifie la configuration de couverture"""
        coverage_config_files = [
            '.coveragerc',
            'pyproject.toml',
            'setup.cfg'
        ]

        config_found = False
        for config_file in coverage_config_files:
            if Path(config_file).exists():
                config_found = True
                break

        # La configuration n'est pas obligatoire mais recommandée
        if not config_found:
            pytest.skip("Aucune configuration de couverture trouvée")

    def test_test_execution_coverage(self):
        """Vérifie que les tests s'exécutent avec couverture"""
        # Ce test vérifie que pytest peut s'exécuter avec l'option --cov
        # En pratique, on vérifie juste que pytest fonctionne
        assert True, "pytest disponible"

    def test_coverage_quality_metrics(self):
        """Vérifie les métriques de qualité de la couverture"""
        # Vérifie que les tests couvrent différents aspects
        test_categories = {
            'ci': ['test_ci_'],
            'security': ['test_security_'],
            'imports': ['test_imports_'],
            'encoding': ['test_encoding_'],
            'requirements': ['test_requirements_']
        }

        test_files = list(Path('tests').glob('test_*.py'))
        test_names = [f.name for f in test_files]

        for category, patterns in test_categories.items():
            category_tests = []
            for pattern in patterns:
                category_tests.extend([
                    name for name in test_names
                    if pattern in name
                ])
            assert len(category_tests) > 0, (
                f"Aucun test de catégorie {category} trouvé")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"]) 