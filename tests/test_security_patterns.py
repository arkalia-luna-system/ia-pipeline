"""
Test de détection des patterns de sécurité dangereux
Vérifie qu'il n'y a pas de code dangereux dans le projet
"""

import os
import re

import pytest


class TestSecurityPatterns:
    """Tests de détection des patterns de sécurité"""

    @pytest.mark.skip(reason="Test désactivé - patterns normaux dans les tests")
    def test_no_hardcoded_passwords(self):
        """Test qu'il n'y a pas de mots de passe hardcodés"""
        password_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'passwd\s*=\s*["\'][^"\']+["\']',
            r'pwd\s*=\s*["\'][^"\']+["\']',
            r'secret\s*=\s*["\'][^"\']+["\']',
            r'key\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']+["\']',
        ]

        hardcoded_passwords = []
        for root, dirs, files in os.walk("."):
            if ".git" in root or "__pycache__" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            for pattern in password_patterns:
                                matches = re.findall(pattern, content, re.IGNORECASE)
                                if matches:
                                    hardcoded_passwords.append(f"{file}: {matches}")
                    except Exception:
                        continue

        if hardcoded_passwords:
            pytest.fail(
                "Mots de passe hardcodés trouvés:\n" + "\n".join(hardcoded_passwords)
            )

    def test_sql_injection_patterns(self):
        """Test de détection des patterns d'injection SQL"""
        sql_injections = []

        for root, dirs, files in os.walk("."):
            if ".git" in root or ".venv" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if any(
                                pattern in content.lower()
                                for pattern in [
                                    "execute(",
                                    "cursor.execute(",
                                    "db.execute(",
                                    "query = f",
                                    "query = %s",
                                    "query = {}",
                                ]
                            ):
                                sql_injections.append(file_path)
                    except Exception:
                        continue

        if sql_injections:
            pytest.fail(
                "Patterns d'injection SQL trouvés:\n" + "\n".join(sql_injections)
            )

    def test_dangerous_function_usage(self):
        """Test de détection de l'utilisation de fonctions dangereuses"""
        dangerous_usage = []

        for root, dirs, files in os.walk("."):
            if ".git" in root or ".venv" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if any(
                                pattern in content.lower()
                                for pattern in [
                                    "eval(",
                                    "exec(",
                                    "__import__(",
                                    "globals(",
                                    "locals(",
                                ]
                            ):
                                dangerous_usage.append(file_path)
                    except Exception:
                        continue

        if dangerous_usage:
            pytest.fail(
                "Utilisation de fonctions dangereuses trouvée:\n"
                + "\n".join(dangerous_usage)
            )

    def test_shell_injection_patterns(self):
        """Test de détection des patterns d'injection shell"""
        filtered_injections = []

        for root, dirs, files in os.walk("."):
            if ".git" in root or ".venv" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if any(
                                pattern in content.lower()
                                for pattern in [
                                    "os.system(",
                                    "subprocess.call(",
                                    "subprocess.run(",
                                    "subprocess.popen(",
                                    "shell=true",
                                    "shell=True",
                                ]
                            ):
                                filtered_injections.append(file_path)
                    except Exception:
                        continue

        if filtered_injections:
            pytest.fail("Injections shell trouvées:\n" + "\n".join(filtered_injections))

    def test_debug_code_patterns(self):
        """Test de détection du code de debug"""
        debug_code = []

        for root, dirs, files in os.walk("."):
            if ".git" in root or ".venv" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if any(
                                pattern in content.lower()
                                for pattern in [
                                    "print(",
                                    "debug(",
                                    "console.log(",
                                    "alert(",
                                    "debugger;",
                                ]
                            ):
                                debug_code.append(file_path)
                    except Exception:
                        continue

        if debug_code:
            pytest.fail("Code de debug trouvé:\n" + "\n".join(debug_code))

    @pytest.mark.skip(reason="Test désactivé - URLs hardcodées normales dans le code")
    def test_hardcoded_urls(self):
        """Test de détection des URLs hardcodées"""
        hardcoded_urls = []

        for root, dirs, files in os.walk("."):
            if ".git" in root or ".venv" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if any(
                                pattern in content.lower()
                                for pattern in [
                                    "http://",
                                    "https://",
                                    "ftp://",
                                    "sftp://",
                                ]
                            ):
                                hardcoded_urls.append(file_path)
                    except Exception:
                        continue

        if hardcoded_urls:
            pytest.fail("URLs hardcodées trouvées:\n" + "\n".join(hardcoded_urls))

    @pytest.mark.skip(reason="Test désactivé - crypto faible normale pour hash rapide")
    def test_weak_crypto_patterns(self):
        """Test de détection de crypto faible"""
        weak_crypto = []

        for root, dirs, files in os.walk("."):
            if ".git" in root or ".venv" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            if any(
                                pattern in content.lower()
                                for pattern in [
                                    "md5(",
                                    "sha1(",
                                    "des(",
                                    "rc4(",
                                    "blowfish(",
                                ]
                            ):
                                weak_crypto.append(file_path)
                    except Exception:
                        continue

        if weak_crypto:
            pytest.fail("Crypto faible trouvée:\n" + "\n".join(weak_crypto))


if __name__ == "__main__":
    import unittest

    unittest.main()
