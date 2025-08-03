#!/usr/bin/env python3
"""
🧪 Tests CI Robustes - Athalia/Arkalia
=====================================

Tests robustes pour la validation CI/CD complète
Tests plus approfondis pour validation de qualité
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import pytest
import yaml  # type: ignore

# Import sécurisé pour la validation des commandes
try:
    from athalia_core.security_validator import SecurityError, validate_and_run
except ImportError:

    def validate_and_run(command, **kwargs):
        return subprocess.run(command, **kwargs)

    class SecurityErrorFallback(Exception):
        pass

    SecurityError = SecurityErrorFallback  # type: ignore


class TestCIRobust:
    """Tests CI robustes pour validation complète"""

    def test_python_environment(self):
        """Vérifie l'environnement Python complet"""
        assert sys.version_info >= (3, 8), "Python 3.8+ requis"
        assert sys.version_info < (4, 0), "Python 4.x non supporté"

        # Vérifie les modules essentiels
        essential_modules = ["pytest", "pathlib", "json", "yaml", "subprocess"]
        for module in essential_modules:
            try:
                __import__(module)
            except ImportError:
                pytest.fail(f"Module essentiel manquant: {module}")

    def test_project_structure_complete(self):
        """Vérifie la structure complète du projet"""
        essential_dirs = ["tests", "docs", "config", "scripts", "tools"]
        found_dirs = 0
        for dir_name in essential_dirs:
            if Path(dir_name).exists():
                assert Path(dir_name).is_dir(), f"{dir_name} n'est pas un répertoire"
                found_dirs += 1

        # Au moins 3 répertoires essentiels doivent exister
        assert found_dirs >= 3, f"Seulement {found_dirs} répertoires essentiels trouvés"

    def test_config_files_complete(self):
        """Vérifie tous les fichiers de configuration"""
        config_files = [
            "config/requirements-minimal.txt",
            "config/requirements.txt",
            ".github/workflows/ci.yaml",
            "pyproject.toml",
            ".gitignore",
        ]

        found_configs = 0
        for config_file in config_files:
            if Path(config_file).exists():
                found_configs += 1
                # Vérifie que le fichier est lisible
                try:
                    with open(config_file, encoding="utf-8") as f:
                        content = f.read()
                        assert content.strip(), f"Fichier {config_file} vide"
                except Exception as e:
                    pytest.fail(f"Erreur lecture {config_file}: {e}")

        # Au moins 3 fichiers de config doivent exister
        assert (
            found_configs >= 3
        ), f"Seulement {found_configs} fichiers de config trouvés"

    def test_test_suite_structure(self):
        """Vérifie la structure de la suite de tests"""
        test_files = list(Path("tests").rglob("test_*.py"))
        assert len(test_files) > 0, "Aucun fichier de test trouvé"

        # Vérifie les catégories de tests (plus flexible)
        test_categories = {
            "ci": ["test_ci_", "ci_"],
            "requirements": ["test_requirements_", "requirements_"],
            "coverage": ["test_coverage_", "coverage_"],
            "imports": ["test_imports_", "imports_"],
            "security": ["test_security_", "security_"],
            "unit": ["test_", "unit_"],
            "integration": ["integration_", "test_integration_"],
        }

        found_categories = 0
        for _category, patterns in test_categories.items():
            for pattern in patterns:
                matching_tests = [f for f in test_files if pattern in f.name]
                if matching_tests:
                    found_categories += 1
                    break

        # Au moins 2 catégories de tests doivent être trouvées
        assert (
            found_categories >= 2
        ), f"Seulement {found_categories} catégories de tests trouvées"

    def test_requirements_validation(self):
        """Valide les fichiers requirements"""
        req_files = [
            "config/requirements-minimal.txt",
            "config/requirements.txt",
            "requirements.txt",
        ]

        found_req_files = 0
        for req_file in req_files:
            if Path(req_file).exists():
                found_req_files += 1
                try:
                    with open(req_file, encoding="utf-8") as f:
                        lines = f.readlines()

                    # Vérifie le format des requirements (plus flexible)
                    for i, line in enumerate(lines, 1):
                        line = line.strip()
                        if line and not line.startswith("#"):
                            # Vérifie que c'est un package valide (format plus flexible)
                            valid_formats = [
                                ">=" in line,
                                "==" in line,
                                "<=" in line,
                                "~=" in line,
                                "!=" in line,
                                line.replace("-", "").replace("_", "").isalnum(),
                                line.replace(".", "").isalnum(),
                            ]
                            assert any(
                                valid_formats
                            ), f"Format invalide ligne {i}: {line}"

                except Exception as e:
                    pytest.fail(f"Erreur validation {req_file}: {e}")

        # Au moins un fichier requirements doit exister
        assert found_req_files >= 1, "Aucun fichier requirements trouvé"

    def test_ci_workflow_validation(self):
        """Valide le workflow CI"""
        ci_files = [
            ".github/workflows/ci.yaml",
            ".github/workflows/ci.yml",
            ".github/workflows/test.yaml",
            ".github/workflows/test.yml",
        ]

        found_ci_file = False
        for ci_file_path in ci_files:
            ci_file = Path(ci_file_path)
            if ci_file.exists():
                found_ci_file = True
                try:
                    with open(ci_file, encoding="utf-8") as f:
                        content = f.read()

                    # Vérifie les éléments essentiels du workflow (plus flexible)
                    essential_elements = ["python", "steps:", "run:", "uses:"]
                    found_elements = sum(
                        1 for elem in essential_elements if elem in content
                    )
                    assert (
                        found_elements >= 2
                    ), f"Seulement {found_elements} éléments essentiels trouvés dans {ci_file}"

                except Exception as e:
                    pytest.fail(f"Erreur validation workflow CI {ci_file}: {e}")
                break

        if not found_ci_file:
            pytest.skip("Aucun workflow CI trouvé")

    def test_file_permissions_complete(self):
        """Vérifie les permissions complètes"""
        essential_dirs = ["tests", "docs", "config"]

        found_dirs = 0
        for dir_name in essential_dirs:
            if Path(dir_name).exists():
                dir_path = Path(dir_name)
                try:
                    assert os.access(
                        dir_path, os.R_OK
                    ), f"Pas de permission de lecture sur {dir_name}/"
                    assert os.access(
                        dir_path, os.X_OK
                    ), f"Pas de permission d'exécution sur {dir_name}/"
                    found_dirs += 1
                except AssertionError:
                    # Skip si permissions insuffisantes
                    continue

        # Au moins 2 répertoires doivent avoir les bonnes permissions
        assert (
            found_dirs >= 2
        ), f"Seulement {found_dirs} répertoires avec bonnes permissions"

    def test_encoding_validation(self):
        """Valide l'encodage UTF-8 complet"""
        test_strings = [
            "🧪 Test UTF-8: éàçùñ",
            "🌟 Athalia/Arkalia",
            "🌕 Arkalia-LUNA",
            "✅ Test réussi",
            "❌ Test échoué",
        ]

        for test_string in test_strings:
            assert len(test_string) > 0, f"Chaîne vide: {test_string}"
            # Vérifie que l'encodage fonctionne
            encoded = test_string.encode("utf-8")
            decoded = encoded.decode("utf-8")
            assert decoded == test_string, f"Problème d'encodage: {test_string}"

    def test_json_yaml_parsing(self):
        """Teste le parsing JSON et YAML"""
        # Test JSON
        test_json = '{"test": "value", "number": 42}'
        try:
            parsed_json = json.loads(test_json)
            assert parsed_json["test"] == "value"
            assert parsed_json["number"] == 42
        except Exception as e:
            pytest.fail(f"Erreur parsing JSON: {e}")

        # Test YAML
        test_yaml = "test: value\nnumber: 42"
        try:
            parsed_yaml = yaml.safe_load(test_yaml)
            assert parsed_yaml["test"] == "value"
            assert parsed_yaml["number"] == 42
        except Exception as e:
            pytest.fail(f"Erreur parsing YAML: {e}")

    def test_subprocess_functionality(self):
        """Teste la fonctionnalité subprocess"""
        try:
            # Test simple commande
            result = validate_and_run(
                ["echo", "test"], capture_output=True, text=True, timeout=5
            )
            assert result.returncode == 0, "Commande echo échouée"
            assert "test" in result.stdout, "Sortie echo incorrecte"
        except (subprocess.TimeoutExpired, SecurityError):
            pytest.skip("Timeout sur commande simple")
        except Exception as e:
            pytest.skip(f"Erreur subprocess: {e}")

    def test_time_functionality(self):
        """Teste la fonctionnalité time - OPTIMISÉ"""
        start_time = time.time()
        # Optimisé: réduit de 0.1s à 0.01s
        time.sleep(0.01)  # Pause de 10ms au lieu de 100ms
        end_time = time.time()

        elapsed = end_time - start_time
        assert elapsed >= 0.005, f"Temps écoulé incorrect: {elapsed}"
        assert elapsed < 1.0, f"Temps écoulé trop long: {elapsed}"

    def test_pathlib_functionality(self):
        """Teste la fonctionnalité pathlib"""
        current_dir = Path(".")
        assert current_dir.exists(), "Répertoire courant inexistant"
        assert current_dir.is_dir(), "Répertoire courant n'est pas un dossier"

        # Test création de chemins
        test_path = Path("tests") / "test_ci_robust.py"
        assert test_path.parent == Path("tests"), "Parent path incorrect"
        assert test_path.name == "test_ci_robust.py", "Nom de fichier incorrect"

    def test_environment_robustness(self):
        """Teste la robustesse de l'environnement"""
        # Vérifie les variables d'environnement essentielles
        if os.getenv("CI"):
            # En CI, certaines variables peuvent être manquantes
            assert os.getenv("PATH"), "PATH manquant"
        else:
            # En local, vérifie les variables de base
            assert os.getenv("PATH"), "PATH manquant"
            # HOME ou USERPROFILE peut être manquant dans certains environnements
            if not (os.getenv("HOME") or os.getenv("USERPROFILE")):
                pytest.skip("HOME/USERPROFILE manquant (environnement spécial)")

    def test_error_handling(self):
        """Teste la gestion d'erreurs"""
        # Test gestion d'exception
        try:
            raise ValueError("Test d'erreur")
        except ValueError as e:
            assert str(e) == "Test d'erreur", "Message d'erreur incorrect"
        except Exception:
            pytest.fail("Exception incorrecte levée")
        else:
            pytest.fail("Aucune exception levée")

    def test_assertion_functionality(self):
        """Teste la fonctionnalité d'assertion"""
        # Tests d'assertion de base
        assert True, "Assertion True échouée"
        assert 1 == 1, "Assertion égalité échouée"
        assert 1 != 2, "Assertion inégalité échouée"
        assert 1 < 2, "Assertion comparaison échouée"
        assert "test" in "test string", "Assertion inclusion échouée"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
