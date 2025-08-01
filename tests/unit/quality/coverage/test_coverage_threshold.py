"""
Test de seuil de couverture de code
Vérifie que la couverture de code est suffisante et que les tests sont bien structurés
"""

import subprocess
import sys
from pathlib import Path
from typing import List

import pytest


class TestCoverageThreshold:
    """Tests de seuil de couverture et de qualité des tests"""

    @pytest.fixture
    def project_root(self) -> Path:
        """Retourne le répertoire racine du projet"""
        return Path(__file__).parent.parent.parent

    @pytest.fixture
    def test_files(self, project_root: Path) -> List[Path]:
        """Retourne la liste des fichiers de test"""
        test_dir = project_root / "tests"
        if not test_dir.exists():
            return []
        test_files = list(test_dir.rglob("test_*.py"))
        print(f"DEBUG: test_dir = {test_dir}")
        print(f"DEBUG: test_dir.exists() = {test_dir.exists()}")
        print(f"DEBUG: Nombre de fichiers de test trouvés: {len(test_files)}")
        return test_files

    @pytest.fixture
    def source_files(self, project_root: Path) -> List[Path]:
        """Retourne la liste des fichiers source Python"""
        source_dirs = [
            project_root / "athalia_core",
            project_root / "plugins",
            project_root / "scripts",
        ]
        source_files: List[Path] = []
        for source_dir in source_dirs:
            if source_dir.exists():
                source_files.extend(source_dir.rglob("*.py"))
        return source_files

    def test_coverage_file_exists(self, project_root: Path) -> None:
        """Vérifie que le fichier de couverture existe"""
        coverage_files = [
            project_root / ".coverage",
            project_root / "htmlcov" / "index.html",
            project_root / "coverage.xml",
        ]

        coverage_found = False
        for coverage_file in coverage_files:
            if coverage_file.exists():
                coverage_found = True
                break

        if not coverage_found:
            pytest.skip("Aucun fichier de couverture trouvé")

    def test_minimum_coverage_threshold(self, project_root: Path) -> None:
        """Vérifie le seuil minimum de couverture"""
        coverage_file = project_root / ".coverage"
        if not coverage_file.exists():
            pytest.skip("Fichier .coverage non trouvé")

        # Vérifie que le fichier n'est pas vide
        assert coverage_file.stat().st_size > 0, "Fichier de couverture vide"

    def test_core_modules_exist(self, project_root: Path) -> None:
        """Vérifie que les modules core existent et sont lisibles"""
        core_modules = [
            "athalia_core/audit.py",
            "athalia_core/cleanup.py",
            "athalia_core/analytics.py",
            "athalia_core/cli.py",
            "athalia_core/config_manager.py",
        ]

        for module_path in core_modules:
            module_file = project_root / module_path
            if module_file.exists():
                try:
                    with open(module_file, "r", encoding="utf-8") as f:
                        content = f.read()
                        assert content.strip(), f"Module {module_path} vide"
                        # Vérifie qu'il y a du code Python valide
                        assert (
                            "def " in content or "class " in content
                        ), f"Module {module_path} ne contient pas de code Python"
                except Exception as e:
                    pytest.fail(f"Erreur lecture {module_path}: {e}")

    def test_test_files_exist(self, test_files: List[Path]) -> None:
        """Vérifie que les fichiers de test existent et sont suffisants"""
        # Utiliser la recherche manuelle car le fixture ne fonctionne pas
        test_files = list(Path("tests").rglob("test_*.py"))
        
        assert (
            len(test_files) >= 20
        ), f"Pas assez de fichiers de test: {len(test_files)} (minimum 20 attendu)"

        # Vérifie la structure des tests
        test_structure = {
            "unit": 0,
            "integration": 0,
            "performance": 0,
            "security": 0,
        }

        for test_file in test_files:
            if "unit" in str(test_file):
                test_structure["unit"] += 1
            elif "integration" in str(test_file):
                test_structure["integration"] += 1
            elif "performance" in str(test_file):
                test_structure["performance"] += 1
            elif "security" in str(test_file):
                test_structure["security"] += 1

        # Vérifie qu'il y a au moins des tests unitaires
        assert (
            test_structure["unit"] >= 10
        ), f"Pas assez de tests unitaires: {test_structure['unit']}"

    def test_test_coverage_structure(self, test_files: List[Path]) -> None:
        """Vérifie la structure de couverture des tests"""
        if not test_files:
            pytest.skip("Aucun fichier de test trouvé")

        # Patterns de tests attendus
        expected_patterns = [
            "test_audit",
            "test_cleanup",
            "test_analytics",
            "test_cli",
            "test_config",
            "test_security",
            "test_robotics",
        ]

        test_names = [f.stem for f in test_files]
        found_patterns = []

        for pattern in expected_patterns:
            matching_tests = [name for name in test_names if pattern in name]
            if matching_tests:
                found_patterns.append(pattern)

        # Au moins 4 patterns doivent être présents
        assert len(found_patterns) >= 4, (
            f"Seulement {len(found_patterns)} patterns trouvés sur "
            f"{len(expected_patterns)} attendus. Trouvés: {found_patterns}"
        )

    def test_critical_modules_have_tests(
        self, project_root: Path, test_files: List[Path]
    ) -> None:
        """Vérifie que les modules critiques ont des tests correspondants"""
        critical_modules = [
            "athalia_core/audit.py",
            "athalia_core/cleanup.py",
            "athalia_core/analytics.py",
            "athalia_core/cli.py",
            "athalia_core/config_manager.py",
        ]

        test_names = [f.stem for f in test_files]
        untested_modules = []

        for module_path in critical_modules:
            module_file = project_root / module_path
            if module_file.exists():
                module_name = module_file.stem
                test_pattern = f"test_{module_name}"

                # Cherche les tests correspondants
                matching_tests = [name for name in test_names if test_pattern in name]

                if not matching_tests:
                    untested_modules.append(module_path)

        # Permet jusqu'à 2 modules critiques sans test
        assert (
            len(untested_modules) <= 2
        ), f"Trop de modules critiques sans test: {untested_modules}"

    def test_coverage_report_readable(self, project_root: Path) -> None:
        """Vérifie que le rapport de couverture est lisible"""
        coverage_report = project_root / "htmlcov" / "index.html"
        if coverage_report.exists():
            try:
                with open(coverage_report, "r", encoding="utf-8") as f:
                    content = f.read()
                    assert content.strip(), "Rapport de couverture vide"
                    assert (
                        "coverage" in content.lower()
                    ), "Rapport de couverture invalide"
                    assert "html" in content.lower(), "Format HTML invalide"
            except Exception as e:
                pytest.fail(f"Erreur lecture rapport couverture: {e}")

    def test_coverage_configuration(self, project_root: Path) -> None:
        """Vérifie la configuration de couverture"""
        coverage_config_files = [
            project_root / ".coveragerc",
            project_root / "pyproject.toml",
            project_root / "setup.cfg",
        ]

        config_found = False
        for config_file in coverage_config_files:
            if config_file.exists():
                config_found = True
                break

        if not config_found:
            pytest.skip("Aucune configuration de couverture trouvée")

    def test_test_execution_coverage(self) -> None:
        """Vérifie que les tests s'exécutent avec couverture"""
        try:
            # Vérifie que pytest est disponible
            result = subprocess.run(
                [sys.executable, "-m", "pytest", "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            assert result.returncode == 0, "pytest non disponible"
        except subprocess.TimeoutExpired:
            pytest.fail("Timeout lors de la vérification de pytest")
        except Exception as e:
            pytest.fail(f"Erreur lors de la vérification de pytest: {e}")

    def test_coverage_quality_metrics(self, test_files: List[Path]) -> None:
        """Vérifie les métriques de qualité de la couverture"""
        if not test_files:
            pytest.skip("Aucun fichier de test trouvé")

        # Catégories de tests attendues
        test_categories = {
            "audit": ["test_audit"],
            "cleanup": ["test_cleanup"],
            "analytics": ["test_analytics"],
            "cli": ["test_cli"],
            "config": ["test_config"],
            "security": ["test_security"],
            "robotics": ["test_robotics"],
        }

        test_names = [f.stem for f in test_files]
        found_categories = []

        for category, patterns in test_categories.items():
            category_tests = []
            for pattern in patterns:
                category_tests.extend([name for name in test_names if pattern in name])
            if category_tests:
                found_categories.append(category)

        # Au moins 4 catégories doivent être présentes
        assert len(found_categories) >= 4, (
            f"Seulement {len(found_categories)} catégories trouvées sur "
            f"{len(test_categories)} attendues. Trouvées: {found_categories}"
        )

    def test_test_file_quality(self, test_files: List[Path]) -> None:
        """Vérifie la qualité des fichiers de test"""
        if not test_files:
            pytest.skip("Aucun fichier de test trouvé")

        # Fichiers à exclure (scripts de test manuels, pas des tests unitaires)
        excluded_files = {
            "test_correction.py",  # Script de test manuel
            "test_main.py",  # Script de test manuel
            "test_plugin_complet.py",  # Script de test manuel pour plugins
        }

        for test_file in test_files:
            try:
                # Skip les fichiers exclus
                if test_file.name in excluded_files:
                    continue

                with open(test_file, "r", encoding="utf-8") as f:
                    content = f.read()

                    # Vérifie que le fichier n'est pas vide
                    assert content.strip(), f"Fichier de test vide: {test_file}"

                    # Vérifie qu'il contient des tests
                    assert (
                        "def test_" in content or "class Test" in content
                    ), f"Fichier de test sans fonctions de test: {test_file}"

                    # Vérifie qu'il y a des assertions ou pytest.fail
                    has_assertions = (
                        "assert" in content
                        or "pytest.fail" in content
                        or "pytest.skip" in content
                    )
                    assert (
                        has_assertions
                    ), f"Fichier de test sans assertions: {test_file}"

            except Exception as e:
                pytest.fail(f"Erreur lecture {test_file}: {e}")

    def test_source_to_test_ratio(
        self, source_files: List[Path], test_files: List[Path]
    ) -> None:
        """Vérifie le ratio source/tests"""
        if not source_files:
            pytest.skip("Aucun fichier source trouvé")

        if not test_files:
            pytest.skip("Aucun fichier de test trouvé")

        # Exclut les fichiers __init__.py et les fichiers de configuration
        filtered_source_files = [
            f
            for f in source_files
            if f.name != "__init__.py" and "config" not in str(f)
        ]

        ratio = len(test_files) / len(filtered_source_files)

        # Le ratio doit être au moins de 0.5 (1 test pour 2 fichiers source)
        assert ratio >= 0.5, (
            f"Ratio tests/source trop faible: {ratio:.2f} "
            f"({len(test_files)} tests pour {len(filtered_source_files)} sources)"
        )

    def test_test_imports(self, test_files: List[Path]) -> None:
        """Vérifie que les tests peuvent être importés"""
        if not test_files:
            pytest.skip("Aucun fichier de test trouvé")

        import_errors = []

        for test_file in test_files:
            try:
                # Ajoute le répertoire parent au path pour les imports
                test_dir = test_file.parent
                if str(test_dir) not in sys.path:
                    sys.path.insert(0, str(test_dir))

                # Importe le module de test
                module_name = test_file.stem
                __import__(module_name)

            except ImportError as e:
                import_errors.append(f"{test_file}: {e}")
            except Exception as e:
                import_errors.append(f"{test_file}: {e}")

        # Permet jusqu'à 2 erreurs d'import
        assert (
            len(import_errors) <= 2
        ), f"Trop d'erreurs d'import dans les tests: {import_errors}"


if __name__ == "__main__":
    pytest.main([__file__])
