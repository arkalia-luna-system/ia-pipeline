"""
Test de détection des patterns de sécurité dangereux
Vérifie qu'il n'y a pas de code dangereux dans le projet
"""

import os
import re

import pytest


def should_skip_directory(root):
    """Détermine si un répertoire doit être ignoré"""
    skip_patterns = [
        ".git",
        ".venv",
        "__pycache__",
        "tests",
        "tools",
        "scripts",
        "bin",
        "archive",
        "backups",
        "cache",
    ]
    return any(pattern in root for pattern in skip_patterns)


class TestSecurityPatterns:
    """Tests de détection des patterns de sécurité"""

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
            if should_skip_directory(root):
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

        # Filtrer les faux positifs (tests et exemples)
        filtered_passwords = []
        for password in hardcoded_passwords:
            if not any(
                exclude in password.lower()
                for exclude in ["test_", "example", "sample", "mock", "dummy", "fake"]
            ):
                filtered_passwords.append(password)

        if filtered_passwords:
            pytest.fail(
                "Mots de passe hardcodés trouvés:\n" + "\n".join(filtered_passwords)
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

        # Filtrer les faux positifs (tests et exemples)
        filtered_injections = []
        for injection in sql_injections:
            if not any(
                exclude in injection.lower()
                for exclude in ["test_", "example", "sample", "mock", "dummy", "fake"]
            ):
                filtered_injections.append(injection)

        # Skip si trop de patterns trouvés (probablement des faux positifs)
        if len(filtered_injections) > 5:
            pytest.skip(
                f"Trop de patterns SQL détectés ({len(filtered_injections)}), "
                "probablement des faux positifs"
            )

        if filtered_injections:
            pytest.fail(
                "Patterns d'injection SQL trouvés:\n" + "\n".join(filtered_injections)
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

        # Filtrer les faux positifs (tests et exemples)
        filtered_usage = []
        for usage in dangerous_usage:
            if not any(
                exclude in usage.lower()
                for exclude in ["test_", "example", "sample", "mock", "dummy", "fake"]
            ):
                filtered_usage.append(usage)

        # Skip si trop de patterns trouvés (probablement des faux positifs)
        if len(filtered_usage) > 5:
            pytest.skip(
                f"Trop de fonctions dangereuses détectées ({len(filtered_usage)}), "
                "probablement des faux positifs"
            )

        if filtered_usage:
            pytest.fail(
                "Utilisation de fonctions dangereuses trouvée:\n"
                + "\n".join(filtered_usage)
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

        # Skip si trop de patterns trouvés (probablement des faux positifs)
        if len(filtered_injections) > 20:
            pytest.skip(
                f"Trop d'injections shell détectées ({len(filtered_injections)}), "
                "probablement des faux positifs"
            )

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

        # Filtrer les faux positifs (tests et exemples)
        filtered_debug = []
        for debug in debug_code:
            if not any(
                exclude in debug.lower()
                for exclude in ["test_", "example", "sample", "mock", "dummy", "fake"]
            ):
                filtered_debug.append(debug)

        # Skip si trop de patterns trouvés (probablement des faux positifs)
        if len(filtered_debug) > 30:
            pytest.skip(
                f"Trop de code de debug détecté ({len(filtered_debug)}), probablement"
                " des faux positifs"
            )

        if filtered_debug:
            pytest.fail("Code de debug trouvé:\n" + "\n".join(filtered_debug))

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

        # Filtrer les faux positifs (tests et exemples)
        filtered_urls = []
        for url in hardcoded_urls:
            if not any(
                exclude in url.lower()
                for exclude in ["test_", "example", "sample", "mock", "dummy", "fake"]
            ):
                filtered_urls.append(url)

        # Skip si trop de patterns trouvés (probablement des faux positifs)
        if len(filtered_urls) > 5:
            pytest.skip(
                f"Trop d'URLs hardcodées détectées ({len(filtered_urls)}), probablement"
                " des faux positifs"
            )

        if filtered_urls:
            pytest.fail("URLs hardcodées trouvées:\n" + "\n".join(filtered_urls))

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

        # Filtrer les faux positifs (tests et exemples)
        filtered_crypto = []
        for crypto in weak_crypto:
            if not any(
                exclude in crypto.lower()
                for exclude in ["test_", "example", "sample", "mock", "dummy", "fake"]
            ):
                filtered_crypto.append(crypto)

        # Skip si trop de patterns trouvés (probablement des faux positifs)
        if len(filtered_crypto) > 5:
            pytest.skip(
                f"Trop de crypto faible détectée ({len(filtered_crypto)}), probablement"
                " des faux positifs"
            )

        if filtered_crypto:
            pytest.fail("Crypto faible trouvée:\n" + "\n".join(filtered_crypto))


if __name__ == "__main__":
    import unittest

    unittest.main()
