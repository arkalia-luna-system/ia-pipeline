"""
Test de vérification de l'encodage UTF-8
Vérifie que tous les fichiers sont correctement encodés en UTF-8
"""

from pathlib import Path

import pytest


class TestEncodingUTF8:
    """Tests de vérification de l'encodage UTF-8"""

    def test_python_files_utf8(self):
        """Vérifie que tous les fichiers Python sont en UTF-8 - OPTIMISÉ"""
        python_files = list(Path(".").glob("**/*.py"))
        python_files = [
            f
            for f in python_files
            if ".git" not in str(f)
            and "__pycache__" not in str(f)
            and not f.name.startswith("._")
            and "venv" not in str(f)  # Optimisé: exclure venv
        ]

        encoding_errors = []
        for py_file in python_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    f.read()
            except UnicodeDecodeError as e:
                encoding_errors.append(f"{py_file}: {e}")

        # Assertion pour vérifier qu'il n'y a pas d'erreurs d'encodage
        assert (
            len(encoding_errors) == 0
        ), "Erreurs d'encodage UTF-8 trouvées:\n" + "\n".join(encoding_errors)

    def test_markdown_files_utf8(self):
        """Vérifie que tous les fichiers Markdown sont en UTF-8"""
        markdown_files = list(Path(".").glob("**/*.md"))
        markdown_files = [
            f
            for f in markdown_files
            if ".git" not in str(f) and not f.name.startswith("._")
        ]

        encoding_errors = []
        for md_file in markdown_files:
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    f.read()
            except UnicodeDecodeError as e:
                encoding_errors.append(f"{md_file}: {e}")

        # Assertion pour vérifier qu'il n'y a pas d'erreurs d'encodage
        assert (
            len(encoding_errors) == 0
        ), "Erreurs d'encodage UTF-8 dans les fichiers MD:\n" + "\n".join(
            encoding_errors
        )

    def test_yaml_files_utf8(self):
        """Vérifie que tous les fichiers YAML sont en UTF-8"""
        yaml_files = list(Path(".").glob("**/*.yaml"))
        yaml_files.extend(Path(".").glob("**/*.yml"))
        yaml_files = [
            f
            for f in yaml_files
            if ".git" not in str(f) and not f.name.startswith("._")
        ]

        encoding_errors = []
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, "r", encoding="utf-8") as f:
                    f.read()
            except UnicodeDecodeError as e:
                encoding_errors.append(f"{yaml_file}: {e}")

        # Assertion pour vérifier qu'il n'y a pas d'erreurs d'encodage
        assert (
            len(encoding_errors) == 0
        ), "Erreurs d'encodage UTF-8 dans les fichiers YAML:\n" + "\n".join(
            encoding_errors
        )

    def test_txt_files_utf8(self):
        """Vérifie que tous les fichiers TXT sont en UTF-8"""
        txt_files = list(Path(".").glob("**/*.txt"))
        txt_files = [
            f for f in txt_files if ".git" not in str(f) and not f.name.startswith("._")
        ]

        encoding_errors = []
        for txt_file in txt_files:
            try:
                with open(txt_file, "r", encoding="utf-8") as f:
                    f.read()
            except UnicodeDecodeError as e:
                encoding_errors.append(f"{txt_file}: {e}")

        # Assertion pour vérifier qu'il n'y a pas d'erreurs d'encodage
        assert (
            len(encoding_errors) == 0
        ), "Erreurs d'encodage UTF-8 dans les fichiers TXT:\n" + "\n".join(
            encoding_errors
        )

    def test_requirements_utf8(self):
        """Vérifie que requirements.txt est en UTF-8 - OPTIMISÉ"""
        requirements_file = Path("config/requirements.txt")
        if requirements_file.exists():
            try:
                with open(requirements_file, "r", encoding="utf-8") as f:
                    f.read()
            except UnicodeDecodeError as e:
                pytest.fail(f"Erreur d'encodage dans requirements.txt: {e}")

    def test_config_utf8(self):
        """Vérifie que les fichiers de config sont en UTF-8 - OPTIMISÉ"""
        config_files = [
            "config/athalia_config.yaml",
            "config/pyproject.toml",
            "pytest-ci.ini",
        ]

        for config_file in config_files:
            if Path(config_file).exists():
                try:
                    with open(config_file, "r", encoding="utf-8") as f:
                        f.read()
                except UnicodeDecodeError as e:
                    pytest.fail(f"Erreur d'encodage dans {config_file}: {e}")

    def test_no_bom_marker(self):
        """Vérifie qu'il n'y a pas de marqueur BOM UTF-8"""
        python_files = list(Path(".").glob("**/*.py"))
        python_files = [
            f
            for f in python_files
            if ".git" not in str(f)
            and "__pycache__" not in str(f)
            and not f.name.startswith("._")
        ]

        bom_files = []
        for py_file in python_files:
            try:
                with open(py_file, "rb") as f:
                    content = f.read(3)
                    if content.startswith(b"\xef\xbb\xbf"):
                        bom_files.append(py_file)
            except Exception:
                continue

        # Assertion pour vérifier qu'il n'y a pas de marqueurs BOM
        assert (
            len(bom_files) == 0
        ), "Fichiers avec marqueur BOM UTF-8 trouvés:\n" + "\n".join(
            str(f) for f in bom_files
        )

    def test_consistent_line_endings(self):
        """Test que tous les fichiers ont des fins de ligne cohérentes"""
        import os

        # Exclure les dossiers qui peuvent contenir des fichiers avec des fins de
        # ligne mixtes
        exclude_dirs = {
            ".git",
            "__pycache__",
            ".venv",
            "venv",
            "node_modules",
            "build",
            "dist",
        }

        files_with_mixed_endings = []

        for root, dirs, files in os.walk("."):
            # Exclure les dossiers non désirés
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                if file.endswith((".py", ".md", ".txt", ".yaml", ".yml", ".json")):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rb") as f:
                            content = f.read()

                        # Vérifier les fins de ligne
                        has_crlf = b"\r\n" in content
                        has_lf = b"\n" in content
                        has_cr = b"\r" in content and b"\r\n" not in content

                        # Détecter les fins de ligne mixtes
                        if (has_crlf and has_lf and not has_cr) or (has_cr and has_lf):
                            files_with_mixed_endings.append(file_path)

                    except Exception:
                        continue

        # Assertion pour vérifier qu'il n'y a pas de fins de ligne mixtes
        assert (
            len(files_with_mixed_endings) == 0
        ), "Fichiers avec fins de ligne mixtes trouvés:\n" + "\n".join(
            files_with_mixed_endings
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
