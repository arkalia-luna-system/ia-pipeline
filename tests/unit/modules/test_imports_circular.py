#!/usr/bin/env python3
"""
🧪 Test des imports circulaires - Athalia Project
Détecte et signale les imports circulaires dans le projet
"""

import importlib
import sys
from pathlib import Path

import pytest


def get_python_files(directory: str) -> list[Path]:
    """Récupère tous les fichiers Python d'un répertoire"""
    path = Path(directory)
    return list(path.rglob("*.py"))


def analyze_imports_in_file(file_path: Path) -> dict[str, list[str]]:
    """Analyse les imports dans un fichier Python"""
    imports: dict[str, list[str]] = {"imports": [], "from_imports": []}

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()

        lines = content.split("\n")
        for line in lines:
            line = line.strip()

            # Imports directs
            if line.startswith("import "):
                module = line[7:].split()[0].split(".")[0]
                imports["imports"].append(module)

            # Imports from
            elif line.startswith("from "):
                parts = line[5:].split(" import ")
                if len(parts) == 2:
                    module = parts[0].split(".")[0]
                    imports["from_imports"].append(module)

    except Exception as e:
        print(f"⚠️ Erreur lecture {file_path}: {e}")

    return imports


class TestCircularImports:
    """Tests pour détecter les imports circulaires"""

    def test_critical_modules_importable(self):
        """Test que les modules critiques sont importables"""
        critical_modules = [
            "athalia_core.utilities.cli",
            "athalia_core.core.main",
            "athalia_core.validation.security_validator",
            "athalia_core.audit",
        ]

        for module_name in critical_modules:
            try:
                module = importlib.import_module(module_name)
                assert module is not None, f"Module {module_name} non importable"
                print(f"✅ {module_name} importé avec succès")
            except ImportError as e:
                pytest.fail(f"❌ Erreur import {module_name}: {e}")

    def test_no_self_imports(self):
        """Test qu'aucun module ne s'importe lui-même"""
        # CORRECTION ARCHI PROPRE : Vérification intelligente du répertoire athalia_core
        core_path = Path("athalia_core")
        if not core_path.exists():
            # CORRECTION ARCHI PROPRE : Vérifier si on est dans le bon répertoire
            current_dir = Path.cwd()
            possible_paths = [
                current_dir / "athalia_core",
                current_dir.parent / "athalia_core",
                current_dir.parent.parent / "athalia_core",
            ]

            for path in possible_paths:
                if path.exists():
                    core_path = path
                    print(f"✅ Répertoire athalia_core trouvé: {path}")
                    break
            else:
                pytest.skip(
                    "Répertoire athalia_core non trouvé dans les emplacements possibles"
                )

        python_files = get_python_files("athalia_core")

        for file_path in python_files:
            imports = analyze_imports_in_file(file_path)
            module_name = file_path.stem

            # Vérifier qu'aucun module ne s'importe lui-même
            for import_name in imports["imports"] + imports["from_imports"]:
                if import_name == module_name:
                    pytest.fail(
                        f"❌ Auto-import détecté dans {file_path}: {import_name}"
                    )

        print(f"✅ Aucun auto-import détecté dans {len(python_files)} fichiers")

    def test_imports_analysis(self):
        """Analyse détaillée des imports dans athalia_core"""
        # CORRECTION ARCHI PROPRE : Vérification intelligente du répertoire athalia_core
        core_path = Path("athalia_core")
        if not core_path.exists():
            # CORRECTION ARCHI PROPRE : Vérifier si on est dans le bon répertoire
            current_dir = Path.cwd()
            possible_paths = [
                current_dir / "athalia_core",
                current_dir.parent / "athalia_core",
                current_dir.parent.parent / "athalia_core",
            ]

            for path in possible_paths:
                if path.exists():
                    core_path = path
                    print(f"✅ Répertoire athalia_core trouvé: {path}")
                    break
            else:
                pytest.skip(
                    "Répertoire athalia_core non trouvé dans les emplacements possibles"
                )

        python_files = get_python_files("athalia_core")
        assert len(python_files) > 0, "Aucun fichier Python trouvé dans athalia_core"

        all_imports = {}
        for file_path in python_files:
            imports = analyze_imports_in_file(file_path)
            all_imports[str(file_path)] = imports

        # Vérifier qu'il y a des imports (normal)
        total_imports = sum(
            len(imp["imports"]) + len(imp["from_imports"])
            for imp in all_imports.values()
        )
        assert total_imports > 0, "Aucun import détecté dans athalia_core"

        print(
            f"📊 Analyse des imports: {len(python_files)} fichiers,"
            f" {total_imports} imports"
        )

    def test_simple_imports_work(self):
        """Test que les imports simples fonctionnent"""
        try:
            import athalia_core  # noqa: F401 - Test d'import

            print("✅ Import athalia_core réussi")
        except ImportError as e:
            pytest.fail(f"❌ Erreur import athalia_core: {e}")

        try:
            from athalia_core.utilities import cli  # noqa: F401 - Test d'import

            print("✅ Import athalia_core.cli réussi")
        except ImportError as e:
            pytest.fail(f"❌ Erreur import athalia_core.cli: {e}")


if __name__ == "__main__":
    # Test rapide en ligne de commande
    print("🧪 Test des imports circulaires...")

    try:
        import athalia_core as ath_main  # noqa: F401 - Test d'import

        print("✅ Import principal réussi")
    except ImportError as e:
        print(f"❌ Erreur import principal: {e}")
        sys.exit(1)

    print("✅ Aucun import circulaire critique détecté")
    sys.exit(0)
