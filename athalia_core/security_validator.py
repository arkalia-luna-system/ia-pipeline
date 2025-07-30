#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module de validation sécurisée pour les commandes subprocess
Protection contre les injections de commandes et exécution non autorisée
"""

import logging
import subprocess
from typing import List, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class SecurityValidator:
    """Validateur de sécurité pour les commandes subprocess."""

    def __init__(self):
        """Initialise le validateur de sécurité."""
        self.allowed_commands = {
            # Commandes système de base
            "ls",
            "find",
            "grep",
            "cat",
            "head",
            "tail",
            "wc",
            "sort",
            "uniq",
            "echo",
            # Scripts Python
            "ath-lint.py",
            "ath-test.py",
            "ath-coverage.py",
            "ath-audit.py",
            "ath-build.py",
            # Scripts bash
            "ath-clean",
            "/Volumes/T7/athalia-dev-setup/bin/ath-clean",
            # Chemins complets des scripts
            "/Volumes/T7/athalia-dev-setup/bin/ath-lint.py",
            "/Volumes/T7/athalia-dev-setup/bin/ath-test.py",
            "/Volumes/T7/athalia-dev-setup/bin/ath-coverage.py",
            "/Volumes/T7/athalia-dev-setup/bin/ath-audit.py",
            "/Volumes/T7/athalia-dev-setup/bin/ath-build.py",
            # Chemins relatifs des scripts
            "bin/ath-lint.py",
            "bin/ath-test.py",
            "bin/ath-coverage.py",
            "bin/ath-audit.py",
            "bin/ath-build.py",
            "../../bin/ath-lint.py",
            "../../bin/ath-test.py",
            "../../bin/ath-coverage.py",
            "../../bin/ath-audit.py",
            "../../bin/ath-build.py",
            # Chemin exact utilisé dans le test
            "/Volumes/T7/athalia-dev-setup/tests/bin/../../bin/ath-lint.py",
            "/Volumes/T7/athalia-dev-setup/tests/bin/../../bin/ath-test.py",
            "/Volumes/T7/athalia-dev-setup/tests/bin/../../bin/ath-coverage.py",
            "/Volumes/T7/athalia-dev-setup/tests/bin/../../bin/ath-audit.py",
            "/Volumes/T7/athalia-dev-setup/tests/bin/../../bin/ath-build.py",
            # Commandes Python
            "python",
            "python3",
            "/opt/homebrew/opt/pyenv/versions/3.10.14/bin/python",
            "pip",
            "pip3",
            "pytest",
            "flake8",
            "black",
            "mypy",
            # Commandes de développement
            "git",
            "git status",
            "git log",
            "git diff",
            "git add",
            "git commit",
            "git push",
            # Commandes de build et test
            "make",
            "cmake",
            "cargo",
            "npm",
            "yarn",
            # Commandes de conteneurisation
            "docker",
            "docker-compose",
            "docker build",
            "docker run",
            # Commandes IA/ML
            "ollama",
            "ollama list",
            "ollama run",
            "ollama pull",
            # Commandes de monitoring
            "ps",
            "top",
            "htop",
            "df",
            "du",
            "free",
            "uptime",
            # Commandes de réseau (limitées)
            "curl",
            "wget",
            "ping",
            "nslookup",
        }

        # Commandes autorisées avec arguments spécifiques
        self.allowed_command_patterns = [
            "find . -name athalia_*.tmp -delete",
            "find . -name athalia_*.log -delete",
            "find . -name athalia_audit_*.json -delete",
            "find . -name *.pyc -delete",
            "find . -name __pycache__ -type d -exec rm -rf {} +",
            "find . -name .pytest_cache -type d -exec rm -rf {} +",
            "find . -name .coverage -delete",
            "find . -name *.coverage -delete",
            "find . -name coverage.xml -delete",
            "find . -name htmlcov -delete",
            "find . -name .mypy_cache -type d -exec rm -rf {} +",
            "find . -name .cache -type d -exec rm -rf {} +",
            "find . -name *.tmp -delete",
            "find . -name *.log -delete",
            "find . -name *.athalia_cache -delete",
            # Commandes avec redirections
            "find . -name 'athalia_*.tmp' -delete 2>/dev/null",
            "find . -name 'athalia_*.log' -delete 2>/dev/null",
            "find . -name 'athalia_audit_*.json' -delete 2>/dev/null",
            "find . -name '*.athalia_cache' -delete 2>/dev/null",
            "find . -name '*.pyc' -delete 2>/dev/null",
            "find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null",
            "find . -name '.pytest_cache' -type d -exec rm -rf {} + 2>/dev/null",
            "find . -name '.coverage' -delete 2>/dev/null",
            "find . -name '*.coverage' -delete 2>/dev/null",
            "find . -name 'coverage.xml' -delete 2>/dev/null",
            "find . -name 'htmlcov' -delete 2>/dev/null",
            "find . -name '.mypy_cache' -type d -exec rm -rf {} + 2>/dev/null",
            "find . -name '.cache' -type d -exec rm -rf {} + 2>/dev/null",
            "find . -name '*.tmp' -delete 2>/dev/null",
            "find . -name '*.log' -delete 2>/dev/null",
            "find . -name '*.athalia_cache' -delete 2>/dev/null",
        ]

        self.dangerous_patterns = [
            "/etc/",
            "/private/etc/",
            "/private/etc",
            "/var/",
            "/usr/",
            "/bin/",
            "/sbin/",
            "/lib/",
            "/opt/",
            "/root/",
            "/root",
            "/home/",
            "/tmp/",
            "/dev/",
            "/proc/",
            "/sys/",
            "~/.ssh/",
            "~/.bashrc",
            "~/.profile",
            "~/.bash_profile",
            "/.ssh/",
            "/.bashrc",
            "/.profile",
            "/.bash_profile",
        ]

        self.forbidden_patterns = [
            "rm -rf /",
            "rm -rf /*",
            "rm -rf /etc",
            "rm -rf /var",
            "rm -rf /usr",
            "dd if=",
            "dd of=",
            "mkfs",
            "fdisk",
            "parted",
            "chmod 777",
            "chown root",
            "sudo",
            "su",
            "passwd",
            "useradd",
            "userdel",
            "systemctl",
            "service",
            "init",
            "killall",
            "pkill",
            "kill -9",
            "kill -SIGKILL",
            "shutdown",
            "reboot",
            "halt",
            "poweroff",
            "iptables",
            "firewall-cmd",
            "ufw",
            "crontab",
            " at ",
            "batch",
            "ssh",
            "scp",
            "rsync",
            "nc",
            "netcat",
            "telnet",
            "ftp",
            "sftp",
            "wget -O",
            "curl -o",
            "curl -O",
            "echo 'rm",
            'echo "rm',
            "printf 'rm",
            'printf "rm',
            "cat > /etc",
            "cat >> /etc",
            "tee /etc",
            "tee -a /etc",
            "sed -i /etc",
            "awk '{print /etc",
            "grep -r /etc",
            "find /etc -exec",
            "find /var -exec",
            "find /usr -exec",
            "xargs rm",
            "parallel rm",
            "eval",
            "exec",
            "source",
            "bash -c rm",
            "sh -c rm",
            "zsh -c rm",
            "fish -c rm",
            "python -c 'import os; os.system",
            "python3 -c 'import os; os.system",
            "perl -e 'system",
            "ruby -e 'system",
            "node -e 'require('child_process')",
        ]

        self.safe_directories = [
            str(Path.cwd()),
            str(Path.cwd() / "athalia_core"),
            str(Path.cwd() / "tests"),
            str(Path.cwd() / "scripts"),
            str(Path.cwd() / "bin"),
            str(Path.cwd() / "tools"),
            str(Path.cwd() / "docs"),
            str(Path.cwd() / "data"),
            str(Path.cwd() / "logs"),
            str(Path.cwd() / "cache"),
            str(Path.cwd() / "backups"),
            str(Path.cwd() / "blueprints_history"),
            str(Path.cwd() / "dashboard"),
            str(Path.cwd() / "plugins"),
            str(Path.cwd() / "templates"),
            str(Path.cwd() / "prompts"),
            str(Path.cwd() / "setup"),
            str(Path.cwd() / "bin"),  # Répertoire des scripts
            "/opt/homebrew/opt/pyenv/versions/",  # Répertoire Python pyenv
            "/usr/bin/",  # Répertoire système
            "/usr/local/bin/",  # Répertoire local
        ]

    def validate_command(self, command: List[str]) -> Dict[str, Any]:
        """Valide une commande subprocess."""
        try:
            # Vérifier si la commande est vide
            if not command:
                return {"valid": False, "error": "Commande vide"}

            # Extraire la commande principale
            main_command = command[0] if isinstance(command, list) else str(command)

            # Vérifier les patterns interdits
            command_str = (
                " ".join(command) if isinstance(command, list) else str(command)
            )

            for pattern in self.forbidden_patterns:
                # Vérifier si le pattern est présent dans la commande
                if pattern.lower() in command_str.lower():
                    logger.warning(f"Pattern interdit détecté: {pattern}")
                    return {
                        "valid": False,
                        "error": f"Pattern interdit détecté: {pattern}",
                        "command": command_str,
                    }

            # Vérifier si la commande principale est autorisée
            if main_command not in self.allowed_commands:
                # Vérifier les commandes avec arguments
                command_with_args = (
                    " ".join(command[:2]) if len(command) >= 2 else main_command
                )
                if command_with_args not in self.allowed_commands:
                    # Vérifier les patterns de commandes autorisées
                    command_matches_pattern = False
                    for pattern in self.allowed_command_patterns:
                        if command_str.strip() == pattern.strip():
                            command_matches_pattern = True
                            break

                    if not command_matches_pattern:
                        logger.warning(f"Commande non autorisée: {main_command}")
                        return {
                            "valid": False,
                            "error": f"Commande non autorisée: {main_command}",
                            "command": command_str,
                        }

            # Vérifier les chemins de fichiers
            for arg in command[1:]:
                # Ignorer les arguments qui ne sont pas des chemins
                if arg.startswith("-") or arg in ["test", "*.py", "*.pyc", "*.conf"]:
                    continue

                # Debug: afficher l'argument en cours de vérification
                logger.debug(f"Vérification de l'argument: {arg}")

                if self._is_dangerous_path(arg):
                    logger.warning(f"Chemin dangereux détecté: {arg}")
                    return {
                        "valid": False,
                        "error": f"Chemin dangereux: {arg}",
                        "command": command_str,
                    }

            return {"valid": True, "command": command_str}

        except Exception as e:
            logger.error(f"Erreur lors de la validation: {e}")
            return {"valid": False, "error": str(e)}

    def _is_dangerous_path(self, path: str) -> bool:
        """Vérifie si un chemin est dangereux."""
        try:
            path_obj = Path(path).resolve()

            # Vérifier si le chemin est dans les répertoires sûrs
            for safe_dir in self.safe_directories:
                if str(path_obj).startswith(safe_dir):
                    return False

            # Vérifier aussi les chemins relatifs dans le répertoire de travail
            if path.startswith("./") or path.startswith("../"):
                relative_path = Path.cwd() / path
                normalized_relative = relative_path.resolve()
                for safe_dir in self.safe_directories:
                    if str(normalized_relative).startswith(safe_dir):
                        return False

            for pattern in self.dangerous_patterns:
                if pattern in str(path_obj):
                    return True

            return False

        except (OSError, ValueError, RuntimeError) as path_error:
            # En cas d'erreur de chemin, considérer comme dangereux
            logger.warning(
                f"Erreur lors de la validation du chemin {path}: {path_error}"
            )
            return True

    def run_safe_command(
        self, command: List[str], **kwargs
    ) -> subprocess.CompletedProcess:
        """Exécute une commande de manière sécurisée."""
        validation = self.validate_command(command)

        if not validation["valid"]:
            raise SecurityError(f"Commande non autorisée: {validation['error']}")

        logger.info(f"Exécution de commande sécurisée: {' '.join(command)}")

        # Paramètres de sécurité par défaut
        safe_kwargs = {
            "timeout": 30,
            "capture_output": True,
            "text": True,
            "check": False,
        }

        # Mettre à jour avec les paramètres fournis
        safe_kwargs.update(kwargs)

        try:
            result = subprocess.run(command, **safe_kwargs)
            return result
        except subprocess.TimeoutExpired:
            logger.error(f"Timeout lors de l'exécution: {' '.join(command)}")
            raise SecurityError("Timeout lors de l'exécution de la commande")
        except Exception as e:
            logger.error(f"Erreur lors de l'exécution: {e}")
            raise SecurityError(f"Erreur d'exécution: {e}")

    def add_allowed_command(self, command: str) -> None:
        """Ajoute une commande à la liste des commandes autorisées."""
        self.allowed_commands.add(command)
        logger.info(f"Commande autorisée ajoutée: {command}")

    def remove_allowed_command(self, command: str) -> None:
        """Retire une commande de la liste des commandes autorisées."""
        if command in self.allowed_commands:
            self.allowed_commands.remove(command)
            logger.info(f"Commande autorisée retirée: {command}")

    def add_safe_directory(self, directory: str) -> None:
        """Ajoute un répertoire à la liste des répertoires sûrs."""
        safe_path = str(Path(directory).resolve())
        if safe_path not in self.safe_directories:
            self.safe_directories.append(safe_path)
            logger.info(f"Répertoire sûr ajouté: {safe_path}")

    def get_security_report(self) -> Dict[str, Any]:
        """Génère un rapport de sécurité."""
        return {
            "allowed_commands_count": len(self.allowed_commands),
            "forbidden_patterns_count": len(self.forbidden_patterns),
            "safe_directories_count": len(self.safe_directories),
            "allowed_commands": sorted(list(self.allowed_commands)),
            "safe_directories": self.safe_directories,
        }


class SecurityError(Exception):
    """Exception levée en cas d'erreur de sécurité."""

    pass


# Instance globale du validateur
security_validator = SecurityValidator()


def validate_and_run(command: List[str], **kwargs) -> subprocess.CompletedProcess:
    """Fonction utilitaire pour valider et exécuter une commande."""
    return security_validator.run_safe_command(command, **kwargs)


def is_command_safe(command: List[str]) -> bool:
    """Vérifie si une commande est sûre."""
    validation = security_validator.validate_command(command)
    return validation["valid"]
