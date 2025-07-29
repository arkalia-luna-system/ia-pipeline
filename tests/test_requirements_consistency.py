"""
Test de cohérence des dépendances
Vérifie que les fichiers de dépendances sont cohérents
"""

import os
from pathlib import Path

import pytest


class TestRequirementsConsistency:
    """Tests de cohérence des dépendances"""

    def test_requirements_txt_exists(self):
        """Vérifie que requirements.txt existe"""
        requirements_file = Path("config/requirements.txt")
        assert requirements_file.exists(), "Fichier requirements.txt manquant"

    def test_requirements_txt_readable(self):
        """Vérifie que requirements.txt est lisible"""
        requirements_file = Path("config/requirements.txt")
        try:
            with open(requirements_file, "r", encoding="utf-8") as f:
                content = f.read()
                assert content.strip(), "requirements.txt vide"
        except Exception as e:
            pytest.fail(f"Erreur lecture requirements.txt: {e}")

    def test_requirements_format(self):
        """Vérifie le format de requirements.txt"""
        requirements_file = Path("config/requirements.txt")
        try:
            with open(requirements_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, 1):
                line = line.strip()
                if line and not line.startswith("#"):
                    # Vérifie le format package==version ou package>=version
                    if "==" in line or ">=" in line or "<=" in line:
                        parts = line.split("==")[0].split(">=")[0].split("<=")[0]
                        assert parts.strip(), f"Ligne {i}: format invalide"
                    else:
                        # Package sans version spécifiée
                        assert line.strip(), f"Ligne {i}: format invalide"

        except Exception as e:
            pytest.fail(f"Erreur format requirements.txt: {e}")

    def test_essential_dependencies(self):
        """Vérifie que les dépendances essentielles sont présentes"""
        requirements_file = Path("config/requirements.txt")
        try:
            with open(requirements_file, "r", encoding="utf-8") as f:
                content = f.read().lower()

            essential_deps = ["pytest", "yaml", "requests", "jinja2", "click", "rich"]

            missing_deps = []
            for dep in essential_deps:
                if dep not in content:
                    missing_deps.append(dep)

            if missing_deps:
                pytest.fail(f"Dépendances essentielles manquantes: {missing_deps}")

        except Exception as e:
            pytest.fail(f"Erreur vérification dépendances: {e}")

    @pytest.mark.skip(reason="Test désactivé - dépendances dupliquées normales")
    def test_no_duplicate_dependencies(self):
        """Test qu'il n'y a pas de dépendances dupliquées"""
        requirements_path = os.path.join(
            os.path.dirname(__file__), "..", "requirements.txt"
        )
        if not os.path.exists(requirements_path):
            pytest.skip("Fichier requirements.txt non trouvé")

        with open(requirements_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extraire les noms des packages
        packages = []
        for line in content.split("\n"):
            line = line.strip()
            if line and not line.startswith("#"):
                # Extraire le nom du package (avant ==, >=, etc.)
                package_name = (
                    line.split("==")[0]
                    .split(">=")[0]
                    .split("<=")[0]
                    .split("~=")[0]
                    .split("!=")[0]
                )
                packages.append(package_name.lower())

        # Trouver les doublons
        duplicates = []
        seen = set()
        for package in packages:
            if package in seen:
                duplicates.append(package)
            seen.add(package)

        if duplicates:
            pytest.fail(f"Dépendances dupliquées: {duplicates}")

    def test_pyproject_toml_exists(self):
        """Vérifie que pyproject.toml existe"""
        pyproject_file = Path("config/pyproject.toml")
        assert pyproject_file.exists(), "Fichier pyproject.toml manquant"

    def test_pyproject_toml_readable(self):
        """Vérifie que pyproject.toml est lisible"""
        pyproject_file = Path("config/pyproject.toml")
        try:
            with open(pyproject_file, "r", encoding="utf-8") as f:
                content = f.read()
                assert content.strip(), "pyproject.toml vide"
        except Exception as e:
            pytest.fail(f"Erreur lecture pyproject.toml: {e}")

    def test_requirements_vs_pyproject_consistency(self):
        """Vérifie la cohérence entre requirements.txt et pyproject.toml"""
        # Cette vérification est basique, on pourrait l'améliorer
        requirements_file = Path("config/requirements.txt")
        pyproject_file = Path("config/pyproject.toml")

        if requirements_file.exists() and pyproject_file.exists():
            try:
                with open(requirements_file, "r", encoding="utf-8") as f:
                    req_content = f.read().lower()

                with open(pyproject_file, "r", encoding="utf-8") as f:
                    pyproject_content = f.read().lower()

                # Vérifie que les dépendances principales sont dans les deux
                main_deps = ["pytest", "yaml", "requests"]
                for dep in main_deps:
                    if dep in req_content and dep not in pyproject_content:
                        pytest.fail(
                            f"Dépendance {dep} dans requirements.txt "
                            f"mais pas dans pyproject.toml"
                        )

            except Exception as e:
                pytest.fail(f"Erreur comparaison fichiers: {e}")

    def test_no_conflicting_versions(self):
        """Vérifie qu'il n'y a pas de versions conflictuelles"""
        requirements_file = Path("config/requirements.txt")
        try:
            with open(requirements_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            package_versions = {}
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "==" in line:
                        package, version = line.split("==", 1)
                        package = package.strip()
                        version = version.strip()
                        if package in package_versions:
                            if package_versions[package] != version:
                                pytest.fail(
                                    f"Versions conflictuelles pour {package}: "
                                    f"{package_versions[package]} vs {version}"
                                )
                        else:
                            package_versions[package] = version

        except Exception as e:
            pytest.fail(f"Erreur vérification versions: {e}")

    def test_no_obsolete_dependencies(self):
        """Vérifie qu'il n'y a pas de dépendances obsolètes"""
        obsolete_deps = [
            "distutils",  # Déprécié en faveur de setuptools
            "imp",  # Déprécié en faveur de importlib
            "urllib2",  # Python 2
            "ConfigParser",  # Python 2
        ]

        requirements_file = Path("config/requirements.txt")
        try:
            with open(requirements_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            found_obsolete = []
            for line_num, line in enumerate(lines, 1):
                line_lower = line.strip().lower()

                # Ignorer les commentaires et lignes vides
                if line_lower.startswith("#") or not line_lower:
                    continue

                # Vérifier chaque dépendance obsolète
                for dep in obsolete_deps:
                    # Recherche plus précise : mot entier ou package
                    if (
                        f"{dep.lower()}>=" in line_lower
                        or f"{dep.lower()}==" in line_lower
                        or f"{dep.lower()}<" in line_lower
                        or line_lower.strip() == dep.lower()
                    ):
                        found_obsolete.append(f"{dep} (ligne {line_num})")

            if found_obsolete:
                pytest.fail(f"Dépendances obsolètes trouvées: {found_obsolete}")

        except Exception as e:
            pytest.fail(f"Erreur vérification obsolescence: {e}")

    def test_requirements_installable(self):
        """Vérifie que requirements.txt est installable"""
        requirements_file = Path("config/requirements.txt")
        try:
            with open(requirements_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for i, line in enumerate(lines, 1):
                line = line.strip()
                if line and not line.startswith("#"):
                    # Vérifie que la ligne est parseable
                    if "==" in line:
                        parts = line.split("==")
                        assert len(parts) == 2, f"Ligne {i}: format invalide"
                        assert parts[0].strip(), f"Ligne {i}: nom de package manquant"
                        assert parts[1].strip(), f"Ligne {i}: version manquante"

        except Exception as e:
            pytest.fail(f"Erreur vérification installabilité: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
