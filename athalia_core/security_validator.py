#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module de validation sécurisée pour les commandes subprocess
Protection contre les injections de commandes et exécution non autorisée
"""

import logging
import subprocess
from typing import List, Optional, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class SecurityValidator:
    """Validateur de sécurité pour les commandes subprocess."""

    def __init__(self):
        """Initialise le validateur de sécurité."""
        self.allowed_commands = {
            # Commandes système de base
            "ls", "find", "grep", "cat", "head", "tail", "wc", "sort", "uniq",
            
            # Commandes Python
            "python", "python3", "pip", "pip3", "pytest", "flake8", "black", "mypy",
            
            # Commandes de développement
            "git", "git status", "git log", "git diff", "git add", "git commit", "git push",
            
            # Commandes de build et test
            "make", "cmake", "cargo", "npm", "yarn",
            
            # Commandes de conteneurisation
            "docker", "docker-compose", "docker build", "docker run",
            
            # Commandes IA/ML
            "ollama", "ollama list", "ollama run", "ollama pull",
            
            # Commandes de monitoring
            "ps", "top", "htop", "df", "du", "free", "uptime",
            
            # Commandes de réseau (limitées)
            "curl", "wget", "ping", "nslookup",
        }
        
        self.forbidden_patterns = [
            "rm -rf", "rm -r", "rm -f", "rm -rf /", "rm -rf /*",
            "dd if=", "dd of=", "mkfs", "fdisk", "parted",
            "chmod 777", "chmod +x", "chown root",
            "sudo", "su", "passwd", "useradd", "userdel",
            "systemctl", "service", "init", "killall",
            "pkill", "kill -9", "kill -SIGKILL",
            "shutdown", "reboot", "halt", "poweroff",
            "iptables", "firewall-cmd", "ufw",
            "crontab", "at", "batch",
            "ssh", "scp", "rsync", "nc", "netcat",
            "telnet", "ftp", "sftp",
            "wget -O", "curl -o", "curl -O",
            "echo '", "echo \"", "printf '", "printf \"",
            "cat >", "cat >>", "tee", "tee -a",
            "sed -i", "awk '{print", "grep -r",
            "find . -exec", "find . -delete",
            "xargs", "parallel",
            "eval", "exec", "source", ".",
            "bash -c", "sh -c", "zsh -c", "fish -c",
            "python -c", "python3 -c",
            "perl -e", "ruby -e", "node -e",
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
            command_str = " ".join(command) if isinstance(command, list) else str(command)
            
            for pattern in self.forbidden_patterns:
                if pattern.lower() in command_str.lower():
                    logger.warning(f"Pattern interdit détecté: {pattern}")
                    return {
                        "valid": False, 
                        "error": f"Pattern interdit détecté: {pattern}",
                        "command": command_str
                    }

            # Vérifier si la commande principale est autorisée
            if main_command not in self.allowed_commands:
                # Vérifier les commandes avec arguments
                command_with_args = " ".join(command[:2]) if len(command) >= 2 else main_command
                if command_with_args not in self.allowed_commands:
                    logger.warning(f"Commande non autorisée: {main_command}")
                    return {
                        "valid": False,
                        "error": f"Commande non autorisée: {main_command}",
                        "command": command_str
                    }

            # Vérifier les chemins de fichiers
            for arg in command[1:]:
                if self._is_dangerous_path(arg):
                    logger.warning(f"Chemin dangereux détecté: {arg}")
                    return {
                        "valid": False,
                        "error": f"Chemin dangereux: {arg}",
                        "command": command_str
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
            
            # Vérifier les patterns dangereux
            dangerous_patterns = [
                "/etc/", "/var/", "/usr/", "/bin/", "/sbin/", "/lib/", "/opt/",
                "/root/", "/home/", "/tmp/", "/dev/", "/proc/", "/sys/",
                "~/.ssh/", "~/.bashrc", "~/.profile", "~/.bash_profile",
                "/.ssh/", "/.bashrc", "/.profile", "/.bash_profile",
            ]
            
            for pattern in dangerous_patterns:
                if pattern in str(path_obj):
                    return True
            
            return False
            
        except Exception:
            # En cas d'erreur, considérer comme dangereux
            return True

    def run_safe_command(self, command: List[str], **kwargs) -> subprocess.CompletedProcess:
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
            raise SecurityError(f"Timeout lors de l'exécution de la commande")
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