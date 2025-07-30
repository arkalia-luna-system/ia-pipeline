#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests pour détecter les chemins hardcodés
"""

import os
import re

import pytest


class TestHardcodedPaths:
    """Tests pour détecter les chemins hardcodés"""

    def test_no_absolute_paths_in_source(self):
        """Test qu'il n'y a pas de chemins absolus dans le code source (sauf tests)"""
        # Exclure les fichiers de test
        source_files = []
        for root, dirs, files in os.walk("."):
            if ".git" in root or "__pycache__" in root or "tests" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    source_files.append(os.path.join(root, file))

        absolute_paths = []
        for file_path in source_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Chercher les chemins absolus
                    matches = re.findall(r'["\'](/[^"\']*?)["\']', content)
                    if matches:
                        absolute_paths.append((file_path, matches))
            except Exception:
                continue

        # Filtrer les chemins acceptables (comme /tmp, /etc, etc.)
        problematic_paths = []
        for file_path, paths in absolute_paths:
            filtered_paths = [p for p in paths if not self._is_acceptable_path(p)]
            if filtered_paths:
                problematic_paths.append((file_path, filtered_paths))

        if problematic_paths:
            pytest.fail(
                "Chemins absolus hardcodés trouvés:\n"
                + "\n".join([f"{file}: {paths}" for file, paths in problematic_paths])
            )

    @pytest.mark.skip(
        reason="Test désactivé - chemins hardcodés acceptables dans les tests"
    )
    def test_no_absolute_paths(self):
        """Test qu'il n'y a pas de chemins absolus hardcodés"""
        python_files = []
        for root, dirs, files in os.walk("."):
            if ".git" in root or "__pycache__" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))

        absolute_paths = []
        for py_file in python_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Chercher les chemins absolus
                    matches = re.findall(r'["\'](/[^"\']*?)["\']', content)
                    if matches:
                        absolute_paths.append((py_file, matches))
            except Exception:
                continue

        if absolute_paths:
            pytest.fail(
                "Chemins absolus hardcodés trouvés:\n"
                + "\n".join([f"{file}: {paths}" for file, paths in absolute_paths])
            )

    @pytest.mark.skip(
        reason="Test désactivé - chemins Desktop acceptables dans les tests"
    )
    def test_no_desktop_paths(self):
        """Test qu'il n'y a pas de chemins Desktop hardcodés"""
        python_files = []
        for root, dirs, files in os.walk("."):
            if ".git" in root or "__pycache__" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))

        desktop_paths = []
        for py_file in python_files:
            try:
                with open(py_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Chercher les chemins Desktop
                    matches = re.findall(
                        r'["\']([^"\']*?Desktop[^"\']*?)["\']', content
                    )
                    if matches:
                        desktop_paths.append((py_file, matches))
            except Exception:
                continue

        if desktop_paths:
            pytest.fail(
                "Chemins Desktop hardcodés trouvés:\n"
                + "\n".join([f"{file}: {paths}" for file, paths in desktop_paths])
            )

    def _is_acceptable_path(self, path):
        """Vérifie si un chemin absolu est acceptable"""
        acceptable_patterns = [
            r"^/tmp/",
            r"^/var/",
            r"^/etc/",
            r"^/usr/",
            r"^/bin/",
            r"^/sbin/",
            r"^/dev/",
            r"^/proc/",
            r"^/sys/",
            r"^/home/[^/]+/\.",
            r"^/Users/[^/]+/\.",
        ]
        return any(re.match(pattern, path) for pattern in acceptable_patterns)


if __name__ == "__main__":
    import unittest

    unittest.main()
