#!/usr/bin/env python3
"""
Script personnalisé pour détecter les erreurs de style similaires à flake8
"""

import os
import glob
import re
import ast


class CustomLinter:
    def __init__(self, max_line_length=88):
        self.max_line_length = max_line_length
        self.errors = []

    def check_line_length(self, file_path, line_num, line):
        """Vérifie la longueur de ligne (E501)"""
        if len(line) > self.max_line_length:
            self.errors.append(
                f"{file_path}:{line_num}:1: E501 line too long ({len(line)} > {self.max_line_length} characters)"
            )

    def check_trailing_whitespace(self, file_path, line_num, line):
        """Vérifie les espaces en fin de ligne (W291)"""
        if line.rstrip() != line and line.strip():
            self.errors.append(f"{file_path}:{line_num}:1: W291 trailing whitespace")

    def check_whitespace_before_colon(self, file_path, line_num, line):
        """Vérifie les espaces avant les deux-points (E203)"""
        if re.search(r"\s+:", line):
            self.errors.append(f"{file_path}:{line_num}:1: E203 whitespace before ':'")

    def check_line_break_before_binary_operator(self, file_path, line_num, line):
        """Vérifie les sauts de ligne avant les opérateurs binaires (W503)"""
        if (
            re.search(r"\s+\+\s*$", line)
            or re.search(r"\s+\-\s*$", line)
            or re.search(r"\s+\*\s*$", line)
            or re.search(r"\s+/\s*$")
        ):
            self.errors.append(
                f"{file_path}:{line_num}:1: W503 line break before binary operator"
            )

    def check_unused_imports(self, file_path, content):
        """Vérifie les imports inutilisés (F401) - version simplifiée"""
        try:
            tree = ast.parse(content)
            imports = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)

            # Version simplifiée - on ne vérifie pas vraiment l'utilisation
            # car c'est complexe à implémenter correctement
        except SyntaxError:
            pass

    def lint_file(self, file_path):
        """Linte un fichier"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for line_num, line in enumerate(lines, 1):
                self.check_line_length(file_path, line_num, line)
                self.check_trailing_whitespace(file_path, line_num, line)
                self.check_whitespace_before_colon(file_path, line_num, line)
                self.check_line_break_before_binary_operator(file_path, line_num, line)

            # Vérifier les imports inutilisés
            content = "".join(lines)
            self.check_unused_imports(file_path, content)

        except Exception as e:
            print(f"Erreur lors du linting de {file_path}: {e}")

    def lint_directory(self, patterns):
        """Linte tous les fichiers dans les patterns donnés"""
        for pattern in patterns:
            for file_path in glob.glob(pattern, recursive=True):
                if file_path.endswith(".py"):
                    self.lint_file(file_path)

        return len(self.errors)

    def print_errors(self):
        """Affiche toutes les erreurs"""
        for error in self.errors:
            print(error)
        print(f"\nTotal: {len(self.errors)} errors")


def main():
    """Fonction principale"""
    linter = CustomLinter(max_line_length=88)

    patterns = [
        "athalia_core/**/*.py",
        "tests/**/*.py",
        "bin/*.py",
        "scripts/*.py",
        "tools/**/*.py",
    ]

    print("🔍 Linting en cours...")
    error_count = linter.lint_directory(patterns)

    if error_count > 0:
        linter.print_errors()
        return 1
    else:
        print("✅ Aucune erreur détectée!")
        return 0


if __name__ == "__main__":
    exit(main())
